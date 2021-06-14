#!/usr/bin/env python3

import uuid

from ondewo.vtsi.client import ConfigManager
from ondewo.vtsi.dataclasses.server_configurations_dataclasses import VtsiConfiguration, AudioConfiguration, \
    AsteriskConfiguration, CaiConfiguration
from ondewo.vtsi.voip_pb2 import StartCallInstanceResponse

#     SIP
SIP_SIM_VERSION: str = "0.2.2"
PHONE_NUMBER: str = "+1234567"

#     VTSI_SERVER
# For testing purposes 0.0.0.0 can be used
VTSI_HOST: str = "grpc-vtsi.ondewo.com"
VTSI_PORT: int = 443
VTSI_SECURE: bool = True  # if true, VTSI cert is needed
VTSI_CERT: str = "./grpc_cert"
#     SPEECH2TEXT
S2T_HOST: str = "grpc-s2t.ondewo.com"
S2T_PORT: int = 443
S2T_TYPE: str = "ONDEWO"
S2T_LANGUAGE: str = "default_german"
#     TEXT2SPEECH
T2S_HOST: str = "grpc-t2s.ondewo.com"
T2S_PORT: int = 443
T2S_TYPE: str = "ONDEWO"
T2S_LANGUAGE: str = "kerstin"
#     ASTERISK
ASTERISK_HOST: str = "aim.ondewo.com"
#     CAI
CAI_HOST: str = "grpc-nlu.ondewo.com"
CAI_PORT: int = 443
#     PROJECT
PROJECT_ID: str = "project_id"
#  Init text is being used when the caller wants to send text to the NLU (CAI) first,
#  for example to activate a special intent in the beginning of the conversation

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

response: StartCallInstanceResponse = manager.client.start_caller(
    phone_number=PHONE_NUMBER,
    call_id=str(uuid.uuid4()),
    sip_sim_version=SIP_SIM_VERSION,
    project_id=PROJECT_ID,
    initial_intent='Default Welcome Intent'
)
