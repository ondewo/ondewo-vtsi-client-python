# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ondewo/nlu/context.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'ondewo/nlu/context.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18ondewo/nlu/context.proto\x12\nondewo.nlu\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbe\x04\n\x07\x43ontext\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0elifespan_count\x18\x02 \x01(\x05\x12\x37\n\nparameters\x18\x03 \x03(\x0b\x32#.ondewo.nlu.Context.ParametersEntry\x12\x15\n\rlifespan_time\x18\x04 \x01(\x02\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bmodified_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x07 \x01(\t\x12\x13\n\x0bmodified_by\x18\x08 \x01(\t\x1a\xe0\x01\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x16\n\x0evalue_original\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bmodified_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x07 \x01(\t\x12\x13\n\x0bmodified_by\x18\x08 \x01(\t\x1aP\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.ondewo.nlu.Context.Parameter:\x02\x38\x01\"=\n\x13ListContextsRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\"V\n\x14ListContextsResponse\x12%\n\x08\x63ontexts\x18\x01 \x03(\x0b\x32\x13.ondewo.nlu.Context\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"!\n\x11GetContextRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"P\n\x14\x43reateContextRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12$\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x13.ondewo.nlu.Context\"m\n\x14UpdateContextRequest\x12$\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x13.ondewo.nlu.Context\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"$\n\x14\x44\x65leteContextRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\".\n\x18\x44\x65leteAllContextsRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t2\xce\x06\n\x08\x43ontexts\x12\x8c\x01\n\x0cListContexts\x12\x1f.ondewo.nlu.ListContextsRequest\x1a .ondewo.nlu.ListContextsResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v2/{parent=projects/*/agent/sessions/*}/contexts\x12{\n\nGetContext\x12\x1d.ondewo.nlu.GetContextRequest\x1a\x13.ondewo.nlu.Context\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v2/{name=projects/*/agent/sessions/*/contexts/*}\x12\x8a\x01\n\rCreateContext\x12 .ondewo.nlu.CreateContextRequest\x1a\x13.ondewo.nlu.Context\"B\x82\xd3\xe4\x93\x02<\"1/v2/{parent=projects/*/agent/sessions/*}/contexts:\x07\x63ontext\x12\x92\x01\n\rUpdateContext\x12 .ondewo.nlu.UpdateContextRequest\x1a\x13.ondewo.nlu.Context\"J\x82\xd3\xe4\x93\x02\x44\x32\x39/v2/{context.name=projects/*/agent/sessions/*/contexts/*}:\x07\x63ontext\x12\x84\x01\n\rDeleteContext\x12 .ondewo.nlu.DeleteContextRequest\x1a\x16.google.protobuf.Empty\"9\x82\xd3\xe4\x93\x02\x33*1/v2/{name=projects/*/agent/sessions/*/contexts/*}\x12\x8c\x01\n\x11\x44\x65leteAllContexts\x12$.ondewo.nlu.DeleteAllContextsRequest\x1a\x16.google.protobuf.Empty\"9\x82\xd3\xe4\x93\x02\x33*1/v2/{parent=projects/*/agent/sessions/*}/contextsB\x9b\x01\n\x1e\x63om.google.cloud.dialogflow.v2B\x0c\x43ontextProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ondewo.nlu.context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\036com.google.cloud.dialogflow.v2B\014ContextProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\370\001\001\242\002\002DF\252\002\032Google.Cloud.Dialogflow.V2'
    _globals['_CONTEXT_PARAMETERSENTRY']._loaded_options = None
    _globals['_CONTEXT_PARAMETERSENTRY']._serialized_options = b'8\001'
    _globals['_CONTEXTS'].methods_by_name['ListContexts']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name[
        'ListContexts']._serialized_options = b'\202\323\344\223\0023\0221/v2/{parent=projects/*/agent/sessions/*}/contexts'
    _globals['_CONTEXTS'].methods_by_name['GetContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name[
        'GetContext']._serialized_options = b'\202\323\344\223\0023\0221/v2/{name=projects/*/agent/sessions/*/contexts/*}'
    _globals['_CONTEXTS'].methods_by_name['CreateContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name[
        'CreateContext']._serialized_options = b'\202\323\344\223\002<\"1/v2/{parent=projects/*/agent/sessions/*}/contexts:\007context'
    _globals['_CONTEXTS'].methods_by_name['UpdateContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name[
        'UpdateContext']._serialized_options = b'\202\323\344\223\002D29/v2/{context.name=projects/*/agent/sessions/*/contexts/*}:\007context'
    _globals['_CONTEXTS'].methods_by_name['DeleteContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name[
        'DeleteContext']._serialized_options = b'\202\323\344\223\0023*1/v2/{name=projects/*/agent/sessions/*/contexts/*}'
    _globals['_CONTEXTS'].methods_by_name['DeleteAllContexts']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name[
        'DeleteAllContexts']._serialized_options = b'\202\323\344\223\0023*1/v2/{parent=projects/*/agent/sessions/*}/contexts'
    _globals['_CONTEXT']._serialized_start = 167
    _globals['_CONTEXT']._serialized_end = 741
    _globals['_CONTEXT_PARAMETER']._serialized_start = 435
    _globals['_CONTEXT_PARAMETER']._serialized_end = 659
    _globals['_CONTEXT_PARAMETERSENTRY']._serialized_start = 661
    _globals['_CONTEXT_PARAMETERSENTRY']._serialized_end = 741
    _globals['_LISTCONTEXTSREQUEST']._serialized_start = 743
    _globals['_LISTCONTEXTSREQUEST']._serialized_end = 804
    _globals['_LISTCONTEXTSRESPONSE']._serialized_start = 806
    _globals['_LISTCONTEXTSRESPONSE']._serialized_end = 892
    _globals['_GETCONTEXTREQUEST']._serialized_start = 894
    _globals['_GETCONTEXTREQUEST']._serialized_end = 927
    _globals['_CREATECONTEXTREQUEST']._serialized_start = 929
    _globals['_CREATECONTEXTREQUEST']._serialized_end = 1009
    _globals['_UPDATECONTEXTREQUEST']._serialized_start = 1011
    _globals['_UPDATECONTEXTREQUEST']._serialized_end = 1120
    _globals['_DELETECONTEXTREQUEST']._serialized_start = 1122
    _globals['_DELETECONTEXTREQUEST']._serialized_end = 1158
    _globals['_DELETEALLCONTEXTSREQUEST']._serialized_start = 1160
    _globals['_DELETEALLCONTEXTSREQUEST']._serialized_end = 1206
    _globals['_CONTEXTS']._serialized_start = 1209
    _globals['_CONTEXTS']._serialized_end = 2055
# @@protoc_insertion_point(module_scope)
