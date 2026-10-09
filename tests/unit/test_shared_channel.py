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
``Client(..., use_shared_channel=True)`` / ``AsyncClient(...)`` give every service ONE gRPC channel.

The default stays one channel per service. Real channels against an in-process insecure server: a
shared channel must reach the server (an RPC answered ``UNIMPLEMENTED`` by a server with no servicers
proves the request arrived), and ``disconnect()`` must close it exactly once.
"""

from concurrent import futures
from typing import (
    Any,
    Iterator,
    List,
)
from unittest.mock import patch

import grpc
import pytest

from ondewo.vtsi import projects_pb2
from ondewo.vtsi.client.async_client import AsyncClient
from ondewo.vtsi.client.client import Client
from ondewo.vtsi.client.client_config import ClientConfig


@pytest.fixture
def config() -> Iterator[ClientConfig]:
    # A gRPC server with no servicers: every RPC that reaches it is answered UNIMPLEMENTED.
    server: grpc.Server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    port: int = server.add_insecure_port("127.0.0.1:0")
    server.start()
    try:
        yield ClientConfig(host="127.0.0.1", port=str(port))
    finally:
        server.stop(grace=None)


def _channels(client: Any) -> List[Any]:
    services: Any = client.services
    return [services.projects.grpc_channel, services.calls.grpc_channel, services.logs.grpc_channel]


class TestSyncClient:
    def test_by_default_every_service_opens_its_own_channel(self, config: ClientConfig) -> None:
        client: Client = Client(config=config, use_secure_channel=False)
        assert len({id(channel) for channel in _channels(client)}) == 3
        client.disconnect()

    def test_opt_in_gives_every_service_the_same_channel_and_it_reaches_the_server(self, config: ClientConfig) -> None:
        client: Client = Client(config=config, use_secure_channel=False, use_shared_channel=True)
        channels: List[Any] = _channels(client)
        assert all(channel is channels[0] for channel in channels)

        grpc.channel_ready_future(channels[0]).result(timeout=10)
        with pytest.raises(grpc.RpcError) as error:
            client.services.projects.get_vtsi_project(projects_pb2.GetVtsiProjectRequest())
        assert error.value.code() == grpc.StatusCode.UNIMPLEMENTED

        with patch.object(channels[0], "close", wraps=channels[0].close) as close:
            client.disconnect()
        close.assert_called_once_with()

    def test_connect_after_disconnect_keeps_sharing(self, config: ClientConfig) -> None:
        client: Client = Client(config=config, use_secure_channel=False, use_shared_channel=True)
        client.disconnect()
        client.connect(config=config, use_secure_channel=False)
        channels: List[Any] = _channels(client)
        assert all(channel is channels[0] for channel in channels)
        client.disconnect()


class TestAsyncClient:
    @pytest.mark.asyncio
    async def test_by_default_every_service_opens_its_own_channel(self, config: ClientConfig) -> None:
        client: AsyncClient = AsyncClient(config=config, use_secure_channel=False)
        assert len({id(channel) for channel in _channels(client)}) == 3
        await client.disconnect()

    @pytest.mark.asyncio
    async def test_opt_in_gives_every_service_the_same_channel_and_it_reaches_the_server(
        self, config: ClientConfig
    ) -> None:
        # Built inside the running loop, as a grpc.aio channel must be.
        client: AsyncClient = AsyncClient(config=config, use_secure_channel=False, use_shared_channel=True)
        channels: List[Any] = _channels(client)
        assert all(channel is channels[0] for channel in channels)

        with pytest.raises(grpc.aio.AioRpcError) as error:
            await client.services.projects.get_vtsi_project(projects_pb2.GetVtsiProjectRequest())
        assert error.value.code() == grpc.StatusCode.UNIMPLEMENTED

        with patch.object(channels[0], "close", wraps=channels[0].close) as close:
            await client.disconnect()
        close.assert_awaited_once()
