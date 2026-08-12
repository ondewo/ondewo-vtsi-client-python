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
Mock-based tests for the ``examples/calls/list_calls.py`` example.

No live server is contacted: the VTSI :class:`Client` (and the gRPC stub underneath it) is
replaced with a :class:`unittest.mock.MagicMock`, so the tests assert only that the example
builds the correct request message and returns / prints the handled response.
"""

from typing import Any
from unittest import mock

import pytest

from examples.calls.list_calls import (
    build_config,
    list_calls,
    main,
)
from ondewo.vtsi.calls_pb2 import (
    Call,
    ListCallsRequest,
    ListCallsResponse,
)

# Bound exactly once so a refactor that changes only an input or only an expectation cannot
# silently make a test tautological.
HOST: str = "localhost"
PORT: str = "50200"
PROJECT_NAME: str = "projects/22222222-2222-2222-2222-222222222222/project"
CALL_NAME: str = "projects/22222222-2222-2222-2222-222222222222/calls/abc"
_KEYCLOAK_ENV_VARS = (
    "KEYCLOAK_URL",
    "KEYCLOAK_REALM",
    "KEYCLOAK_CLIENT_ID",
    "KEYCLOAK_USER_NAME",
    "KEYCLOAK_PASSWORD",
)


class TestBuildConfig:
    """Tests for the ``build_config`` helper's default (no-Keycloak) mode."""

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


class TestListCalls:
    """Tests for the ``list_calls`` RPC wrapper against a mocked client."""

    def test_builds_request_and_returns_response(self) -> None:
        """The helper sends ``ListCallsRequest(vtsi_project_name=...)`` and returns the response."""
        expected_response = ListCallsResponse(calls=[Call(name=CALL_NAME)])
        client = mock.MagicMock()
        client.services.calls.list_calls.return_value = expected_response

        result = list_calls(client=client, vtsi_project_name=PROJECT_NAME)

        client.services.calls.list_calls.assert_called_once()
        sent_request: Any = client.services.calls.list_calls.call_args.kwargs["request"]
        assert type(sent_request) is ListCallsRequest
        assert sent_request.vtsi_project_name == PROJECT_NAME
        assert result is expected_response


class TestMain:
    """End-to-end test of ``main`` with the ``Client`` class patched out."""

    def test_main_constructs_client_and_lists_calls(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """``main`` reads the environment, builds an insecure client, and lists the calls."""
        expected_response = ListCallsResponse(calls=[Call(name=CALL_NAME)])
        monkeypatch.setenv("ONDEWO_HOST", HOST)
        monkeypatch.setenv("ONDEWO_PORT", PORT)
        monkeypatch.setenv("ONDEWO_USE_SECURE_CHANNEL", "false")
        monkeypatch.setenv("ONDEWO_VTSI_PROJECT_NAME", PROJECT_NAME)
        for name in _KEYCLOAK_ENV_VARS:
            monkeypatch.delenv(name, raising=False)

        with mock.patch("examples.calls.list_calls.Client") as client_cls:
            client_cls.return_value.services.calls.list_calls.return_value = expected_response
            main()

        client_cls.assert_called_once()
        assert client_cls.call_args.kwargs["use_secure_channel"] is False

        list_calls_stub = client_cls.return_value.services.calls.list_calls
        list_calls_stub.assert_called_once()
        sent_request: Any = list_calls_stub.call_args.kwargs["request"]
        assert sent_request.vtsi_project_name == PROJECT_NAME
