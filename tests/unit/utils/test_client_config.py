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
"""Unit tests for `ClientConfig` validation of the D18 Keycloak offline-token auth fields."""
from __future__ import annotations

import pytest

from ondewo.vtsi.client.client_config import ClientConfig

# Bound exactly once so a refactor that changes only an input or only an expectation cannot
# silently make a test tautological.
HOST: str = "localhost"
PORT: str = "50051"
KEYCLOAK_URL: str = "https://keycloak.example.com/auth"
REALM: str = "ondewo-ccai-platform"
CLIENT_ID: str = "ondewo-nlu-cai-sdk-public"
USERNAME: str = "tech-user@example.com"
PASSWORD: str = "s3cret-pw"


class TestNoKeycloak:
    def test_config_without_keycloak_fields_is_valid(self) -> None:
        config = ClientConfig(host=HOST, port=PORT)

        assert config.is_keycloak_auth_configured is False
        # http_token was removed (D5) — it must not be a field on the config.
        assert not hasattr(config, "http_token")

    def test_config_without_keycloak_fields_has_no_keycloak_values(self) -> None:
        config = ClientConfig(host=HOST, port=PORT)

        assert config.keycloak_url is None
        assert config.realm is None
        assert config.client_id is None
        assert config.username is None
        assert config.password is None
        assert config.token_expiration_in_s is None


class TestKeycloakPath:
    def test_full_keycloak_config_is_valid_and_flagged(self) -> None:
        config = ClientConfig(
            host=HOST,
            port=PORT,
            keycloak_url=KEYCLOAK_URL,
            realm=REALM,
            client_id=CLIENT_ID,
            username=USERNAME,
            password=PASSWORD,
        )

        assert config.is_keycloak_auth_configured is True
        assert config.client_id == CLIENT_ID

    def test_full_keycloak_config_with_positive_token_expiration_is_valid(self) -> None:
        token_expiration_in_s: int = 3600
        config = ClientConfig(
            host=HOST,
            port=PORT,
            keycloak_url=KEYCLOAK_URL,
            realm=REALM,
            client_id=CLIENT_ID,
            username=USERNAME,
            password=PASSWORD,
            token_expiration_in_s=token_expiration_in_s,
        )

        assert config.is_keycloak_auth_configured is True
        assert config.token_expiration_in_s == token_expiration_in_s

    def test_partial_keycloak_config_missing_password_raises(self) -> None:
        with pytest.raises(ValueError, match="password"):
            ClientConfig(
                host=HOST,
                port=PORT,
                keycloak_url=KEYCLOAK_URL,
                realm=REALM,
                client_id=CLIENT_ID,
                username=USERNAME,
                # password missing
            )

    def test_single_keycloak_field_set_triggers_all_or_nothing_validation(self) -> None:
        # Setting only keycloak_url flips `is_keycloak_auth_configured` on, so the full set is
        # validated and the four missing fields are reported.
        with pytest.raises(ValueError, match="realm, client_id, username, password"):
            ClientConfig(host=HOST, port=PORT, keycloak_url=KEYCLOAK_URL)

    def test_empty_string_keycloak_field_is_treated_as_missing(self) -> None:
        # An empty string is set (not None) so it triggers validation but counts as missing.
        with pytest.raises(ValueError, match="keycloak_url"):
            ClientConfig(
                host=HOST,
                port=PORT,
                keycloak_url="",
                realm=REALM,
                client_id=CLIENT_ID,
                username=USERNAME,
                password=PASSWORD,
            )


class TestTokenExpirationValidation:
    def test_zero_token_expiration_raises(self) -> None:
        with pytest.raises(ValueError, match="token_expiration_in_s"):
            ClientConfig(
                host=HOST,
                port=PORT,
                keycloak_url=KEYCLOAK_URL,
                realm=REALM,
                client_id=CLIENT_ID,
                username=USERNAME,
                password=PASSWORD,
                token_expiration_in_s=0,
            )

    def test_negative_token_expiration_raises(self) -> None:
        with pytest.raises(ValueError, match="token_expiration_in_s"):
            ClientConfig(
                host=HOST,
                port=PORT,
                keycloak_url=KEYCLOAK_URL,
                realm=REALM,
                client_id=CLIENT_ID,
                username=USERNAME,
                password=PASSWORD,
                token_expiration_in_s=-5,
            )


class TestNoClientSecret:
    def test_config_has_no_client_secret_field(self) -> None:
        # Q1: the SDK client is PUBLIC — there must be no client_secret on the config.
        config = ClientConfig(
            host=HOST,
            port=PORT,
            keycloak_url=KEYCLOAK_URL,
            realm=REALM,
            client_id=CLIENT_ID,
            username=USERNAME,
            password=PASSWORD,
        )

        assert not hasattr(config, "client_secret")
