# Copyright 2021 ONDEWO GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid
from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING, Optional, Dict, Union

from ondewo.nlu import context_pb2
from ondewo.vtsi import voip_pb2
from ondewo.vtsi.voip_pb2 import BaseServiceConfig, Credentials, NLUConfig, T2SConfig, S2TConfig, SIPConfig, \
    AsteriskConfig, CommonServicesConfigs
from ondewo.t2s import text_to_speech_pb2
from ondewo.s2t import speech_to_text_pb2
from ondewo.nlu.context_pb2 import Context

if TYPE_CHECKING:
    from ondewo.vtsi.client import ConfigManager


@dataclass
class BaseServiceConfig:
    """
    Base configuration of services like asterisk, cai, stt, tts

    Args:
        host: IP address of service
        port: port of service
        grpc_cert: grpc_cert of service
    """

    host: str
    port: str
    grpc_cert: Optional[str] = None

    def to_proto(self) -> voip_pb2.BaseServiceConfig:
        return voip_pb2.BaseServiceConfig(
            host=self.host,
            port=int(self.port),
            grpc_cert=self.grpc_cert,
        )


@dataclass
class Credentials:
    account_name: str
    password: str

    def to_proto(self) -> voip_pb2.Credentials:
        return voip_pb2.Credentials(
            account_name=self.account_name,
            password=self.password
        )


@dataclass
class NLUConfig:
    """
    configuration cai "nlu"
    """

    base_config: BaseServiceConfig
    authentication: Union[Credentials, str]
    language_code: str
    project_id: str
    initial_intent: str
    contexts: List[Context]

    def to_proto(self) -> voip_pb2.NLUConfig:
        return voip_pb2.NLUConfig(
            base_config=self.base_config,
            credentials=self.authentication if isinstance(self.authentication, Credentials) else None,
            auth_token=self.authentication if isinstance(self.authentication, str) else None,
            language_code=self.language_code,
            project_id=self.project_id,
            initial_intent=self.initial_intent,
            contexts=self.contexts
        )


@dataclass
class T2SConfig:
    """
    configuration cai "nlu"
    """

    base_config: BaseServiceConfig
    t2s_config: text_to_speech_pb2.RequestConfig

    def to_proto(self) -> voip_pb2.T2SConfig:
        return voip_pb2.T2SConfig(
            base_config=self.base_config,
            t2s_config=self.t2s_config
        )


@dataclass
class S2TConfig:
    """
    configuration cai "nlu"
    """

    base_config: BaseServiceConfig
    s2t_config: speech_to_text_pb2.TranscribeRequestConfig

    def to_proto(self) -> voip_pb2.S2TConfig:
        return voip_pb2.S2TConfig(
            base_config=self.base_config,
            s2t_config=self.s2t_config
        )


@dataclass
class AsteriskConfig:
    """
    configuration cai "nlu"
    """

    base_config: BaseServiceConfig

    def to_proto(self) -> voip_pb2.AsteriskConfig:
        return voip_pb2.AsteriskConfig(
            base_config=self.base_config,
        )


@dataclass
class CommonServicesConfigs:
    """
    configuration cai "nlu"
    """

    asterisk_config: AsteriskConfig
    cai_config: NLUConfig
    stt_config: S2TConfig
    tts_config: T2SConfig

    def to_proto(self) -> voip_pb2.CommonServicesConfigs:
        return voip_pb2.CommonServicesConfigs(
            asterisk_config=self.asterisk_config,
            cai_config=self.cai_config,
            stt_config=self.stt_config,
            tts_config=self.tts_config
        )


@dataclass
class SIPConfig:
    """
    configuration cai "nlu"
    """

    call_id: str
    call_display_name: str
    sip_sim_version: str
    sip_prefix: str
    sip_account: str
    account_password_dictionary = Optional[Dict[str, str]]
    phone_number: str
    headers: Dict[str, str]

    def to_proto(self) -> voip_pb2.SIPConfig:
        return voip_pb2.SIPConfig(
            call_id=self.call_id,
            call_display_name=self.call_display_name,
            sip_sim_version=self.sip_sim_version,
            sip_prefix=self.sip_prefix,
            sip_account=self.sip_account,
            account_password_dictionary=self.account_password_dictionary,
            phone_number=self.phone_number,
            headers=self.headers,
        )


@dataclass
class VtsiConfiguration:
    """location of voip server"""
    host: str = "grpc-vtsi.ondewo.com"
    port: int = 443
    secure: bool = False
    cert_path: str = ''

class CallConfig:
    """
    provides functions to create
        StartCallInstanceRequest
    requests from data in the ConfigManager
    """

    @staticmethod
    def get_call_proto_request(
            project_id: str,
            call_id: str,
            sip_sim_version: str,
            initial_intent: str,
            contexts: List[context_pb2.Context],
            phone_number: Optional[str] = None,
            sip_name: Optional[str] = None,
            sip_prefix: Optional[str] = None,
            password_dictionary: Optional[Dict[str, str]] = None,
            headers: Optional[Dict[str, str]] = None
    ):

        sip_config = voip_pb2.SIPConfig(
            call_id=call_id,
            sip_sim_version=sip_sim_version,
            sip_account=sip_name,
            account_password_dictionary=password_dictionary,
            phone_number=phone_number,
            headers=headers
        )


        services_configs = voip_pb2.CommonServicesConfigs(
            asterisk_config=config_asterisk.to_proto(),
            cai_config=config_cai.to_proto(),
            stt_config=config_stt.to_proto(),
            tts_config=config_tts.to_proto(),
        )
        return voip_pb2.StartCallInstanceRequest(
            sip_config=sip_config,
            services_configs=services_configs
        )
        return voip_pb2.StartCallInstanceRequest(
            call_id=call_id,
            project_id=project_id,
            sip_sim_version=sip_sim_version,
            phone_number=phone_number,
            contexts=contexts,
            init_text=init_text,
            initial_intent=initial_intent,
            sip_name=sip_name,
            sip_prefix=sip_prefix,
            password_dictionary=password_struct,
            asterisk_config=ServiceConfig(
                host=manager.config_asterisk.host, port=manager.config_asterisk.port,
                service_identifier="asterisk",
            ),
            cai_config=ServiceConfig(
                language_code=manager.config_cai.cai_language,
                host=manager.config_cai.host,
                port=manager.config_cai.port,
                service_identifier=manager.config_cai.cai_type,
                grpc_cert=manager.config_cai.nlu_grpc_cert,
            ),
            stt_config=ServiceConfig(
                language_code=manager.config_audio.s2t_language,
                host=manager.config_audio.s2t_host,
                port=manager.config_audio.s2t_port,
                service_identifier=manager.config_audio.s2t_type,
                grpc_cert=manager.config_audio.s2t_grpc_cert,
            ),
            tts_config=ServiceConfig(
                language_code=manager.config_audio.t2s_language,
                host=manager.config_audio.t2s_host,
                port=manager.config_audio.t2s_port,
                service_identifier=manager.config_audio.t2s_type,
                grpc_cert=manager.config_audio.t2s_grpc_cert,
            ),
        )


@dataclass
class Manifest:
    manifest_id: str
    contexts: List[context_pb2.Context]
    calles: List[voip_pb2.StartCallInstanceRequest]
