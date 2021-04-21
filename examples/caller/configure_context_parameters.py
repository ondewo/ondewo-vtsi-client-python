import uuid
from typing import Dict, Optional

from ondewo.nlu import context_pb2
from ondewo.vtsi.client import VtsiClient
from ondewo.vtsi.dataclasses.server_configurations_dataclasses import CaiConfiguration
from ondewo.vtsi.voip_pb2 import StartCallInstanceResponse

#     SIP
SIP_SIM_VERSION: str = "1.5.4"
#     VTSI_SERVER
# For testing purposes 0.0.0.0 can be used
VTSI_HOST: str = "grpc-vtsi.ondewo.com"
VTSI_PORT: int = 443
VTSI_SECURE: bool = False  # if true, VTSI cert is needed
VTSI_CERT: str = ""

PROJECT_ID: str = "example_project_id"
call_id = str(uuid.uuid4())

# Name of the input context to pass through the call
input_context_name = "c-input"

# Input context parameters in plain, dictionary format
plain_context_parameters = {
    "test": "test_value"
}

# Input context list to pass
contexts_to_pass = []


# Helper function to convert plain dictionary format to ONDEWO Context Parameter dictionary format
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


# Helper function to append context to the contexts list
def append_context(input_context_parameters: Dict[str, str], name: str):
    context = context_pb2.Context(
        name=name,
        lifespan_count=10000,
        parameters=create_parameter_dict(input_context_parameters),
    )
    contexts_to_pass.append(context)


# Append to input context list (several context can be added)
append_context(
    plain_context_parameters,
    name=f"projects/{PROJECT_ID}/agent/sessions/{call_id}/contexts/{input_context_name}"
)

# Context list can be passed during CaiConfiguration initialization (global) OR
# VtsiClient.start_caller() function call (local)

#################################################################################################
# VtsiClient.start_caller() case

client: VtsiClient = VtsiClient.get_minimal_client(voip_host=VTSI_HOST, voip_port=str(VTSI_PORT),
                                                   secure=VTSI_SECURE, cert_path=VTSI_CERT)

call_id: str = str(uuid.uuid4())
phone_number: str = "+123442"

# Input contexts can be passed here (passed contexts will be used for only THIS call) or
response: StartCallInstanceResponse = client.start_caller(
    phone_number=phone_number,
    call_id=call_id,
    sip_sim_version=SIP_SIM_VERSION,
    project_id=PROJECT_ID,
    contexts=contexts_to_pass
)

#################################################################################################
#  CaiConfiguration initialization case

#     CAI
CAI_HOST: str = "0.0.0.0"
CAI_PORT: int = 12345

# Input contexts can be passed here as well (passed contexts will be used for every call)
config_cai = CaiConfiguration(
    host=CAI_HOST,
    port=CAI_PORT,
    cai_project_id=PROJECT_ID,
    cai_contexts=contexts_to_pass,
)

# Full usage in full_demo.py
