# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/vtsi/voip.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ondewo.nlu import context_pb2 as ondewo_dot_nlu_dot_context__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ondewo.s2t import speech_to_text_pb2 as ondewo_dot_s2t_dot_speech__to__text__pb2
from ondewo.t2s import text_to_speech_pb2 as ondewo_dot_t2s_dot_text__to__speech__pb2
from ondewo.sip import sip_pb2 as ondewo_dot_sip_dot_sip__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16ondewo/vtsi/voip.proto\x12\x0bondewo.vtsi\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x18ondewo/nlu/context.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fondewo/s2t/speech-to-text.proto\x1a\x1fondewo/t2s/text-to-speech.proto\x1a\x14ondewo/sip/sip.proto\"B\n\x11\x42\x61seServiceConfig\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x11\n\tgrpc_cert\x18\x03 \x01(\t\"5\n\x0b\x43redentials\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x83\x02\n\tNLUConfig\x12\x33\n\x0b\x62\x61se_config\x18\x01 \x01(\x0b\x32\x1e.ondewo.vtsi.BaseServiceConfig\x12/\n\x0b\x63redentials\x18\x02 \x01(\x0b\x32\x18.ondewo.vtsi.CredentialsH\x00\x12\x14\n\nauth_token\x18\x03 \x01(\tH\x00\x12\x15\n\rlanguage_code\x18\x04 \x01(\t\x12\x12\n\nproject_id\x18\x05 \x01(\t\x12\x16\n\x0einitial_intent\x18\x06 \x01(\t\x12%\n\x08\x63ontexts\x18\x07 \x03(\x0b\x32\x13.ondewo.nlu.ContextB\x10\n\x0e\x61uthentication\"o\n\tT2SConfig\x12\x33\n\x0b\x62\x61se_config\x18\x01 \x01(\x0b\x32\x1e.ondewo.vtsi.BaseServiceConfig\x12-\n\nt2s_config\x18\x02 \x01(\x0b\x32\x19.ondewo.t2s.RequestConfig\"y\n\tS2TConfig\x12\x33\n\x0b\x62\x61se_config\x18\x01 \x01(\x0b\x32\x1e.ondewo.vtsi.BaseServiceConfig\x12\x37\n\ns2t_config\x18\x02 \x01(\x0b\x32#.ondewo.s2t.TranscribeRequestConfig\"E\n\x0e\x41steriskConfig\x12\x33\n\x0b\x62\x61se_config\x18\x01 \x01(\x0b\x32\x1e.ondewo.vtsi.BaseServiceConfig\"\xfd\x01\n\x15\x43ommonServicesConfigs\x12\x34\n\x0f\x61sterisk_config\x18\x01 \x01(\x0b\x32\x1b.ondewo.vtsi.AsteriskConfig\x12*\n\ncai_config\x18\x02 \x01(\x0b\x32\x16.ondewo.vtsi.NLUConfig\x12*\n\nstt_config\x18\x03 \x01(\x0b\x32\x16.ondewo.vtsi.S2TConfig\x12*\n\ntts_config\x18\x04 \x01(\x0b\x32\x16.ondewo.vtsi.T2SConfig\x12*\n\ncsi_config\x18\x05 \x01(\x0b\x32\x16.ondewo.vtsi.CsiConfig\"\x9f\x02\n\rSIPBaseConfig\x12\x0f\n\x07\x63\x61ll_id\x18\x01 \x01(\t\x12\x19\n\x11\x63\x61ll_display_name\x18\x02 \x01(\t\x12\x17\n\x0fsip_sim_version\x18\x03 \x01(\t\x12\x12\n\nsip_prefix\x18\x04 \x01(\t\x12\x13\n\x0bsip_account\x18\x05 \x01(\t\x12^\n\x1b\x61\x63\x63ount_password_dictionary\x18\x06 \x03(\x0b\x32\x39.ondewo.vtsi.SIPBaseConfig.AccountPasswordDictionaryEntry\x1a@\n\x1e\x41\x63\x63ountPasswordDictionaryEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc8\x01\n\x0fSIPCallerConfig\x12\x33\n\x0fsip_base_config\x18\x01 \x01(\x0b\x32\x1a.ondewo.vtsi.SIPBaseConfig\x12\x14\n\x0cphone_number\x18\x02 \x01(\t\x12:\n\x07headers\x18\x03 \x03(\x0b\x32).ondewo.vtsi.SIPCallerConfig.HeadersEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xac\x02\n\tCsiConfig\x12\x30\n\rs2t_callbacks\x18\x01 \x01(\x0b\x32\x19.ondewo.vtsi.S2tCallbacks\x12\x30\n\rnlu_callbacks\x18\x02 \x01(\x0b\x32\x19.ondewo.vtsi.NluCallbacks\x12\x30\n\rt2s_callbacks\x18\x03 \x01(\x0b\x32\x19.ondewo.vtsi.T2sCallbacks\x12H\n\x19\x61udio_object_store_config\x18\x04 \x01(\x0b\x32%.ondewo.vtsi.AudioObjectStorageConfig\x12?\n\x15message_broker_config\x18\x05 \x01(\x0b\x32 .ondewo.vtsi.MessageBrokerConfig\"d\n\x18\x41udioObjectStorageConfig\x12\x30\n\x0cminio_config\x18\x01 \x01(\x0b\x32\x18.ondewo.vtsi.MinioConfigH\x00\x42\x16\n\x14\x61udio_storage_config\"g\n\x13MessageBrokerConfig\x12\x37\n\x10rabbit_mq_config\x18\x01 \x01(\x0b\x32\x1b.ondewo.vtsi.RabbitMqConfigH\x00\x42\x17\n\x15message_broker_config\"\\\n\x0eRabbitMqConfig\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x0e\n\x06port_2\x18\x03 \x01(\t\x12\x0c\n\x04user\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\"&\n\x08\x45ndpoint\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\"\x85\x01\n\x0bMinioConfig\x12\'\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32\x15.ondewo.vtsi.Endpoint\x12\x12\n\naccess_key\x18\x02 \x01(\t\x12\x12\n\nsecret_key\x18\x03 \x01(\t\x12\x0e\n\x06secure\x18\x04 \x01(\x08\x12\x15\n\rsession_token\x18\x05 \x01(\t\"E\n\x0cS2tCallbacks\x12\x19\n\x11pre_s2t_callbacks\x18\x01 \x03(\t\x12\x1a\n\x12post_s2t_callbacks\x18\x02 \x03(\t\"E\n\x0cNluCallbacks\x12\x19\n\x11pre_nlu_callbacks\x18\x01 \x03(\t\x12\x1a\n\x12post_nlu_callbacks\x18\x02 \x03(\t\"E\n\x0cT2sCallbacks\x12\x19\n\x11pre_t2s_callbacks\x18\x01 \x03(\t\x12\x1a\n\x12post_t2s_callbacks\x18\x02 \x03(\t\"\x84\x01\n\x14StartListenerRequest\x12.\n\nsip_config\x18\x01 \x01(\x0b\x32\x1a.ondewo.vtsi.SIPBaseConfig\x12<\n\x10services_configs\x18\x02 \x01(\x0b\x32\".ondewo.vtsi.CommonServicesConfigs\"t\n\x15StartListenerResponse\x12\x32\n\x07request\x18\x01 \x01(\x0b\x32!.ondewo.vtsi.StartListenerRequest\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x16\n\x0e\x65rror_messages\x18\x03 \x01(\t\"\x84\x01\n\x12StartCallerRequest\x12\x30\n\nsip_config\x18\x01 \x01(\x0b\x32\x1c.ondewo.vtsi.SIPCallerConfig\x12<\n\x10services_configs\x18\x02 \x01(\x0b\x32\".ondewo.vtsi.CommonServicesConfigs\"p\n\x13StartCallerResponse\x12\x30\n\x07request\x18\x01 \x01(\x0b\x32\x1f.ondewo.vtsi.StartCallerRequest\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x16\n\x0e\x65rror_messages\x18\x03 \x01(\t\"\x83\x01\n\x1bStartScheduledCallerRequest\x12\x30\n\x07request\x18\x01 \x01(\x0b\x32\x1f.ondewo.vtsi.StartCallerRequest\x12\x32\n\x0escheduled_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x82\x01\n\x1cStartScheduledCallerResponse\x12\x39\n\x07request\x18\x01 \x01(\x0b\x32(.ondewo.vtsi.StartScheduledCallerRequest\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x16\n\x0e\x65rror_messages\x18\x03 \x01(\t\"L\n\x15StartListenersRequest\x12\x33\n\x08requests\x18\x01 \x03(\x0b\x32!.ondewo.vtsi.StartListenerRequest\"v\n\x16StartListenersResponse\x12\x33\n\x07request\x18\x01 \x01(\x0b\x32\".ondewo.vtsi.StartListenersRequest\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x16\n\x0e\x65rror_messages\x18\x03 \x01(\t\"H\n\x13StartCallersRequest\x12\x31\n\x08requests\x18\x01 \x03(\x0b\x32\x1f.ondewo.vtsi.StartCallerRequest\"r\n\x14StartCallersResponse\x12\x31\n\x07request\x18\x01 \x01(\x0b\x32 .ondewo.vtsi.StartCallersRequest\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x16\n\x0e\x65rror_messages\x18\x03 \x01(\t\"Z\n\x1cStartScheduledCallersRequest\x12:\n\x08requests\x18\x01 \x03(\x0b\x32(.ondewo.vtsi.StartScheduledCallerRequest\"\x84\x01\n\x1dStartScheduledCallersResponse\x12:\n\x07request\x18\x01 \x01(\x0b\x32).ondewo.vtsi.StartScheduledCallersRequest\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x16\n\x0e\x65rror_messages\x18\x03 \x01(\t\"A\n\x0fStopCallRequest\x12\x11\n\x07\x63\x61ll_id\x18\x01 \x01(\tH\x00\x12\x15\n\x0bsip_account\x18\x02 \x01(\tH\x00\x42\x04\n\x02id\"\x7f\n\x10StopCallResponse\x12-\n\x07request\x18\x01 \x01(\x0b\x32\x1c.ondewo.vtsi.StopCallRequest\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x16\n\x0e\x65rror_messages\x18\x03 \x01(\t\x12\x13\n\x0blog_message\x18\x04 \x01(\t\"B\n\x10StopCallsRequest\x12.\n\x08requests\x18\x01 \x03(\x0b\x32\x1c.ondewo.vtsi.StopCallRequest\"E\n\x11StopCallsResponse\x12\x30\n\tresponses\x18\x01 \x03(\x0b\x32\x1d.ondewo.vtsi.StopCallResponse\"R\n\x14StopAllCallsResponse\x12:\n\x13stop_call_responses\x18\x01 \x03(\x0b\x32\x1d.ondewo.vtsi.StopCallResponse\"Z\n\x13TransferCallRequest\x12\x11\n\x07\x63\x61ll_id\x18\x01 \x01(\tH\x00\x12\x15\n\x0bsip_account\x18\x02 \x01(\tH\x00\x12\x13\n\x0btransfer_id\x18\x03 \x01(\tB\x04\n\x02id\"r\n\x14TransferCallResponse\x12\x31\n\x07request\x18\x01 \x01(\x0b\x32 .ondewo.vtsi.TransferCallRequest\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x16\n\x0e\x65rror_messages\x18\x03 \x01(\t\"\xae\x01\n\x16GetVoipCallInfoRequest\x12\x11\n\x07\x63\x61ll_id\x18\x01 \x01(\tH\x00\x12\x15\n\x0bsip_account\x18\x02 \x01(\tH\x00\x12:\n\x13voip_call_info_view\x18\x03 \x01(\x0e\x32\x1d.ondewo.vtsi.VoipCallInfoView\x12(\n\tcall_type\x18\x04 \x01(\x0e\x32\x15.ondewo.vtsi.CallTypeB\x04\n\x02id\"v\n\x17GetVoipCallInfoResponse\x12-\n\nactive_log\x18\x01 \x01(\x0b\x32\x19.ondewo.vtsi.VoipCallInfo\x12,\n\tdone_logs\x18\x02 \x03(\x0b\x32\x19.ondewo.vtsi.VoipCallInfo\"\xf2\x02\n\x0cVoipCallInfo\x12\x0f\n\x07\x63\x61ll_id\x18\x01 \x01(\t\x12\x13\n\x0bsip_account\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x16\n\x0e\x63ontainer_name\x18\x04 \x01(\t\x12(\n\tcall_type\x18\x05 \x01(\x0e\x32\x15.ondewo.vtsi.CallType\x12\x14\n\x0cphone_number\x18\x06 \x01(\t\x12\x12\n\nstart_time\x18\x07 \x01(\x01\x12\x10\n\x08\x65nd_time\x18\x08 \x01(\x01\x12)\n\nsip_status\x18\t \x01(\x0b\x32\x15.ondewo.sip.SipStatus\x12@\n\x12sip_status_history\x18\n \x01(\x0b\x32$.ondewo.sip.SipStatusHistoryResponse\x12;\n\x11services_statuses\x18\x0b \x01(\x0b\x32 .ondewo.vtsi.AllServicesStatuses\"\x7f\n\x17ListVoipCallInfoRequest\x12:\n\x13voip_call_info_view\x18\x01 \x01(\x0e\x32\x1d.ondewo.vtsi.VoipCallInfoView\x12(\n\tcall_type\x18\x02 \x01(\x0e\x32\x15.ondewo.vtsi.CallType\"H\n\x18ListVoipCallInfoResponse\x12,\n\tvoip_info\x18\x01 \x03(\x0b\x32\x19.ondewo.vtsi.VoipCallInfo\"\x8a\x02\n\x13\x41llServicesStatuses\x12.\n\nstatus_sip\x18\x01 \x01(\x0b\x32\x1a.ondewo.vtsi.ServiceStatus\x12\x33\n\x0fstatus_asterisk\x18\x02 \x01(\x0b\x32\x1a.ondewo.vtsi.ServiceStatus\x12.\n\nstatus_cai\x18\x03 \x01(\x0b\x32\x1a.ondewo.vtsi.ServiceStatus\x12.\n\nstatus_stt\x18\x04 \x01(\x0b\x32\x1a.ondewo.vtsi.ServiceStatus\x12.\n\nstatus_tts\x18\x05 \x01(\x0b\x32\x1a.ondewo.vtsi.ServiceStatus\"9\n\rServiceStatus\x12\x0f\n\x07healthy\x18\x01 \x01(\x08\x12\x17\n\x0f\x65rror_messsages\x18\x02 \x01(\t\"3\n\x16GetSipAccountsResponse\x12\x19\n\x11\x61sterisk_accounts\x18\x01 \x03(\t\";\n\x1fGetCallIDsFromSipAccountRequest\x12\x18\n\x10\x61sterisk_account\x18\x01 \x03(\t\"4\n GetCallIDsFromSipAccountResponse\x12\x10\n\x08\x63\x61ll_ids\x18\x01 \x03(\t\"o\n\x13GetAudioFileRequest\x12\x13\n\x0b\x62ucket_name\x18\x01 \x01(\t\x12\x13\n\x0bobject_name\x18\x02 \x01(\t\x12.\n\x0cminio_config\x18\x03 \x01(\x0b\x32\x18.ondewo.vtsi.MinioConfig\"%\n\x14GetAudioFileResponse\x12\r\n\x05\x61udio\x18\x01 \x01(\x0c\"\x80\x01\n#GetFullConversationAudioFileRequest\x12\x13\n\x0b\x62ucket_name\x18\x01 \x01(\t\x12\x14\n\x0cobject_names\x18\x02 \x03(\t\x12.\n\x0cminio_config\x18\x03 \x01(\x0b\x32\x18.ondewo.vtsi.MinioConfig\"5\n$GetFullConversationAudioFileResponse\x12\r\n\x05\x61udio\x18\x01 \x01(\x0c*=\n\x10VoipCallInfoView\x12\x15\n\x11Info_VIEW_SHALLOW\x10\x00\x12\x12\n\x0eInfo_VIEW_FULL\x10\x01*/\n\x08\x43\x61llType\x12\x08\n\x04\x62oth\x10\x00\x12\x0b\n\x07inbound\x10\x01\x12\x0c\n\x08outbound\x10\x02\x32\x80\t\n\x0cVoipSessions\x12Y\n\x0eStartListeners\x12\".ondewo.vtsi.StartListenersRequest\x1a#.ondewo.vtsi.StartListenersResponse\x12S\n\x0cStartCallers\x12 .ondewo.vtsi.StartCallersRequest\x1a!.ondewo.vtsi.StartCallersResponse\x12n\n\x15StartScheduledCallers\x12).ondewo.vtsi.StartScheduledCallersRequest\x1a*.ondewo.vtsi.StartScheduledCallersResponse\x12J\n\tStopCalls\x12\x1d.ondewo.vtsi.StopCallsRequest\x1a\x1e.ondewo.vtsi.StopCallsResponse\x12I\n\x0cStopAllCalls\x12\x16.google.protobuf.Empty\x1a!.ondewo.vtsi.StopAllCallsResponse\x12S\n\x0cTransferCall\x12 .ondewo.vtsi.TransferCallRequest\x1a!.ondewo.vtsi.TransferCallResponse\x12\\\n\x0fGetVoipCallInfo\x12#.ondewo.vtsi.GetVoipCallInfoRequest\x1a$.ondewo.vtsi.GetVoipCallInfoResponse\x12_\n\x10ListVoipCallInfo\x12$.ondewo.vtsi.ListVoipCallInfoRequest\x1a%.ondewo.vtsi.ListVoipCallInfoResponse\x12M\n\x0eGetSipAccounts\x12\x16.google.protobuf.Empty\x1a#.ondewo.vtsi.GetSipAccountsResponse\x12w\n\x18GetCallIDsFromSipAccount\x12,.ondewo.vtsi.GetCallIDsFromSipAccountRequest\x1a-.ondewo.vtsi.GetCallIDsFromSipAccountResponse\x12U\n\x0cGetAudioFile\x12 .ondewo.vtsi.GetAudioFileRequest\x1a!.ondewo.vtsi.GetAudioFileResponse\"\x00\x12\x85\x01\n\x1cGetFullConversationAudioFile\x12\x30.ondewo.vtsi.GetFullConversationAudioFileRequest\x1a\x31.ondewo.vtsi.GetFullConversationAudioFileResponse\"\x00\x62\x06proto3')

_VOIPCALLINFOVIEW = DESCRIPTOR.enum_types_by_name['VoipCallInfoView']
VoipCallInfoView = enum_type_wrapper.EnumTypeWrapper(_VOIPCALLINFOVIEW)
_CALLTYPE = DESCRIPTOR.enum_types_by_name['CallType']
CallType = enum_type_wrapper.EnumTypeWrapper(_CALLTYPE)
Info_VIEW_SHALLOW = 0
Info_VIEW_FULL = 1
both = 0
inbound = 1
outbound = 2


_BASESERVICECONFIG = DESCRIPTOR.message_types_by_name['BaseServiceConfig']
_CREDENTIALS = DESCRIPTOR.message_types_by_name['Credentials']
_NLUCONFIG = DESCRIPTOR.message_types_by_name['NLUConfig']
_T2SCONFIG = DESCRIPTOR.message_types_by_name['T2SConfig']
_S2TCONFIG = DESCRIPTOR.message_types_by_name['S2TConfig']
_ASTERISKCONFIG = DESCRIPTOR.message_types_by_name['AsteriskConfig']
_COMMONSERVICESCONFIGS = DESCRIPTOR.message_types_by_name['CommonServicesConfigs']
_SIPBASECONFIG = DESCRIPTOR.message_types_by_name['SIPBaseConfig']
_SIPBASECONFIG_ACCOUNTPASSWORDDICTIONARYENTRY = _SIPBASECONFIG.nested_types_by_name['AccountPasswordDictionaryEntry']
_SIPCALLERCONFIG = DESCRIPTOR.message_types_by_name['SIPCallerConfig']
_SIPCALLERCONFIG_HEADERSENTRY = _SIPCALLERCONFIG.nested_types_by_name['HeadersEntry']
_CSICONFIG = DESCRIPTOR.message_types_by_name['CsiConfig']
_AUDIOOBJECTSTORAGECONFIG = DESCRIPTOR.message_types_by_name['AudioObjectStorageConfig']
_MESSAGEBROKERCONFIG = DESCRIPTOR.message_types_by_name['MessageBrokerConfig']
_RABBITMQCONFIG = DESCRIPTOR.message_types_by_name['RabbitMqConfig']
_ENDPOINT = DESCRIPTOR.message_types_by_name['Endpoint']
_MINIOCONFIG = DESCRIPTOR.message_types_by_name['MinioConfig']
_S2TCALLBACKS = DESCRIPTOR.message_types_by_name['S2tCallbacks']
_NLUCALLBACKS = DESCRIPTOR.message_types_by_name['NluCallbacks']
_T2SCALLBACKS = DESCRIPTOR.message_types_by_name['T2sCallbacks']
_STARTLISTENERREQUEST = DESCRIPTOR.message_types_by_name['StartListenerRequest']
_STARTLISTENERRESPONSE = DESCRIPTOR.message_types_by_name['StartListenerResponse']
_STARTCALLERREQUEST = DESCRIPTOR.message_types_by_name['StartCallerRequest']
_STARTCALLERRESPONSE = DESCRIPTOR.message_types_by_name['StartCallerResponse']
_STARTSCHEDULEDCALLERREQUEST = DESCRIPTOR.message_types_by_name['StartScheduledCallerRequest']
_STARTSCHEDULEDCALLERRESPONSE = DESCRIPTOR.message_types_by_name['StartScheduledCallerResponse']
_STARTLISTENERSREQUEST = DESCRIPTOR.message_types_by_name['StartListenersRequest']
_STARTLISTENERSRESPONSE = DESCRIPTOR.message_types_by_name['StartListenersResponse']
_STARTCALLERSREQUEST = DESCRIPTOR.message_types_by_name['StartCallersRequest']
_STARTCALLERSRESPONSE = DESCRIPTOR.message_types_by_name['StartCallersResponse']
_STARTSCHEDULEDCALLERSREQUEST = DESCRIPTOR.message_types_by_name['StartScheduledCallersRequest']
_STARTSCHEDULEDCALLERSRESPONSE = DESCRIPTOR.message_types_by_name['StartScheduledCallersResponse']
_STOPCALLREQUEST = DESCRIPTOR.message_types_by_name['StopCallRequest']
_STOPCALLRESPONSE = DESCRIPTOR.message_types_by_name['StopCallResponse']
_STOPCALLSREQUEST = DESCRIPTOR.message_types_by_name['StopCallsRequest']
_STOPCALLSRESPONSE = DESCRIPTOR.message_types_by_name['StopCallsResponse']
_STOPALLCALLSRESPONSE = DESCRIPTOR.message_types_by_name['StopAllCallsResponse']
_TRANSFERCALLREQUEST = DESCRIPTOR.message_types_by_name['TransferCallRequest']
_TRANSFERCALLRESPONSE = DESCRIPTOR.message_types_by_name['TransferCallResponse']
_GETVOIPCALLINFOREQUEST = DESCRIPTOR.message_types_by_name['GetVoipCallInfoRequest']
_GETVOIPCALLINFORESPONSE = DESCRIPTOR.message_types_by_name['GetVoipCallInfoResponse']
_VOIPCALLINFO = DESCRIPTOR.message_types_by_name['VoipCallInfo']
_LISTVOIPCALLINFOREQUEST = DESCRIPTOR.message_types_by_name['ListVoipCallInfoRequest']
_LISTVOIPCALLINFORESPONSE = DESCRIPTOR.message_types_by_name['ListVoipCallInfoResponse']
_ALLSERVICESSTATUSES = DESCRIPTOR.message_types_by_name['AllServicesStatuses']
_SERVICESTATUS = DESCRIPTOR.message_types_by_name['ServiceStatus']
_GETSIPACCOUNTSRESPONSE = DESCRIPTOR.message_types_by_name['GetSipAccountsResponse']
_GETCALLIDSFROMSIPACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['GetCallIDsFromSipAccountRequest']
_GETCALLIDSFROMSIPACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['GetCallIDsFromSipAccountResponse']
_GETAUDIOFILEREQUEST = DESCRIPTOR.message_types_by_name['GetAudioFileRequest']
_GETAUDIOFILERESPONSE = DESCRIPTOR.message_types_by_name['GetAudioFileResponse']
_GETFULLCONVERSATIONAUDIOFILEREQUEST = DESCRIPTOR.message_types_by_name['GetFullConversationAudioFileRequest']
_GETFULLCONVERSATIONAUDIOFILERESPONSE = DESCRIPTOR.message_types_by_name['GetFullConversationAudioFileResponse']
BaseServiceConfig = _reflection.GeneratedProtocolMessageType('BaseServiceConfig', (_message.Message,), {
  'DESCRIPTOR' : _BASESERVICECONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.BaseServiceConfig)
  })
_sym_db.RegisterMessage(BaseServiceConfig)

Credentials = _reflection.GeneratedProtocolMessageType('Credentials', (_message.Message,), {
  'DESCRIPTOR' : _CREDENTIALS,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.Credentials)
  })
_sym_db.RegisterMessage(Credentials)

NLUConfig = _reflection.GeneratedProtocolMessageType('NLUConfig', (_message.Message,), {
  'DESCRIPTOR' : _NLUCONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.NLUConfig)
  })
_sym_db.RegisterMessage(NLUConfig)

T2SConfig = _reflection.GeneratedProtocolMessageType('T2SConfig', (_message.Message,), {
  'DESCRIPTOR' : _T2SCONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.T2SConfig)
  })
_sym_db.RegisterMessage(T2SConfig)

S2TConfig = _reflection.GeneratedProtocolMessageType('S2TConfig', (_message.Message,), {
  'DESCRIPTOR' : _S2TCONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.S2TConfig)
  })
_sym_db.RegisterMessage(S2TConfig)

AsteriskConfig = _reflection.GeneratedProtocolMessageType('AsteriskConfig', (_message.Message,), {
  'DESCRIPTOR' : _ASTERISKCONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.AsteriskConfig)
  })
_sym_db.RegisterMessage(AsteriskConfig)

CommonServicesConfigs = _reflection.GeneratedProtocolMessageType('CommonServicesConfigs', (_message.Message,), {
  'DESCRIPTOR' : _COMMONSERVICESCONFIGS,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.CommonServicesConfigs)
  })
_sym_db.RegisterMessage(CommonServicesConfigs)

SIPBaseConfig = _reflection.GeneratedProtocolMessageType('SIPBaseConfig', (_message.Message,), {

  'AccountPasswordDictionaryEntry' : _reflection.GeneratedProtocolMessageType('AccountPasswordDictionaryEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIPBASECONFIG_ACCOUNTPASSWORDDICTIONARYENTRY,
    '__module__' : 'ondewo.vtsi.voip_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.SIPBaseConfig.AccountPasswordDictionaryEntry)
    })
  ,
  'DESCRIPTOR' : _SIPBASECONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.SIPBaseConfig)
  })
_sym_db.RegisterMessage(SIPBaseConfig)
_sym_db.RegisterMessage(SIPBaseConfig.AccountPasswordDictionaryEntry)

SIPCallerConfig = _reflection.GeneratedProtocolMessageType('SIPCallerConfig', (_message.Message,), {

  'HeadersEntry' : _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIPCALLERCONFIG_HEADERSENTRY,
    '__module__' : 'ondewo.vtsi.voip_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.SIPCallerConfig.HeadersEntry)
    })
  ,
  'DESCRIPTOR' : _SIPCALLERCONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.SIPCallerConfig)
  })
_sym_db.RegisterMessage(SIPCallerConfig)
_sym_db.RegisterMessage(SIPCallerConfig.HeadersEntry)

CsiConfig = _reflection.GeneratedProtocolMessageType('CsiConfig', (_message.Message,), {
  'DESCRIPTOR' : _CSICONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.CsiConfig)
  })
_sym_db.RegisterMessage(CsiConfig)

AudioObjectStorageConfig = _reflection.GeneratedProtocolMessageType('AudioObjectStorageConfig', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOOBJECTSTORAGECONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.AudioObjectStorageConfig)
  })
_sym_db.RegisterMessage(AudioObjectStorageConfig)

MessageBrokerConfig = _reflection.GeneratedProtocolMessageType('MessageBrokerConfig', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEBROKERCONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.MessageBrokerConfig)
  })
_sym_db.RegisterMessage(MessageBrokerConfig)

RabbitMqConfig = _reflection.GeneratedProtocolMessageType('RabbitMqConfig', (_message.Message,), {
  'DESCRIPTOR' : _RABBITMQCONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.RabbitMqConfig)
  })
_sym_db.RegisterMessage(RabbitMqConfig)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINT,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.Endpoint)
  })
_sym_db.RegisterMessage(Endpoint)

MinioConfig = _reflection.GeneratedProtocolMessageType('MinioConfig', (_message.Message,), {
  'DESCRIPTOR' : _MINIOCONFIG,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.MinioConfig)
  })
_sym_db.RegisterMessage(MinioConfig)

S2tCallbacks = _reflection.GeneratedProtocolMessageType('S2tCallbacks', (_message.Message,), {
  'DESCRIPTOR' : _S2TCALLBACKS,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.S2tCallbacks)
  })
_sym_db.RegisterMessage(S2tCallbacks)

NluCallbacks = _reflection.GeneratedProtocolMessageType('NluCallbacks', (_message.Message,), {
  'DESCRIPTOR' : _NLUCALLBACKS,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.NluCallbacks)
  })
_sym_db.RegisterMessage(NluCallbacks)

T2sCallbacks = _reflection.GeneratedProtocolMessageType('T2sCallbacks', (_message.Message,), {
  'DESCRIPTOR' : _T2SCALLBACKS,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.T2sCallbacks)
  })
_sym_db.RegisterMessage(T2sCallbacks)

StartListenerRequest = _reflection.GeneratedProtocolMessageType('StartListenerRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTLISTENERREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartListenerRequest)
  })
_sym_db.RegisterMessage(StartListenerRequest)

StartListenerResponse = _reflection.GeneratedProtocolMessageType('StartListenerResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTLISTENERRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartListenerResponse)
  })
_sym_db.RegisterMessage(StartListenerResponse)

StartCallerRequest = _reflection.GeneratedProtocolMessageType('StartCallerRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTCALLERREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartCallerRequest)
  })
_sym_db.RegisterMessage(StartCallerRequest)

StartCallerResponse = _reflection.GeneratedProtocolMessageType('StartCallerResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTCALLERRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartCallerResponse)
  })
_sym_db.RegisterMessage(StartCallerResponse)

StartScheduledCallerRequest = _reflection.GeneratedProtocolMessageType('StartScheduledCallerRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTSCHEDULEDCALLERREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartScheduledCallerRequest)
  })
_sym_db.RegisterMessage(StartScheduledCallerRequest)

StartScheduledCallerResponse = _reflection.GeneratedProtocolMessageType('StartScheduledCallerResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTSCHEDULEDCALLERRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartScheduledCallerResponse)
  })
_sym_db.RegisterMessage(StartScheduledCallerResponse)

StartListenersRequest = _reflection.GeneratedProtocolMessageType('StartListenersRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTLISTENERSREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartListenersRequest)
  })
_sym_db.RegisterMessage(StartListenersRequest)

StartListenersResponse = _reflection.GeneratedProtocolMessageType('StartListenersResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTLISTENERSRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartListenersResponse)
  })
_sym_db.RegisterMessage(StartListenersResponse)

StartCallersRequest = _reflection.GeneratedProtocolMessageType('StartCallersRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTCALLERSREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartCallersRequest)
  })
_sym_db.RegisterMessage(StartCallersRequest)

StartCallersResponse = _reflection.GeneratedProtocolMessageType('StartCallersResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTCALLERSRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartCallersResponse)
  })
_sym_db.RegisterMessage(StartCallersResponse)

StartScheduledCallersRequest = _reflection.GeneratedProtocolMessageType('StartScheduledCallersRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTSCHEDULEDCALLERSREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartScheduledCallersRequest)
  })
_sym_db.RegisterMessage(StartScheduledCallersRequest)

StartScheduledCallersResponse = _reflection.GeneratedProtocolMessageType('StartScheduledCallersResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTSCHEDULEDCALLERSRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StartScheduledCallersResponse)
  })
_sym_db.RegisterMessage(StartScheduledCallersResponse)

StopCallRequest = _reflection.GeneratedProtocolMessageType('StopCallRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPCALLREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StopCallRequest)
  })
_sym_db.RegisterMessage(StopCallRequest)

StopCallResponse = _reflection.GeneratedProtocolMessageType('StopCallResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPCALLRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StopCallResponse)
  })
_sym_db.RegisterMessage(StopCallResponse)

StopCallsRequest = _reflection.GeneratedProtocolMessageType('StopCallsRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPCALLSREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StopCallsRequest)
  })
_sym_db.RegisterMessage(StopCallsRequest)

StopCallsResponse = _reflection.GeneratedProtocolMessageType('StopCallsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPCALLSRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StopCallsResponse)
  })
_sym_db.RegisterMessage(StopCallsResponse)

StopAllCallsResponse = _reflection.GeneratedProtocolMessageType('StopAllCallsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPALLCALLSRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.StopAllCallsResponse)
  })
_sym_db.RegisterMessage(StopAllCallsResponse)

TransferCallRequest = _reflection.GeneratedProtocolMessageType('TransferCallRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERCALLREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.TransferCallRequest)
  })
_sym_db.RegisterMessage(TransferCallRequest)

TransferCallResponse = _reflection.GeneratedProtocolMessageType('TransferCallResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERCALLRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.TransferCallResponse)
  })
_sym_db.RegisterMessage(TransferCallResponse)

GetVoipCallInfoRequest = _reflection.GeneratedProtocolMessageType('GetVoipCallInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVOIPCALLINFOREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetVoipCallInfoRequest)
  })
_sym_db.RegisterMessage(GetVoipCallInfoRequest)

GetVoipCallInfoResponse = _reflection.GeneratedProtocolMessageType('GetVoipCallInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVOIPCALLINFORESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetVoipCallInfoResponse)
  })
_sym_db.RegisterMessage(GetVoipCallInfoResponse)

VoipCallInfo = _reflection.GeneratedProtocolMessageType('VoipCallInfo', (_message.Message,), {
  'DESCRIPTOR' : _VOIPCALLINFO,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.VoipCallInfo)
  })
_sym_db.RegisterMessage(VoipCallInfo)

ListVoipCallInfoRequest = _reflection.GeneratedProtocolMessageType('ListVoipCallInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTVOIPCALLINFOREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.ListVoipCallInfoRequest)
  })
_sym_db.RegisterMessage(ListVoipCallInfoRequest)

ListVoipCallInfoResponse = _reflection.GeneratedProtocolMessageType('ListVoipCallInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTVOIPCALLINFORESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.ListVoipCallInfoResponse)
  })
_sym_db.RegisterMessage(ListVoipCallInfoResponse)

AllServicesStatuses = _reflection.GeneratedProtocolMessageType('AllServicesStatuses', (_message.Message,), {
  'DESCRIPTOR' : _ALLSERVICESSTATUSES,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.AllServicesStatuses)
  })
_sym_db.RegisterMessage(AllServicesStatuses)

ServiceStatus = _reflection.GeneratedProtocolMessageType('ServiceStatus', (_message.Message,), {
  'DESCRIPTOR' : _SERVICESTATUS,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.ServiceStatus)
  })
_sym_db.RegisterMessage(ServiceStatus)

GetSipAccountsResponse = _reflection.GeneratedProtocolMessageType('GetSipAccountsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSIPACCOUNTSRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetSipAccountsResponse)
  })
_sym_db.RegisterMessage(GetSipAccountsResponse)

GetCallIDsFromSipAccountRequest = _reflection.GeneratedProtocolMessageType('GetCallIDsFromSipAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCALLIDSFROMSIPACCOUNTREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetCallIDsFromSipAccountRequest)
  })
_sym_db.RegisterMessage(GetCallIDsFromSipAccountRequest)

GetCallIDsFromSipAccountResponse = _reflection.GeneratedProtocolMessageType('GetCallIDsFromSipAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCALLIDSFROMSIPACCOUNTRESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetCallIDsFromSipAccountResponse)
  })
_sym_db.RegisterMessage(GetCallIDsFromSipAccountResponse)

GetAudioFileRequest = _reflection.GeneratedProtocolMessageType('GetAudioFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAUDIOFILEREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetAudioFileRequest)
  })
_sym_db.RegisterMessage(GetAudioFileRequest)

GetAudioFileResponse = _reflection.GeneratedProtocolMessageType('GetAudioFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETAUDIOFILERESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetAudioFileResponse)
  })
_sym_db.RegisterMessage(GetAudioFileResponse)

GetFullConversationAudioFileRequest = _reflection.GeneratedProtocolMessageType('GetFullConversationAudioFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFULLCONVERSATIONAUDIOFILEREQUEST,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetFullConversationAudioFileRequest)
  })
_sym_db.RegisterMessage(GetFullConversationAudioFileRequest)

GetFullConversationAudioFileResponse = _reflection.GeneratedProtocolMessageType('GetFullConversationAudioFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFULLCONVERSATIONAUDIOFILERESPONSE,
  '__module__' : 'ondewo.vtsi.voip_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetFullConversationAudioFileResponse)
  })
_sym_db.RegisterMessage(GetFullConversationAudioFileResponse)

_VOIPSESSIONS = DESCRIPTOR.services_by_name['VoipSessions']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIPBASECONFIG_ACCOUNTPASSWORDDICTIONARYENTRY._options = None
  _SIPBASECONFIG_ACCOUNTPASSWORDDICTIONARYENTRY._serialized_options = b'8\001'
  _SIPCALLERCONFIG_HEADERSENTRY._options = None
  _SIPCALLERCONFIG_HEADERSENTRY._serialized_options = b'8\001'
  _VOIPCALLINFOVIEW._serialized_start=6427
  _VOIPCALLINFOVIEW._serialized_end=6488
  _CALLTYPE._serialized_start=6490
  _CALLTYPE._serialized_end=6537
  _BASESERVICECONFIG._serialized_start=275
  _BASESERVICECONFIG._serialized_end=341
  _CREDENTIALS._serialized_start=343
  _CREDENTIALS._serialized_end=396
  _NLUCONFIG._serialized_start=399
  _NLUCONFIG._serialized_end=658
  _T2SCONFIG._serialized_start=660
  _T2SCONFIG._serialized_end=771
  _S2TCONFIG._serialized_start=773
  _S2TCONFIG._serialized_end=894
  _ASTERISKCONFIG._serialized_start=896
  _ASTERISKCONFIG._serialized_end=965
  _COMMONSERVICESCONFIGS._serialized_start=968
  _COMMONSERVICESCONFIGS._serialized_end=1221
  _SIPBASECONFIG._serialized_start=1224
  _SIPBASECONFIG._serialized_end=1511
  _SIPBASECONFIG_ACCOUNTPASSWORDDICTIONARYENTRY._serialized_start=1447
  _SIPBASECONFIG_ACCOUNTPASSWORDDICTIONARYENTRY._serialized_end=1511
  _SIPCALLERCONFIG._serialized_start=1514
  _SIPCALLERCONFIG._serialized_end=1714
  _SIPCALLERCONFIG_HEADERSENTRY._serialized_start=1668
  _SIPCALLERCONFIG_HEADERSENTRY._serialized_end=1714
  _CSICONFIG._serialized_start=1717
  _CSICONFIG._serialized_end=2017
  _AUDIOOBJECTSTORAGECONFIG._serialized_start=2019
  _AUDIOOBJECTSTORAGECONFIG._serialized_end=2119
  _MESSAGEBROKERCONFIG._serialized_start=2121
  _MESSAGEBROKERCONFIG._serialized_end=2224
  _RABBITMQCONFIG._serialized_start=2226
  _RABBITMQCONFIG._serialized_end=2318
  _ENDPOINT._serialized_start=2320
  _ENDPOINT._serialized_end=2358
  _MINIOCONFIG._serialized_start=2361
  _MINIOCONFIG._serialized_end=2494
  _S2TCALLBACKS._serialized_start=2496
  _S2TCALLBACKS._serialized_end=2565
  _NLUCALLBACKS._serialized_start=2567
  _NLUCALLBACKS._serialized_end=2636
  _T2SCALLBACKS._serialized_start=2638
  _T2SCALLBACKS._serialized_end=2707
  _STARTLISTENERREQUEST._serialized_start=2710
  _STARTLISTENERREQUEST._serialized_end=2842
  _STARTLISTENERRESPONSE._serialized_start=2844
  _STARTLISTENERRESPONSE._serialized_end=2960
  _STARTCALLERREQUEST._serialized_start=2963
  _STARTCALLERREQUEST._serialized_end=3095
  _STARTCALLERRESPONSE._serialized_start=3097
  _STARTCALLERRESPONSE._serialized_end=3209
  _STARTSCHEDULEDCALLERREQUEST._serialized_start=3212
  _STARTSCHEDULEDCALLERREQUEST._serialized_end=3343
  _STARTSCHEDULEDCALLERRESPONSE._serialized_start=3346
  _STARTSCHEDULEDCALLERRESPONSE._serialized_end=3476
  _STARTLISTENERSREQUEST._serialized_start=3478
  _STARTLISTENERSREQUEST._serialized_end=3554
  _STARTLISTENERSRESPONSE._serialized_start=3556
  _STARTLISTENERSRESPONSE._serialized_end=3674
  _STARTCALLERSREQUEST._serialized_start=3676
  _STARTCALLERSREQUEST._serialized_end=3748
  _STARTCALLERSRESPONSE._serialized_start=3750
  _STARTCALLERSRESPONSE._serialized_end=3864
  _STARTSCHEDULEDCALLERSREQUEST._serialized_start=3866
  _STARTSCHEDULEDCALLERSREQUEST._serialized_end=3956
  _STARTSCHEDULEDCALLERSRESPONSE._serialized_start=3959
  _STARTSCHEDULEDCALLERSRESPONSE._serialized_end=4091
  _STOPCALLREQUEST._serialized_start=4093
  _STOPCALLREQUEST._serialized_end=4158
  _STOPCALLRESPONSE._serialized_start=4160
  _STOPCALLRESPONSE._serialized_end=4287
  _STOPCALLSREQUEST._serialized_start=4289
  _STOPCALLSREQUEST._serialized_end=4355
  _STOPCALLSRESPONSE._serialized_start=4357
  _STOPCALLSRESPONSE._serialized_end=4426
  _STOPALLCALLSRESPONSE._serialized_start=4428
  _STOPALLCALLSRESPONSE._serialized_end=4510
  _TRANSFERCALLREQUEST._serialized_start=4512
  _TRANSFERCALLREQUEST._serialized_end=4602
  _TRANSFERCALLRESPONSE._serialized_start=4604
  _TRANSFERCALLRESPONSE._serialized_end=4718
  _GETVOIPCALLINFOREQUEST._serialized_start=4721
  _GETVOIPCALLINFOREQUEST._serialized_end=4895
  _GETVOIPCALLINFORESPONSE._serialized_start=4897
  _GETVOIPCALLINFORESPONSE._serialized_end=5015
  _VOIPCALLINFO._serialized_start=5018
  _VOIPCALLINFO._serialized_end=5388
  _LISTVOIPCALLINFOREQUEST._serialized_start=5390
  _LISTVOIPCALLINFOREQUEST._serialized_end=5517
  _LISTVOIPCALLINFORESPONSE._serialized_start=5519
  _LISTVOIPCALLINFORESPONSE._serialized_end=5591
  _ALLSERVICESSTATUSES._serialized_start=5594
  _ALLSERVICESSTATUSES._serialized_end=5860
  _SERVICESTATUS._serialized_start=5862
  _SERVICESTATUS._serialized_end=5919
  _GETSIPACCOUNTSRESPONSE._serialized_start=5921
  _GETSIPACCOUNTSRESPONSE._serialized_end=5972
  _GETCALLIDSFROMSIPACCOUNTREQUEST._serialized_start=5974
  _GETCALLIDSFROMSIPACCOUNTREQUEST._serialized_end=6033
  _GETCALLIDSFROMSIPACCOUNTRESPONSE._serialized_start=6035
  _GETCALLIDSFROMSIPACCOUNTRESPONSE._serialized_end=6087
  _GETAUDIOFILEREQUEST._serialized_start=6089
  _GETAUDIOFILEREQUEST._serialized_end=6200
  _GETAUDIOFILERESPONSE._serialized_start=6202
  _GETAUDIOFILERESPONSE._serialized_end=6239
  _GETFULLCONVERSATIONAUDIOFILEREQUEST._serialized_start=6242
  _GETFULLCONVERSATIONAUDIOFILEREQUEST._serialized_end=6370
  _GETFULLCONVERSATIONAUDIOFILERESPONSE._serialized_start=6372
  _GETFULLCONVERSATIONAUDIOFILERESPONSE._serialized_end=6425
  _VOIPSESSIONS._serialized_start=6540
  _VOIPSESSIONS._serialized_end=7692
# @@protoc_insertion_point(module_scope)
