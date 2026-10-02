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
The ``Campaigns`` and ``Events`` services and the three ``Calls`` status streams.

No network is touched. The gRPC channel factories are patched and the stub is replaced by a mock, so
these tests assert that every RPC of the two new proto services is reachable through
``client.services.campaigns`` / ``client.services.events``, that the request and the auth metadata
are passed through unchanged, and — the part a generated async wrapper gets wrong — that a
server-streaming RPC is returned as an iterator and never awaited.
"""

from pathlib import Path
from types import ModuleType
from typing import (
    Any,
    Dict,
    List,
    Tuple,
    Type,
)
from unittest.mock import (
    AsyncMock,
    MagicMock,
    patch,
)

import pytest

from ondewo.vtsi import (
    calls_pb2,
    calls_pb2_grpc,
    campaigns_pb2,
    campaigns_pb2_grpc,
    events_pb2,
    events_pb2_grpc,
)
from ondewo.vtsi.client.async_client import AsyncClient
from ondewo.vtsi.client.client import Client
from ondewo.vtsi.client.client_config import ClientConfig
from ondewo.vtsi.client.services import (
    async_calls,
    async_campaigns,
    async_events,
)
from ondewo.vtsi.client.services.async_calls import Calls as AsyncCalls
from ondewo.vtsi.client.services.async_campaigns import Campaigns as AsyncCampaigns
from ondewo.vtsi.client.services.async_events import Events as AsyncEvents
from ondewo.vtsi.client.services.calls import Calls
from ondewo.vtsi.client.services.campaigns import Campaigns
from ondewo.vtsi.client.services.events import Events

METADATA: List[Tuple[str, str]] = [("authorization", "Bearer test-access-token")]
HAND_WRITTEN_ASYNC_MARKER: str = "ondewo:hand-written-async-service"

# (wrapper method, stub RPC, request type, response type, server-streaming)
Rpc = Tuple[str, str, str, str, bool]

CAMPAIGN_RPCS: List[Rpc] = [
    ("create_campaign", "CreateCampaign", "CreateCampaignRequest", "Campaign", False),
    ("get_campaign", "GetCampaign", "GetCampaignRequest", "Campaign", False),
    ("update_campaign", "UpdateCampaign", "UpdateCampaignRequest", "Campaign", False),
    ("delete_campaign", "DeleteCampaign", "DeleteCampaignRequest", "DeleteCampaignResponse", False),
    ("list_campaigns", "ListCampaigns", "ListCampaignsRequest", "ListCampaignsResponse", False),
    ("get_campaign_statistics", "GetCampaignStatistics", "GetCampaignStatisticsRequest", "CampaignStatistics", False),
    ("list_campaign_calls", "ListCampaignCalls", "ListCampaignCallsRequest", "ListCampaignCallsResponse", False),
    ("start_campaign", "StartCampaign", "StartCampaignRequest", "Campaign", False),
    ("stop_campaign", "StopCampaign", "StopCampaignRequest", "Campaign", False),
    ("hard_stop_campaign", "HardStopCampaign", "HardStopCampaignRequest", "Campaign", False),
    ("resume_campaign", "ResumeCampaign", "ResumeCampaignRequest", "Campaign", False),
    (
        "stream_campaign_status",
        "StreamCampaignStatus",
        "StreamCampaignStatusRequest",
        "StreamCampaignStatusResponse",
        True,
    ),
]

EVENT_RPCS: List[Rpc] = [
    (
        "create_vtsi_event_subscription",
        "CreateVtsiEventSubscription",
        "CreateVtsiEventSubscriptionRequest",
        "VtsiEventSubscription",
        False,
    ),
    (
        "get_vtsi_event_subscription",
        "GetVtsiEventSubscription",
        "GetVtsiEventSubscriptionRequest",
        "VtsiEventSubscription",
        False,
    ),
    (
        "update_vtsi_event_subscription",
        "UpdateVtsiEventSubscription",
        "UpdateVtsiEventSubscriptionRequest",
        "VtsiEventSubscription",
        False,
    ),
    (
        "delete_vtsi_event_subscription",
        "DeleteVtsiEventSubscription",
        "DeleteVtsiEventSubscriptionRequest",
        "DeleteVtsiEventSubscriptionResponse",
        False,
    ),
    (
        "list_vtsi_event_subscriptions",
        "ListVtsiEventSubscriptions",
        "ListVtsiEventSubscriptionsRequest",
        "ListVtsiEventSubscriptionsResponse",
        False,
    ),
    ("create_webhook", "CreateWebhook", "CreateWebhookRequest", "Webhook", False),
    ("get_webhook", "GetWebhook", "GetWebhookRequest", "Webhook", False),
    ("update_webhook", "UpdateWebhook", "UpdateWebhookRequest", "Webhook", False),
    ("delete_webhook", "DeleteWebhook", "DeleteWebhookRequest", "DeleteWebhookResponse", False),
    ("list_webhooks", "ListWebhooks", "ListWebhooksRequest", "ListWebhooksResponse", False),
    ("test_webhook", "TestWebhook", "TestWebhookRequest", "TestWebhookResponse", False),
    ("subscribe_vtsi_events", "SubscribeVtsiEvents", "SubscribeVtsiEventsRequest", "SubscribeVtsiEventsResponse", True),
]

CALL_STREAM_RPCS: List[Rpc] = [
    (
        "stream_caller_status",
        "StreamCallerStatus",
        "StreamCallerStatusRequest",
        "StreamCallResourceStatusResponse",
        True,
    ),
    (
        "stream_listener_status",
        "StreamListenerStatus",
        "StreamListenerStatusRequest",
        "StreamCallResourceStatusResponse",
        True,
    ),
    (
        "stream_scheduled_caller_status",
        "StreamScheduledCallerStatus",
        "StreamScheduledCallerStatusRequest",
        "StreamCallResourceStatusResponse",
        True,
    ),
]

# (service name, pb2 module, stub class, sync wrapper, async wrapper, rpcs)
SERVICES: List[Tuple[str, ModuleType, Type[Any], Type[Any], Type[Any], List[Rpc]]] = [
    ("Campaigns", campaigns_pb2, campaigns_pb2_grpc.CampaignsStub, Campaigns, AsyncCampaigns, CAMPAIGN_RPCS),
    ("Events", events_pb2, events_pb2_grpc.EventsStub, Events, AsyncEvents, EVENT_RPCS),
]

# Every wrapper case: (sync wrapper, async wrapper, pb2 module, rpc tuple)
WRAPPER_CASES: List[Tuple[Type[Any], Type[Any], ModuleType, Rpc]] = [
    (sync, asynchronous, module, rpc) for _, module, _, sync, asynchronous, rpcs in SERVICES for rpc in rpcs
] + [(Calls, AsyncCalls, calls_pb2, rpc) for rpc in CALL_STREAM_RPCS]


def _config() -> ClientConfig:
    """
    Build an unauthenticated config for an insecure local channel.

    Returns:
        ClientConfig:
            A config pointing to ``localhost:50051`` with no auth.
    """
    return ClientConfig(host="localhost", port="50051")


def _case_id(case: Tuple[Type[Any], Type[Any], ModuleType, Rpc]) -> str:
    """
    Name a wrapper case after its RPC.

    Args:
        case (Tuple[Type[Any], Type[Any], ModuleType, Rpc]):
            The wrapper case.

    Returns:
        str:
            ``<Service>.<Rpc>``.
    """
    return f"{case[0].__name__}.{case[3][1]}"


class TestTheServiceDescriptors:
    """The generated descriptors carry exactly the RPCs listed here, with the documented types."""

    @pytest.mark.parametrize("service_name, module, stub_class, sync, asynchronous, rpcs", SERVICES)
    def test_every_rpc_has_the_documented_request_response_and_streaming_kind(
        self,
        service_name: str,
        module: ModuleType,
        stub_class: Type[Any],
        sync: Type[Any],
        asynchronous: Type[Any],
        rpcs: List[Rpc],
    ) -> None:
        """Each method of the service maps to the request/response pair and streaming kind listed here."""
        service: Any = module.DESCRIPTOR.services_by_name[service_name]
        actual: Dict[str, Tuple[str, str, bool]] = {
            method.name: (method.input_type.name, method.output_type.name, method.server_streaming)
            for method in service.methods
        }
        expected: Dict[str, Tuple[str, str, bool]] = {
            rpc: (request, response, streaming) for _, rpc, request, response, streaming in rpcs
        }
        assert actual == expected

    @pytest.mark.parametrize("service_name, module, stub_class, sync, asynchronous, rpcs", SERVICES)
    def test_the_stub_binds_unary_and_streaming_rpcs_to_their_full_method_paths(
        self,
        service_name: str,
        module: ModuleType,
        stub_class: Type[Any],
        sync: Type[Any],
        asynchronous: Type[Any],
        rpcs: List[Rpc],
    ) -> None:
        """The stub registers unary RPCs via ``unary_unary`` and streams via ``unary_stream``."""
        channel: MagicMock = MagicMock()
        stub_class(channel)
        unary: List[str] = [call.args[0] for call in channel.unary_unary.call_args_list]
        streaming: List[str] = [call.args[0] for call in channel.unary_stream.call_args_list]
        assert unary == [f"/ondewo.vtsi.{service_name}/{rpc}" for _, rpc, _, _, is_stream in rpcs if not is_stream]
        assert streaming == [f"/ondewo.vtsi.{service_name}/{rpc}" for _, rpc, _, _, is_stream in rpcs if is_stream]

    def test_the_calls_service_carries_the_three_status_streams(self) -> None:
        """``Calls`` gained exactly the three server-streaming status RPCs."""
        service: Any = calls_pb2.DESCRIPTOR.services_by_name["Calls"]
        actual: Dict[str, Tuple[str, str]] = {
            method.name: (method.input_type.name, method.output_type.name)
            for method in service.methods
            if method.server_streaming
        }
        assert actual == {rpc: (request, response) for _, rpc, request, response, _ in CALL_STREAM_RPCS}
        channel: MagicMock = MagicMock()
        calls_pb2_grpc.CallsStub(channel)
        streaming: List[str] = [call.args[0] for call in channel.unary_stream.call_args_list]
        assert streaming == [f"/ondewo.vtsi.Calls/{rpc}" for _, rpc, _, _, _ in CALL_STREAM_RPCS]


class TestTheClientExposesTheServices:
    """``client.services.campaigns`` and ``client.services.events`` exist on both clients."""

    def test_sync_client(self) -> None:
        """The sync ``Client`` wires the sync wrappers."""
        with patch("grpc.insecure_channel"):
            client: Client = Client(config=_config(), use_secure_channel=False)
        assert isinstance(client.services.campaigns, Campaigns)
        assert isinstance(client.services.events, Events)

    def test_async_client(self) -> None:
        """The ``AsyncClient`` wires the async wrappers."""
        with patch("grpc.aio.insecure_channel"):
            client: AsyncClient = AsyncClient(config=_config(), use_secure_channel=False)
        assert isinstance(client.services.campaigns, AsyncCampaigns)
        assert isinstance(client.services.events, AsyncEvents)


class TestTheWrappersDelegateToTheStub:
    """Every wrapper method forwards the request and the auth metadata to the stub RPC of the same name."""

    @pytest.mark.parametrize("case", WRAPPER_CASES, ids=_case_id)
    def test_sync(self, case: Tuple[Type[Any], Type[Any], ModuleType, Rpc]) -> None:
        """The sync wrapper returns what the stub returned (the response, or the stream iterator)."""
        sync, _, module, (method_name, rpc, request_type, _, _) = case
        with patch("grpc.insecure_channel"):
            service: Any = sync(config=_config(), use_secure_channel=False)
        request: Any = getattr(module, request_type)()
        expected: object = object()
        stub: MagicMock = MagicMock()
        getattr(stub, rpc).return_value = expected
        with (
            patch.object(sync, "stub", new=stub),
            patch.object(sync, "metadata", new=METADATA),
        ):
            result: Any = getattr(service, method_name)(request=request)
        getattr(stub, rpc).assert_called_once_with(request=request, metadata=METADATA)
        assert result is expected

    @pytest.mark.asyncio
    @pytest.mark.parametrize("case", WRAPPER_CASES, ids=_case_id)
    async def test_async(self, case: Tuple[Type[Any], Type[Any], ModuleType, Rpc]) -> None:
        """
        A unary async wrapper awaits the stub; a streaming one returns the call object WITHOUT awaiting it.

        grpc.aio returns an awaitable for a unary RPC and an async iterator for a server-streaming one, so
        a streaming wrapper must be a plain method returning the stub's result as is.
        """
        _, asynchronous, module, (method_name, rpc, request_type, _, streaming) = case
        with patch("grpc.aio.insecure_channel"):
            service: Any = asynchronous(config=_config(), use_secure_channel=False)
        request: Any = getattr(module, request_type)()
        expected: object = object()
        stub: MagicMock = MagicMock()
        if streaming:
            getattr(stub, rpc).return_value = expected
        else:
            setattr(stub, rpc, AsyncMock(return_value=expected))
        with (
            patch.object(asynchronous, "stub", new=stub),
            patch.object(asynchronous, "metadata", new=METADATA),
        ):
            if streaming:
                result: Any = getattr(service, method_name)(request=request)
            else:
                result = await getattr(service, method_name)(request=request)
        if streaming:
            getattr(stub, rpc).assert_called_once_with(request=request, metadata=METADATA)
        else:
            getattr(stub, rpc).assert_awaited_once_with(request=request, metadata=METADATA)
        assert result is expected

    @pytest.mark.parametrize("module", [async_calls, async_campaigns, async_events], ids=lambda m: m.__name__)
    def test_every_async_module_with_a_stream_survives_make_build(self, module: ModuleType) -> None:
        """
        Each async module containing a streaming RPC carries the marker that ``create_async_services`` keeps.

        Without it ``make build`` regenerates the file from its sync twin and awaits the stream.
        """
        assert module.__file__ is not None
        assert HAND_WRITTEN_ASYNC_MARKER in Path(module.__file__).read_text()


class TestCampaignMessages:
    """The campaign contract a client depends on, read from the generated messages."""

    def test_start_callers_and_start_scheduled_callers_take_a_campaign_assignment(self) -> None:
        """Both batch start requests carry an optional ``campaign_assignment``; the responses the campaign."""
        for request_type in (calls_pb2.StartCallersRequest, calls_pb2.StartScheduledCallersRequest):
            field: Any = request_type.DESCRIPTOR.fields_by_name["campaign_assignment"]
            assert field.message_type is campaigns_pb2.CampaignAssignment.DESCRIPTOR
            assert field.has_presence
        for response_type in (calls_pb2.StartCallersResponse, calls_pb2.StartScheduledCallersResponse):
            assert response_type.DESCRIPTOR.fields_by_name["campaign"].message_type is campaigns_pb2.Campaign.DESCRIPTOR
            response: Any = response_type(campaign_call_names=["a", "b"])
            assert list(response.campaign_call_names) == ["a", "b"]

    def test_a_campaign_assignment_selects_exactly_one_campaign(self) -> None:
        """Existing campaign by name or display name, or a new one, are alternatives of one oneof."""
        assignment: campaigns_pb2.CampaignAssignment = campaigns_pb2.CampaignAssignment(
            new_campaign=campaigns_pb2.Campaign(display_name="spring", max_parallel_calls=10, max_attempts=3),
            start_mode=campaigns_pb2.CAMPAIGN_START_MODE_START,
        )
        assert assignment.WhichOneof("campaign_selector") == "new_campaign"
        assignment.campaign_display_name.CopyFrom(
            campaigns_pb2.CampaignDisplayName(vtsi_project_name="projects/p/project", display_name="spring")
        )
        assert assignment.WhichOneof("campaign_selector") == "campaign_display_name"
        assert not assignment.HasField("new_campaign")
        request: calls_pb2.StartCallersRequest = calls_pb2.StartCallersRequest(campaign_assignment=assignment)
        assert calls_pb2.StartCallersRequest.FromString(request.SerializeToString()) == request

    def test_the_zero_start_mode_is_the_unspecified_sentinel(self) -> None:
        """An unset start mode is ``CAMPAIGN_START_MODE_UNSPECIFIED``, the documented default."""
        assert campaigns_pb2.CampaignAssignment().start_mode == campaigns_pb2.CAMPAIGN_START_MODE_UNSPECIFIED == 0

    def test_the_campaign_states_cover_start_stop_hard_stop_and_completion(self) -> None:
        """The lifecycle states the API documents exist, prefixed with their enum name."""
        assert [value.name for value in campaigns_pb2.CampaignState.DESCRIPTOR.values] == [
            "CAMPAIGN_STATE_UNSPECIFIED",
            "CAMPAIGN_STATE_CREATED",
            "CAMPAIGN_STATE_RUNNING",
            "CAMPAIGN_STATE_STOPPING",
            "CAMPAIGN_STATE_STOPPED",
            "CAMPAIGN_STATE_HARD_STOPPING",
            "CAMPAIGN_STATE_HARD_STOPPED",
            "CAMPAIGN_STATE_COMPLETED",
        ]

    def test_statistics_expose_the_progress_buckets_and_the_attempts(self) -> None:
        """Total, not started, in progress, completed, failed and the attempts are fields of the statistics."""
        fields: List[str] = [field.name for field in campaigns_pb2.CampaignStatistics.DESCRIPTOR.fields]
        for name in ("total", "not_started", "in_progress", "completed", "failed", "total_attempts"):
            assert name in fields

    def test_a_campaign_call_carries_its_sip_status_and_description(self) -> None:
        """Each campaign call reports the ondewo-sip status type and its description."""
        fields: Any = campaigns_pb2.CampaignCall.DESCRIPTOR.fields_by_name
        assert fields["sip_status_type"].enum_type.full_name == "ondewo.sip.SipStatus.StatusType"
        assert fields["sip_status_description"].type == fields["sip_status_description"].TYPE_STRING


class TestEventMessages:
    """The VtsiEvent / webhook contract a client depends on, read from the generated messages."""

    def test_every_vtsi_event_value_carries_the_enum_prefix(self) -> None:
        """proto3 enum values are package-scoped, so every value is ``VTSI_EVENT_*`` and zero is unspecified."""
        values: List[Any] = list(events_pb2.VtsiEvent.DESCRIPTOR.values)
        assert values[0].name == "VTSI_EVENT_UNSPECIFIED" and values[0].number == 0
        assert all(value.name.startswith("VTSI_EVENT_") for value in values)

    @pytest.mark.parametrize(
        "domain", ["CALL", "CALLER", "LISTENER", "SCHEDULED_CALLER", "CAMPAIGN", "VTSI_PROJECT", "ASTERISK"]
    )
    def test_every_domain_the_feature_covers_has_events(self, domain: str) -> None:
        """Calls, Callers, Listeners, ScheduledCallers, Campaigns, the VtsiProject and Asterisk all emit events."""
        names: List[str] = [value.name for value in events_pb2.VtsiEvent.DESCRIPTOR.values]
        assert any(name.startswith(f"VTSI_EVENT_{domain}_") for name in names)

    def test_webhook_custom_headers_are_an_optional_string_map(self) -> None:
        """Custom headers are a ``map<string, string>`` and may be empty."""
        webhook: events_pb2.Webhook = events_pb2.Webhook(url="https://example.com/hook")
        assert len(webhook.custom_headers) == 0
        webhook.custom_headers["Authorization"] = "Bearer x"
        assert events_pb2.Webhook.FromString(webhook.SerializeToString()).custom_headers["Authorization"] == "Bearer x"

    def test_switches_are_plain_bools_whose_zero_is_the_safe_default(self) -> None:
        """``disabled`` (not ``optional bool enabled``) so that every client, Angular included, can send it."""
        for message_type in (events_pb2.Webhook, events_pb2.VtsiEventSubscription):
            field: Any = message_type.DESCRIPTOR.fields_by_name["disabled"]
            assert field.type == field.TYPE_BOOL and not field.has_presence
