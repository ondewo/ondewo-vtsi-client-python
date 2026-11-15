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
The 9.5.0 surface: the ``IvrMenus`` service, the warm transfer intro and the vendored nlu/sip trees it builds on.

No network is touched. The stub is replaced by a mock, so these tests assert that ``IvrMenus`` is reachable through
``client.services.ivr_menus`` of both clients with the request and the auth metadata passed through unchanged, and
that the generated messages carry the field numbers ondewo-vtsi-api 9.5.0 documents. Every RPC having a wrapper is
pinned separately by ``test_every_rpc_has_a_wrapper.py``.
"""

import importlib
from typing import (
    Any,
    List,
    Tuple,
)
from unittest.mock import (
    AsyncMock,
    MagicMock,
    patch,
)

import pytest

from ondewo.vtsi import (
    call_configs_pb2,
    calls_pb2,
    events_pb2,
    ivr_menus_pb2,
    projects_pb2,
)
from ondewo.vtsi.client.async_client import AsyncClient
from ondewo.vtsi.client.client import Client
from ondewo.vtsi.client.client_config import ClientConfig
from ondewo.vtsi.client.services.async_ivr_menus import IvrMenus as AsyncIvrMenus
from ondewo.vtsi.client.services.ivr_menus import IvrMenus

METADATA: List[Tuple[str, str]] = [("authorization", "Bearer test-access-token")]


def _config() -> ClientConfig:
    """
    Build a client config that never connects anywhere.

    Returns:
        ClientConfig:
            A config for ``localhost:50051``.
    """
    return ClientConfig(host="localhost", port="50051")


def test_the_ivr_menus_grpc_module_is_importable_and_has_its_stub() -> None:
    """``ivr_menus_pb2_grpc`` is generated and exposes the stub and servicer of ``IvrMenus``."""
    module: Any = importlib.import_module("ondewo.vtsi.ivr_menus_pb2_grpc")
    assert hasattr(module, "IvrMenusStub")
    assert hasattr(module, "IvrMenusServicer")
    assert hasattr(module, "add_IvrMenusServicer_to_server")


def test_the_vendored_nlu_session_has_the_warm_transfer_intro() -> None:
    """The vendored nlu tree is the one of ondewo-nlu-api 09169d1, which adds ``PrepareWarmTransferIntro``."""
    session_pb2: Any = importlib.import_module("ondewo.nlu.session_pb2")
    session_pb2_grpc: Any = importlib.import_module("ondewo.nlu.session_pb2_grpc")
    assert hasattr(session_pb2, "PrepareWarmTransferIntroRequest")
    assert hasattr(session_pb2, "PrepareWarmTransferIntroResponse")
    assert "PrepareWarmTransferIntro" in session_pb2.DESCRIPTOR.services_by_name["Sessions"].methods_by_name
    assert hasattr(session_pb2_grpc.SessionsStub, "__init__")
    importlib.import_module("ondewo.nlu.logs_pb2_grpc")


def test_the_generated_messages_carry_the_documented_field_numbers() -> None:
    """Field and enum numbers of the warm transfer and IVR surface, as ondewo-vtsi-api 9.5.0 documents them."""
    voice_fields: Any = call_configs_pb2.VoiceInteractionConfig.DESCRIPTOR.fields_by_name
    assert voice_fields["warm_transfer_config"].number == 6
    warm: Any = call_configs_pb2.WarmTransferConfig.DESCRIPTOR.fields_by_name
    assert warm["intro_listener_names"].number == 25
    assert calls_pb2.TransferCallRequest.DESCRIPTOR.fields_by_name["warm_transfer_config"].number == 9
    assert calls_pb2.CallTarget.DESCRIPTOR.fields_by_name["ivr_menu_name"].number == 5
    assert calls_pb2.TransferOutcome.Value("TRANSFER_OUTCOME_INTRO_UNAVAILABLE") == 12
    assert events_pb2.VtsiEvent.Value("VTSI_EVENT_CALL_WARM_TRANSFER_OUTCOME_NOTICE_UNDELIVERED") == 129
    assert events_pb2.VtsiEvent.Value("VTSI_EVENT_IVR_MENU_TESTED") == 1006
    assert projects_pb2.VtsiProject.DESCRIPTOR.fields_by_name["transfer_target_directory"].number == 25
    assert ivr_menus_pb2.IvrNodeType.Value("IVR_NODE_TYPE_GOTO_MENU") == 6
    assert ivr_menus_pb2.IvrMenu.DESCRIPTOR.fields_by_name["node_stats"].number == 22


def test_both_clients_expose_ivr_menus_on_one_shared_channel() -> None:
    """``services.ivr_menus`` exists on the sync and the async client and shares the one channel when opted in."""
    with patch("ondewo.vtsi.client.client.build_shared_channel") as build_sync:
        sync_client: Client = Client(config=_config(), use_secure_channel=False, use_shared_channel=True)
    assert isinstance(sync_client.services.ivr_menus, IvrMenus)
    assert IvrMenus in build_sync.call_args.args[2]
    with patch("ondewo.vtsi.client.async_client.build_shared_channel") as build_async:
        async_client: AsyncClient = AsyncClient(config=_config(), use_secure_channel=False, use_shared_channel=True)
    assert isinstance(async_client.services.ivr_menus, AsyncIvrMenus)
    assert AsyncIvrMenus in build_async.call_args.args[2]


def test_the_sync_wrapper_passes_request_and_metadata_through() -> None:
    """``test_ivr_menu`` hands the request and the auth metadata to the stub and returns its answer unchanged."""
    with patch("grpc.insecure_channel"):
        service: IvrMenus = IvrMenus(config=_config(), use_secure_channel=False)
    stub: MagicMock = MagicMock()
    expected: ivr_menus_pb2.IvrMenuTest = ivr_menus_pb2.IvrMenuTest(test_id="0" * 32)
    stub.TestIvrMenu.return_value = expected
    request: ivr_menus_pb2.TestIvrMenuRequest = ivr_menus_pb2.TestIvrMenuRequest(name="projects/p/ivr_menus/m")
    with (
        patch.object(IvrMenus, "stub", new=stub),
        patch.object(IvrMenus, "metadata", new=METADATA),
    ):
        assert service.test_ivr_menu(request) is expected
    stub.TestIvrMenu.assert_called_once_with(request=request, metadata=METADATA)


@pytest.mark.asyncio
async def test_the_async_wrapper_awaits_the_unary_stub() -> None:
    """The async ``get_ivr_menu_test`` awaits the stub and passes the request and metadata through."""
    with patch("grpc.aio.insecure_channel"):
        service: AsyncIvrMenus = AsyncIvrMenus(config=_config(), use_secure_channel=False)
    stub: MagicMock = MagicMock()
    expected: ivr_menus_pb2.IvrMenuTest = ivr_menus_pb2.IvrMenuTest(test_id="1" * 32)
    stub.GetIvrMenuTest = AsyncMock(return_value=expected)
    request: ivr_menus_pb2.GetIvrMenuTestRequest = ivr_menus_pb2.GetIvrMenuTestRequest(name="t")
    with (
        patch.object(AsyncIvrMenus, "stub", new=stub),
        patch.object(AsyncIvrMenus, "metadata", new=METADATA),
    ):
        assert await service.get_ivr_menu_test(request) is expected
    stub.GetIvrMenuTest.assert_awaited_once_with(request=request, metadata=METADATA)
