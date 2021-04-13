from ondewo.vtsi.client import ConfigManager

from ondewo.vtsi.dataclasses.server_configurations_dataclasses import VtsiConfiguration, AudioConfiguration, \
    AsteriskConfiguration, CaiConfiguration

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

########################################

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
