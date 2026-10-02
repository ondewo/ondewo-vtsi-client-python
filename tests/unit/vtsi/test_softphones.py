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
The ``Softphones`` service: generated stubs, the hand-written wrappers and the client wiring.

No network is touched. The gRPC channel factories are patched, and the wrapper tests replace the stub
with a mock, so these tests assert that every RPC of the proto service is reachable through
``client.services.softphones`` with the request and the auth metadata passed through unchanged, and
that the messages carry the contract the proto documents: one-time secrets only in the
create/rotate responses, explicit presence on ``enabled``, and field-mask paths without a prefix.
"""

from typing import (
    Any,
    Dict,
    List,
    Tuple,
)
from unittest.mock import (
    AsyncMock,
    MagicMock,
    patch,
)

import pytest
from google.protobuf.field_mask_pb2 import FieldMask
from google.protobuf.timestamp_pb2 import Timestamp

from ondewo.vtsi import (
    projects_pb2,
    softphones_pb2,
    softphones_pb2_grpc,
)
from ondewo.vtsi.client.async_client import AsyncClient
from ondewo.vtsi.client.client import Client
from ondewo.vtsi.client.client_config import ClientConfig
from ondewo.vtsi.client.services.async_softphones import Softphones as AsyncSoftphones
from ondewo.vtsi.client.services.softphones import Softphones

ACCOUNT_NAME: str = (
    "projects/11111111-1111-1111-1111-111111111111/softphoneAccounts/22222222-2222-2222-2222-222222222222"
)
PROJECT_NAME: str = "projects/11111111-1111-1111-1111-111111111111/project"
METADATA: List[Tuple[str, str]] = [("authorization", "Bearer test-access-token")]

# (wrapper method, stub RPC, request type, response type) for every RPC of the service.
RPCS: List[Tuple[str, str, str, str]] = [
    (
        "create_softphone_account",
        "CreateSoftphoneAccount",
        "CreateSoftphoneAccountRequest",
        "CreateSoftphoneAccountResponse",
    ),
    ("get_softphone_account", "GetSoftphoneAccount", "GetSoftphoneAccountRequest", "SoftphoneAccount"),
    ("update_softphone_account", "UpdateSoftphoneAccount", "UpdateSoftphoneAccountRequest", "SoftphoneAccount"),
    (
        "delete_softphone_account",
        "DeleteSoftphoneAccount",
        "DeleteSoftphoneAccountRequest",
        "DeleteSoftphoneAccountResponse",
    ),
    (
        "list_softphone_accounts",
        "ListSoftphoneAccounts",
        "ListSoftphoneAccountsRequest",
        "ListSoftphoneAccountsResponse",
    ),
    (
        "rotate_softphone_credentials",
        "RotateSoftphoneCredentials",
        "RotateSoftphoneCredentialsRequest",
        "RotateSoftphoneCredentialsResponse",
    ),
    (
        "list_softphone_certificates",
        "ListSoftphoneCertificates",
        "ListSoftphoneCertificatesRequest",
        "ListSoftphoneCertificatesResponse",
    ),
    ("get_softphone_certificate", "GetSoftphoneCertificate", "GetSoftphoneCertificateRequest", "SoftphoneCertificate"),
    (
        "revoke_softphone_certificate",
        "RevokeSoftphoneCertificate",
        "RevokeSoftphoneCertificateRequest",
        "SoftphoneCertificate",
    ),
    (
        "get_softphone_provisioning",
        "GetSoftphoneProvisioning",
        "GetSoftphoneProvisioningRequest",
        "SoftphoneProvisioning",
    ),
]

UPDATABLE_PATHS: List[str] = [
    "display_name",
    "transport_security",
    "enabled",
    "max_contacts",
    "labels",
    "allowed_destinations",
]

SECRET_FIELD_NAMES: List[str] = ["sip_password", "pkcs12_bundle", "pkcs12_password"]


def _config() -> ClientConfig:
    """
    Build an unauthenticated config for an insecure local channel.

    Returns:
        ClientConfig:
            A config pointing to ``localhost:50051`` with no auth.
    """
    return ClientConfig(host="localhost", port="50051")


class TestTheServiceDescriptor:
    """The generated descriptor carries exactly the RPCs the proto defines, with the documented types."""

    def test_every_rpc_has_the_documented_request_and_response(self) -> None:
        """Each method of ``ondewo.vtsi.Softphones`` maps to the request/response pair listed in RPCS."""
        service: Any = softphones_pb2.DESCRIPTOR.services_by_name["Softphones"]
        actual: Dict[str, Tuple[str, str]] = {
            method.name: (method.input_type.name, method.output_type.name) for method in service.methods
        }
        expected: Dict[str, Tuple[str, str]] = {rpc: (request, response) for _, rpc, request, response in RPCS}
        assert actual == expected

    def test_the_stub_binds_every_rpc_to_its_full_method_path(self) -> None:
        """``SoftphonesStub`` registers each RPC under ``/ondewo.vtsi.Softphones/<Rpc>``."""
        channel: MagicMock = MagicMock()
        stub: softphones_pb2_grpc.SoftphonesStub = softphones_pb2_grpc.SoftphonesStub(channel)
        paths: List[str] = [call.args[0] for call in channel.unary_unary.call_args_list]
        assert paths == [f"/ondewo.vtsi.Softphones/{rpc}" for _, rpc, _, _ in RPCS]
        for _, rpc, _, _ in RPCS:
            assert hasattr(stub, rpc)


class TestTheClientExposesTheService:
    """``client.services.softphones`` exists on both clients and is the matching wrapper."""

    def test_sync_client(self) -> None:
        """The sync ``Client`` wires a sync ``Softphones`` wrapper."""
        with patch("grpc.insecure_channel"):
            client: Client = Client(config=_config(), use_secure_channel=False)
        assert isinstance(client.services.softphones, Softphones)

    def test_async_client(self) -> None:
        """The ``AsyncClient`` wires an async ``Softphones`` wrapper."""
        with patch("grpc.aio.insecure_channel"):
            client: AsyncClient = AsyncClient(config=_config(), use_secure_channel=False)
        assert isinstance(client.services.softphones, AsyncSoftphones)


class TestTheWrappersDelegateToTheStub:
    """Every wrapper method forwards the request and the auth metadata to the stub RPC of the same name."""

    @pytest.mark.parametrize("method_name, rpc, request_type, response_type", RPCS)
    def test_sync(self, method_name: str, rpc: str, request_type: str, response_type: str) -> None:
        """The sync wrapper returns what the stub returned for the request it was given."""
        with patch("grpc.insecure_channel"):
            service: Softphones = Softphones(config=_config(), use_secure_channel=False)
        request: Any = getattr(softphones_pb2, request_type)()
        expected: Any = getattr(softphones_pb2, response_type)()
        stub: MagicMock = MagicMock()
        getattr(stub, rpc).return_value = expected
        with (
            patch.object(Softphones, "stub", new=stub),
            patch.object(Softphones, "metadata", new=METADATA),
        ):
            result: Any = getattr(service, method_name)(request=request)
        getattr(stub, rpc).assert_called_once_with(request=request, metadata=METADATA)
        assert result is expected

    @pytest.mark.asyncio
    @pytest.mark.parametrize("method_name, rpc, request_type, response_type", RPCS)
    async def test_async(self, method_name: str, rpc: str, request_type: str, response_type: str) -> None:
        """The async wrapper awaits the stub RPC and returns its result."""
        with patch("grpc.aio.insecure_channel"):
            service: AsyncSoftphones = AsyncSoftphones(config=_config(), use_secure_channel=False)
        request: Any = getattr(softphones_pb2, request_type)()
        expected: Any = getattr(softphones_pb2, response_type)()
        stub: MagicMock = MagicMock()
        setattr(stub, rpc, AsyncMock(return_value=expected))
        with (
            patch.object(AsyncSoftphones, "stub", new=stub),
            patch.object(AsyncSoftphones, "metadata", new=METADATA),
        ):
            result: Any = await getattr(service, method_name)(request=request)
        getattr(stub, rpc).assert_awaited_once_with(request=request, metadata=METADATA)
        assert result is expected


class TestMessages:
    """The messages round-trip and carry the contract the proto documents."""

    def test_a_create_response_round_trips_with_its_one_time_credentials(self) -> None:
        """Account, labels, destinations, timestamps and the PKCS#12 bytes survive serialisation."""
        response: softphones_pb2.CreateSoftphoneAccountResponse = softphones_pb2.CreateSoftphoneAccountResponse(
            softphone_account=softphones_pb2.SoftphoneAccount(
                name=ACCOUNT_NAME,
                vtsi_project_name=PROJECT_NAME,
                display_name="Support desk",
                sip_username="support-01",
                transport_security=softphones_pb2.SOFTPHONE_TRANSPORT_SECURITY_CLIENT_CERTIFICATE,
                enabled=True,
                max_contacts=2,
                labels={"team": "support"},
                allowed_destinations=["100", "_1XX"],
                current_certificate_expire_time=Timestamp(seconds=1_900_000_000),
            ),
            credentials=softphones_pb2.SoftphoneCredentials(
                sip_password="one-time-password",
                pkcs12_bundle=b"\x30\x82\x01\x00",
                pkcs12_password="one-time-p12-password",
                certificate=softphones_pb2.SoftphoneCertificate(
                    status=softphones_pb2.SOFTPHONE_CERTIFICATE_STATUS_ACTIVE,
                ),
            ),
        )
        parsed: softphones_pb2.CreateSoftphoneAccountResponse = softphones_pb2.CreateSoftphoneAccountResponse()
        parsed.ParseFromString(response.SerializeToString())
        assert parsed == response
        assert parsed.softphone_account.labels["team"] == "support"
        assert list(parsed.softphone_account.allowed_destinations) == ["100", "_1XX"]
        assert parsed.credentials.pkcs12_bundle == b"\x30\x82\x01\x00"

    @pytest.mark.parametrize(
        "message_type",
        ["SoftphoneAccount", "SoftphoneCertificate", "SoftphoneProvisioning"],
    )
    def test_no_readable_resource_can_carry_a_secret(self, message_type: str) -> None:
        """Only ``SoftphoneCredentials`` has secret fields; Get/List/provisioning messages have none."""
        # A secret is a string or bytes field; ``sip_password_set_at`` is a Timestamp and says only WHEN.
        secret_like: List[str] = [
            field.name
            for field in getattr(softphones_pb2, message_type).DESCRIPTOR.fields
            if field.message_type is None and ("password" in field.name or "pkcs12" in field.name)
        ]
        assert secret_like == []
        credential_fields: List[str] = [field.name for field in softphones_pb2.SoftphoneCredentials.DESCRIPTOR.fields]
        assert set(SECRET_FIELD_NAMES) <= set(credential_fields)

    def test_enabled_has_explicit_presence(self) -> None:
        """Unset ``enabled`` (create default true) is distinguishable from an explicit ``False``."""
        account: softphones_pb2.SoftphoneAccount = softphones_pb2.SoftphoneAccount()
        assert softphones_pb2.SoftphoneAccount.DESCRIPTOR.fields_by_name["enabled"].has_presence
        assert not account.HasField("enabled")
        account.enabled = False
        assert account.HasField("enabled")
        assert account.SerializeToString() == b"\x38\x00"

    def test_the_zero_transport_security_is_the_unspecified_sentinel(self) -> None:
        """Value 0 is ``UNSPECIFIED``, which the server treats as ``CLIENT_CERTIFICATE``."""
        assert softphones_pb2.SOFTPHONE_TRANSPORT_SECURITY_UNSPECIFIED == 0
        assert (
            softphones_pb2.SoftphoneAccount().transport_security
            == softphones_pb2.SOFTPHONE_TRANSPORT_SECURITY_UNSPECIFIED
        )
        assert softphones_pb2.SOFTPHONE_TRANSPORT_SECURITY_CLIENT_CERTIFICATE == 1
        assert softphones_pb2.SOFTPHONE_TRANSPORT_SECURITY_SERVER_TLS_ONLY == 2


class TestFieldMasks:
    """Field-mask paths are ``SoftphoneAccount`` paths WITHOUT a ``softphone_account.`` prefix."""

    def test_every_updatable_path_is_valid_for_the_account(self) -> None:
        """The documented updatable paths all resolve against ``SoftphoneAccount``."""
        mask: FieldMask = FieldMask(paths=UPDATABLE_PATHS)
        assert mask.IsValidForDescriptor(softphones_pb2.SoftphoneAccount.DESCRIPTOR)

    def test_a_prefixed_path_is_not_a_softphone_account_path(self) -> None:
        """The prefixed form a caller might copy from ``UpdateAgentRequest`` does not resolve."""
        mask: FieldMask = FieldMask(paths=["softphone_account.display_name"])
        assert not mask.IsValidForDescriptor(softphones_pb2.SoftphoneAccount.DESCRIPTOR)

    def test_update_and_list_requests_carry_their_masks(self) -> None:
        """``update_mask`` and ``field_mask`` round-trip on their requests."""
        update: softphones_pb2.UpdateSoftphoneAccountRequest = softphones_pb2.UpdateSoftphoneAccountRequest(
            softphone_account=softphones_pb2.SoftphoneAccount(name=ACCOUNT_NAME, enabled=False),
            update_mask=FieldMask(paths=["enabled"]),
        )
        listing: softphones_pb2.ListSoftphoneAccountsRequest = softphones_pb2.ListSoftphoneAccountsRequest(
            vtsi_project_name=PROJECT_NAME,
            filter=softphones_pb2.SoftphoneAccountFilter(
                transport_securities=[softphones_pb2.SOFTPHONE_TRANSPORT_SECURITY_SERVER_TLS_ONLY],
                enabled=True,
                labels={"team": ""},
            ),
            field_mask=FieldMask(paths=["display_name", "current_certificate_expire_time"]),
            page_size=50,
        )
        for message in (update, listing):
            parsed: Any = type(message)()
            parsed.ParseFromString(message.SerializeToString())
            assert parsed == message
        assert list(listing.field_mask.paths) == ["display_name", "current_certificate_expire_time"]
        assert not listing.HasField("page_token")

    def test_certificate_listing_scope_is_a_oneof(self) -> None:
        """Setting the account scope clears the project scope and vice versa."""
        request: softphones_pb2.ListSoftphoneCertificatesRequest = softphones_pb2.ListSoftphoneCertificatesRequest(
            vtsi_project_name=PROJECT_NAME,
        )
        assert request.WhichOneof("scope") == "vtsi_project_name"
        request.softphone_account_name = ACCOUNT_NAME
        assert request.WhichOneof("scope") == "softphone_account_name"
        assert request.vtsi_project_name == ""


class TestTheSoftphoneSourceAllowList:
    """``AsteriskConfigsVariables.softphone_permit_cidrs`` is the per-project source allow-list of the TLS ports."""

    def test_it_is_a_repeated_string_that_round_trips(self) -> None:
        """A list of CIDR strings; empty means the server's ceiling, so the zero value is the safe default."""
        field: Any = projects_pb2.AsteriskConfigsVariables.DESCRIPTOR.fields_by_name["softphone_permit_cidrs"]
        assert field.number == 11
        assert field.type == field.TYPE_STRING
        assert field.label == field.LABEL_REPEATED
        variables: projects_pb2.AsteriskConfigsVariables = projects_pb2.AsteriskConfigsVariables(
            softphone_permit_cidrs=["203.0.113.0/24", "2001:db8::/32"],
        )
        parsed: projects_pb2.AsteriskConfigsVariables = projects_pb2.AsteriskConfigsVariables.FromString(
            variables.SerializeToString()
        )
        assert list(parsed.softphone_permit_cidrs) == ["203.0.113.0/24", "2001:db8::/32"]
        assert list(projects_pb2.AsteriskConfigsVariables().softphone_permit_cidrs) == []
