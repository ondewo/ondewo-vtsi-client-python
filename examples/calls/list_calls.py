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
Minimal example: list the calls of a VTSI project through the Calls service.

Configuration is read from ``examples/environment.env`` (loaded via python-dotenv
relative to this script, so the current working directory does not matter). Run it
against a local, insecure server by setting ``ONDEWO_HOST`` / ``ONDEWO_PORT`` /
``ONDEWO_VTSI_PROJECT_NAME`` there and then::

    python -m examples.calls.list_calls

Authentication is the D18 Keycloak offline-token (bearer) flow configured on
:class:`ondewo.vtsi.client.client_config.ClientConfig` via the ``KEYCLOAK_*`` env
vars; see ``examples/projects/get_vtsi_project.py`` for the full auth notes.
"""
import os
import sys
from pathlib import Path
from typing import Optional

import grpc
from dotenv import load_dotenv
from loguru import logger as log

from ondewo.vtsi.calls_pb2 import (
    ListCallsRequest,
    ListCallsResponse,
)
from ondewo.vtsi.client.client import Client
from ondewo.vtsi.client.client_config import ClientConfig

load_dotenv(Path(__file__).resolve().parent.parent / "environment.env")


def _env_or_none(name: str) -> Optional[str]:
    """
    Read an environment variable, treating an unset or empty value as ``None``.

    Args:
        name (str):
            Name of the environment variable.

    Returns:
        Optional[str]:
            The stripped value, or ``None`` if unset/empty.
    """
    value: Optional[str] = os.getenv(name)
    if value is None or not value.strip():
        return None
    return value.strip()


def _env_bool(name: str, default: bool) -> bool:
    """
    Read a boolean environment variable (``true``/``false``, case-insensitive).

    Args:
        name (str):
            Name of the environment variable.
        default (bool):
            Value to use when the variable is unset/empty.

    Returns:
        bool:
            The parsed boolean.
    """
    value: Optional[str] = _env_or_none(name)
    if value is None:
        return default
    return value.lower() in ("1", "true", "yes", "on")


def build_config() -> ClientConfig:
    """
    Build a :class:`ClientConfig` for the VTSI client from the environment.

    Reads the canonical ``ONDEWO_*`` / ``KEYCLOAK_*`` variables. When the Keycloak
    fields are provided the config opts into the D18 offline-token (bearer) auth
    flow; when they are all omitted a plain host/port config is returned.

    Returns:
        ClientConfig:
            The configuration to hand to :class:`Client`.
    """
    return ClientConfig(
        host=os.environ["ONDEWO_HOST"],
        port=os.environ["ONDEWO_PORT"],
        grpc_cert=_env_or_none("ONDEWO_GRPC_CERT"),
        keycloak_url=_env_or_none("KEYCLOAK_URL"),
        realm=_env_or_none("KEYCLOAK_REALM"),
        client_id=_env_or_none("KEYCLOAK_CLIENT_ID"),
        username=_env_or_none("KEYCLOAK_USER_NAME"),
        password=_env_or_none("KEYCLOAK_PASSWORD"),
        keycloak_verify_ssl=_env_bool("KEYCLOAK_VERIFY_SSL", default=True),
    )


def list_calls(client: Client, vtsi_project_name: str) -> ListCallsResponse:
    """
    List the calls belonging to a VTSI project.

    Args:
        client (Client):
            A connected VTSI :class:`Client`.
        vtsi_project_name (str):
            Resource name of the project, e.g. ``"projects/<project_uuid>/project"``.

    Returns:
        ListCallsResponse:
            The response carrying the project's calls and the next-page token.

    Raises:
        grpc.RpcError:
            If the Calls service call fails.
    """
    log.info(f"START: list_calls: vtsi_project_name={vtsi_project_name!r}")
    request: ListCallsRequest = ListCallsRequest(vtsi_project_name=vtsi_project_name)
    try:
        response: ListCallsResponse = client.services.calls.list_calls(request=request)
    except grpc.RpcError as rpc_error:
        log.error(f"gRPC ListCalls failed: code={rpc_error.code()} details={rpc_error.details()}")
        raise
    log.info(f"DONE: list_calls: received {len(response.calls)} call(s)")
    return response


def main() -> None:
    """Entry point: build the client, list the project's calls, and log how many were returned."""
    config: ClientConfig = build_config()
    use_secure_channel: bool = _env_bool("ONDEWO_USE_SECURE_CHANNEL", default=False)
    vtsi_project_name: str = os.environ["ONDEWO_VTSI_PROJECT_NAME"]

    log.info(f"Connecting to VTSI at {config.host}:{config.port} (secure={use_secure_channel})")
    client: Client = Client(config=config, use_secure_channel=use_secure_channel)
    response: ListCallsResponse = list_calls(client=client, vtsi_project_name=vtsi_project_name)
    log.info(f"Listed {len(response.calls)} call(s) for project {vtsi_project_name!r}.")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        log.exception("Failed to list VTSI calls.")
        sys.exit(1)
