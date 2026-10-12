# Copyright 2021-2026 ONDEWO GmbH
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
The ondewo-vtsi-api 9.1.0 caller, listener and call contract, read from the generated messages.

The ``Update{Caller,Listener,Call}[s]`` RPCs with their ``update_mask``, the ``field_mask`` on every CRUD request of
callers, listeners and calls, ``Call.labels``, ``Campaign.campaign_callers`` and the campaign selector of
``ListCallers`` / ``ListCalls``; and the ``Calls`` service wrappers (sync and async) of the new RPCs.
"""

import asyncio
from typing import (
    Any,
    List,
    Optional,
    Tuple,
)
from unittest.mock import (
    AsyncMock,
    MagicMock,
    patch,
)

import pytest
from google.protobuf.descriptor import (
    Descriptor,
    FieldDescriptor,
)
from google.protobuf.field_mask_pb2 import FieldMask

from ondewo.vtsi import (
    calls_pb2,
    campaigns_pb2,
)
from ondewo.vtsi.client.services import (
    async_calls,
    calls,
)

# (request, field number of its new ``field_mask``), as listed in the 9.1.0 release notes.
CRUD_REQUESTS_WITH_A_FIELD_MASK: List[Tuple[Any, int]] = [
    (calls_pb2.StartCallerRequest, 4),
    (calls_pb2.StartCallersRequest, 5),
    (calls_pb2.StartListenerRequest, 4),
    (calls_pb2.StartListenersRequest, 4),
    (calls_pb2.GetCallerRequest, 4),
    (calls_pb2.GetListenerRequest, 4),
    (calls_pb2.GetCallRequest, 4),
    (calls_pb2.StopCallerRequest, 2),
    (calls_pb2.StopCallersRequest, 2),
    (calls_pb2.StopListenerRequest, 2),
    (calls_pb2.StopListenersRequest, 2),
    (calls_pb2.DeleteCallerRequest, 2),
    (calls_pb2.DeleteCallersRequest, 2),
    (calls_pb2.DeleteListenerRequest, 2),
    (calls_pb2.DeleteListenersRequest, 2),
    (calls_pb2.StopCallRequest, 3),
    (calls_pb2.StopCallsRequest, 3),
    (calls_pb2.StopAllCallsRequest, 2),
]

# (rpc, resource field of the single request, batch entries field, batch responses field, wrapper name)
UPDATE_RPCS: List[Tuple[str, str, str, str, str]] = [
    ("Caller", "caller", "update_caller_requests", "update_caller_responses", "caller"),
    ("Listener", "listener", "update_listener_requests", "update_listener_responses", "listener"),
    ("Call", "call", "update_call_requests", "update_call_responses", "call"),
]


def _field(message: Any, name: str) -> FieldDescriptor:
    """Return the descriptor of ``message.name``."""
    descriptor: FieldDescriptor = message.DESCRIPTOR.fields_by_name[name]
    return descriptor


def _message_type(message: Any, name: str) -> Descriptor:
    """Return the message type of the message field ``message.name``."""
    message_type: Optional[Descriptor] = _field(message, name).message_type
    assert message_type is not None
    return message_type


class TestFieldMasksOnEveryCrudRequest:
    """Every CRUD request of callers, listeners and calls carries a ``google.protobuf.FieldMask field_mask``."""

    @pytest.mark.parametrize("request_type, number", CRUD_REQUESTS_WITH_A_FIELD_MASK)
    def test_the_field_mask_has_its_number_and_type(self, request_type: Any, number: int) -> None:
        assert _field(request_type, "field_mask").number == number
        assert _message_type(request_type, "field_mask").full_name == "google.protobuf.FieldMask"

    def test_a_masked_get_caller_request_round_trips(self) -> None:
        request: calls_pb2.GetCallerRequest = calls_pb2.GetCallerRequest(
            name="projects/p/callers/c", field_mask=FieldMask(paths=["call_name", "sip_caller_config"])
        )
        parsed: calls_pb2.GetCallerRequest = calls_pb2.GetCallerRequest.FromString(request.SerializeToString())
        assert list(parsed.field_mask.paths) == ["call_name", "sip_caller_config"]


def _dry_run_field(resource: str) -> List[Tuple[str, int]]:
    """
    Name the dry-run field an update request of ``resource`` carries.

    Args:
        resource (str):
            ``Caller``, ``Listener`` or ``Call``.

    Returns:
        List[Tuple[str, int]]:
            ``[("validate_only", 4)]`` for callers and listeners; a live call has no dry run in 9.1.0.
    """
    return [] if resource == "Call" else [("validate_only", 4)]


class TestTheUpdateRpcs:
    """The six ``Update*`` RPCs and their messages."""

    def test_the_calls_service_declares_them(self) -> None:
        methods: List[str] = [method.name for method in calls_pb2.DESCRIPTOR.services_by_name["Calls"].methods]
        for rpc in ("UpdateCaller", "UpdateCallers", "UpdateListener", "UpdateListeners", "UpdateCall", "UpdateCalls"):
            assert rpc in methods

    @pytest.mark.parametrize("resource, resource_field, entries, responses, _wrapper", UPDATE_RPCS)
    def test_the_single_request_and_response(
        self, resource: str, resource_field: str, entries: str, responses: str, _wrapper: str
    ) -> None:
        request: Any = getattr(calls_pb2, f"Update{resource}Request")
        assert [(f.name, f.number) for f in request.DESCRIPTOR.fields] == [
            (resource_field, 1),
            ("update_mask", 2),
            ("field_mask", 3),
        ] + _dry_run_field(resource)
        assert _message_type(request, resource_field).full_name == f"ondewo.vtsi.{resource}"
        assert _message_type(request, "update_mask").full_name == "google.protobuf.FieldMask"
        response: Any = getattr(calls_pb2, f"Update{resource}Response")
        assert [(f.name, f.number) for f in response.DESCRIPTOR.fields] == [
            ("name", 1),
            (resource_field, 2),
            ("error_message", 3),
        ]

    @pytest.mark.parametrize("resource, _resource_field, entries, responses, _wrapper", UPDATE_RPCS)
    def test_the_batch_takes_repeated_single_requests(
        self, resource: str, _resource_field: str, entries: str, responses: str, _wrapper: str
    ) -> None:
        batch_request: Any = getattr(calls_pb2, f"Update{resource}sRequest")
        assert [(f.name, f.number) for f in batch_request.DESCRIPTOR.fields] == [
            ("vtsi_project_name", 1),
            (entries, 2),
            ("field_mask", 3),
        ] + _dry_run_field(resource)
        assert _field(batch_request, entries).is_repeated
        assert _message_type(batch_request, entries).name == f"Update{resource}Request"
        batch_response: Any = getattr(calls_pb2, f"Update{resource}sResponse")
        assert [(f.name, f.number) for f in batch_response.DESCRIPTOR.fields] == [
            ("vtsi_project_name", 1),
            (responses, 2),
            ("error_message", 3),
        ]

    def test_an_update_caller_request_round_trips(self) -> None:
        request: calls_pb2.UpdateCallerRequest = calls_pb2.UpdateCallerRequest(
            caller=calls_pb2.Caller(name="projects/p/callers/c"),
            update_mask=FieldMask(paths=["sip_caller_config.sip_sim_version"]),
            field_mask=FieldMask(paths=["sip_caller_config"]),
        )
        parsed: calls_pb2.UpdateCallerRequest = calls_pb2.UpdateCallerRequest.FromString(request.SerializeToString())
        assert parsed.caller.name == "projects/p/callers/c"
        assert list(parsed.update_mask.paths) == ["sip_caller_config.sip_sim_version"]


class TestCallLabels:
    """``Call.labels`` is the one mutable field of a call."""

    def test_labels_is_a_string_map_with_number_26(self) -> None:
        assert _field(calls_pb2.Call, "labels").number == 26
        entry: Descriptor = _message_type(calls_pb2.Call, "labels")
        assert entry.GetOptions().map_entry
        assert entry.fields_by_name["key"].type == FieldDescriptor.TYPE_STRING
        assert entry.fields_by_name["value"].type == FieldDescriptor.TYPE_STRING

    def test_an_update_call_request_with_labels_round_trips(self) -> None:
        request: calls_pb2.UpdateCallRequest = calls_pb2.UpdateCallRequest(
            call=calls_pb2.Call(name="projects/p/calls/c", labels={"team": "sales"}),
            update_mask=FieldMask(paths=["labels"]),
        )
        parsed: calls_pb2.UpdateCallRequest = calls_pb2.UpdateCallRequest.FromString(request.SerializeToString())
        assert dict(parsed.call.labels) == {"team": "sales"}


class TestTheCallersAndCallsOfACampaign:
    """``Campaign.campaign_callers`` and the campaign selector of ``ListCallers`` / ``ListCalls``."""

    def test_campaign_callers_and_its_truncation_flag(self) -> None:
        callers: FieldDescriptor = _field(campaigns_pb2.Campaign, "campaign_callers")
        assert (callers.number, callers.type, callers.is_repeated) == (20, FieldDescriptor.TYPE_STRING, True)
        truncated: FieldDescriptor = _field(campaigns_pb2.Campaign, "campaign_callers_truncated")
        assert (truncated.number, truncated.type) == (21, FieldDescriptor.TYPE_BOOL)

    @pytest.mark.parametrize(
        "message, numbers",
        [(calls_pb2.ListCallersRequest, (5, 6)), (calls_pb2.CallFilter, (16, 17))],
    )
    def test_the_campaign_selector_is_a_oneof(self, message: Any, numbers: Tuple[int, int]) -> None:
        name: FieldDescriptor = _field(message, "campaign_name")
        display_name: FieldDescriptor = _field(message, "campaign_display_name")
        assert (name.number, display_name.number) == numbers
        assert name.containing_oneof is not None and name.containing_oneof.name == "campaign"
        assert display_name.containing_oneof is name.containing_oneof

    def test_setting_one_member_clears_the_other(self) -> None:
        request: calls_pb2.ListCallersRequest = calls_pb2.ListCallersRequest(campaign_name="projects/p/campaigns/c")
        request.campaign_display_name = "Spring"
        assert request.WhichOneof("campaign") == "campaign_display_name"
        assert request.campaign_name == ""


class TestTheServiceWrappers:
    """``Calls.update_*`` forward to the stub with the client's metadata, sync and async."""

    @pytest.mark.parametrize("resource, _resource_field, _entries, _responses, wrapper", UPDATE_RPCS)
    @pytest.mark.parametrize("batch", [False, True])
    def test_the_sync_wrapper_calls_the_stub(
        self, resource: str, _resource_field: str, _entries: str, _responses: str, wrapper: str, batch: bool
    ) -> None:
        suffix: str = "s" if batch else ""
        request: Any = getattr(calls_pb2, f"Update{resource}{suffix}Request")()
        service: calls.Calls = calls.Calls.__new__(calls.Calls)
        stub: MagicMock = MagicMock()
        with (
            patch.object(calls.Calls, "stub", new=stub),
            patch.object(calls.Calls, "metadata", new=[("k", "v")]),
        ):
            result: Any = getattr(service, f"update_{wrapper}{suffix}")(request)
        rpc: MagicMock = getattr(stub, f"Update{resource}{suffix}")
        rpc.assert_called_once_with(request=request, metadata=[("k", "v")])
        assert result is rpc.return_value

    @pytest.mark.parametrize("resource, _resource_field, _entries, _responses, wrapper", UPDATE_RPCS)
    @pytest.mark.parametrize("batch", [False, True])
    def test_the_async_wrapper_awaits_the_stub(
        self, resource: str, _resource_field: str, _entries: str, _responses: str, wrapper: str, batch: bool
    ) -> None:
        suffix: str = "s" if batch else ""
        request: Any = getattr(calls_pb2, f"Update{resource}{suffix}Request")()
        service: async_calls.Calls = async_calls.Calls.__new__(async_calls.Calls)
        stub: MagicMock = MagicMock()
        rpc: AsyncMock = AsyncMock(return_value="response")
        setattr(stub, f"Update{resource}{suffix}", rpc)
        with (
            patch.object(async_calls.Calls, "stub", new=stub),
            patch.object(async_calls.Calls, "metadata", new=[("k", "v")]),
        ):
            result: Any = asyncio.run(getattr(service, f"update_{wrapper}{suffix}")(request))
        rpc.assert_awaited_once_with(request=request, metadata=[("k", "v")])
        assert result == "response"
