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
Minimal example: create a softphone account and print its Zoiper provisioning.

Configuration is read from ``examples/environment.env`` exactly like the projects example. Set
``ONDEWO_VTSI_PROJECT_NAME`` to a deployed project and ``ONDEWO_VTSI_SOFTPHONE_SIP_USERNAME`` to the
SIP user to create, then::

    python -m examples.softphones.create_softphone_account

The create response is the ONLY place the SIP password and the PKCS#12 bundle (client key + certificate)
ever appear. This example writes the bundle to ``<sip_username>.p12`` with mode 0600 and prints the two
passwords once to stdout for the human who configures the softphone; it never passes them to the logger.
A lost secret cannot be fetched again -- rotate it with ``rotate_softphone_credentials``.
"""

import os
import sys
from pathlib import Path

from loguru import logger as log

from examples.projects.get_vtsi_project import (
    _env_bool,
    build_config,
)
from ondewo.vtsi.client.client import Client
from ondewo.vtsi.client.client_config import ClientConfig
from ondewo.vtsi.softphones_pb2 import (
    SOFTPHONE_TRANSPORT_SECURITY_CLIENT_CERTIFICATE,
    CreateSoftphoneAccountRequest,
    CreateSoftphoneAccountResponse,
    GetSoftphoneProvisioningRequest,
    SoftphoneAccount,
    SoftphoneProvisioning,
)


def create_softphone_account(
    client: Client,
    vtsi_project_name: str,
    sip_username: str,
) -> CreateSoftphoneAccountResponse:
    """
    Create a mutual-TLS softphone account in a project.

    Args:
        client (Client):
            A connected VTSI :class:`Client`.
        vtsi_project_name (str):
            Resource name of the project, e.g. ``"projects/<project_uuid>/project"``.
        sip_username (str):
            SIP user (extension) of the new account.

    Returns:
        CreateSoftphoneAccountResponse:
            The account plus its ONE-TIME credentials.
    """
    log.info(f"START: create_softphone_account: sip_username={sip_username!r}")
    request: CreateSoftphoneAccountRequest = CreateSoftphoneAccountRequest(
        vtsi_project_name=vtsi_project_name,
        softphone_account=SoftphoneAccount(
            sip_username=sip_username,
            display_name=sip_username,
            transport_security=SOFTPHONE_TRANSPORT_SECURITY_CLIENT_CERTIFICATE,
            labels={"created_by": "example"},
        ),
    )
    response: CreateSoftphoneAccountResponse = client.services.softphones.create_softphone_account(request=request)
    log.info(
        f"DONE: create_softphone_account: name={response.softphone_account.name!r} "
        f"certificate={response.softphone_account.current_certificate_sha256_fingerprint!r}"
    )
    return response


def write_pkcs12_bundle(pkcs12_bundle: bytes, path: Path) -> None:
    """
    Write the PKCS#12 bundle so only the current user can read it.

    Args:
        pkcs12_bundle (bytes):
            The password-protected PKCS#12 bytes from the create response.
        path (Path):
            Target file; created with mode 0600, never world-readable in between.
    """
    file_descriptor: int = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(file_descriptor, "wb") as handle:
        handle.write(pkcs12_bundle)


def main() -> None:
    """Entry point: create the account, save its bundle and print the provisioning instructions."""
    config: ClientConfig = build_config()
    use_secure_channel: bool = _env_bool("ONDEWO_USE_SECURE_CHANNEL", default=False)
    vtsi_project_name: str = os.environ["ONDEWO_VTSI_PROJECT_NAME"]
    sip_username: str = os.environ["ONDEWO_VTSI_SOFTPHONE_SIP_USERNAME"]

    client: Client = Client(config=config, use_secure_channel=use_secure_channel)
    created: CreateSoftphoneAccountResponse = create_softphone_account(
        client=client,
        vtsi_project_name=vtsi_project_name,
        sip_username=sip_username,
    )
    bundle_path: Path = Path(f"{sip_username}.p12")
    write_pkcs12_bundle(pkcs12_bundle=created.credentials.pkcs12_bundle, path=bundle_path)
    # One-time secrets go to the human on stdout, never through the logger.
    print(f"SIP password (shown once): {created.credentials.sip_password}")
    print(f"PKCS#12 bundle written to {bundle_path}; its password (shown once): {created.credentials.pkcs12_password}")

    provisioning: SoftphoneProvisioning = client.services.softphones.get_softphone_provisioning(
        request=GetSoftphoneProvisioningRequest(name=created.softphone_account.name),
    )
    print(provisioning.zoiper_instructions)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        log.exception("Failed to create the softphone account.")
        sys.exit(1)
