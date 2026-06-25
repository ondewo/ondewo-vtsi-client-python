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
Hermetic unit tests for the D18 headless offline-token Keycloak auth helper.

No network is touched: the Keycloak token endpoint is mocked with an in-memory fake transport that
records every request and returns scripted responses, and (for the default `requests`-backed
transport) `requests.post` is monkeypatched, so every assertion is deterministic.
"""
from __future__ import annotations

import asyncio
import time
from typing import (
    Any,
    Dict,
    List,
    Tuple,
)

import pytest

from ondewo.vtsi.client.client_config import ClientConfig
from ondewo.vtsi.client.utils import keycloak as keycloak_module
from ondewo.vtsi.client.utils.keycloak import (
    AsyncKeycloakTokenProvider,
    KeycloakAuthError,
    KeycloakTokenProvider,
    RequestsTokenTransport,
    TokenResponse,
    _ExecutorAsyncTokenTransport,
    _require_keycloak_config,
    bearer_metadata,
    build_token_url,
)

# Bound exactly once so a refactor that changes only an input or only an expectation cannot
# silently make a test tautological.
KEYCLOAK_URL: str = "https://keycloak.example.com/auth"
REALM: str = "ondewo-ccai-platform"
CLIENT_ID: str = "ondewo-nlu-cai-sdk-public"
USERNAME: str = "tech-user@example.com"
PASSWORD: str = "s3cret-pw"
EXPECTED_TOKEN_URL: str = (
    "https://keycloak.example.com/auth/realms/ondewo-ccai-platform/protocol/openid-connect/token"
)


def _keycloak_config(token_expiration_in_s: int | None = None) -> ClientConfig:
    """
    Build a fully-configured D18 `ClientConfig` for the tests.

    Args:
        token_expiration_in_s (int | None):
            Optional bound on the refresh loop, forwarded to the config. ``None`` ⇒ unbounded.

    Returns:
        ClientConfig:
            A config with every D18 Keycloak field populated from the module-level test constants.
    """
    return ClientConfig(
        host="localhost",
        port="50051",
        keycloak_url=KEYCLOAK_URL,
        realm=REALM,
        client_id=CLIENT_ID,
        username=USERNAME,
        password=PASSWORD,
        token_expiration_in_s=token_expiration_in_s,
    )


class FakeTokenTransport:
    """Synchronous fake transport: records requests, returns scripted responses in order."""

    def __init__(self, responses: List[Dict[str, Any]]) -> None:
        """
        Args:
            responses (List[Dict[str, Any]]):
                The JSON bodies to return, one per `post_token` call, in order.
        """
        self._responses: List[Dict[str, Any]] = list(responses)
        self.requests: List[Tuple[str, Dict[str, str]]] = []

    def post_token(self, token_url: str, data: Dict[str, str]) -> Dict[str, Any]:
        """
        Record the request and return the next scripted response.

        Args:
            token_url (str):
                The token endpoint URL the provider posted to.
            data (Dict[str, str]):
                The form fields the provider sent.

        Returns:
            Dict[str, Any]:
                The next scripted JSON body.

        Raises:
            AssertionError:
                If called more times than there are scripted responses.
        """
        self.requests.append((token_url, dict(data)))
        if not self._responses:
            raise AssertionError("FakeTokenTransport received an unexpected extra request.")
        return self._responses.pop(0)


class FakeAsyncTokenTransport:
    """Asynchronous fake transport mirroring `FakeTokenTransport`."""

    def __init__(self, responses: List[Dict[str, Any]]) -> None:
        """
        Args:
            responses (List[Dict[str, Any]]):
                The JSON bodies to return, one per `post_token` call, in order.
        """
        self._responses: List[Dict[str, Any]] = list(responses)
        self.requests: List[Tuple[str, Dict[str, str]]] = []

    async def post_token(self, token_url: str, data: Dict[str, str]) -> Dict[str, Any]:
        """
        Record the request and return the next scripted response.

        Args:
            token_url (str):
                The token endpoint URL the provider posted to.
            data (Dict[str, str]):
                The form fields the provider sent.

        Returns:
            Dict[str, Any]:
                The next scripted JSON body.

        Raises:
            AssertionError:
                If called more times than there are scripted responses.
        """
        self.requests.append((token_url, dict(data)))
        if not self._responses:
            raise AssertionError("FakeAsyncTokenTransport received an unexpected extra request.")
        return self._responses.pop(0)


class FakeRequestsResponse:
    """Minimal `requests.Response` stand-in for monkeypatching `requests.post`."""

    def __init__(self, status_code: int, body: Dict[str, Any]) -> None:
        """
        Args:
            status_code (int):
                The HTTP status code the fake response reports.
            body (Dict[str, Any]):
                The JSON body returned by `json` (and echoed by `text`).
        """
        self.status_code: int = status_code
        self._body: Dict[str, Any] = body

    def json(self) -> Dict[str, Any]:
        """
        Returns:
            Dict[str, Any]:
                The configured JSON body.
        """
        return self._body

    @property
    def text(self) -> str:
        """
        Returns:
            str:
                The `repr` of the body, mirroring how the transport renders an error response.
        """
        return repr(self._body)


def _token_body(access_token: str, refresh_token: str, expires_in: int) -> Dict[str, Any]:
    """
    Build a Keycloak token-endpoint JSON body for the tests.

    Args:
        access_token (str):
            The access token to embed.
        refresh_token (str):
            The (offline) refresh token to embed.
        expires_in (int):
            The access-token lifetime in seconds.

    Returns:
        Dict[str, Any]:
            A token response body with `access_token`, `refresh_token`, `expires_in`, `token_type`.
    """
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": expires_in,
        "token_type": "Bearer",
    }


# --------------------------------------------------------------------------------------------------
# URL + metadata builders
# --------------------------------------------------------------------------------------------------
def test_build_token_url_tolerates_trailing_slash() -> None:
    """`build_token_url` produces the same endpoint whether or not the base URL has a trailing slash."""
    assert build_token_url(KEYCLOAK_URL, REALM) == EXPECTED_TOKEN_URL
    assert build_token_url(KEYCLOAK_URL + "/", REALM) == EXPECTED_TOKEN_URL


def test_bearer_metadata_shape() -> None:
    """`bearer_metadata` returns the `("authorization", "Bearer <token>")` gRPC metadata tuple."""
    access_token: str = "abc.def.ghi"
    key, value = bearer_metadata(access_token)
    assert key == "authorization"
    assert value == f"Bearer {access_token}"


# --------------------------------------------------------------------------------------------------
# _require_keycloak_config
# --------------------------------------------------------------------------------------------------
def test_require_keycloak_config_returns_fields() -> None:
    """`_require_keycloak_config` returns the five D18 fields as a tuple in the documented order."""
    fields = _require_keycloak_config(_keycloak_config())
    assert fields == (KEYCLOAK_URL, REALM, CLIENT_ID, USERNAME, PASSWORD)


def test_require_keycloak_config_raises_when_not_configured() -> None:
    """`_require_keycloak_config` raises `ValueError` when the config has no Keycloak fields set."""
    config = ClientConfig(host="localhost", port="50051")
    with pytest.raises(ValueError, match="no Keycloak"):
        _require_keycloak_config(config)


# --------------------------------------------------------------------------------------------------
# Sync provider: login (ROPC + offline_access)
# --------------------------------------------------------------------------------------------------
def test_login_sends_password_grant_with_offline_access_and_no_secret() -> None:
    """`login` posts a `password` grant with `scope=offline_access`, no `client_secret`, and vends the token."""
    transport = FakeTokenTransport([_token_body("access-1", "offline-1", expires_in=300)])
    provider = KeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)

    assert len(transport.requests) == 1
    url, data = transport.requests[0]
    assert url == EXPECTED_TOKEN_URL
    assert data["grant_type"] == "password"
    assert data["scope"] == "offline_access"
    assert data["client_id"] == CLIENT_ID
    assert data["username"] == USERNAME
    assert data["password"] == PASSWORD
    # Q1: public client — no client_secret must ever be sent.
    assert "client_secret" not in data
    assert provider.access_token == "access-1"
    assert provider.get_metadata() == ("authorization", "Bearer access-1")


def test_login_uses_default_expires_in_when_omitted() -> None:
    """When Keycloak omits `expires_in`, the provider uses the default lifetime and does not refresh."""
    # Keycloak omits expires_in → the provider falls back to _DEFAULT_EXPIRES_IN_S, so the freshly
    # logged-in token is treated as valid and no immediate refresh is triggered.
    transport = FakeTokenTransport([{"access_token": "access-1", "refresh_token": "offline-1"}])
    provider = KeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)

    assert provider.get_metadata() == ("authorization", "Bearer access-1")
    assert len(transport.requests) == 1


def test_login_without_refresh_token_raises_offline_access_hint() -> None:
    """A login response without a refresh token raises `KeycloakAuthError` hinting at `offline_access`."""
    transport = FakeTokenTransport([{"access_token": "access-1", "expires_in": 300}])
    with pytest.raises(KeycloakAuthError, match="offline_access"):
        KeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)


def test_login_without_access_token_raises() -> None:
    """A login response without an access token raises `KeycloakAuthError`."""
    transport = FakeTokenTransport([{"refresh_token": "offline-1", "expires_in": 300}])
    with pytest.raises(KeycloakAuthError, match="access_token"):
        KeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)


def test_login_rejects_when_keycloak_not_configured() -> None:
    """`login` raises `ValueError` when the config carries no Keycloak fields, before any request."""
    transport = FakeTokenTransport([_token_body("access-1", "offline-1", expires_in=300)])
    config = ClientConfig(host="localhost", port="50051")
    with pytest.raises(ValueError, match="no Keycloak"):
        KeycloakTokenProvider.login(config=config, transport=transport)


# --------------------------------------------------------------------------------------------------
# Sync provider: auto-refresh from the offline refresh token
# --------------------------------------------------------------------------------------------------
def test_get_metadata_refreshes_when_access_token_near_expiry() -> None:
    """A near-expiry access token triggers a `refresh_token` grant on the next `get_metadata` call."""
    # First token expires almost immediately (within the refresh skew) → next call refreshes.
    transport = FakeTokenTransport(
        [
            _token_body("access-1", "offline-1", expires_in=1),
            _token_body("access-2", "offline-2", expires_in=300),
        ]
    )
    provider = KeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)

    # Second call triggers a refresh-token grant.
    key, value = provider.get_metadata()
    assert value == "Bearer access-2"
    assert len(transport.requests) == 2
    _, refresh_data = transport.requests[1]
    assert refresh_data["grant_type"] == "refresh_token"
    assert refresh_data["refresh_token"] == "offline-1"
    assert refresh_data["client_id"] == CLIENT_ID
    assert "client_secret" not in refresh_data


def test_get_access_token_returns_string_and_refreshes() -> None:
    """`get_access_token` returns the bare refreshed token string when the current one is near expiry."""
    transport = FakeTokenTransport(
        [
            _token_body("access-1", "offline-1", expires_in=1),
            _token_body("access-2", "offline-2", expires_in=300),
        ]
    )
    provider = KeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)

    assert provider.get_access_token() == "access-2"
    assert len(transport.requests) == 2


def test_get_metadata_does_not_refresh_when_token_is_fresh() -> None:
    """A fresh access token is reused across repeated `get_metadata` calls with no extra requests."""
    transport = FakeTokenTransport([_token_body("access-1", "offline-1", expires_in=300)])
    provider = KeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)

    for _ in range(3):
        assert provider.get_metadata() == ("authorization", "Bearer access-1")
    # No refresh requests — the token stayed fresh.
    assert len(transport.requests) == 1


def test_force_refresh_recovers_from_unauthenticated() -> None:
    """`get_metadata(force_refresh=True)` refreshes even a still-fresh token, modelling UNAUTHENTICATED recovery."""
    transport = FakeTokenTransport(
        [
            _token_body("access-1", "offline-1", expires_in=300),
            _token_body("access-2", "offline-2", expires_in=300),
        ]
    )
    provider = KeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)

    # Simulate a forced refresh-and-replay after an UNAUTHENTICATED response.
    assert provider.get_metadata(force_refresh=True) == ("authorization", "Bearer access-2")
    assert len(transport.requests) == 2
    assert transport.requests[1][1]["grant_type"] == "refresh_token"


def test_refresh_failure_raises() -> None:
    """A refresh whose response omits the access token surfaces as `KeycloakAuthError`."""
    transport = FakeTokenTransport(
        [
            _token_body("access-1", "offline-1", expires_in=1),
            # Refresh response missing the access_token → KeycloakAuthError.
            {"refresh_token": "offline-2", "expires_in": 300},
        ]
    )
    provider = KeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)

    with pytest.raises(KeycloakAuthError, match="access_token"):
        provider.get_metadata()


# --------------------------------------------------------------------------------------------------
# Sync provider: token_expiration_in_s bounds the refresh loop
# --------------------------------------------------------------------------------------------------
def test_token_expiration_stops_refresh_loop() -> None:
    """Once `token_expiration_in_s` has elapsed, no refresh happens — the last (stale) token is returned."""
    transport = FakeTokenTransport([_token_body("access-1", "offline-1", expires_in=1)])
    # Construct directly with a login timestamp well in the past so the 10s window is already closed.
    past_login: float = time.monotonic() - 1000.0
    provider = KeycloakTokenProvider(
        token_url=EXPECTED_TOKEN_URL,
        client_id=CLIENT_ID,
        token=TokenResponse(
            access_token="access-1",
            refresh_token="offline-1",
            expires_in_s=1.0,
            obtained_at=past_login,
        ),
        token_expiration_in_s=10,
        transport=transport,
        login_monotonic=past_login,
    )

    # The window is closed: even though the token is stale, no refresh happens — the last token is
    # returned and no request is made.
    assert provider.get_metadata() == ("authorization", "Bearer access-1")
    assert provider.get_metadata(force_refresh=True) == ("authorization", "Bearer access-1")
    assert transport.requests == []


def test_token_expiration_allows_refresh_inside_window() -> None:
    """Inside the `token_expiration_in_s` window, a near-expiry token still triggers a refresh."""
    # Provider is constructed directly (no login call), so the only queued response is the refresh
    # result the provider fetches when the near-expiry token triggers a refresh.
    transport = FakeTokenTransport([_token_body("access-2", "offline-2", expires_in=300)])
    now: float = time.monotonic()
    provider = KeycloakTokenProvider(
        token_url=EXPECTED_TOKEN_URL,
        client_id=CLIENT_ID,
        token=TokenResponse(
            access_token="access-1",
            refresh_token="offline-1",
            expires_in_s=1.0,
            obtained_at=now,
        ),
        token_expiration_in_s=10_000,
        transport=transport,
        login_monotonic=now,
    )
    # Inside the window and near expiry → refresh happens.
    assert provider.get_metadata() == ("authorization", "Bearer access-2")
    assert len(transport.requests) == 1


def test_unbounded_expiration_keeps_refreshing() -> None:
    """With `token_expiration_in_s=None` the refresh window is always open, so near-expiry tokens refresh."""
    # token_expiration_in_s=None → the refresh window is always open.
    transport = FakeTokenTransport([_token_body("access-2", "offline-2", expires_in=300)])
    now: float = time.monotonic()
    provider = KeycloakTokenProvider(
        token_url=EXPECTED_TOKEN_URL,
        client_id=CLIENT_ID,
        token=TokenResponse(
            access_token="access-1",
            refresh_token="offline-1",
            expires_in_s=1.0,
            obtained_at=now,
        ),
        token_expiration_in_s=None,
        transport=transport,
        login_monotonic=now,
    )
    assert provider.get_metadata() == ("authorization", "Bearer access-2")


# --------------------------------------------------------------------------------------------------
# TokenResponse.expires_at
# --------------------------------------------------------------------------------------------------
def test_token_response_expires_at() -> None:
    """`TokenResponse.expires_at` is `obtained_at + expires_in_s`."""
    token = TokenResponse(
        access_token="access-1",
        refresh_token="offline-1",
        expires_in_s=300.0,
        obtained_at=1000.0,
    )
    assert token.expires_at == 1300.0


# --------------------------------------------------------------------------------------------------
# Default RequestsTokenTransport (requests.post monkeypatched — no network)
# --------------------------------------------------------------------------------------------------
def test_requests_transport_success(monkeypatch: pytest.MonkeyPatch) -> None:
    """The default `requests` transport posts with the configured timeout and returns the decoded body.

    Args:
        monkeypatch (pytest.MonkeyPatch):
            Fixture used to replace `requests.post` with a hermetic fake.
    """
    captured: Dict[str, Any] = {}

    def fake_post(url: str, data: Dict[str, str], timeout: float) -> FakeRequestsResponse:
        """Capture the call arguments and return a successful fake response.

        Args:
            url (str):
                The URL the transport posted to.
            data (Dict[str, str]):
                The form fields the transport sent.
            timeout (float):
                The per-request timeout the transport applied.

        Returns:
            FakeRequestsResponse:
                A 200 response carrying a valid token body.
        """
        captured["url"] = url
        captured["data"] = data
        captured["timeout"] = timeout
        return FakeRequestsResponse(200, _token_body("access-1", "offline-1", expires_in=300))

    monkeypatch.setattr(keycloak_module.requests, "post", fake_post)

    transport = RequestsTokenTransport(timeout_s=12.0)
    body = transport.post_token(EXPECTED_TOKEN_URL, {"grant_type": "password"})

    assert body["access_token"] == "access-1"
    assert captured["url"] == EXPECTED_TOKEN_URL
    assert captured["timeout"] == 12.0


def test_requests_transport_non_200_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    """A non-200 HTTP status from `requests.post` is turned into a `KeycloakAuthError`.

    Args:
        monkeypatch (pytest.MonkeyPatch):
            Fixture used to replace `requests.post` with a hermetic fake.
    """

    def fake_post(url: str, data: Dict[str, str], timeout: float) -> FakeRequestsResponse:
        """Return a 401 fake response.

        Args:
            url (str):
                The URL the transport posted to.
            data (Dict[str, str]):
                The form fields the transport sent.
            timeout (float):
                The per-request timeout the transport applied.

        Returns:
            FakeRequestsResponse:
                A 401 response carrying an error body.
        """
        return FakeRequestsResponse(401, {"error": "invalid_grant"})

    monkeypatch.setattr(keycloak_module.requests, "post", fake_post)

    transport = RequestsTokenTransport()
    with pytest.raises(KeycloakAuthError, match="HTTP 401"):
        transport.post_token(EXPECTED_TOKEN_URL, {"grant_type": "password"})


def test_requests_transport_request_exception_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    """A `requests.RequestException` (e.g. connection refused) is wrapped in a `KeycloakAuthError`.

    Args:
        monkeypatch (pytest.MonkeyPatch):
            Fixture used to replace `requests.post` with a hermetic fake.
    """

    def fake_post(url: str, data: Dict[str, str], timeout: float) -> FakeRequestsResponse:
        """Raise a transport-level `RequestException`.

        Args:
            url (str):
                The URL the transport posted to.
            data (Dict[str, str]):
                The form fields the transport sent.
            timeout (float):
                The per-request timeout the transport applied.

        Returns:
            FakeRequestsResponse:
                Never returns; always raises.

        Raises:
            requests.RequestException:
                Always, to simulate a connection failure.
        """
        raise keycloak_module.requests.RequestException("connection refused")

    monkeypatch.setattr(keycloak_module.requests, "post", fake_post)

    transport = RequestsTokenTransport()
    with pytest.raises(KeycloakAuthError, match="failed"):
        transport.post_token(EXPECTED_TOKEN_URL, {"grant_type": "password"})


# --------------------------------------------------------------------------------------------------
# Default _ExecutorAsyncTokenTransport delegates to the sync transport in the loop executor
# --------------------------------------------------------------------------------------------------
def test_executor_async_transport_delegates_to_sync() -> None:
    """`_ExecutorAsyncTokenTransport` forwards `post_token` to the wrapped sync transport via the loop executor."""
    sync_transport = FakeTokenTransport([_token_body("access-1", "offline-1", expires_in=300)])
    async_transport = _ExecutorAsyncTokenTransport(sync_transport)

    async def _run() -> Dict[str, Any]:
        """Await the async transport once.

        Returns:
            Dict[str, Any]:
                The body returned by the delegated sync transport.
        """
        return await async_transport.post_token(EXPECTED_TOKEN_URL, {"grant_type": "password"})

    body = asyncio.run(_run())
    assert body["access_token"] == "access-1"
    assert sync_transport.requests == [(EXPECTED_TOKEN_URL, {"grant_type": "password"})]


# --------------------------------------------------------------------------------------------------
# Async provider mirrors the sync behaviour
# --------------------------------------------------------------------------------------------------
def test_async_login_and_refresh() -> None:
    """The async provider posts the same `password` grant and refreshes a near-expiry token like the sync one."""

    async def _run() -> None:
        """Drive the async login + near-expiry refresh and assert on the recorded requests."""
        transport = FakeAsyncTokenTransport(
            [
                _token_body("access-1", "offline-1", expires_in=1),
                _token_body("access-2", "offline-2", expires_in=300),
            ]
        )
        provider = await AsyncKeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)

        url, data = transport.requests[0]
        assert url == EXPECTED_TOKEN_URL
        assert data["grant_type"] == "password"
        assert data["scope"] == "offline_access"
        assert "client_secret" not in data
        assert provider.access_token == "access-1"

        # Near-expiry → refresh on next metadata fetch.
        assert await provider.get_metadata() == ("authorization", "Bearer access-2")
        assert transport.requests[1][1]["grant_type"] == "refresh_token"
        assert transport.requests[1][1]["refresh_token"] == "offline-1"

    asyncio.run(_run())


def test_async_get_access_token_no_refresh_when_fresh() -> None:
    """The async provider reuses a fresh access token without issuing a refresh request."""

    async def _run() -> None:
        """Log in async, fetch a fresh token, and assert only the login request was made."""
        transport = FakeAsyncTokenTransport([_token_body("access-1", "offline-1", expires_in=300)])
        provider = await AsyncKeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)

        # Token is fresh → no refresh request beyond the login.
        assert await provider.get_access_token() == "access-1"
        assert len(transport.requests) == 1

    asyncio.run(_run())


def test_async_force_refresh() -> None:
    """The async provider's `get_metadata(force_refresh=True)` refreshes even a still-fresh token."""

    async def _run() -> None:
        """Log in async then force a refresh and assert a `refresh_token` grant was sent."""
        transport = FakeAsyncTokenTransport(
            [
                _token_body("access-1", "offline-1", expires_in=300),
                _token_body("access-2", "offline-2", expires_in=300),
            ]
        )
        provider = await AsyncKeycloakTokenProvider.login(config=_keycloak_config(), transport=transport)

        assert await provider.get_metadata(force_refresh=True) == ("authorization", "Bearer access-2")
        assert len(transport.requests) == 2
        assert transport.requests[1][1]["grant_type"] == "refresh_token"

    asyncio.run(_run())


def test_async_login_rejects_when_keycloak_not_configured() -> None:
    """The async `login` raises `ValueError` when the config carries no Keycloak fields."""

    async def _run() -> None:
        """Attempt an async login against an unconfigured config and assert it raises."""
        transport = FakeAsyncTokenTransport([_token_body("access-1", "offline-1", expires_in=300)])
        config = ClientConfig(host="localhost", port="50051")
        with pytest.raises(ValueError, match="no Keycloak"):
            await AsyncKeycloakTokenProvider.login(config=config, transport=transport)

    asyncio.run(_run())


def test_async_token_expiration_stops_refresh_loop() -> None:
    """Once the async provider's expiration window has closed, no refresh happens and the last token is returned."""

    async def _run() -> None:
        """Construct an async provider with an already-closed window and assert no refresh is issued."""
        transport = FakeAsyncTokenTransport([_token_body("access-1", "offline-1", expires_in=1)])
        past_login: float = time.monotonic() - 1000.0
        provider = AsyncKeycloakTokenProvider(
            token_url=EXPECTED_TOKEN_URL,
            client_id=CLIENT_ID,
            token=TokenResponse(
                access_token="access-1",
                refresh_token="offline-1",
                expires_in_s=1.0,
                obtained_at=past_login,
            ),
            token_expiration_in_s=10,
            transport=transport,
            login_monotonic=past_login,
        )
        assert await provider.get_metadata() == ("authorization", "Bearer access-1")
        assert await provider.get_metadata(force_refresh=True) == ("authorization", "Bearer access-1")
        assert transport.requests == []

    asyncio.run(_run())
