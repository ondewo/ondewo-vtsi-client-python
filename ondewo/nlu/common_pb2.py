# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/nlu/common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17ondewo/nlu/common.proto\x12\nondewo.nlu\"\x1d\n\x0cStatResponse\x12\r\n\x05value\x18\x01 \x01(\r*,\n\x0bSortingMode\x12\r\n\tASCENDING\x10\x00\x12\x0e\n\nDESCENDING\x10\x01\x62\x06proto3')

_SORTINGMODE = DESCRIPTOR.enum_types_by_name['SortingMode']
SortingMode = enum_type_wrapper.EnumTypeWrapper(_SORTINGMODE)
ASCENDING = 0
DESCENDING = 1


_STATRESPONSE = DESCRIPTOR.message_types_by_name['StatResponse']
StatResponse = _reflection.GeneratedProtocolMessageType('StatResponse', (_message.Message,), {
    'DESCRIPTOR': _STATRESPONSE,
    '__module__': 'ondewo.nlu.common_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.StatResponse)
})
_sym_db.RegisterMessage(StatResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _SORTINGMODE._serialized_start = 70
    _SORTINGMODE._serialized_end = 114
    _STATRESPONSE._serialized_start = 39
    _STATRESPONSE._serialized_end = 68
# @@protoc_insertion_point(module_scope)
