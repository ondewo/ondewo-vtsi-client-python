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
from __future__ import annotations

from dataclasses import dataclass

from dataclasses_json import dataclass_json
from ondewo.utils.base_client_config import BaseClientConfig


@dataclass_json
@dataclass(frozen=True)
class ClientConfig(BaseClientConfig):
    """
    Config for the ONDEWO VTSI client.

    Supports the D18 headless offline-token auth flow: the client logs in once against a **public**
    Keycloak client with ``grant_type=password`` + ``scope=offline_access`` (Resource Owner Password
    Credentials, ROPC), then auto-refreshes the short-lived access token and attaches it as the
    ``Authorization: Bearer`` gRPC metadata. The SDK client is **public**, so there is intentionally
    **no** ``client_secret`` (Q1, 2026-06-23). The legacy ``http_token`` (``Authorization: Basic``)
    is removed (D5) and is no longer required by ``__post_init__``.

    Attributes:
        host (str):
            IP address / hostname of the ONDEWO VTSI services host (e.g. ``"localhost"``).
        port (str):
            Port of the ONDEWO VTSI services host (e.g. ``"50051"``).
        grpc_cert (str | None):
            Certificate for a secure gRPC channel. Required unless the client is instantiated with
            ``use_secure_channel=False``.
        keycloak_url (str | None):
            Base URL of the Keycloak server (e.g. ``"https://keycloak.example.com/auth"``). Required
            for the D18 offline-token auth flow.
        realm (str | None):
            Keycloak realm name (e.g. ``"ondewo-ccai-platform"``). Required for the D18 flow.
        client_id (str | None):
            Id of the **public** Keycloak client used for the ROPC grant (e.g.
            ``"ondewo-nlu-cai-sdk-public"``). Required for the D18 flow. No ``client_secret`` exists
            (Q1 — public client).
        username (str | None):
            Username / email of the (2FA-exempt technical) user authenticating via ROPC. Required for
            the D18 flow.
        password (str | None):
            Password of that user. Required for the D18 flow.
        token_expiration_in_s (int | None):
            Optional bound (seconds) on how long the auto-refresh loop runs. Once this many seconds
            have elapsed since login the access token is no longer refreshed and a re-login is needed.
            ``None`` ⇒ refresh until the Keycloak offline session itself expires.
        keycloak_verify_ssl (bool):
            Whether to verify the Keycloak server's TLS certificate on the token-endpoint
            call. Defaults to ``True`` (secure). Set ``False`` only for a self-signed/local
            Envoy at ``https://localhost:12001/auth``.
    """

    keycloak_url: str | None = None
    realm: str | None = None
    client_id: str | None = None
    username: str | None = None
    password: str | None = None
    token_expiration_in_s: int | None = None
    keycloak_verify_ssl: bool = True

    def __post_init__(self) -> None:
        # Keep the base behaviour (encode the grpc certificate); intentionally does NOT require the
        # legacy ``http_token`` any more (D5 — clients no longer send ``Authorization: Basic``).
        super().__post_init__()

        if self.is_keycloak_auth_configured:
            self._validate_keycloak_auth()

    @property
    def is_keycloak_auth_configured(self) -> bool:
        """
        Whether any Keycloak D18 auth field is set.

        Returns:
            bool:
                ``True`` if at least one of the Keycloak ROPC fields is provided, in which case the
                full set is validated by ``__post_init__``.
        """
        return any(
            field_value is not None
            for field_value in (
                self.keycloak_url,
                self.realm,
                self.client_id,
                self.username,
                self.password,
            )
        )

    def _validate_keycloak_auth(self) -> None:
        """
        Validate that the full D18 ROPC field set is present.

        Raises:
            ValueError:
                If any of ``keycloak_url`` / ``realm`` / ``client_id`` / ``username`` / ``password``
                is missing, or ``token_expiration_in_s`` is non-positive.
        """
        required_fields: dict[str, str | None] = {
            "keycloak_url": self.keycloak_url,
            "realm": self.realm,
            "client_id": self.client_id,
            "username": self.username,
            "password": self.password,
        }
        missing: list[str] = [name for name, value in required_fields.items() if not value]
        if missing:
            raise ValueError(
                "Keycloak (D18) auth requires all of keycloak_url, realm, client_id, username, "
                f"password to be set; missing/empty: {', '.join(missing)}."
            )

        if self.token_expiration_in_s is not None and self.token_expiration_in_s <= 0:
            raise ValueError(
                f"token_expiration_in_s must be a positive number of seconds, got {self.token_expiration_in_s}."
            )
