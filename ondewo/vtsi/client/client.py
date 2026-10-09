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
from typing import (
    Any,
    Optional,
    Set,
    Tuple,
)

import grpc
from ondewo.utils.base_client import BaseClient
from ondewo.utils.base_services_interface import build_shared_channel
from ondewo.utils.base_client_config import BaseClientConfig

from ondewo.vtsi.client.client_config import ClientConfig
from ondewo.vtsi.client.services.calls import Calls
from ondewo.vtsi.client.services.logs import Logs
from ondewo.vtsi.client.services.projects import Projects
from ondewo.vtsi.client.services_container import ServicesContainer


class Client(BaseClient):
    """
    The core python client for interacting with ONDEWO VTSI services.
    """

    def __init__(
        self,
        config: ClientConfig,
        use_secure_channel: bool = True,
        options: Optional[Set[Tuple[str, Any]]] = None,
        *,
        use_shared_channel: bool = False,
    ) -> None:
        """
        Initialize the client and its service clients.

        Args:
            config (ClientConfig):
                Configuration for the client.
            use_secure_channel (bool):
                Whether to use a secure gRPC channel. Defaults to ``True``.
            options (Optional[Set[Tuple[str, Any]]]):
                Additional options for the gRPC channel. Defaults to ``None``.
            use_shared_channel (bool):
                If ``True``, all services share ONE gRPC channel (one connection, one TLS handshake) built
                with ``build_shared_channel``, also on every later ``connect``. Defaults to ``False``: each
                service opens its own channel, as before.
        """
        self._use_shared_channel: bool = use_shared_channel
        super().__init__(config=config, use_secure_channel=use_secure_channel, options=options)

    def _initialize_services(
        self,
        config: BaseClientConfig,
        use_secure_channel: bool,
        options: Optional[Set[Tuple[str, Any]]] = None,
    ) -> None:
        """

        Initialize the service clients and lLogin with the current config and set up the services in self.services

        Args:
            config (BaseClientConfig):
                Configuration for the client.
            use_secure_channel (bool):
                Whether to use a secure gRPC channel.
            options (Optional[Set[Tuple[str, Any]]]):
                Additional options for the gRPC channel.
        """
        if not isinstance(config, ClientConfig):
            raise ValueError("The provided config must be of type `ondewo.vtsi.client.client_config.ClientConfig`")

        # One channel for all services when opted in; None makes every service open its own.
        grpc_channel: Optional[grpc.Channel] = (
            build_shared_channel(config, use_secure_channel, (Projects, Calls, Logs), options)
            if self._use_shared_channel
            else None
        )
        self.services: ServicesContainer = ServicesContainer(
            projects=Projects(
                config=config, use_secure_channel=use_secure_channel, options=options, grpc_channel=grpc_channel
            ),
            calls=Calls(
                config=config, use_secure_channel=use_secure_channel, options=options, grpc_channel=grpc_channel
            ),
            logs=Logs(config=config, use_secure_channel=use_secure_channel, options=options, grpc_channel=grpc_channel),
        )
