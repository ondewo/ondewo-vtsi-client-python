# Copyright 2021 ONDEWO GmbH
# Licensed under the ONDEWO GmbH license, Version 1.0 (the "License");
# you must not use this file except in compliance with the License.
# You must obtain a copy of the License at
# office@ondewo.com
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid
from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING

from ondewo.nlu import context_pb2
from ondewo.vtsi import voip_pb2
from ondewo.vtsi.voip_pb2 import ServiceConfig

if TYPE_CHECKING:
    from vtsi_client.voip_server_client import ConfigManager


@dataclass
class AudioConfiguration:
    """language and location of audio services (s2t, t2s) & demuxer"""

    language_code: str

    # text-to-speech
    t2s_host: str = "0.0.0.0"
    t2s_port: int = 8013
    t2s_type: str = "ONDEWO text-to-speech"  # OPTIONS: "ONDEWO" in str (or not -> use Cloud provider name)
    # t2s_port_ondewo = 40015  # used internally by sip-sim

    # speech-to-text
    s2t_host: str = "0.0.0.0"
    s2t_port: int = 40014
    s2t_type: str = "ONDEWO speech-to-text"  # OPTIONS: "ONDEWO" in str (or not -> use Cloud provider name)
    # s2t_port_cloud: int = 8012
    # s2t_port_ondewo: int = 40014

    # demux settings
    demux_host: str = "0.0.0.0"
    demux_port: int = 8011


@dataclass
class CaiConfiguration:
    """location of cai"""

    cai_project_id: str
    cai_contexts: List[context_pb2.Context] = field(default_factory=list)

    host: str = "localhost"
    port: int = 50053  # 50055 = cai, 50053 = bpi
    context_session_id: str = str(uuid.uuid4())  # overwritten by sip-sim
    cai_type: str = ""  # can be set to "mirror" to activate CAI="mirror" environment variable when deploying sip-sim


@dataclass
class AsteriskConfiguration:
    """location of asterisk"""

    host: str = "10.164.0.2"  # "34.90.21.10"  # gcloud IP
    port: int = 5060  # unused / not transferred (hardcoded in sip-sim)


@dataclass
class VtsiServerConfiguration:
    """location of voip server"""
    host: str
    port: int = 40045


class CallConfig:
    """
    provides functions to create
        PerformCallRequest and
        StartListenerRequest
    requests from data in the ConfigManager
    """

    @staticmethod
    def get_caller_proto_request(
        manager: "ConfigManager",
        phone_number: str,
        project_id: str,
        call_id: str,
        sip_sim_version: str,
        contexts: List[context_pb2.Context],
    ):
        return voip_pb2.PerformCallRequest(
            call_id=call_id,
            sip_sim_version=sip_sim_version,
            project_id=project_id,
            phone_number=phone_number,
            contexts=contexts,
            asterisk_config=ServiceConfig(
                host=manager.config_asterisk.host, port=manager.config_asterisk.port, service_identifier="asterisk",
            ),
            cai_config=ServiceConfig(
                host=manager.config_cai.host,
                port=manager.config_cai.port,
                service_identifier=manager.config_cai.cai_type,
            ),
            stt_config=ServiceConfig(
                language_code=manager.config_audio.language_code,
                host=manager.config_audio.s2t_host,
                port=manager.config_audio.s2t_port,
                service_identifier=manager.config_audio.s2t_type,
            ),
            tts_config=ServiceConfig(
                language_code=manager.config_audio.language_code,
                host=manager.config_audio.t2s_host,
                port=manager.config_audio.t2s_port,
                service_identifier=manager.config_audio.t2s_type,
            ),
            demux_config=ServiceConfig(
                host=manager.config_audio.demux_host, port=manager.config_audio.demux_port, service_identifier="demux",
            ),
        )

    @staticmethod
    def get_listener_proto_request(
        manager: "ConfigManager",
        project_id: str,
        call_id: str,
        sip_sim_version: str,
        init_text: str,
    ):
        return voip_pb2.StartListenerRequest(
            call_id=call_id,
            project_id=project_id,
            sip_sim_version=sip_sim_version,
            init_text=init_text,
            asterisk_config=ServiceConfig(
                host=manager.config_asterisk.host, port=manager.config_asterisk.port, service_identifier="asterisk",
            ),
            cai_config=ServiceConfig(
                host=manager.config_cai.host,
                port=manager.config_cai.port,
                service_identifier=manager.config_cai.cai_type,
            ),
            stt_config=ServiceConfig(
                host=manager.config_audio.s2t_host,
                port=manager.config_audio.s2t_port,
                language_code=manager.config_audio.language_code,
                service_identifier=manager.config_audio.s2t_type,
            ),
            tts_config=ServiceConfig(
                host=manager.config_audio.t2s_host,
                port=manager.config_audio.t2s_port,
                language_code=manager.config_audio.language_code,
                service_identifier=manager.config_audio.t2s_type,
            ),
            demux_config=ServiceConfig(
                host=manager.config_audio.demux_host, port=manager.config_audio.demux_port, service_identifier="demux",
            ),
        )


@dataclass
class Manifest:
    manifest_id: str
    contexts: List[context_pb2.Context]
    callers: List[voip_pb2.PerformCallRequest]
    listeners: List[voip_pb2.StartListenerRequest]
