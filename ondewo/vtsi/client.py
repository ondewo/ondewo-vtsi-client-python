# Copyright 2021 ONDEWO GmbH
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

import grpc
import os
from dataclasses import dataclass
from typing import List, Optional, Dict, Any

from ondewo.vtsi import voip_pb2, voip_pb2_grpc


@dataclass
class VtsiConfiguration:
    """
        Vtsi Configurations
        * host : Host of VTSI server
        * port: Port of VTSI server
        * secure: whether the server should be secure or not
        You only need one of the following
        * grpc_cert: GRPC cert
        * cert_path: GRPC cert path
    """
    host: str = "grpc-vtsi.ondewo.com"
    port: int = 443
    secure: bool = False
    grpc_cert: str = ''
    cert_path: str = ''


class VtsiClient:
    """
    exposes the endpoints of the ondewo voip-server in a user-friendly way
    """

    def __init__(self,
                 config_voip: VtsiConfiguration
                 ) -> None:
        self.config_voip = config_voip

        target = f"{self.config_voip.host}:{self.config_voip.port}"

        # create grpc service stub
        if self.config_voip.secure:

            if self.config_voip.grpc_cert:
                grpc_cert = self.config_voip.grpc_cert
            elif os.path.exists(self.config_voip.cert_path):
                with open(self.config_voip.cert_path, "rb") as fi:
                    grpc_cert = fi.read()

            credentials = grpc.ssl_channel_credentials(root_certificates=grpc_cert)
            channel = grpc.secure_channel(target, credentials)
            print(f'Creating a secure channel to {target}')
        else:
            channel = grpc.insecure_channel(target=target)
            print(f'Creating an insecure channel to {target}')
        self.voip_stub = voip_pb2_grpc.VoipSessionsStub(channel=channel)

    def register_project_configs_request(
            self, request: voip_pb2.RegisterProjectConfigsRequest, context: grpc.ServicerContext
    ) -> voip_pb2.RegisterProjectConfigsResponse:
        return self.voip_stub.RegisterProjectConfigs(request=request)

    def get_project_configs_request(
            self,
            request: voip_pb2.GetProjectConfigsRequest,
            context: grpc.ServicerContext
    ) -> voip_pb2.GetProjectConfigsResponse:
        return self.voip_stub.GetProjectConfigs(request=request)

    def update_project_configs_request(
            self,
            request: voip_pb2.UpdateProjectConfigsRequest,
            context: grpc.ServicerContext
    ) -> voip_pb2.UpdateProjectConfigsResponse:
        return self.voip_stub.UpdateProjectConfigs(request=request)

    def delete_project_configs_request(
            self,
            request: voip_pb2.DeleteProjectConfigsRequest,
            context: grpc.ServicerContext
    ) -> voip_pb2.DeleteProjectConfigsResponse:
        return self.voip_stub.DeleteProjectConfigs(request=request)

    def start_listeners(
            self,
            request: voip_pb2.StartListenersRequest,
            context: grpc.ServicerContext,
    ) -> voip_pb2.StartListenersResponse:
        return self.voip_stub.StartListeners(request=request)

    def start_callers(
            self,
            request: voip_pb2.StartCallersRequest,
            context: grpc.ServicerContext,
    ) -> voip_pb2.StartCallersResponse:
        return self.voip_stub.StartCallers(request=request)

    def start_scheduled_callers(
            self,
            request: voip_pb2.StartScheduledCallersRequest,
            context: grpc.ServicerContext,
    ) -> voip_pb2.StartScheduledCallersResponse:
        return self.voip_stub.StartScheduledCallers(request=request)

    def stop_calls(
            self,
            request: voip_pb2.StopCallsRequest,
            context: grpc.ServicerContext,
    ) -> voip_pb2.StopCallsResponse:
        return self.voip_stub.StopCalls(request=request)

    def stop_all_calls(
            self,
            request: voip_pb2.empty_pb2.Empty,
            context: grpc.ServicerContext,
    ) -> voip_pb2.StopAllCallsResponse:
        return self.voip_stub.StopAllCalls(request=request)

    def transfer_call(
            self,
            request: voip_pb2.TransferCallRequest,
            context: grpc.ServicerContext,
    ) -> voip_pb2.TransferCallResponse:
        return self.voip_stub.TransferCall(request=request)

    def get_voip_call_info(
            self,
            request: voip_pb2.GetVoipCallInfoRequest,
            context: grpc.ServicerContext,
    ) -> voip_pb2.GetVoipCallInfoResponse:
        return self.voip_stub.GetVoipCallInfo(request=request)

    def list_voip_call_info(
            self,
            request: voip_pb2.ListVoipCallInfoRequest,
            context: grpc.ServicerContext,
    ) -> voip_pb2.ListVoipCallInfoResponse:
        return self.voip_stub.ListVoipCallInfo(request=request)

    def get_sip_accounts(
            self,
            request: voip_pb2.empty_pb2.Empty,
            context: grpc.ServicerContext,
    ) -> voip_pb2.GetSipAccountsResponse:
        return self.voip_stub.GetSipAccounts(request=request)

    def get_call_ids_from_sip_account(
            self,
            request: voip_pb2.GetCallIDsFromSipAccountRequest,
            context: grpc.ServicerContext,
    ) -> voip_pb2.GetCallIDsFromSipAccountResponse:
        return self.voip_stub.GetCallIDsFromSipAccount(request=request)

    def get_audio_file(
            self,
            request: voip_pb2.GetAudioFileRequest,
            context: grpc.ServicerContext,
    ) -> voip_pb2.GetAudioFileResponse:
        return self.voip_stub.GetAudioFile(request=request)

    def get_full_conversation_audio_file(
            self,
            request: voip_pb2.GetFullConversationAudioFileRequest,
            context: grpc.ServicerContext,
    ) -> voip_pb2.GetFullConversationAudioFileResponse:
        return self.voip_stub.GetFullConversationAudioFile(request=request)
