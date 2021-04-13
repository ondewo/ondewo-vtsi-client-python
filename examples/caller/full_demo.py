import threading
import uuid
from threading import Thread
from typing import List, Dict, Optional

from ondewo.nlu import context_pb2
from ondewo.vtsi.client import ConfigManager
from ondewo.vtsi.dataclasses.server_configurations_dataclasses import (
    AsteriskConfiguration,
    AudioConfiguration,
    CaiConfiguration,
    VtsiConfiguration,
)
from ondewo.vtsi.voip_pb2 import StartCallInstanceResponse

###################
#     Globals
###################

#     SIP
SIP_SIM_VERSION: str = "1.5.4"
#     VTSI_SERVER
VTSI_HOST: str = "0.0.0.0"
VTSI_PORT: int = 12345
VTSI_SECURE: bool = False  # if true, VTSI cert is needed
VTSI_CERT: str = ""
#     SPEECH2TEXT
S2T_HOST: str = ""
S2T_PORT: int = 123
S2T_TYPE: str = "ONDEWO"
S2T_LANGUAGE: str = "example_s2t_language"
#     TEXT2SPEECH
T2S_HOST: str = ""
T2S_PORT: int = 123
T2S_TYPE: str = "ONDEWO"
T2S_LANGUAGE: str = "example_t2s_language"
#     ASTERISK
ASTERISK_HOST: str = "127.0.0.1"
#     CAI
CAI_HOST: str = "0.0.0.0"
CAI_PORT: int = 12345
CAI_CLIENT_CONFIG: str = "cert/path.json"
#     PROJECT
PROJECT_ID: str = "example_project_id"
INIT_TEXT: str = "hello"

###################
#   Configure
###################

PHONE_NUMBERS = ["+11233232", "+2342345"]

config_voip = VtsiConfiguration(
    host=VTSI_HOST, port=VTSI_PORT, secure=VTSI_SECURE, cert_path=VTSI_CERT
)
config_audio_ondewo = AudioConfiguration(
    t2s_host=T2S_HOST,
    t2s_port=T2S_PORT,
    t2s_type=T2S_TYPE,
    t2s_language=T2S_LANGUAGE,
    s2t_host=S2T_HOST,
    s2t_port=S2T_PORT,
    s2t_type=S2T_TYPE,
    s2t_language=S2T_LANGUAGE,
)
config_asterisk = AsteriskConfiguration(
    host=ASTERISK_HOST,
)

# I. Input contexts can be passed here (passed contexts will be used for every calls)
config_cai = CaiConfiguration(
    host=CAI_HOST,
    port=CAI_PORT,
    cai_project_id=PROJECT_ID,
    cai_contexts=[],
)

manager = ConfigManager(
    config_audio=config_audio_ondewo,
    config_cai=config_cai,
    config_voip=config_voip,
    config_asterisk=config_asterisk,
)

###################
#   Set contexts
###################

input_context_parameters = {
    "test": "test_value"
}


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


parameter_dict = create_parameter_dict(input_context_parameters)

call_id: str = str(uuid.uuid4())
context = context_pb2.Context(
    name=f"projects/{PROJECT_ID}/agent/sessions/{call_id}/contexts/input",
    lifespan_count=10000,
    lifespan_time=10000,
    parameters=parameter_dict,
)

contexts = [context]

###################
#   Start call
###################


def deploy_caller(phone_number: str) -> StartCallInstanceResponse:
    # II. OR input contexts can be passed here (passed contexts will be used for THIS call)
    response: StartCallInstanceResponse = manager.client.start_caller(
        init_text=INIT_TEXT,
        phone_number=phone_number,
        call_id=call_id,
        sip_sim_version=SIP_SIM_VERSION,
        project_id=PROJECT_ID,
        contexts=contexts
    )
    return response


###################
#   Start multi-threaded calls
###################

threads: List[Thread] = [
    threading.Thread(target=deploy_caller, args=[phone_number])
    for phone_number in PHONE_NUMBERS
]
for thread in threads:
    thread.start()
