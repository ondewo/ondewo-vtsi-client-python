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
Mock-based tests for the ``examples/softphones/create_softphone_account.py`` example.

No live server is contacted: the VTSI :class:`Client` is replaced with a :class:`unittest.mock.MagicMock`.
"""

import stat
from pathlib import Path
from typing import (
    Any,
    List,
)
from unittest import mock

import pytest

from examples.softphones.create_softphone_account import (
    create_softphone_account,
    main,
    write_pkcs12_bundle,
)
from ondewo.vtsi.softphones_pb2 import (
    SOFTPHONE_TRANSPORT_SECURITY_CLIENT_CERTIFICATE,
    CreateSoftphoneAccountRequest,
    CreateSoftphoneAccountResponse,
    SoftphoneAccount,
    SoftphoneCredentials,
    SoftphoneProvisioning,
)

PROJECT_NAME: str = "projects/11111111-1111-1111-1111-111111111111/project"
ACCOUNT_NAME: str = (
    "projects/11111111-1111-1111-1111-111111111111/softphoneAccounts/22222222-2222-2222-2222-222222222222"
)
SIP_USERNAME: str = "support-01"
SIP_PASSWORD: str = "planted-sip-password"
PKCS12_PASSWORD: str = "planted-p12-password"
PKCS12_BUNDLE: bytes = b"\x30\x82\x01\x00planted"


def _created() -> CreateSoftphoneAccountResponse:
    """
    Build a create response carrying planted one-time secrets.

    Returns:
        CreateSoftphoneAccountResponse:
            The response the mocked service returns.
    """
    return CreateSoftphoneAccountResponse(
        softphone_account=SoftphoneAccount(name=ACCOUNT_NAME, sip_username=SIP_USERNAME),
        credentials=SoftphoneCredentials(
            sip_password=SIP_PASSWORD,
            pkcs12_bundle=PKCS12_BUNDLE,
            pkcs12_password=PKCS12_PASSWORD,
        ),
    )


def test_create_builds_a_client_certificate_account_request() -> None:
    """The helper sends a mutual-TLS account for the given project and user and returns the response."""
    client: mock.MagicMock = mock.MagicMock()
    client.services.softphones.create_softphone_account.return_value = _created()

    result: CreateSoftphoneAccountResponse = create_softphone_account(
        client=client,
        vtsi_project_name=PROJECT_NAME,
        sip_username=SIP_USERNAME,
    )

    sent: Any = client.services.softphones.create_softphone_account.call_args.kwargs["request"]
    assert type(sent) is CreateSoftphoneAccountRequest
    assert sent.vtsi_project_name == PROJECT_NAME
    assert sent.softphone_account.sip_username == SIP_USERNAME
    assert sent.softphone_account.transport_security == SOFTPHONE_TRANSPORT_SECURITY_CLIENT_CERTIFICATE
    assert result.credentials.sip_password == SIP_PASSWORD


def test_the_bundle_is_written_owner_only(tmp_path: Path) -> None:
    """The PKCS#12 file holds the bytes and is readable by its owner alone."""
    path: Path = tmp_path / "support-01.p12"
    write_pkcs12_bundle(pkcs12_bundle=PKCS12_BUNDLE, path=path)
    assert path.read_bytes() == PKCS12_BUNDLE
    assert stat.S_IMODE(path.stat().st_mode) == 0o600


def test_main_prints_secrets_once_and_never_logs_them(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """``main`` saves the bundle, prints the instructions, and the logger never sees a secret."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("ONDEWO_HOST", "localhost")
    monkeypatch.setenv("ONDEWO_PORT", "50200")
    monkeypatch.setenv("ONDEWO_USE_SECURE_CHANNEL", "false")
    monkeypatch.setenv("ONDEWO_VTSI_PROJECT_NAME", PROJECT_NAME)
    monkeypatch.setenv("ONDEWO_VTSI_SOFTPHONE_SIP_USERNAME", SIP_USERNAME)
    logged: List[str] = []

    with (
        mock.patch("examples.softphones.create_softphone_account.Client") as client_cls,
        mock.patch("examples.softphones.create_softphone_account.log") as log,
    ):
        softphones: Any = client_cls.return_value.services.softphones
        softphones.create_softphone_account.return_value = _created()
        softphones.get_softphone_provisioning.return_value = SoftphoneProvisioning(
            zoiper_instructions="1. Accounts > Add account",
        )
        main()
        logged = [str(call) for call in log.mock_calls]

    assert (tmp_path / f"{SIP_USERNAME}.p12").read_bytes() == PKCS12_BUNDLE
    assert softphones.get_softphone_provisioning.call_args.kwargs["request"].name == ACCOUNT_NAME
    printed: str = capsys.readouterr().out
    assert SIP_PASSWORD in printed and PKCS12_PASSWORD in printed
    assert "1. Accounts > Add account" in printed
    assert logged, "the example logs its START/DONE lines"
    assert not [line for line in logged if SIP_PASSWORD in line or PKCS12_PASSWORD in line]
