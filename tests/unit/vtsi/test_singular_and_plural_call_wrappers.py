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
The singular and plural caller/listener wrappers of ``Calls`` reach the RPC their name says.

Until 9.2.0 ``delete_caller``, ``stop_caller``, ``stop_listener`` and ``delete_listener`` took the PLURAL request and
called the plural RPC, so the singular RPCs were unreachable, and ``GetScheduledCaller``, ``ListScheduledCallers`` and
``CancelScheduledCaller`` had no wrapper at all. Each case here pins the request type the wrapper is annotated with,
the stub RPC it calls (with the request and the auth metadata unchanged) and the response it returns, sync and async.
"""

from typing import (
    Any,
    Dict,
    List,
    Tuple,
    get_type_hints,
)
from unittest.mock import (
    AsyncMock,
    MagicMock,
    patch,
)

import pytest

from ondewo.vtsi import calls_pb2
from ondewo.vtsi.client.client_config import ClientConfig
from ondewo.vtsi.client.services.async_calls import Calls as AsyncCalls
from ondewo.vtsi.client.services.calls import Calls

METADATA: List[Tuple[str, str]] = [("authorization", "Bearer test-access-token")]

# (wrapper method, stub RPC, request type, response type)
RPCS: List[Tuple[str, str, str, str]] = [
    ("delete_caller", "DeleteCaller", "DeleteCallerRequest", "DeleteCallerResponse"),
    ("delete_callers", "DeleteCallers", "DeleteCallersRequest", "DeleteCallersResponse"),
    ("stop_caller", "StopCaller", "StopCallerRequest", "StopCallerResponse"),
    ("stop_callers", "StopCallers", "StopCallersRequest", "StopCallersResponse"),
    ("delete_listener", "DeleteListener", "DeleteListenerRequest", "DeleteListenerResponse"),
    ("delete_listeners", "DeleteListeners", "DeleteListenersRequest", "DeleteListenersResponse"),
    ("stop_listener", "StopListener", "StopListenerRequest", "StopListenerResponse"),
    ("stop_listeners", "StopListeners", "StopListenersRequest", "StopListenersResponse"),
    ("get_scheduled_caller", "GetScheduledCaller", "GetScheduledCallerRequest", "ScheduledCaller"),
    ("list_scheduled_callers", "ListScheduledCallers", "ListScheduledCallersRequest", "ListScheduledCallersResponse"),
    (
        "cancel_scheduled_caller",
        "CancelScheduledCaller",
        "CancelScheduledCallerRequest",
        "CancelScheduledCallerResponse",
    ),
]


def _config() -> ClientConfig:
    """
    Build an unauthenticated config for an insecure local channel.

    Returns:
        ClientConfig:
            A config pointing to ``localhost:50051`` with no auth.
    """
    return ClientConfig(host="localhost", port="50051")


def test_the_descriptor_documents_the_pairs_listed_here() -> None:
    """Each RPC listed here takes and returns the message types this module expects of its wrapper."""
    service: Any = calls_pb2.DESCRIPTOR.services_by_name["Calls"]
    actual: Dict[str, Tuple[str, str]] = {
        method.name: (method.input_type.name, method.output_type.name) for method in service.methods
    }
    expected: Dict[str, Tuple[str, str]] = {rpc: (request, response) for _, rpc, request, response in RPCS}
    assert {rpc: actual.get(rpc) for rpc in expected} == expected


@pytest.mark.parametrize("wrapper_class", [Calls, AsyncCalls], ids=["sync", "async"])
@pytest.mark.parametrize("method_name, rpc, request_type, response_type", RPCS)
def test_the_wrapper_is_annotated_with_its_own_rpc_types(
    wrapper_class: Any, method_name: str, rpc: str, request_type: str, response_type: str
) -> None:
    """The wrapper declares the request and response type of the RPC its name says, never the other number's."""
    hints: Dict[str, Any] = get_type_hints(getattr(wrapper_class, method_name))
    assert hints["request"] is getattr(calls_pb2, request_type)
    assert hints["return"] is getattr(calls_pb2, response_type)


@pytest.mark.parametrize("method_name, rpc, request_type, response_type", RPCS)
def test_sync(method_name: str, rpc: str, request_type: str, response_type: str) -> None:
    """The sync wrapper calls its RPC with the request and metadata and returns what the stub returned."""
    with patch("grpc.insecure_channel"):
        service: Calls = Calls(config=_config(), use_secure_channel=False)
    request: Any = getattr(calls_pb2, request_type)()
    expected: Any = getattr(calls_pb2, response_type)()
    stub: MagicMock = MagicMock()
    getattr(stub, rpc).return_value = expected
    with (
        patch.object(Calls, "stub", new=stub),
        patch.object(Calls, "metadata", new=METADATA),
    ):
        result: Any = getattr(service, method_name)(request=request)
    getattr(stub, rpc).assert_called_once_with(request=request, metadata=METADATA)
    assert result is expected
    assert [call[0] for call in stub.method_calls] == [rpc]


@pytest.mark.asyncio
@pytest.mark.parametrize("method_name, rpc, request_type, response_type", RPCS)
async def test_async(method_name: str, rpc: str, request_type: str, response_type: str) -> None:
    """The async wrapper awaits its RPC with the request and metadata and returns the result."""
    with patch("grpc.aio.insecure_channel"):
        service: AsyncCalls = AsyncCalls(config=_config(), use_secure_channel=False)
    request: Any = getattr(calls_pb2, request_type)()
    expected: Any = getattr(calls_pb2, response_type)()
    stub: MagicMock = MagicMock()
    setattr(stub, rpc, AsyncMock(return_value=expected))
    with (
        patch.object(AsyncCalls, "stub", new=stub),
        patch.object(AsyncCalls, "metadata", new=METADATA),
    ):
        result: Any = await getattr(service, method_name)(request=request)
    getattr(stub, rpc).assert_awaited_once_with(request=request, metadata=METADATA)
    assert result is expected
