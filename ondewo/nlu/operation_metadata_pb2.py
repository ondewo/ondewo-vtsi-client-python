# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/nlu/operation_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#ondewo/nlu/operation_metadata.proto\x12\nondewo.nlu\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8e\x07\n\x11OperationMetadata\x12\x34\n\x06status\x18\x01 \x01(\x0e\x32$.ondewo.nlu.OperationMetadata.Status\x12\x1d\n\x15parent_operation_name\x18\x02 \x01(\t\x12\x1b\n\x13sub_operation_names\x18\x03 \x03(\t\x12/\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12!\n\x19is_cancellation_requested\x18\x07 \x01(\x08\x12\x16\n\x0e\x63\x61ncel_command\x18\x08 \x01(\t\x12\x17\n\x0fuser_id_created\x18\t \x01(\t\x12\x19\n\x11user_id_cancelled\x18\n \x01(\t\x12\x16\n\x0eproject_parent\x18\x0b \x01(\t\x12\x43\n\x0eoperation_type\x18\x0c \x01(\x0e\x32+.ondewo.nlu.OperationMetadata.OperationType\x12\x11\n\thost_name\x18\r \x01(\t\x12\x12\n\nnum_reruns\x18\x0e \x01(\x05\x12\x16\n\x0emax_num_reruns\x18\x0f \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x10 \x01(\t\x12\x0b\n\x03log\x18\x11 \x03(\t\x12\x11\n\tlog_limit\x18\x12 \x01(\x05\"g\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNOT_STARTED\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\x08\n\x04\x44ONE\x10\x03\x12\r\n\tCANCELLED\x10\x04\x12\n\n\x06\x46\x41ILED\x10\x05\"\xce\x01\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0c\x43REATE_AGENT\x10\x01\x12\x10\n\x0cIMPORT_AGENT\x10\x02\x12\x10\n\x0c\x45XPORT_AGENT\x10\x03\x12\x10\n\x0c\x44\x45LETE_AGENT\x10\x04\x12\x11\n\rRESTORE_AGENT\x10\x05\x12\x15\n\x11\x42UILD_AGENT_CACHE\x10\x06\x12\x0f\n\x0bTRAIN_AGENT\x10\x07\x12\x1a\n\x16\x45XPORT_BENCHMARK_AGENT\x10\x08\x62\x06proto3')


_OPERATIONMETADATA = DESCRIPTOR.message_types_by_name['OperationMetadata']
_OPERATIONMETADATA_STATUS = _OPERATIONMETADATA.enum_types_by_name['Status']
_OPERATIONMETADATA_OPERATIONTYPE = _OPERATIONMETADATA.enum_types_by_name['OperationType']
OperationMetadata = _reflection.GeneratedProtocolMessageType('OperationMetadata', (_message.Message,), {
    'DESCRIPTOR': _OPERATIONMETADATA,
    '__module__': 'ondewo.nlu.operation_metadata_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.OperationMetadata)
})
_sym_db.RegisterMessage(OperationMetadata)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _OPERATIONMETADATA._serialized_start=85
    _OPERATIONMETADATA._serialized_end=995
    _OPERATIONMETADATA_STATUS._serialized_start=683
    _OPERATIONMETADATA_STATUS._serialized_end=786
    _OPERATIONMETADATA_OPERATIONTYPE._serialized_start=789
    _OPERATIONMETADATA_OPERATIONTYPE._serialized_end=995
# @@protoc_insertion_point(module_scope)
