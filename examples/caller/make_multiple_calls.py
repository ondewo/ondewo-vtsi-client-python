import threading
import uuid
from threading import Thread
from typing import List

from ondewo.vtsi.client import VtsiClient
from ondewo.vtsi.voip_pb2 import StartCallInstanceResponse

#     SIP
SIP_SIM_VERSION: str = "1.5.4"

#     VTSI_SERVER
# For testing purposes 0.0.0.0 can be used
VTSI_HOST: str = "grpc-vtsi.ondewo.com"
VTSI_PORT: int = 443

#     PROJECT
PROJECT_ID: str = "example_project_id"

#########################################

# Phone numbers to call
PHONE_NUMBERS = ["+11233232", "+2342345"]

# get_minimal_client() returns the minimal working VTSI client
client: VtsiClient = VtsiClient.get_minimal_client(voip_host=VTSI_HOST, voip_port=str(VTSI_PORT))


# deploy_caller() function for multi-threading
def deploy_caller(phone_number: str) -> StartCallInstanceResponse:
    response: StartCallInstanceResponse = client.start_caller(
        phone_number=phone_number,
        call_id=str(uuid.uuid4()),
        sip_sim_version=SIP_SIM_VERSION,
        project_id=PROJECT_ID,
    )
    return response


# Iterating through phone number list, start the parallel calls
threads: List[Thread] = [
    threading.Thread(target=deploy_caller, args=[phone_number])
    for phone_number in PHONE_NUMBERS
]
for thread in threads:
    thread.start()
