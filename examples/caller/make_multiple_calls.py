import threading
import uuid
from threading import Thread
from typing import List

from ondewo.vtsi.client import VtsiClient
from ondewo.vtsi.voip_pb2 import StartCallInstanceResponse


#     SIP
SIP_SIM_VERSION: str = "1.5.4"

#     VTSI_SERVER
VTSI_HOST: str = "0.0.0.0"
VTSI_PORT: int = 12345
VTSI_SECURE: bool = False  # if true, VTSI cert is needed
VTSI_CERT: str = ""

#     PROJECT
PROJECT_ID: str = "example_project_id"
INIT_TEXT: str = "hello"

#########################################

PHONE_NUMBERS = ["+11233232", "+2342345"]

client: VtsiClient = VtsiClient.get_minimal_client(voip_host=VTSI_HOST, voip_port=str(VTSI_PORT),
                                                   secure=VTSI_SECURE, cert_path=VTSI_CERT)


def deploy_caller(phone_number: str) -> StartCallInstanceResponse:
    response: StartCallInstanceResponse = client.start_caller(
        init_text=INIT_TEXT,
        phone_number=phone_number,
        call_id=str(uuid.uuid4()),
        sip_sim_version=SIP_SIM_VERSION,
        project_id=PROJECT_ID,
    )
    return response


threads: List[Thread] = [
    threading.Thread(target=deploy_caller, args=[phone_number])
    for phone_number in PHONE_NUMBERS
]
for thread in threads:
    thread.start()
