#!/usr/bin/env python3
#
# from ondewo.vtsi.client import VtsiClient
# import uuid
#
# #     SIP
# SIP_SIM_VERSION: str = "1.5.4"
# PHONE_NUMBER: str = "+123123123"
#
# #     VTSI_SERVER
# # For testing purposes 0.0.0.0 can be used
# VTSI_HOST: str = "grpc-vtsi.ondewo.com"
# VTSI_PORT: int = 443
#
# #     PROJECT
# PROJECT_ID: str = "example_project_id"
#
#
# client = VtsiClient.get_minimal_client(
#     vtsi_host=VTSI_HOST,
#     vtsi_port=VTSI_PORT
# )
#
# client.start_caller(
#     call_id=str(uuid.uuid4()),
#     sip_sim_version=SIP_SIM_VERSION,
#     project_id=PROJECT_ID,
#     phone_number=PHONE_NUMBER,
# )
