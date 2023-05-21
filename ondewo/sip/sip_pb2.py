# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/sip/sip.proto
"""Generated protocol buffer code."""
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14ondewo/sip/sip.proto\x12\nondewo.sip\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"(\n\x11SipEndCallRequest\x12\x13\n\x0bhard_hangup\x18\x01 \x01(\x08\"\x97\x01\n\x13SipStartCallRequest\x12\x11\n\tcallee_id\x18\x01 \x01(\t\x12=\n\x07headers\x18\x02 \x03(\x0b\x32,.ondewo.sip.SipStartCallRequest.HeadersEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"r\n\x19SipRegisterAccountRequest\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x15\n\rauth_username\x18\x03 \x01(\t\x12\x16\n\x0eoutbound_proxy\x18\x04 \x01(\t\"L\n\x16SipStartSessionRequest\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\t\x12\x1c\n\x14\x61uto_answer_interval\x18\x02 \x01(\x05\"\x9f\x01\n\x16SipTransferCallRequest\x12\x13\n\x0btransfer_id\x18\x01 \x01(\t\x12@\n\x07headers\x18\x02 \x03(\x0b\x32/.ondewo.sip.SipTransferCallRequest.HeadersEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x97\x07\n\tSipStatus\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x0bstatus_type\x18\x03 \x01(\x0e\x32 .ondewo.sip.SipStatus.StatusType\x12\x11\n\tcallee_id\x18\x04 \x01(\t\x12\x18\n\x10transfer_call_id\x18\x05 \x01(\t\x12\x33\n\x07headers\x18\x06 \x03(\x0b\x32\".ondewo.sip.SipStatus.HeadersEntry\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x16\n\x0e\x65xception_name\x18\x08 \x01(\t\x12\x1b\n\x13\x65xception_traceback\x18\t \x01(\t\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb1\x04\n\nStatusType\x12\x0e\n\nNO_SESSION\x10\x00\x12\x0e\n\nREGISTERED\x10\x01\x12\t\n\x05READY\x10\x02\x12\x1b\n\x17INCOMING_CALL_INITIATED\x10\x03\x12\x1b\n\x17OUTGOING_CALL_INITIATED\x10\x04\x12\x1b\n\x17OUTGOING_CALL_CONNECTED\x10\x05\x12\x1b\n\x17INCOMING_CALL_CONNECTED\x10\x06\x12\x1b\n\x17TRANSFER_CALL_INITIATED\x10\x07\x12\x19\n\x15SOFT_HANGUP_INITIATED\x10\x08\x12\x19\n\x15HARD_HANGUP_INITIATED\x10\t\x12\x18\n\x14INCOMING_CALL_FAILED\x10\n\x12\x18\n\x14OUTGOING_CALL_FAILED\x10\x0b\x12\x1a\n\x16INCOMING_CALL_FINISHED\x10\x0c\x12\x1a\n\x16OUTGOING_CALL_FINISHED\x10\r\x12\x1f\n\x1bSESSION_REGISTRATION_FAILED\x10\x0e\x12\x13\n\x0fSESSION_STARTED\x10\x0f\x12\x11\n\rSESSION_ENDED\x10\x10\x12\x18\n\x14TRANSFER_CALL_FAILED\x10\x11\x12\x14\n\x10MICROPHONE_MUTED\x10\x12\x12\x16\n\x12MICROPHONE_UNMUTED\x10\x13\x12\x1f\n\x1bMICROPHONE_WAV_FILES_PLAYED\x10\x14\x12\x13\n\x0fNO_ONGOING_CALL\x10\x15\"I\n\x18SipStatusHistoryResponse\x12-\n\x0estatus_history\x18\x01 \x03(\x0b\x32\x15.ondewo.sip.SipStatus\"+\n\x16SipPlayWavFilesRequest\x12\x11\n\twav_files\x18\x01 \x03(\x0c\x32\xb5\x06\n\x03Sip\x12N\n\x0fSipStartSession\x12\".ondewo.sip.SipStartSessionRequest\x1a\x15.ondewo.sip.SipStatus\"\x00\x12@\n\rSipEndSession\x12\x16.google.protobuf.Empty\x1a\x15.ondewo.sip.SipStatus\"\x00\x12H\n\x0cSipStartCall\x12\x1f.ondewo.sip.SipStartCallRequest\x1a\x15.ondewo.sip.SipStatus\"\x00\x12\x44\n\nSipEndCall\x12\x1d.ondewo.sip.SipEndCallRequest\x1a\x15.ondewo.sip.SipStatus\"\x00\x12N\n\x0fSipTransferCall\x12\".ondewo.sip.SipTransferCallRequest\x1a\x15.ondewo.sip.SipStatus\"\x00\x12T\n\x12SipRegisterAccount\x12%.ondewo.sip.SipRegisterAccountRequest\x1a\x15.ondewo.sip.SipStatus\"\x00\x12\x42\n\x0fSipGetSipStatus\x12\x16.google.protobuf.Empty\x1a\x15.ondewo.sip.SipStatus\"\x00\x12X\n\x16SipGetSipStatusHistory\x12\x16.google.protobuf.Empty\x1a$.ondewo.sip.SipStatusHistoryResponse\"\x00\x12N\n\x0fSipPlayWavFiles\x12\".ondewo.sip.SipPlayWavFilesRequest\x1a\x15.ondewo.sip.SipStatus\"\x00\x12:\n\x07SipMute\x12\x16.google.protobuf.Empty\x1a\x15.ondewo.sip.SipStatus\"\x00\x12<\n\tSipUnMute\x12\x16.google.protobuf.Empty\x1a\x15.ondewo.sip.SipStatus\"\x00\x62\x06proto3')


_SIPENDCALLREQUEST = DESCRIPTOR.message_types_by_name['SipEndCallRequest']
_SIPSTARTCALLREQUEST = DESCRIPTOR.message_types_by_name['SipStartCallRequest']
_SIPSTARTCALLREQUEST_HEADERSENTRY = _SIPSTARTCALLREQUEST.nested_types_by_name['HeadersEntry']
_SIPREGISTERACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['SipRegisterAccountRequest']
_SIPSTARTSESSIONREQUEST = DESCRIPTOR.message_types_by_name['SipStartSessionRequest']
_SIPTRANSFERCALLREQUEST = DESCRIPTOR.message_types_by_name['SipTransferCallRequest']
_SIPTRANSFERCALLREQUEST_HEADERSENTRY = _SIPTRANSFERCALLREQUEST.nested_types_by_name['HeadersEntry']
_SIPSTATUS = DESCRIPTOR.message_types_by_name['SipStatus']
_SIPSTATUS_HEADERSENTRY = _SIPSTATUS.nested_types_by_name['HeadersEntry']
_SIPSTATUSHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['SipStatusHistoryResponse']
_SIPPLAYWAVFILESREQUEST = DESCRIPTOR.message_types_by_name['SipPlayWavFilesRequest']
_SIPSTATUS_STATUSTYPE = _SIPSTATUS.enum_types_by_name['StatusType']
SipEndCallRequest = _reflection.GeneratedProtocolMessageType('SipEndCallRequest', (_message.Message,), {
    'DESCRIPTOR': _SIPENDCALLREQUEST,
    '__module__': 'ondewo.sip.sip_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.sip.SipEndCallRequest)
})
_sym_db.RegisterMessage(SipEndCallRequest)

SipStartCallRequest = _reflection.GeneratedProtocolMessageType('SipStartCallRequest', (_message.Message,), {

    'HeadersEntry': _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
        'DESCRIPTOR': _SIPSTARTCALLREQUEST_HEADERSENTRY,
        '__module__': 'ondewo.sip.sip_pb2'
        # @@protoc_insertion_point(class_scope:ondewo.sip.SipStartCallRequest.HeadersEntry)
    }),
    'DESCRIPTOR': _SIPSTARTCALLREQUEST,
    '__module__': 'ondewo.sip.sip_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.sip.SipStartCallRequest)
})
_sym_db.RegisterMessage(SipStartCallRequest)
_sym_db.RegisterMessage(SipStartCallRequest.HeadersEntry)

SipRegisterAccountRequest = _reflection.GeneratedProtocolMessageType('SipRegisterAccountRequest', (_message.Message,), {
    'DESCRIPTOR': _SIPREGISTERACCOUNTREQUEST,
    '__module__': 'ondewo.sip.sip_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.sip.SipRegisterAccountRequest)
})
_sym_db.RegisterMessage(SipRegisterAccountRequest)

SipStartSessionRequest = _reflection.GeneratedProtocolMessageType('SipStartSessionRequest', (_message.Message,), {
    'DESCRIPTOR': _SIPSTARTSESSIONREQUEST,
    '__module__': 'ondewo.sip.sip_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.sip.SipStartSessionRequest)
})
_sym_db.RegisterMessage(SipStartSessionRequest)

SipTransferCallRequest = _reflection.GeneratedProtocolMessageType('SipTransferCallRequest', (_message.Message,), {

    'HeadersEntry': _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
        'DESCRIPTOR': _SIPTRANSFERCALLREQUEST_HEADERSENTRY,
        '__module__': 'ondewo.sip.sip_pb2'
        # @@protoc_insertion_point(class_scope:ondewo.sip.SipTransferCallRequest.HeadersEntry)
    }),
    'DESCRIPTOR': _SIPTRANSFERCALLREQUEST,
    '__module__': 'ondewo.sip.sip_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.sip.SipTransferCallRequest)
})
_sym_db.RegisterMessage(SipTransferCallRequest)
_sym_db.RegisterMessage(SipTransferCallRequest.HeadersEntry)

SipStatus = _reflection.GeneratedProtocolMessageType('SipStatus', (_message.Message,), {

    'HeadersEntry': _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
        'DESCRIPTOR': _SIPSTATUS_HEADERSENTRY,
        '__module__': 'ondewo.sip.sip_pb2'
        # @@protoc_insertion_point(class_scope:ondewo.sip.SipStatus.HeadersEntry)
    }),
    'DESCRIPTOR': _SIPSTATUS,
    '__module__': 'ondewo.sip.sip_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.sip.SipStatus)
})
_sym_db.RegisterMessage(SipStatus)
_sym_db.RegisterMessage(SipStatus.HeadersEntry)

SipStatusHistoryResponse = _reflection.GeneratedProtocolMessageType('SipStatusHistoryResponse', (_message.Message,), {
    'DESCRIPTOR': _SIPSTATUSHISTORYRESPONSE,
    '__module__': 'ondewo.sip.sip_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.sip.SipStatusHistoryResponse)
})
_sym_db.RegisterMessage(SipStatusHistoryResponse)

SipPlayWavFilesRequest = _reflection.GeneratedProtocolMessageType('SipPlayWavFilesRequest', (_message.Message,), {
    'DESCRIPTOR': _SIPPLAYWAVFILESREQUEST,
    '__module__': 'ondewo.sip.sip_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.sip.SipPlayWavFilesRequest)
})
_sym_db.RegisterMessage(SipPlayWavFilesRequest)

_SIP = DESCRIPTOR.services_by_name['Sip']
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _SIPSTARTCALLREQUEST_HEADERSENTRY._options = None
    _SIPSTARTCALLREQUEST_HEADERSENTRY._serialized_options = b'8\001'
    _SIPTRANSFERCALLREQUEST_HEADERSENTRY._options = None
    _SIPTRANSFERCALLREQUEST_HEADERSENTRY._serialized_options = b'8\001'
    _SIPSTATUS_HEADERSENTRY._options = None
    _SIPSTATUS_HEADERSENTRY._serialized_options = b'8\001'
    _SIPENDCALLREQUEST._serialized_start = 98
    _SIPENDCALLREQUEST._serialized_end = 138
    _SIPSTARTCALLREQUEST._serialized_start = 141
    _SIPSTARTCALLREQUEST._serialized_end = 292
    _SIPSTARTCALLREQUEST_HEADERSENTRY._serialized_start = 246
    _SIPSTARTCALLREQUEST_HEADERSENTRY._serialized_end = 292
    _SIPREGISTERACCOUNTREQUEST._serialized_start = 294
    _SIPREGISTERACCOUNTREQUEST._serialized_end = 408
    _SIPSTARTSESSIONREQUEST._serialized_start = 410
    _SIPSTARTSESSIONREQUEST._serialized_end = 486
    _SIPTRANSFERCALLREQUEST._serialized_start = 489
    _SIPTRANSFERCALLREQUEST._serialized_end = 648
    _SIPTRANSFERCALLREQUEST_HEADERSENTRY._serialized_start = 246
    _SIPTRANSFERCALLREQUEST_HEADERSENTRY._serialized_end = 292
    _SIPSTATUS._serialized_start = 651
    _SIPSTATUS._serialized_end = 1570
    _SIPSTATUS_HEADERSENTRY._serialized_start = 246
    _SIPSTATUS_HEADERSENTRY._serialized_end = 292
    _SIPSTATUS_STATUSTYPE._serialized_start = 1009
    _SIPSTATUS_STATUSTYPE._serialized_end = 1570
    _SIPSTATUSHISTORYRESPONSE._serialized_start = 1572
    _SIPSTATUSHISTORYRESPONSE._serialized_end = 1645
    _SIPPLAYWAVFILESREQUEST._serialized_start = 1647
    _SIPPLAYWAVFILESREQUEST._serialized_end = 1690
    _SIP._serialized_start = 1693
    _SIP._serialized_end = 2514
# @@protoc_insertion_point(module_scope)
