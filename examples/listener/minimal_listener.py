#!/usr/bin/env python3

import uuid

from ondewo.vtsi.client import VtsiClient

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

# SIP-SIM CONFIGURATION
sip_sim_version: str = "1.5.3"

client: VtsiClient = VtsiClient.get_minimal_client()
# client: VtsiClient = VtsiClient.get_minimal_client(vtsi_host="localhost", vtsi_port=50200, secure=False)  # for local testing
client.start_listener(
    call_id=str(uuid.uuid4()),
    project_id=str(uuid.uuid4()),
    sip_sim_version=sip_sim_version,
)
