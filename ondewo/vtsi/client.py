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

from ondewo.vtsi import vtsi_pb2, vtsi_pb2_grpc


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
    exposes the endpoints of the ondewo vtsi-server in a user-friendly way.
    """

    def __init__(self, config_vtsi: VtsiConfiguration) -> None:
        self.config_vtsi = config_vtsi
        target = f"{self.config_vtsi.host}:{self.config_vtsi.port}"
        # create grpc service stub
        if self.config_vtsi.secure:

            if self.config_vtsi.grpc_cert:
                grpc_cert = self.config_vtsi.grpc_cert
            elif os.path.exists(self.config_vtsi.cert_path):
                with open(self.config_vtsi.cert_path, "rb") as fi:
                    grpc_cert = fi.read()

            credentials = grpc.ssl_channel_credentials(root_certificates=grpc_cert)
            channel = grpc.secure_channel(target, credentials)
            print(f'Creating a secure channel to {target}')
        else:
            channel = grpc.insecure_channel(target=target)
            print(f'Creating an insecure channel to {target}')
        self.vtsi_stub = vtsi_pb2_grpc.VtsiStub(channel=channel)

    def create_vtsi_project(self, request: vtsi_pb2.CreateVtsiProjectRequest) -> vtsi_pb2.CreateVtsiProjectResponse:
        return self.vtsi_stub.CreateVtsiProject(request=request)

    def get_vtsi_project(self, request: vtsi_pb2.GetVtsiProjectRequest) -> vtsi_pb2.VtsiProject:
        return self.vtsi_stub.GetVtsiProject(request=request)

    def update_vtsi_project(self, request: vtsi_pb2.UpdateVtsiProjectRequest) -> vtsi_pb2.UpdateVtsiProjectResponse:
        return self.vtsi_stub.UpdateVtsiProject(request=request)

    def delete_vtsi_project(self, request: vtsi_pb2.DeleteVtsiProjectRequest) -> vtsi_pb2.DeleteVtsiProjectResponse:
        return self.vtsi_stub.DeleteVtsiProject(request=request)

    def deploy_vtsi_project(self, request: vtsi_pb2.DeployVtsiProjectRequest) -> vtsi_pb2.DeployVtsiProjectResponse:
        return self.vtsi_stub.DeployVtsiProject(request=request)

    def undeploy_vtsi_project(
        self,
        request: vtsi_pb2.UndeployVtsiProjectRequest
    ) -> vtsi_pb2.UndeployVtsiProjectResponse:
        return self.vtsi_stub.UndeployVtsiProject(request=request)

    def start_caller(self, request: vtsi_pb2.StartCallerRequest) -> vtsi_pb2.StartCallerResponse:
        return self.vtsi_stub.StartCaller(request=request)

    def start_callers(self, request: vtsi_pb2.StartCallersRequest) -> vtsi_pb2.StartCallersResponse:
        return self.vtsi_stub.StartCallers(request=request)

    def start_listener(self, request: vtsi_pb2.StartListenerRequest) -> vtsi_pb2.StartListenerResponse:
        return self.vtsi_stub.StartListener(request=request)

    def start_listeners(self, request: vtsi_pb2.StartListenersRequest) -> vtsi_pb2.StartListenersResponse:
        return self.vtsi_stub.StartListeners(request=request)

    def start_scheduled_caller(
        self,
        request: vtsi_pb2.StartScheduledCallerRequest
    ) -> vtsi_pb2.StartScheduledCallerResponse:
        return self.vtsi_stub.StartScheduledCaller(request=request)

    def start_scheduled_callers(
        self, request: vtsi_pb2.StartScheduledCallersRequest
    ) -> vtsi_pb2.StartScheduledCallersResponse:
        return self.vtsi_stub.StartScheduledCallers(request=request)

    def stop_call(self, request: vtsi_pb2.StopCallRequest) -> vtsi_pb2.StopCallResponse:
        return self.vtsi_stub.StopCall(request=request)

    def stop_calls(self, request: vtsi_pb2.StopCallsRequest) -> vtsi_pb2.StopCallsResponse:
        return self.vtsi_stub.StopCalls(request=request)

    def stop_all_calls(self, request: vtsi_pb2.StopAllCallsRequest) -> vtsi_pb2.StopCallsResponse:
        return self.vtsi_stub.StopAllCalls(request=request)

    def transfer_call(self, request: vtsi_pb2.TransferCallRequest) -> vtsi_pb2.TransferCallResponse:
        return self.vtsi_stub.TransferCall(request=request)

    def transfer_calls(self, request: vtsi_pb2.TransferCallsRequest) -> vtsi_pb2.TransferCallsResponse:
        return self.vtsi_stub.TransferCalls(request=request)

    def get_vtsi_call_info(self, request: vtsi_pb2.GetCallInfoRequest) -> vtsi_pb2.GetCallInfoResponse:
        return self.vtsi_stub.GetCallInfo(request=request)

    def list_vtsi_call_info(self, request: vtsi_pb2.ListCallInfoRequest) -> vtsi_pb2.ListCallInfoResponse:
        return self.vtsi_stub.ListCallInfo(request=request)

    def get_audio_file(self, request: vtsi_pb2.GetAudioFileRequest) -> vtsi_pb2.GetAudioFileResponse:
        return self.vtsi_stub.GetAudioFile(request=request)

    def get_full_conversation_audio_file(
        self,
        request: vtsi_pb2.GetFullConversationAudioFileRequest
    ) -> vtsi_pb2.GetFullConversationAudioFileResponse:
        return self.vtsi_stub.GetFullConversationAudioFile(request=request)
