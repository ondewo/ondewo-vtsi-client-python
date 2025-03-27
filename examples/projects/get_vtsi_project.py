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
import argparse
import json
from typing import (
    Any,
    Set,
    Tuple,
)

import grpc
from ondewo.utils.base_client_config import BaseClientConfig

from ondewo.vtsi.client.client import Client
from ondewo.vtsi.client.client_config import ClientConfig
from ondewo.vtsi.projects_pb2 import GetVtsiProjectRequest


def main() -> None:
    parser = argparse.ArgumentParser(description="File transcription example.")
    parser.add_argument(
        "--config",
        type=str,
        help="The GRPC configuration file path. "
             "See examples/configs in the ondewo-s2t-client-python repository.",
    )
    parser.add_argument(
        "--secure",
        default=False,
        action="store_true",
        help="Use secure GRPC connection (default is insecure).",
    )
    args = parser.parse_args()

    config: BaseClientConfig
    if args.config:
        with open(args.config) as f:
            config = ClientConfig.from_json(f.read())
    else:
        config = BaseClientConfig(
            host="localhost",
            port="50200",
        )

    # https://github.com/grpc/grpc-proto/blob/master/grpc/service_config/service_config.proto
    service_config_json: str = json.dumps(
        {
            "methodConfig": [
                {
                    "name": [
                        # To apply retry to all methods, put [{}] as a value in the "name" field
                        # {}
                        # List single rpc method calls
                        {"service": "ondewo.vtsi.Calls", "method": "ListCalls"},
                        {"service": "ondewo.vtsi.Projects", "method": "GetVtsiProject"},
                    ],
                    "retryPolicy": {
                        "maxAttempts": 10,
                        "initialBackoff": "1.1s",
                        "maxBackoff": "3000s",
                        "backoffMultiplier": 2,
                        "retryableStatusCodes": [
                            grpc.StatusCode.CANCELLED.name,
                            grpc.StatusCode.UNKNOWN.name,
                            grpc.StatusCode.DEADLINE_EXCEEDED.name,
                            grpc.StatusCode.NOT_FOUND.name,
                            grpc.StatusCode.RESOURCE_EXHAUSTED.name,
                            grpc.StatusCode.ABORTED.name,
                            grpc.StatusCode.INTERNAL.name,
                            grpc.StatusCode.UNAVAILABLE.name,
                            grpc.StatusCode.DATA_LOSS.name,
                        ],
                    },
                }
            ]
        }
    )

    options: Set[Tuple[str, Any]] = {
        # Define custom max message sizes: 1MB here is an arbitrary example.
        ("grpc.max_send_message_length", 1024 * 1024),
        ("grpc.max_receive_message_length", 1024 * 1024),
        # Example of setting KeepAlive options through generic channel_args
        ("grpc.keepalive_time_ms", 2 ** 31 - 1),
        ("grpc.keepalive_timeout_ms", 20000),
        ("grpc.keepalive_permit_without_calls", False),
        ("grpc.http2.max_pings_without_data", 2),
        # Example arg requested for the feature
        ("grpc.dns_enable_srv_queries", 1),
        ("grpc.enable_retries", 1),
        ("grpc.service_config", service_config_json)
    }

    client: Client = Client(config=config, use_secure_channel=False, options=options)
    client.services.projects.get_vtsi_project(request=GetVtsiProjectRequest(name="test"))


if __name__ == "__main__":
    main()
