# Copyright 2021-2025 ONDEWO GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
D18 headless offline-token Keycloak auth for the ONDEWO VTSI python SDK.

The SDK authenticates once against a **public** Keycloak client (no ``client_secret`` — Q1,
2026-06-23) using the OAuth2 Resource Owner Password Credentials (ROPC) grant with
``scope=offline_access``. Keycloak returns a short-lived access token plus a long-lived **offline**
refresh token. The :class:`KeycloakTokenProvider` then auto-refreshes the access token
(``grant_type=refresh_token``) just before it expires and exposes the current token as the
``Authorization: Bearer`` gRPC metadata tuple. The refresh loop stops once ``token_expiration_in_s``
has elapsed since login (``None`` ⇒ run until the offline session itself expires).

No 2FA is involved — the authenticating account is a 2FA-exempt technical user (D14) and ROPC bypasses
the browser flow. See ``docs/development/keycloak-migration-plan.md`` §7.4/§7.8 + D18 and
``keycloak-architecture.md`` §5.4 for the full contract.

The HTTP transport is injectable (the :class:`TokenTransport` / :class:`AsyncTokenTransport`
protocols) so the helper can be unit-tested fully hermetically (no network). The default sync
transport uses ``requests``; the default async transport runs the same sync request in a thread
executor, so no extra async HTTP dependency is required.
"""
from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass
from typing import (
    Any,
    Dict,
    Optional,
    Protocol,
    Tuple,
)

import requests

from ondewo.vtsi.client.client_config import ClientConfig

#: gRPC metadata key carrying the bearer access token (lower-case per gRPC metadata rules).
AUTHORIZATION_METADATA_KEY: str = "authorization"

#: OAuth2 / OIDC grant types and scope used by the D18 ROPC offline-token flow.
GRANT_TYPE_PASSWORD: str = "password"
GRANT_TYPE_REFRESH_TOKEN: str = "refresh_token"
OFFLINE_ACCESS_SCOPE: str = "offline_access"

#: Seconds before the access token's own ``expires_in`` at which a proactive refresh is triggered,
#: so a call never goes out with an already-expired token.
_REFRESH_SKEW_S: float = 30.0

#: Fallback access-token lifetime (seconds) if Keycloak omits ``expires_in`` in the response.
_DEFAULT_EXPIRES_IN_S: float = 300.0


class KeycloakAuthError(Exception):
    """Raised when the Keycloak token endpoint rejects a request or returns an unusable response."""


@dataclass(frozen=True)
class TokenResponse:
    """
    A parsed Keycloak token-endpoint response.

    Args:
        access_token (str):
            The short-lived OIDC access token (JWT) sent as ``Authorization: Bearer``.
        refresh_token (str):
            The offline refresh token (``scope=offline_access``) used for subsequent refreshes.
        expires_in_s (float):
            Lifetime of ``access_token`` in seconds, as reported by Keycloak.
        obtained_at (float):
            Monotonic timestamp (``time.monotonic()``) at which the response was received.
    """

    access_token: str
    refresh_token: str
    expires_in_s: float
    obtained_at: float

    @property
    def expires_at(self) -> float:
        """
        Returns:
            float:
                Monotonic timestamp at which ``access_token`` expires.
        """
        return self.obtained_at + self.expires_in_s


class TokenTransport(Protocol):
    """Synchronous HTTP transport for the Keycloak token endpoint (injectable for hermetic tests)."""

    def post_token(self, token_url: str, data: Dict[str, str]) -> Dict[str, Any]:
        """
        POST form-encoded ``data`` to ``token_url`` and return the decoded JSON body.

        Args:
            token_url (str):
                The Keycloak token endpoint URL.
            data (Dict[str, str]):
                The form fields (``grant_type``, ``client_id``, …).

        Returns:
            Dict[str, Any]:
                The decoded JSON response body.

        Raises:
            KeycloakAuthError:
                If the request fails or the response is not a successful token response.
        """
        ...


class AsyncTokenTransport(Protocol):
    """Asynchronous HTTP transport for the Keycloak token endpoint (injectable for hermetic tests)."""

    async def post_token(self, token_url: str, data: Dict[str, str]) -> Dict[str, Any]:
        """
        Async variant of :meth:`TokenTransport.post_token`.

        Args:
            token_url (str):
                The Keycloak token endpoint URL.
            data (Dict[str, str]):
                The form fields.

        Returns:
            Dict[str, Any]:
                The decoded JSON response body.

        Raises:
            KeycloakAuthError:
                If the request fails or the response is not a successful token response.
        """
        ...


class RequestsTokenTransport:
    """Default synchronous transport backed by ``requests``."""

    def __init__(self, timeout_s: float = 30.0) -> None:
        """
        Args:
            timeout_s (float):
                Per-request timeout in seconds.
        """
        self._timeout_s: float = timeout_s

    def post_token(self, token_url: str, data: Dict[str, str]) -> Dict[str, Any]:
        try:
            response: requests.Response = requests.post(token_url, data=data, timeout=self._timeout_s)
        except requests.RequestException as exc:
            raise KeycloakAuthError(f"Keycloak token request to {token_url} failed: {exc}") from exc

        if response.status_code != 200:
            raise KeycloakAuthError(
                f"Keycloak token request to {token_url} returned HTTP {response.status_code}: {response.text}"
            )

        body: Dict[str, Any] = response.json()
        return body


class _ExecutorAsyncTokenTransport:
    """Default async transport: runs a synchronous transport in the running loop's executor."""

    def __init__(self, sync_transport: TokenTransport) -> None:
        """
        Args:
            sync_transport (TokenTransport):
                The synchronous transport to delegate to.
        """
        self._sync_transport: TokenTransport = sync_transport

    async def post_token(self, token_url: str, data: Dict[str, str]) -> Dict[str, Any]:
        loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self._sync_transport.post_token, token_url, data)


def build_token_url(keycloak_url: str, realm: str) -> str:
    """
    Build the Keycloak OIDC token endpoint URL for a realm.

    Args:
        keycloak_url (str):
            Base Keycloak URL (e.g. ``"https://host/auth"``); a trailing slash is tolerated.
        realm (str):
            Realm name.

    Returns:
        str:
            ``{keycloak_url}/realms/{realm}/protocol/openid-connect/token``.
    """
    base: str = keycloak_url.rstrip("/")
    return f"{base}/realms/{realm}/protocol/openid-connect/token"


def _parse_token_response(body: Dict[str, Any]) -> TokenResponse:
    """
    Parse a token-endpoint JSON body into a :class:`TokenResponse`.

    Args:
        body (Dict[str, Any]):
            The decoded JSON body.

    Returns:
        TokenResponse:
            The parsed tokens and timing.

    Raises:
        KeycloakAuthError:
            If ``access_token`` or ``refresh_token`` is missing (e.g. ``offline_access`` was not
            granted, so no offline refresh token was issued).
    """
    access_token: Optional[str] = body.get("access_token")
    refresh_token: Optional[str] = body.get("refresh_token")
    if not access_token:
        raise KeycloakAuthError(f"Keycloak response did not contain an access_token: {body!r}")
    if not refresh_token:
        raise KeycloakAuthError(
            "Keycloak response did not contain a refresh_token — was scope=offline_access granted to "
            f"the client? body={body!r}"
        )
    expires_in_s: float = float(body.get("expires_in", _DEFAULT_EXPIRES_IN_S))
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in_s=expires_in_s,
        obtained_at=time.monotonic(),
    )


def _password_grant_data(client_id: str, username: str, password: str) -> Dict[str, str]:
    """
    Build the form body for the ROPC offline-token grant.

    Args:
        client_id (str):
            The public SDK client id (no ``client_secret`` — Q1).
        username (str):
            The technical user's username / email.
        password (str):
            The technical user's password.

    Returns:
        Dict[str, str]:
            The ``grant_type=password`` + ``scope=offline_access`` form fields.
    """
    return {
        "grant_type": GRANT_TYPE_PASSWORD,
        "client_id": client_id,
        "username": username,
        "password": password,
        "scope": OFFLINE_ACCESS_SCOPE,
    }


def _refresh_grant_data(client_id: str, refresh_token: str) -> Dict[str, str]:
    """
    Build the form body for the refresh-token grant.

    Args:
        client_id (str):
            The public SDK client id (no ``client_secret`` — Q1).
        refresh_token (str):
            The offline refresh token.

    Returns:
        Dict[str, str]:
            The ``grant_type=refresh_token`` form fields.
    """
    return {
        "grant_type": GRANT_TYPE_REFRESH_TOKEN,
        "client_id": client_id,
        "refresh_token": refresh_token,
    }


def bearer_metadata(access_token: str) -> Tuple[str, str]:
    """
    Build the gRPC metadata tuple carrying the bearer access token.

    Args:
        access_token (str):
            The OIDC access token (JWT).

    Returns:
        Tuple[str, str]:
            ``("authorization", "Bearer <access_token>")``.
    """
    return AUTHORIZATION_METADATA_KEY, f"Bearer {access_token}"


class KeycloakTokenProvider:
    """
    Synchronous offline-token provider: ROPC login + bounded auto-refresh + ``Authorization: Bearer``.

    Acquire one with :meth:`login`, then call :meth:`get_metadata` before each gRPC call. The provider
    refreshes the access token from the offline refresh token when it is about to expire, and stops
    refreshing once ``token_expiration_in_s`` has elapsed since login. After that the last token is
    returned until it expires; calls then fail (``UNAUTHENTICATED``) until a fresh :meth:`login`.
    """

    def __init__(
        self,
        token_url: str,
        client_id: str,
        token: TokenResponse,
        token_expiration_in_s: Optional[int],
        transport: TokenTransport,
        login_monotonic: float,
    ) -> None:
        self._token_url: str = token_url
        self._client_id: str = client_id
        self._token: TokenResponse = token
        self._token_expiration_in_s: Optional[int] = token_expiration_in_s
        self._transport: TokenTransport = transport
        self._login_monotonic: float = login_monotonic

    @classmethod
    def login(
        cls,
        config: ClientConfig,
        transport: Optional[TokenTransport] = None,
    ) -> "KeycloakTokenProvider":
        """
        Perform the one-time ROPC offline-token login from a :class:`ClientConfig`.

        Args:
            config (ClientConfig):
                A config whose Keycloak D18 fields are fully set.
            transport (Optional[TokenTransport]):
                HTTP transport; defaults to a ``requests``-backed transport. Injected in tests.

        Returns:
            KeycloakTokenProvider:
                A logged-in provider ready to vend ``Authorization: Bearer`` metadata.

        Raises:
            ValueError:
                If the config's Keycloak fields are not fully configured.
            KeycloakAuthError:
                If Keycloak rejects the credentials or omits the offline refresh token.
        """
        keycloak_url, realm, client_id, username, password = _require_keycloak_config(config)
        active_transport: TokenTransport = transport if transport is not None else RequestsTokenTransport()
        token_url: str = build_token_url(keycloak_url=keycloak_url, realm=realm)

        body: Dict[str, Any] = active_transport.post_token(
            token_url=token_url,
            data=_password_grant_data(client_id=client_id, username=username, password=password),
        )
        token: TokenResponse = _parse_token_response(body)
        return cls(
            token_url=token_url,
            client_id=client_id,
            token=token,
            token_expiration_in_s=config.token_expiration_in_s,
            transport=active_transport,
            login_monotonic=token.obtained_at,
        )

    @property
    def access_token(self) -> str:
        """
        Returns:
            str:
                The current (possibly already-expired) access token, without refreshing.
        """
        return self._token.access_token

    def _refresh_window_open(self, now: float) -> bool:
        """
        Whether auto-refresh is still allowed at ``now``.

        Args:
            now (float):
                A ``time.monotonic()`` reading.

        Returns:
            bool:
                ``False`` once ``token_expiration_in_s`` has elapsed since login.
        """
        if self._token_expiration_in_s is None:
            return True
        return (now - self._login_monotonic) < self._token_expiration_in_s

    def _needs_refresh(self, now: float) -> bool:
        """
        Whether the access token should be refreshed at ``now``.

        Args:
            now (float):
                A ``time.monotonic()`` reading.

        Returns:
            bool:
                ``True`` if within ``_REFRESH_SKEW_S`` of expiry and the refresh window is still open.
        """
        if not self._refresh_window_open(now):
            return False
        return now >= (self._token.expires_at - _REFRESH_SKEW_S)

    def _refresh(self) -> None:
        """
        Exchange the offline refresh token for a fresh access token.

        Raises:
            KeycloakAuthError:
                If Keycloak rejects the refresh or omits a token.
        """
        body: Dict[str, Any] = self._transport.post_token(
            token_url=self._token_url,
            data=_refresh_grant_data(client_id=self._client_id, refresh_token=self._token.refresh_token),
        )
        self._token = _parse_token_response(body)

    def get_access_token(self, force_refresh: bool = False) -> str:
        """
        Return a current access token, refreshing first if needed (or if forced).

        Args:
            force_refresh (bool):
                Force a refresh regardless of expiry (used to recover from ``UNAUTHENTICATED``). A
                forced refresh is still bounded by ``token_expiration_in_s``.

        Returns:
            str:
                A current access token.
        """
        now: float = time.monotonic()
        if (force_refresh and self._refresh_window_open(now)) or self._needs_refresh(now):
            self._refresh()
        return self._token.access_token

    def get_metadata(self, force_refresh: bool = False) -> Tuple[str, str]:
        """
        Return the ``Authorization: Bearer`` gRPC metadata tuple, refreshing the token if needed.

        Args:
            force_refresh (bool):
                Force a refresh before building the tuple (e.g. on ``UNAUTHENTICATED``).

        Returns:
            Tuple[str, str]:
                ``("authorization", "Bearer <access_token>")``.
        """
        return bearer_metadata(self.get_access_token(force_refresh=force_refresh))


class AsyncKeycloakTokenProvider:
    """Asynchronous mirror of :class:`KeycloakTokenProvider` (D18 offline-token + bounded auto-refresh)."""

    def __init__(
        self,
        token_url: str,
        client_id: str,
        token: TokenResponse,
        token_expiration_in_s: Optional[int],
        transport: AsyncTokenTransport,
        login_monotonic: float,
    ) -> None:
        self._token_url: str = token_url
        self._client_id: str = client_id
        self._token: TokenResponse = token
        self._token_expiration_in_s: Optional[int] = token_expiration_in_s
        self._transport: AsyncTokenTransport = transport
        self._login_monotonic: float = login_monotonic
        self._lock: asyncio.Lock = asyncio.Lock()

    @classmethod
    async def login(
        cls,
        config: ClientConfig,
        transport: Optional[AsyncTokenTransport] = None,
    ) -> "AsyncKeycloakTokenProvider":
        """
        Async ROPC offline-token login from a :class:`ClientConfig`.

        Args:
            config (ClientConfig):
                A config whose Keycloak D18 fields are fully set.
            transport (Optional[AsyncTokenTransport]):
                Async HTTP transport; defaults to running a ``requests``-backed transport in the
                running loop's executor. Injected in tests.

        Returns:
            AsyncKeycloakTokenProvider:
                A logged-in async provider.

        Raises:
            ValueError:
                If the config's Keycloak fields are not fully configured.
            KeycloakAuthError:
                If Keycloak rejects the credentials or omits the offline refresh token.
        """
        keycloak_url, realm, client_id, username, password = _require_keycloak_config(config)
        active_transport: AsyncTokenTransport = (
            transport if transport is not None else _ExecutorAsyncTokenTransport(RequestsTokenTransport())
        )
        token_url: str = build_token_url(keycloak_url=keycloak_url, realm=realm)

        body: Dict[str, Any] = await active_transport.post_token(
            token_url=token_url,
            data=_password_grant_data(client_id=client_id, username=username, password=password),
        )
        token: TokenResponse = _parse_token_response(body)
        return cls(
            token_url=token_url,
            client_id=client_id,
            token=token,
            token_expiration_in_s=config.token_expiration_in_s,
            transport=active_transport,
            login_monotonic=token.obtained_at,
        )

    @property
    def access_token(self) -> str:
        """
        Returns:
            str:
                The current (possibly already-expired) access token, without refreshing.
        """
        return self._token.access_token

    def _refresh_window_open(self, now: float) -> bool:
        if self._token_expiration_in_s is None:
            return True
        return (now - self._login_monotonic) < self._token_expiration_in_s

    def _needs_refresh(self, now: float) -> bool:
        if not self._refresh_window_open(now):
            return False
        return now >= (self._token.expires_at - _REFRESH_SKEW_S)

    async def _refresh(self) -> None:
        body: Dict[str, Any] = await self._transport.post_token(
            token_url=self._token_url,
            data=_refresh_grant_data(client_id=self._client_id, refresh_token=self._token.refresh_token),
        )
        self._token = _parse_token_response(body)

    async def get_access_token(self, force_refresh: bool = False) -> str:
        """
        Async variant of :meth:`KeycloakTokenProvider.get_access_token`.

        Args:
            force_refresh (bool):
                Force a refresh (bounded by ``token_expiration_in_s``).

        Returns:
            str:
                A current access token.
        """
        async with self._lock:
            now: float = time.monotonic()
            if (force_refresh and self._refresh_window_open(now)) or self._needs_refresh(now):
                await self._refresh()
            return self._token.access_token

    async def get_metadata(self, force_refresh: bool = False) -> Tuple[str, str]:
        """
        Async variant of :meth:`KeycloakTokenProvider.get_metadata`.

        Args:
            force_refresh (bool):
                Force a refresh before building the tuple.

        Returns:
            Tuple[str, str]:
                ``("authorization", "Bearer <access_token>")``.
        """
        return bearer_metadata(await self.get_access_token(force_refresh=force_refresh))


def _require_keycloak_config(config: ClientConfig) -> Tuple[str, str, str, str, str]:
    """
    Extract the validated, non-empty Keycloak D18 fields from a config.

    Args:
        config (ClientConfig):
            The client config.

    Returns:
        Tuple[str, str, str, str, str]:
            ``(keycloak_url, realm, client_id, username, password)``.

    Raises:
        ValueError:
            If any required Keycloak field is missing or empty.
    """
    if not config.is_keycloak_auth_configured:
        raise ValueError("ClientConfig has no Keycloak (D18) auth fields configured.")
    # ``ClientConfig.__post_init__`` already validated the full set when any field is set; re-bind
    # to locals here to narrow the declared-Optional fields to ``str`` for the type checker.
    keycloak_url: Optional[str] = config.keycloak_url
    realm: Optional[str] = config.realm
    client_id: Optional[str] = config.client_id
    username: Optional[str] = config.username
    password: Optional[str] = config.password
    if not (keycloak_url and realm and client_id and username and password):
        raise ValueError("ClientConfig Keycloak (D18) auth fields are incompletely configured.")
    return keycloak_url, realm, client_id, username, password
