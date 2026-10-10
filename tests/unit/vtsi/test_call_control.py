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
Call control on ``Calls``: invite, remove participant, media control, live call audio and typed transfers.

No network is touched. The stub is replaced by a mock, so these tests assert that the five new RPCs are
reachable through ``client.services.calls`` with the request (or request iterator) and the auth metadata
passed through unchanged, that a streaming RPC is returned as an iterator and never awaited, and that the
generated messages carry the field numbers the API documents.
"""

from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Tuple,
)
from unittest.mock import (
    AsyncMock,
    MagicMock,
    patch,
)

import pytest

from ondewo.sip import sip_pb2
from ondewo.vtsi import (
    calls_pb2,
    events_pb2,
    projects_pb2,
)
from ondewo.vtsi.client.client_config import ClientConfig
from ondewo.vtsi.client.services.async_calls import Calls as AsyncCalls
from ondewo.vtsi.client.services.calls import Calls

METADATA: List[Tuple[str, str]] = [("authorization", "Bearer test-access-token")]

# (wrapper method, stub RPC, request type, response type)
UNARY_RPCS: List[Tuple[str, str, str, str]] = [
    ("invite_to_call", "InviteToCall", "InviteToCallRequest", "InviteToCallResponse"),
    (
        "remove_call_participant",
        "RemoveCallParticipant",
        "RemoveCallParticipantRequest",
        "RemoveCallParticipantResponse",
    ),
    ("set_call_media_control", "SetCallMediaControl", "SetCallMediaControlRequest", "SetCallMediaControlResponse"),
]


def _config() -> ClientConfig:
    """
    Build an unauthenticated config for an insecure local channel.

    Returns:
        ClientConfig:
            A config pointing to ``localhost:50051`` with no auth.
    """
    return ClientConfig(host="localhost", port="50051")


def _requests(consumed: List[int]) -> Iterator[calls_pb2.StreamCallAudioRequest]:
    """
    Yield one config request, recording that the generator was advanced.

    Args:
        consumed (List[int]):
            Sink receiving one entry when the generator is advanced.

    Yields:
        calls_pb2.StreamCallAudioRequest:
            A single LISTEN config request.
    """
    consumed.append(1)
    yield calls_pb2.StreamCallAudioRequest(
        config=calls_pb2.StreamCallAudioConfig(mode=calls_pb2.CALL_AUDIO_MODE_LISTEN),
    )


class TestTheDescriptors:
    """The five call-control RPCs exist with the documented request, response and streaming kind."""

    def test_the_call_control_rpcs(self) -> None:
        """Each RPC maps to its request/response pair and its client/server streaming kind."""
        service: Any = calls_pb2.DESCRIPTOR.services_by_name["Calls"]
        actual: Dict[str, Tuple[str, str, bool, bool]] = {
            method.name: (
                method.input_type.name,
                method.output_type.name,
                method.client_streaming,
                method.server_streaming,
            )
            for method in service.methods
        }
        assert actual["InviteToCall"] == ("InviteToCallRequest", "InviteToCallResponse", False, False)
        assert actual["RemoveCallParticipant"] == (
            "RemoveCallParticipantRequest",
            "RemoveCallParticipantResponse",
            False,
            False,
        )
        assert actual["SetCallMediaControl"] == (
            "SetCallMediaControlRequest",
            "SetCallMediaControlResponse",
            False,
            False,
        )
        assert actual["StreamCallAudio"] == ("StreamCallAudioRequest", "StreamCallAudioResponse", True, True)
        assert actual["ListenCallAudio"] == ("ListenCallAudioRequest", "StreamCallAudioResponse", False, True)

    def test_the_call_carries_the_call_control_fields_on_their_documented_numbers(self) -> None:
        """``Call`` gained fields 22-25 and none of them carries the ``optional`` keyword."""
        fields: Dict[str, Any] = {field.name: field for field in calls_pb2.Call.DESCRIPTOR.fields}
        assert {name: fields[name].number for name in ("media_control", "participants", "last_transfer")} == {
            "media_control": 22,
            "participants": 23,
            "last_transfer": 24,
        }
        assert fields["sip_call_id"].number == 25
        assert fields["participants"].is_repeated
        assert not fields["sip_call_id"].has_presence

    def test_the_transfer_request_and_response_keep_their_legacy_fields(self) -> None:
        """``TransferCallRequest`` / ``Response`` keep 1-3 / 1-4 and gain the typed target and the outcome."""
        request: Dict[str, int] = {f.name: f.number for f in calls_pb2.TransferCallRequest.DESCRIPTOR.fields}
        response: Dict[str, int] = {f.name: f.number for f in calls_pb2.TransferCallResponse.DESCRIPTOR.fields}
        assert request == {
            "vtsi_project_name": 1,
            "call_name": 2,
            "transfer_id": 3,
            "target": 4,
            "mode": 5,
            "headers": 6,
            "ring_timeout_s": 7,
        }
        assert response == {
            "vtsi_project_name": 1,
            "call_name": 2,
            "transfer_id": 3,
            "error_message": 4,
            "outcome": 5,
            "resolved_target": 6,
            "sip_response_code": 7,
            "error_reason": 8,
        }

    def test_a_call_target_selects_exactly_one_target(self) -> None:
        """Setting a second member of the ``CallTarget`` oneof replaces the first."""
        target: calls_pb2.CallTarget = calls_pb2.CallTarget(phone_number="+4312345678")
        target.listener_queue.SetInParent()
        assert target.WhichOneof("target") == "listener_queue"
        assert target.phone_number == ""

    def test_the_zero_values_are_the_documented_defaults(self) -> None:
        """Unset mode / policy / setting enums read as the documented ``*_UNSPECIFIED`` / ``*_UNCHANGED``."""
        assert calls_pb2.TransferCallRequest().mode == calls_pb2.TRANSFER_MODE_UNSPECIFIED
        assert calls_pb2.InviteToCallRequest().mode == calls_pb2.PARTICIPANT_MODE_UNSPECIFIED
        assert calls_pb2.InviteToCallRequest().bot_policy == calls_pb2.BOT_POLICY_ON_JOIN_UNSPECIFIED
        assert calls_pb2.SetCallMediaControlRequest().bot_voice == calls_pb2.CALL_MEDIA_SETTING_UNCHANGED
        assert calls_pb2.StreamCallAudioConfig().mode == calls_pb2.CALL_AUDIO_MODE_UNSPECIFIED

    def test_the_call_control_events_take_112_to_121(self) -> None:
        """``VtsiEvent`` gained the participant, media control and audio stream events on 112-121."""
        assert {
            name: events_pb2.VtsiEvent.Value(name)
            for name in events_pb2.VtsiEvent.keys()
            if 112 <= events_pb2.VtsiEvent.Value(name) <= 121
        } == {
            "VTSI_EVENT_CALL_PARTICIPANT_INVITED": 112,
            "VTSI_EVENT_CALL_PARTICIPANT_JOINED": 113,
            "VTSI_EVENT_CALL_PARTICIPANT_FAILED": 114,
            "VTSI_EVENT_CALL_PARTICIPANT_LEFT": 115,
            "VTSI_EVENT_CALL_BOT_MUTED": 116,
            "VTSI_EVENT_CALL_BOT_UNMUTED": 117,
            "VTSI_EVENT_CALL_LISTENING_PAUSED": 118,
            "VTSI_EVENT_CALL_LISTENING_RESUMED": 119,
            "VTSI_EVENT_CALL_AUDIO_STREAM_CONNECTED": 120,
            "VTSI_EVENT_CALL_AUDIO_STREAM_DISCONNECTED": 121,
        }

    def test_the_project_carries_the_transfer_phone_number_allowlist(self) -> None:
        """``VtsiProject.transfer_phone_number_allowlist`` is a repeated string on field 17."""
        field: Any = projects_pb2.VtsiProject.DESCRIPTOR.fields_by_name["transfer_phone_number_allowlist"]
        assert field.number == 17
        assert field.is_repeated

    def test_the_vendored_sip_status_carries_the_call_scope_fields(self) -> None:
        """The vendored ``ondewo/sip`` is the call-control generation (``SipStatus`` fields 12-16)."""
        numbers: Dict[str, int] = {f.name: f.number for f in sip_pb2.SipStatus.DESCRIPTOR.fields}
        assert {name: numbers[name] for name in ("call_id", "bot_muted", "listening_paused")} == {
            "call_id": 12,
            "bot_muted": 13,
            "listening_paused": 14,
        }
        assert numbers["call_audio_streams"] == 15
        assert numbers["sip_response_code"] == 16
        assert "SipStreamCallAudio" in sip_pb2.DESCRIPTOR.services_by_name["Sip"].methods_by_name


class TestTheWrappersDelegateToTheStub:
    """Each wrapper forwards the request (or request iterator) and the auth metadata to its stub RPC."""

    @pytest.mark.parametrize("method_name, rpc, request_type, response_type", UNARY_RPCS)
    def test_sync_unary(self, method_name: str, rpc: str, request_type: str, response_type: str) -> None:
        """The sync unary wrapper returns what the stub returned."""
        with patch("grpc.insecure_channel"):
            service: Calls = Calls(config=_config(), use_secure_channel=False)
        request: Any = getattr(calls_pb2, request_type)()
        expected: object = object()
        stub: MagicMock = MagicMock()
        getattr(stub, rpc).return_value = expected
        with patch.object(Calls, "stub", new=stub), patch.object(Calls, "metadata", new=METADATA):
            result: Any = getattr(service, method_name)(request=request)
        getattr(stub, rpc).assert_called_once_with(request=request, metadata=METADATA)
        assert result is expected

    @pytest.mark.asyncio
    @pytest.mark.parametrize("method_name, rpc, request_type, response_type", UNARY_RPCS)
    async def test_async_unary(self, method_name: str, rpc: str, request_type: str, response_type: str) -> None:
        """The async unary wrapper awaits the stub and returns its result."""
        with patch("grpc.aio.insecure_channel"):
            service: AsyncCalls = AsyncCalls(config=_config(), use_secure_channel=False)
        request: Any = getattr(calls_pb2, request_type)()
        expected: object = object()
        stub: MagicMock = MagicMock()
        setattr(stub, rpc, AsyncMock(return_value=expected))
        with patch.object(AsyncCalls, "stub", new=stub), patch.object(AsyncCalls, "metadata", new=METADATA):
            result: Any = await getattr(service, method_name)(request=request)
        getattr(stub, rpc).assert_awaited_once_with(request=request, metadata=METADATA)
        assert result is expected

    @pytest.mark.parametrize(
        "service_class, channel_factory", [(Calls, "grpc.insecure_channel"), (AsyncCalls, "grpc.aio.insecure_channel")]
    )
    def test_stream_call_audio_is_returned_unawaited_and_leaves_the_requests_unconsumed(
        self,
        service_class: Any,
        channel_factory: str,
    ) -> None:
        """
        ``stream_call_audio`` hands the request iterator over lazily and returns the stub's stream as is.

        Pulling from the request iterator inside the wrapper would block on live agent audio, and awaiting
        a grpc.aio bidirectional call fails.
        """
        with patch(channel_factory):
            service: Any = service_class(config=_config(), use_secure_channel=False)
        consumed: List[int] = []
        request_iterator: Iterator[calls_pb2.StreamCallAudioRequest] = _requests(consumed)
        expected: object = object()
        stub: MagicMock = MagicMock()
        stub.StreamCallAudio.return_value = expected
        with patch.object(service_class, "stub", new=stub), patch.object(service_class, "metadata", new=METADATA):
            result: Any = service.stream_call_audio(request_iterator)
        stub.StreamCallAudio.assert_called_once_with(request_iterator, metadata=METADATA)
        assert result is expected
        assert consumed == []

    @pytest.mark.parametrize(
        "service_class, channel_factory", [(Calls, "grpc.insecure_channel"), (AsyncCalls, "grpc.aio.insecure_channel")]
    )
    def test_listen_call_audio_is_returned_unawaited(self, service_class: Any, channel_factory: str) -> None:
        """``listen_call_audio`` returns the stub's server stream as is, also on the async service."""
        with patch(channel_factory):
            service: Any = service_class(config=_config(), use_secure_channel=False)
        request: calls_pb2.ListenCallAudioRequest = calls_pb2.ListenCallAudioRequest()
        expected: object = object()
        stub: MagicMock = MagicMock()
        stub.ListenCallAudio.return_value = expected
        with patch.object(service_class, "stub", new=stub), patch.object(service_class, "metadata", new=METADATA):
            result: Any = service.listen_call_audio(request)
        stub.ListenCallAudio.assert_called_once_with(request=request, metadata=METADATA)
        assert result is expected
