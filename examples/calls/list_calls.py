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

Run it against a local, insecure server::

    python -m examples.calls.list_calls \\
        --host localhost --port 50200 \\
        --vtsi-project-name "projects/<project_uuid>/project"

Authentication is the D18 Keycloak offline-token (bearer) flow configured on
:class:`ondewo.vtsi.client.client_config.ClientConfig`; see
``examples/projects/get_vtsi_project.py`` for the full auth notes.
"""
import argparse
from typing import Optional

from ondewo.vtsi.calls_pb2 import (
    ListCallsRequest,
    ListCallsResponse,
)
from ondewo.vtsi.client.client import Client
from ondewo.vtsi.client.client_config import ClientConfig


def build_config(
    host: str,
    port: str,
    keycloak_url: Optional[str] = None,
    realm: Optional[str] = None,
    client_id: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    grpc_cert: Optional[str] = None,
) -> ClientConfig:
    """
    Build a :class:`ClientConfig` for the VTSI client.

    When the Keycloak fields are all provided the config opts into the D18 offline-token
    (bearer) auth flow; when they are all omitted a plain host/port config is returned.

    Args:
        host (str):
            Hostname / IP of the ONDEWO VTSI server, e.g. ``"localhost"``.
        port (str):
            Port of the ONDEWO VTSI server, e.g. ``"50200"``.
        keycloak_url (Optional[str]):
            Base URL of the Keycloak server.
        realm (Optional[str]):
            Keycloak realm name.
        client_id (Optional[str]):
            Id of the public Keycloak SDK client (no secret).
        username (Optional[str]):
            Username / email of the technical user for the ROPC grant.
        password (Optional[str]):
            Password of that user.
        grpc_cert (Optional[str]):
            PEM certificate for a secure channel; omit for an insecure channel.

    Returns:
        ClientConfig:
            The configuration to hand to :class:`Client`.
    """
    return ClientConfig(
        host=host,
        port=port,
        grpc_cert=grpc_cert,
        keycloak_url=keycloak_url,
        realm=realm,
        client_id=client_id,
        username=username,
        password=password,
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
    """
    request: ListCallsRequest = ListCallsRequest(vtsi_project_name=vtsi_project_name)
    response: ListCallsResponse = client.services.calls.list_calls(request=request)
    return response


def _parse_args() -> argparse.Namespace:
    """Parse the command-line arguments for the example."""
    parser = argparse.ArgumentParser(description="List the calls of a VTSI project.")
    parser.add_argument("--host", default="localhost", help="VTSI server host.")
    parser.add_argument("--port", default="50200", help="VTSI server port.")
    parser.add_argument("--vtsi-project-name", required=True, help="Resource name of the VTSI project.")
    parser.add_argument("--keycloak-url", default=None, help="Keycloak base URL (D18 auth).")
    parser.add_argument("--realm", default=None, help="Keycloak realm (D18 auth).")
    parser.add_argument("--client-id", default=None, help="Public Keycloak client id (D18 auth).")
    parser.add_argument("--username", default=None, help="Technical-user username (D18 auth).")
    parser.add_argument("--password", default=None, help="Technical-user password (D18 auth).")
    parser.add_argument(
        "--secure",
        action="store_true",
        help="Use a secure gRPC channel (default is insecure).",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point: build the client, list the project's calls, and print how many were returned."""
    args: argparse.Namespace = _parse_args()
    config: ClientConfig = build_config(
        host=args.host,
        port=args.port,
        keycloak_url=args.keycloak_url,
        realm=args.realm,
        client_id=args.client_id,
        username=args.username,
        password=args.password,
    )
    client: Client = Client(config=config, use_secure_channel=args.secure)
    response: ListCallsResponse = list_calls(client=client, vtsi_project_name=args.vtsi_project_name)
    print(f"Listed {len(response.calls)} call(s) for project {args.vtsi_project_name!r}.")


if __name__ == "__main__":
    main()
