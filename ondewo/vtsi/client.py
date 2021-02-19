import time
from dataclasses import dataclass
from typing import List, Optional, Dict

import grpc
from ondewo.nlu import context_pb2
from ondewo.vtsi import call_log_pb2, call_log_pb2_grpc, voip_pb2, voip_pb2_grpc

from ondewo.vtsi.dataclasses.server_configurations_dataclasses import (
    CaiConfiguration,
    VtsiServerConfiguration,
    AudioConfiguration,
    AsteriskConfiguration,
    CallConfig,
)


def create_parameter_dict(my_dict: Dict) -> Optional[Dict[str, context_pb2.Context.Parameter]]:
    assert isinstance(my_dict, dict) or my_dict is None, "parameter must be a dict or None"
    if my_dict is not None:
        return {
            key: context_pb2.Context.Parameter(
                display_name=key,
                value=my_dict[key]
            )
            for key in my_dict
        }
    return None


@dataclass
class ConfigManager:
    """
    stores all configurations and provides access to the .client

    the helper functions in utils.py and functions defined in /dataclasses/server_configurations_dataclasses.py
        use the manager to extract information when constructing requests
    this means a separate manager instance should be used for different deployments (for example a separate instance for
    each cai project, language, etc.)
    """

    def __init__(
        self,
        config_voip: VtsiServerConfiguration,
        config_cai: CaiConfiguration,
        config_audio: AudioConfiguration,
        config_asterisk: AsteriskConfiguration,
    ):
        self.config_voip = config_voip
        self.config_cai = config_cai
        self.config_audio = config_audio
        self.config_asterisk = config_asterisk

        self.client = VtsiServerClient(manager=self)


class VtsiServerClient:
    """
    exposes the endpoints of the ondewo voip-server in a user-friendly way
    """

    def __init__(self, manager: ConfigManager) -> None:
        self.manager: ConfigManager = manager

        # create grpc service stub
        channel = grpc.insecure_channel(target=f"{self.manager.config_voip.host}:{self.manager.config_voip.port}")
        self.voip_stub = voip_pb2_grpc.VoipSessionsStub(channel=channel)
        self.call_log_stub = call_log_pb2_grpc.VoipCallLogsStub(channel=channel)

    @staticmethod
    def get_minimal_client(voip_host: str, voip_port: str) -> 'VtsiServerClient':
        manager = ConfigManager(
            config_voip=VtsiServerConfiguration(
                host=voip_host,
                port=int(voip_port),
            ),
            config_cai=CaiConfiguration(
                cai_project_id="[PLACEHOLDER]",
            ),
            config_audio=AudioConfiguration(
                language_code="[PLACEHOLDER",
            ),
            config_asterisk=AsteriskConfiguration(),
        )
        return VtsiServerClient(manager=manager)

    def load_manifest(self, request: voip_pb2.VoipManifest,) -> bool:
        """
        hand a list of callers and listeners (manifest) to the voip server
        context information can be provided for the full manifest
        the voip server will load the list into its memory and wait for further instructions (like run_manifest)
        """
        print("loading manifest")
        response: voip_pb2.VoipManifestResponse = self.voip_stub.LoadManifest(request=request)
        return response.success  # type: ignore

    def run_manifest(self, manifest_id: str,) -> bool:
        """
        deploy a loaded manifest - perform the defined calls and set up the defined number of listeners
        """
        request = voip_pb2.ManifestRequest(manifest_id=manifest_id)
        print("running manifest")
        response: voip_pb2.RunManifestResponse = self.voip_stub.RunManifest(request=request)
        return response.started  # type: ignore

    def remove_manifest(self, manifest_id: str,) -> voip_pb2.RemoveManifestResponse:
        """
        remove a loaded manifest - stop any running calls, stop listeners
        """
        request = voip_pb2.ManifestRequest(manifest_id=manifest_id)
        print("removing manifest")
        response: voip_pb2.RemoveManifestResponse = self.voip_stub.RemoveManifest(request=request)
        return response

    def perform_call(self,
                     phone_number: str,
                     call_id: str,
                     sip_sim_version: str,
                     project_id: str,
                     init_text: str,
                     contexts: List[context_pb2.Context],
                     ) -> voip_pb2.PerformCallResponse:
        """
        perform a single call
        """
        request = CallConfig.get_caller_proto_request(
            manager=self.manager,
            call_id=call_id,
            init_text=init_text,
            sip_sim_version=sip_sim_version,
            phone_number=phone_number,
            project_id=project_id,
            contexts=contexts,
        )
        print("performing call")
        response: voip_pb2.PerformCallResponse = self.voip_stub.PerformCall(request=request)
        return response

    def stop_call(
        self, call_id: Optional[str] = None, sip_id: Optional[str] = None,
    ) -> bool:
        """
        stop an ongoing call
        """
        if call_id:
            request = voip_pb2.StopCallRequest(call_id=call_id)
        elif sip_id:
            request = voip_pb2.StopCallRequest(sip_id=sip_id)
        else:
            raise ValueError("either call_id or sip_id needs to be specified!")
        print("stopping call")
        response: voip_pb2.StopCallResponse = self.voip_stub.StopCall(request=request)
        return response.success  # type: ignore

    def start_listener(self,
                       project_id: str,
                       call_id: str,
                       sip_sim_version: str,
                       init_text: str
                       ) -> voip_pb2.StartListenerResponse:
        """
        start an ondewo-sip-sim instance to listen for calls
        """
        request = CallConfig.get_listener_proto_request(
            manager=self.manager,
            project_id=project_id,
            call_id=call_id,
            init_text=init_text,
            sip_sim_version=sip_sim_version,
        )
        print("starting listener")
        response: voip_pb2.StartListenerResponse = self.voip_stub.StartListener(request=request)
        return response

    def stop_listener(
        self, call_id: Optional[str] = None, sip_id: Optional[str] = None,
    ) -> bool:
        """
        stop a listener instance
        """
        if call_id:
            request = voip_pb2.StopCallRequest(call_id=call_id)
        elif sip_id:
            request = voip_pb2.StopCallRequest(sip_id=sip_id)
        else:
            raise ValueError("either call_id or sip_id needs to be specified!")
        print("stopping listener")
        response: voip_pb2.StopListenerResponse = self.voip_stub.StopListener(request=request)
        return response.success  # type: ignore

    def get_manifest_status(self, manifest_id: str,) -> voip_pb2.VoipManifestStatus:
        """
        get the status of all caller and listener instances of a manifest, as well as the status of associated services
        """
        request = voip_pb2.VoipManifestStatusRequest(manifest_id=manifest_id)
        print("getting manifest status")
        response: voip_pb2.VoipManifestStatus = self.voip_stub.GetManifestStatus(request=request)
        return response

    def get_instance_status(self, call_id: Optional[str] = None, sip_id: Optional[str] = None,) -> voip_pb2.VoipStatus:
        """
        stop a listener instance
        """
        if call_id:
            request = voip_pb2.GetVoipStatusRequest(call_id=call_id)
        elif sip_id:
            request = voip_pb2.GetVoipStatusRequest(sip_id=sip_id)
        else:
            raise ValueError("either call_id or sip_id needs to be specified!")
        print("getting instance status")
        response: voip_pb2.VoipStatus = self.voip_stub.GetInstanceStatus(request=request)
        return response

    def update_services_status(
        self, call_id: Optional[str] = None, sip_id: Optional[str] = None, manifest_id: Optional[str] = None,
    ) -> voip_pb2.UpdateServicesStatusResponse:
        """
        send update requests to speech-to-text, asterisk, text-to-speech and cai, which can then be retrieved by
            get_instance_status() or
            get_manifest_status()
        """
        if call_id:
            request = voip_pb2.UpdateServicesStatusRequest(call_id=call_id)
        elif sip_id:
            request = voip_pb2.UpdateServicesStatusRequest(sip_id=sip_id)
        elif manifest_id:
            request = voip_pb2.UpdateServicesStatusRequest(manifest_id=manifest_id)
        else:
            raise ValueError("either call_id, sip_id or manifest_id needs to be specified!")
        print("updating services' status")
        response: voip_pb2.UpdateServicesStatusResponse = self.voip_stub.UpdateServicesStatus(request=request)
        return response

    def get_call_ids(self) -> List[str]:
        """
        get all call_ids known to the voip manager
        """
        request = voip_pb2.GetCallIDsRequest()
        response: voip_pb2.GetCallIDsResponse = self.voip_stub.GetCallIDs(request=request)
        call_ids = []
        for call_id in response.call_ids:
            call_ids.append(call_id)
        return call_ids

    def get_manifest_ids(self) -> List[str]:
        """
        get all manifest_ids known to the voip manager
        """
        request = voip_pb2.GetManifestIDsRequest()
        response: voip_pb2.GetManifestIDsResponse = self.voip_stub.GetManifestIDs(request=request)
        manifest_ids = []
        for manifest_id in response.manifest_ids:
            manifest_ids.append(manifest_id)
        return manifest_ids

    def shutdown_unhealthy_calls(self) -> bool:
        """
        shutdown any deployed call instances with unhealthy overall voip status
        """
        request = voip_pb2.ShutdownUnhealthyCallsRequest()
        response: voip_pb2.ShutdownUnhealthyCallsResponse = self.voip_stub.ShutdownUnhealthyCalls(request=request)
        return response.success     # type: ignore

    # def get_call_ids(self, sip_id: str,) -> List[str]:
    #     """
    #     get all call_ids associated with a sip-instance (currently only 1)
    #     """
    #     request = call_log_pb2.GetCallIdsRequest(sip_id=sip_id)
    #     print("get call IDs")
    #     response: call_log_pb2.GetCallIdsResponse = self.call_log_stub.GetCallIds(request=request)
    #     return [call_id for call_id in response.call_ids]

    def start_voip_log(self, call_id: str, start_time: Optional[float] = None,) -> call_log_pb2.VoipLogResponse:
        """
        start log of a call instance with the current time as start
        """
        if not start_time:
            start_time = time.time()
        request = call_log_pb2.StartVoipLogRequest(call_id=call_id, start_time=start_time,)
        print("starting voip log")
        response: call_log_pb2.VoipLogResponse = self.call_log_stub.StartVoipLog(request=request)
        return response

    def finish_voip_log(self, call_id: str, end_time: Optional[float] = None,) -> call_log_pb2.VoipLogResponse:
        """
        finish the log of a call instance with current time as end
        """
        if not end_time:
            end_time = time.time()
        request = call_log_pb2.FinishVoipLogRequest(call_id=call_id, end_time=end_time,)
        print("finishing voip log")
        response: call_log_pb2.VoipLogResponse = self.call_log_stub.FinishVoipLog(request=request)
        return response

    def update_voip_log(
        self, call_id: str, service_name: str, log_message: str, counters: Optional[dict] = None,
    ) -> call_log_pb2.VoipLogResponse:
        """
        update the call log with a <log_message> logged by <service_name>
        can also update '15s' and '60s' counters by specifying ~ {'15s': 4, '60s': 2}
        """
        if not counters:
            request = call_log_pb2.UpdateVoipLogRequest(
                call_id=call_id, service_name=service_name, log_message=log_message,
            )
        else:
            if counters:
                counters = create_parameter_dict(counters)
            request = call_log_pb2.UpdateVoipLogRequest(
                call_id=call_id,
                service_name=service_name,
                log_message=log_message,
                counters=counters,
            )
        print("updating voip log")
        response: call_log_pb2.VoipLogResponse = self.call_log_stub.UpdateVoipLog(request=request)
        return response

    def activate_call_logs(self) -> call_log_pb2.SaveCallLogsResponse:
        """
        activate call logs globally for the voip manager
        """
        request = call_log_pb2.SaveCallLogsRequest()
        response: call_log_pb2.SaveCallLogsResponse = self.call_log_stub.ActivateSaveCallLogs(request=request)
        return response

    def get_voip_log(self, call_id: str) -> call_log_pb2.VoipLog:
        """
        get the call log of a sip-sim instance
        """
        request = call_log_pb2.GetVoipLogRequest(call_id=call_id)
        response: call_log_pb2.VoipLog = self.call_log_stub.GetVoipLog(request=request)
        return response

    def get_manifest_voip_log(self, manifest_id: str) -> call_log_pb2.ManifestVoipLog:
        """
        get the call logs of a full manifest of calls
        """
        request = call_log_pb2.GetManifestVoipLogRequest(manifest_id=manifest_id)
        response: call_log_pb2.ManifestVoipLog = self.call_log_stub.GetManifestVoipLog(request=request)
        return response

    def deploy_precondition_image(
        self, sip_sim_version: str, asterisk_host: str, asterisk_port: Optional[int] = None,
    ) -> bool:
        """
        deploy the 'precondition-for-working-setup' sip image
        """
        request = voip_pb2.DeployPreconditionRequest(
            sip_sim_version=sip_sim_version,
            asterisk_config=voip_pb2.ServiceConfig(
                host=asterisk_host,
                port=asterisk_port,
            )
        )
        response: voip_pb2.DeployPreconditionResponse = self.voip_stub.DeployPreconditionForWorkingSetup(
            request=request
        )
        return response.success  # type: ignore
