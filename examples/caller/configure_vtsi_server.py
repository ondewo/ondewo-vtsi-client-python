import uuid

from ondewo.vtsi.client import ConfigManager
from ondewo.vtsi.dataclasses.server_configurations_dataclasses import VtsiConfiguration, AudioConfiguration, \
    AsteriskConfiguration, CaiConfiguration
from ondewo.vtsi.voip_pb2 import StartCallInstanceResponse

#     SIP
SIP_SIM_VERSION: str = "1.5.4"

#     VTSI_SERVER
# For testing purposes 0.0.0.0 can be used
VTSI_HOST: str = "grpc-vtsi.ondewo.com"
VTSI_PORT: int = 443
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
#     PROJECT
PROJECT_ID: str = "example_project_id"
#  Init text is being used when the caller wants to send text to the NLU (CAI) first,
#  for example to activate a special intent in the beginning of the conversation
INIT_TEXT: str = "Hello"

########################################
# Full configuration for VTSI, Asterisk, SIP, T2S, S2T modules

# VTSI configuration
config_voip = VtsiConfiguration(
    host=VTSI_HOST,
    port=VTSI_PORT,
    secure=VTSI_SECURE,
    cert_path=VTSI_CERT
)

# S2T and T2S configuration
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

# Asterisk configuration
config_asterisk = AsteriskConfiguration(
    host=ASTERISK_HOST,
)

# CAI/BPI configuration
# I. Input contexts can be passed here (passed contexts will be used for every calls)
# or in VtsiClient.start_caller() call
config_cai = CaiConfiguration(
    host=CAI_HOST,
    port=CAI_PORT,
    cai_project_id=PROJECT_ID,
)

# ConfigManager to use VTSI client and reach the configs of the different modules
manager = ConfigManager(
    config_audio=config_audio_ondewo,
    config_cai=config_cai,
    config_voip=config_voip,
    config_asterisk=config_asterisk,
)

# Start call
call_id: str = str(uuid.uuid4())
phone_number: str = "+1234567"

response: StartCallInstanceResponse = manager.client.start_caller(
    phone_number=phone_number,
    call_id=call_id,
    sip_sim_version=SIP_SIM_VERSION,
    project_id=PROJECT_ID,
    init_text=INIT_TEXT
)
