#!/usr/bin/env python3

import uuid
from typing import List, Tuple

from ondewo.nlu import context_pb2

from ondewo.vtsi.dataclasses.server_configurations_dataclasses import VtsiConfiguration, CaiConfiguration, \
    AudioConfiguration, AsteriskConfiguration
from ondewo.vtsi.client import ConfigManager

"""
deploying 1 listener instance
name of instance (and hence assigned phone number in asterisk) is determined by order of deployment

1st deploy -> ondewo01 -> extension 01
2nd deploy -> ondewo02 -> extension 02
etc.

speech-to-text: ONDEWO
text-to-speech: ONDEWO
cai/bpi: 50052 ("BPI_PORT_LOCAL")

"""

######################################################
# CONFIGURATIONS
######################################################
#########################
# COMMON
#########################

# SIP-SIM CONFIGURATION
sip_sim_version = "0.8.1"

# VOIP SERVER CONFIGURATION
config_voip = VtsiConfiguration(
    host="grpc-vtsi.ondewo.com",
    port=443,
)

# AUDIO CONFIGURATION
config_audio_ondewo = AudioConfiguration(
    language_code="de-DE",

    # --- text-to-speech ---
    t2s_host="grpc-t2s.ondewo.com",
    t2s_port=443,
    t2s_type="ONDEWO",

    # --- speech-to-text ---
    s2t_host="grpc-s2t.ondewo.com",
    s2t_port=443,
    s2t_type="ONDEWO",  # == default, OPTIONS: "ONDEWO" in string (or not -> use Cloud provider name)
)

config_asterisk = AsteriskConfiguration(
    host="127.0.0.1"
)

TYPE = "listener"  # "caller" or "listener" [context set only for caller]
phone_number = ""  # only needed for "caller" instance
greeting_text = "hello"
contexts: List[context_pb2.Context] = []

deployments: List[Tuple[str, CaiConfiguration, AudioConfiguration]] = []

#########################
# IMAGE 1: Mirror
#########################

# CONVERSATIONAL AI CONFIGURATION
project_id = "not_a_cai_project"  # parent = projects/not_a_project/agent
config_cai = CaiConfiguration(
    host="0.0.0.0",
    port=50102,
    cai_project_id=project_id,
    cai_contexts=contexts,
    cai_type="mirror",
)
config_audio = config_audio_ondewo

deployments.append((project_id, config_cai, config_audio))

######################################################
# assemble configurations
for project_id, config_cai, config_audio in deployments:
    manager = ConfigManager(
        config_audio=config_audio,
        config_cai=config_cai,
        config_voip=config_voip,
        config_asterisk=config_asterisk,
    )

    manager.client.start_listener(
        init_text=greeting_text,
        call_id=str(uuid.uuid4()),
        project_id=project_id,
        sip_sim_version=sip_sim_version,
    )

######################################################
