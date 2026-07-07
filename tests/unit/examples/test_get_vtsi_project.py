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
Mock-based tests for the ``examples/projects/get_vtsi_project.py`` example.

No live server is contacted: the VTSI :class:`Client` (and the gRPC stub underneath it) is
replaced with a :class:`unittest.mock.MagicMock`, so the tests assert only that the example
builds the correct request message and returns / prints the handled response.
"""
from typing import Any
from unittest import mock

import pytest

from examples.projects.get_vtsi_project import (
    build_config,
    get_vtsi_project,
    main,
)
from ondewo.vtsi.projects_pb2 import (
    GetVtsiProjectRequest,
    VtsiProject,
)

# Bound exactly once so a refactor that changes only an input or only an expectation cannot
# silently make a test tautological.
HOST: str = "localhost"
PORT: str = "50200"
PROJECT_NAME: str = "projects/11111111-1111-1111-1111-111111111111/project"
DISPLAY_NAME: str = "My VTSI Project"
KEYCLOAK_URL: str = "https://keycloak.example.com/auth"
REALM: str = "ondewo-ccai-platform"
CLIENT_ID: str = "ondewo-nlu-cai-sdk-public"
USERNAME: str = "tech-user@example.com"
PASSWORD: str = "s3cr3t-pw"
_KEYCLOAK_ENV_VARS = (
    "KEYCLOAK_URL",
    "KEYCLOAK_REALM",
    "KEYCLOAK_CLIENT_ID",
    "KEYCLOAK_USER_NAME",
    "KEYCLOAK_PASSWORD",
)


class TestBuildConfig:
    """Tests for the ``build_config`` helper's two auth modes."""

    def test_without_keycloak_fields_is_valid_and_unflagged(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Omitting the Keycloak fields yields a valid config that does not opt into D18 auth."""
        monkeypatch.setenv("ONDEWO_HOST", HOST)
        monkeypatch.setenv("ONDEWO_PORT", PORT)
        for name in _KEYCLOAK_ENV_VARS:
            monkeypatch.delenv(name, raising=False)

        config = build_config()

        assert config.host == HOST
        assert config.port == PORT
        assert config.is_keycloak_auth_configured is False

    def test_with_keycloak_fields_opts_into_d18_auth(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Providing the full Keycloak field set flips ``is_keycloak_auth_configured`` on."""
        monkeypatch.setenv("ONDEWO_HOST", HOST)
        monkeypatch.setenv("ONDEWO_PORT", PORT)
        monkeypatch.setenv("KEYCLOAK_URL", KEYCLOAK_URL)
        monkeypatch.setenv("KEYCLOAK_REALM", REALM)
        monkeypatch.setenv("KEYCLOAK_CLIENT_ID", CLIENT_ID)
        monkeypatch.setenv("KEYCLOAK_USER_NAME", USERNAME)
        monkeypatch.setenv("KEYCLOAK_PASSWORD", PASSWORD)

        config = build_config()

        assert config.is_keycloak_auth_configured is True
        assert config.client_id == CLIENT_ID
        # Q1: the SDK client is public — the config must never carry a client_secret.
        assert not hasattr(config, "client_secret")


class TestGetVtsiProject:
    """Tests for the ``get_vtsi_project`` RPC wrapper against a mocked client."""

    def test_builds_request_and_returns_response(self) -> None:
        """The helper sends ``GetVtsiProjectRequest(name=...)`` and returns the stub's response."""
        expected_project = VtsiProject(name=PROJECT_NAME, display_name=DISPLAY_NAME)
        client = mock.MagicMock()
        client.services.projects.get_vtsi_project.return_value = expected_project

        result = get_vtsi_project(client=client, vtsi_project_name=PROJECT_NAME)

        client.services.projects.get_vtsi_project.assert_called_once()
        sent_request: Any = client.services.projects.get_vtsi_project.call_args.kwargs["request"]
        assert type(sent_request) is GetVtsiProjectRequest
        assert sent_request.name == PROJECT_NAME
        assert result is expected_project


class TestMain:
    """End-to-end test of ``main`` with the ``Client`` class patched out."""

    def test_main_constructs_client_and_fetches_project(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """``main`` reads the environment, builds an insecure client, and fetches the project."""
        expected_project = VtsiProject(name=PROJECT_NAME, display_name=DISPLAY_NAME)
        monkeypatch.setenv("ONDEWO_HOST", HOST)
        monkeypatch.setenv("ONDEWO_PORT", PORT)
        monkeypatch.setenv("ONDEWO_USE_SECURE_CHANNEL", "false")
        monkeypatch.setenv("ONDEWO_VTSI_PROJECT_NAME", PROJECT_NAME)
        for name in _KEYCLOAK_ENV_VARS:
            monkeypatch.delenv(name, raising=False)

        with mock.patch("examples.projects.get_vtsi_project.Client") as client_cls:
            client_cls.return_value.services.projects.get_vtsi_project.return_value = expected_project
            main()

        client_cls.assert_called_once()
        assert client_cls.call_args.kwargs["use_secure_channel"] is False
        config: Any = client_cls.call_args.kwargs["config"]
        assert config.host == HOST
        assert config.port == PORT

        get_project = client_cls.return_value.services.projects.get_vtsi_project
        get_project.assert_called_once()
        sent_request: Any = get_project.call_args.kwargs["request"]
        assert sent_request.name == PROJECT_NAME
