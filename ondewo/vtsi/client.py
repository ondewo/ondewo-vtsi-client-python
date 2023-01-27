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

import os
from dataclasses import dataclass

import grpc

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
    exposes the endpoints of the ondewo voip-server in a user-friendly way.
    """

    def __init__(self, config_voip: VtsiConfiguration) -> None:
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

    def create_vtsi_project(self, request: voip_pb2.CreateVtsiProjectRequest) -> voip_pb2.CreateVtsiProjectResponse:
        return self.voip_stub.CreateVtsiProject(request=request)

    def get_vtsi_project(self, request: voip_pb2.GetVtsiProjectRequest) -> voip_pb2.VtsiProject:
        return self.voip_stub.GetVtsiProject(request=request)

    def update_vtsi_project(self, request: voip_pb2.UpdateVtsiProjectRequest) -> voip_pb2.UpdateVtsiProjectResponse:
        return self.voip_stub.UpdateVtsiProject(request=request)

    def delete_vtsi_project(self, request: voip_pb2.DeleteVtsiProjectRequest) -> voip_pb2.DeleteVtsiProjectResponse:
        return self.voip_stub.DeleteVtsiProject(request=request)

    def deploy_vtsi_project(self, request: voip_pb2.DeployVtsiProjectRequest) -> voip_pb2.DeployVtsiProjectResponse:
        return self.voip_stub.DeployVtsiProject(request=request)

    def undeploy_vtsi_project(
        self,
        request: voip_pb2.UndeployVtsiProjectRequest
    ) -> voip_pb2.UndeployVtsiProjectResponse:
        return self.voip_stub.UndeployVtsiProject(request=request)

    def start_caller(self, request: voip_pb2.StartCallerRequest) -> voip_pb2.StartCallerResponse:
        return self.voip_stub.StartCaller(request=request)

    def start_callers(self, request: voip_pb2.StartCallersRequest) -> voip_pb2.StartCallersResponse:
        return self.voip_stub.StartCallers(request=request)

    def start_listener(self, request: voip_pb2.StartListenerRequest) -> voip_pb2.StartListenerResponse:
        return self.voip_stub.StartListener(request=request)

    def start_listeners(self, request: voip_pb2.StartListenersRequest) -> voip_pb2.StartListenersResponse:
        return self.voip_stub.StartListeners(request=request)

    def start_scheduled_caller(
        self,
        request: voip_pb2.StartScheduledCallerRequest
    ) -> voip_pb2.StartScheduledCallerResponse:
        return self.voip_stub.StartScheduledCaller(request=request)

    def start_scheduled_callers(
        self, request: voip_pb2.StartScheduledCallersRequest
    ) -> voip_pb2.StartScheduledCallersResponse:
        return self.voip_stub.StartScheduledCallers(request=request)

    def stop_call(self, request: voip_pb2.StopCallRequest) -> voip_pb2.StopCallResponse:
        return self.voip_stub.StopCall(request=request)

    def stop_calls(self, request: voip_pb2.StopCallsRequest) -> voip_pb2.StopCallsResponse:
        return self.voip_stub.StopCalls(request=request)

    def stop_all_calls(self, request: voip_pb2.StopAllCallsRequest) -> voip_pb2.StopCallsResponse:
        return self.voip_stub.StopAllCalls(request=request)

    def transfer_call(self, request: voip_pb2.TransferCallRequest) -> voip_pb2.TransferCallResponse:
        return self.voip_stub.TransferCall(request=request)

    def transfer_calls(self, request: voip_pb2.TransferCallsRequest) -> voip_pb2.TransferCallsResponse:
        return self.voip_stub.TransferCalls(request=request)

    def get_voip_call_info(self, request: voip_pb2.GetVoipCallInfoRequest) -> voip_pb2.GetVoipCallInfoResponse:
        return self.voip_stub.GetVoipCallInfo(request=request)

    def list_voip_call_info(self, request: voip_pb2.ListVoipCallInfoRequest) -> voip_pb2.ListVoipCallInfoResponse:
        return self.voip_stub.ListVoipCallInfo(request=request)

    def get_audio_file(self, request: voip_pb2.GetAudioFileRequest) -> voip_pb2.GetAudioFileResponse:
        return self.voip_stub.GetAudioFile(request=request)

    def get_full_conversation_audio_file(
        self,
        request: voip_pb2.GetFullConversationAudioFileRequest
    ) -> voip_pb2.GetFullConversationAudioFileResponse:
        return self.voip_stub.GetFullConversationAudioFile(request=request)
