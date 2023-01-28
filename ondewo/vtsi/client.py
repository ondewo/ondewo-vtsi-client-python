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

from ondewo.vtsi import projects_pb2, projects_pb2_grpc, calls_pb2_grpc, calls_pb2


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
        self.projects_stub = projects_pb2_grpc.ProjectsStub(channel=channel)
        self.calls_stub = calls_pb2_grpc.CallsStub(channel=channel)

    def create_vtsi_project(
        self,
        request: projects_pb2.CreateVtsiProjectRequest
    ) -> projects_pb2.CreateVtsiProjectResponse:
        return self.projects_stub.CreateVtsiProject(request=request)

    def get_vtsi_project(
        self,
        request: projects_pb2.GetVtsiProjectRequest
    ) -> projects_pb2.VtsiProject:
        return self.projects_stub.GetVtsiProject(request=request)

    def update_vtsi_project(
        self,
        request: projects_pb2.UpdateVtsiProjectRequest
    ) -> projects_pb2.UpdateVtsiProjectResponse:
        return self.projects_stub.UpdateVtsiProject(request=request)

    def delete_vtsi_project(
        self,
        request: projects_pb2.DeleteVtsiProjectRequest
    ) -> projects_pb2.DeleteVtsiProjectResponse:
        return self.projects_stub.DeleteVtsiProject(request=request)

    def deploy_vtsi_project(
        self,
        request: projects_pb2.DeployVtsiProjectRequest
    ) -> projects_pb2.DeployVtsiProjectResponse:
        return self.projects_stub.DeployVtsiProject(request=request)

    def undeploy_vtsi_project(
        self,
        request: projects_pb2.UndeployVtsiProjectRequest
    ) -> projects_pb2.UndeployVtsiProjectResponse:
        return self.projects_stub.UndeployVtsiProject(request=request)

    def start_caller(
        self,
        request: calls_pb2.StartCallerRequest
    ) -> calls_pb2.StartCallerResponse:
        return self.calls_stub.StartCaller(request=request)

    def start_callers(
        self,
        request: calls_pb2.StartCallersRequest
    ) -> calls_pb2.StartCallersResponse:
        return self.calls_stub.StartCallers(request=request)

    def start_listener(
        self,
        request: calls_pb2.StartListenerRequest
    ) -> calls_pb2.StartListenerResponse:
        return self.calls_stub.StartListener(request=request)

    def start_listeners(
        self,
        request: calls_pb2.StartListenersRequest
    ) -> calls_pb2.StartListenersResponse:
        return self.calls_stub.StartListeners(request=request)

    def start_scheduled_caller(
        self,
        request: calls_pb2.StartScheduledCallerRequest
    ) -> calls_pb2.StartScheduledCallerResponse:
        return self.calls_stub.StartScheduledCaller(request=request)

    def start_scheduled_callers(
        self, request: calls_pb2.StartScheduledCallersRequest
    ) -> calls_pb2.StartScheduledCallersResponse:
        return self.calls_stub.StartScheduledCallers(request=request)

    def stop_call(
        self,
        request: calls_pb2.StopCallRequest
    ) -> calls_pb2.StopCallResponse:
        return self.calls_stub.StopCall(request=request)

    def stop_calls(
        self, request:
        calls_pb2.StopCallsRequest
    ) -> calls_pb2.StopCallsResponse:
        return self.calls_stub.StopCalls(request=request)

    def stop_all_calls(
        self,
        request: calls_pb2.StopAllCallsRequest
    ) -> calls_pb2.StopCallsResponse:
        return self.calls_stub.StopAllCalls(request=request)

    def transfer_call(
        self,
        request: calls_pb2.TransferCallRequest
    ) -> calls_pb2.TransferCallResponse:
        return self.calls_stub.TransferCall(request=request)

    def transfer_calls(
        self,
        request: calls_pb2.TransferCallsRequest
    ) -> calls_pb2.TransferCallsResponse:
        return self.calls_stub.TransferCalls(request=request)

    def get_vtsi_call_info(
        self,
        request: calls_pb2.GetCallInfoRequest
    ) -> calls_pb2.GetCallInfoResponse:
        return self.calls_stub.GetCallInfo(request=request)

    def list_vtsi_call_info(
        self,
        request: calls_pb2.ListCallInfoRequest
    ) -> calls_pb2.ListCallInfoResponse:
        return self.calls_stub.ListCallInfo(request=request)

    def get_audio_file(
        self,
        request: calls_pb2.GetAudioFileRequest
    ) -> calls_pb2.GetAudioFileResponse:
        return self.calls_stub.GetAudioFile(request=request)

    def get_full_conversation_audio_file(
        self,
        request: calls_pb2.GetFullConversationAudioFileRequest
    ) -> calls_pb2.GetFullConversationAudioFileResponse:
        return self.calls_stub.GetFullConversationAudioFile(request=request)
