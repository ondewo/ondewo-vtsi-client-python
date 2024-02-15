# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/nlu/project_statistics.proto
"""Generated protocol buffer code."""
from ondewo.nlu import entity_type_pb2 as ondewo_dot_nlu_dot_entity__type__pb2
from ondewo.nlu import common_pb2 as ondewo_dot_nlu_dot_common__pb2
from ondewo.nlu import intent_pb2 as ondewo_dot_nlu_dot_intent__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#ondewo/nlu/project_statistics.proto\x12\nondewo.nlu\x1a\x1cgoogle/api/annotations.proto\x1a\x17ondewo/nlu/intent.proto\x1a\x17ondewo/nlu/common.proto\x1a\x1condewo/nlu/entity_type.proto\"_\n\x15GetIntentCountRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x36\n\x12\x66ilter_by_category\x18\x02 \x01(\x0e\x32\x1a.ondewo.nlu.IntentCategory\"g\n\x19GetEntityTypeCountRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12:\n\x12\x66ilter_by_category\x18\x02 \x01(\x0e\x32\x1e.ondewo.nlu.EntityTypeCategory\"\'\n\x15GetProjectStatRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\"C\n\x1cGetProjectElementStatRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t2\xa6\t\n\x11ProjectStatistics\x12\x7f\n\x0eGetIntentCount\x12!.ondewo.nlu.GetIntentCountRequest\x1a\x18.ondewo.nlu.StatResponse\"0\x82\xd3\xe4\x93\x02*\x12(/{parent=projects/*/agent}/intents:count\x12\x8b\x01\n\x12GetEntityTypeCount\x12%.ondewo.nlu.GetEntityTypeCountRequest\x1a\x18.ondewo.nlu.StatResponse\"4\x82\xd3\xe4\x93\x02.\x12,/{parent=projects/*/agent}/entityTypes:count\x12{\n\x0cGetUserCount\x12!.ondewo.nlu.GetProjectStatRequest\x1a\x18.ondewo.nlu.StatResponse\".\x82\xd3\xe4\x93\x02(\x12&/{parent=projects/*/agent}/users:count\x12\x81\x01\n\x0fGetSessionCount\x12!.ondewo.nlu.GetProjectStatRequest\x1a\x18.ondewo.nlu.StatResponse\"1\x82\xd3\xe4\x93\x02+\x12)/{parent=projects/*/agent}/sessions:count\x12\x9e\x01\n\x16GetTrainingPhraseCount\x12(.ondewo.nlu.GetProjectElementStatRequest\x1a\x18.ondewo.nlu.StatResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/{name=projects/*/agent/intents/*}/trainingPhrases:count\x12\x92\x01\n\x10GetResponseCount\x12(.ondewo.nlu.GetProjectElementStatRequest\x1a\x18.ondewo.nlu.StatResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/{name=projects/*/agent/intents/*}/responses:count\x12\x98\x01\n\x13GetEntityValueCount\x12(.ondewo.nlu.GetProjectElementStatRequest\x1a\x18.ondewo.nlu.StatResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/{name=projects/*/agent/entityTypes/*}/entities:count\x12\xaf\x01\n\x15GetEntitySynonymCount\x12(.ondewo.nlu.GetProjectElementStatRequest\x1a\x18.ondewo.nlu.StatResponse\"R\x82\xd3\xe4\x93\x02L\x12J/{name=projects/*/agent/entityTypes/*/entityValues/*}/entitySynonyms:countb\x06proto3')


_GETINTENTCOUNTREQUEST = DESCRIPTOR.message_types_by_name['GetIntentCountRequest']
_GETENTITYTYPECOUNTREQUEST = DESCRIPTOR.message_types_by_name['GetEntityTypeCountRequest']
_GETPROJECTSTATREQUEST = DESCRIPTOR.message_types_by_name['GetProjectStatRequest']
_GETPROJECTELEMENTSTATREQUEST = DESCRIPTOR.message_types_by_name['GetProjectElementStatRequest']
GetIntentCountRequest = _reflection.GeneratedProtocolMessageType('GetIntentCountRequest', (_message.Message,), {
    'DESCRIPTOR': _GETINTENTCOUNTREQUEST,
    '__module__': 'ondewo.nlu.project_statistics_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.GetIntentCountRequest)
})
_sym_db.RegisterMessage(GetIntentCountRequest)

GetEntityTypeCountRequest = _reflection.GeneratedProtocolMessageType('GetEntityTypeCountRequest', (_message.Message,), {
    'DESCRIPTOR': _GETENTITYTYPECOUNTREQUEST,
    '__module__': 'ondewo.nlu.project_statistics_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.GetEntityTypeCountRequest)
})
_sym_db.RegisterMessage(GetEntityTypeCountRequest)

GetProjectStatRequest = _reflection.GeneratedProtocolMessageType('GetProjectStatRequest', (_message.Message,), {
    'DESCRIPTOR': _GETPROJECTSTATREQUEST,
    '__module__': 'ondewo.nlu.project_statistics_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.GetProjectStatRequest)
})
_sym_db.RegisterMessage(GetProjectStatRequest)

GetProjectElementStatRequest = _reflection.GeneratedProtocolMessageType('GetProjectElementStatRequest', (_message.Message,), {
    'DESCRIPTOR': _GETPROJECTELEMENTSTATREQUEST,
    '__module__': 'ondewo.nlu.project_statistics_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.GetProjectElementStatRequest)
})
_sym_db.RegisterMessage(GetProjectElementStatRequest)

_PROJECTSTATISTICS = DESCRIPTOR.services_by_name['ProjectStatistics']
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _PROJECTSTATISTICS.methods_by_name['GetIntentCount']._options = None
    _PROJECTSTATISTICS.methods_by_name['GetIntentCount']._serialized_options = b'\202\323\344\223\002*\022(/{parent=projects/*/agent}/intents:count'
    _PROJECTSTATISTICS.methods_by_name['GetEntityTypeCount']._options = None
    _PROJECTSTATISTICS.methods_by_name['GetEntityTypeCount']._serialized_options = b'\202\323\344\223\002.\022,/{parent=projects/*/agent}/entityTypes:count'
    _PROJECTSTATISTICS.methods_by_name['GetUserCount']._options = None
    _PROJECTSTATISTICS.methods_by_name['GetUserCount']._serialized_options = b'\202\323\344\223\002(\022&/{parent=projects/*/agent}/users:count'
    _PROJECTSTATISTICS.methods_by_name['GetSessionCount']._options = None
    _PROJECTSTATISTICS.methods_by_name['GetSessionCount']._serialized_options = b'\202\323\344\223\002+\022)/{parent=projects/*/agent}/sessions:count'
    _PROJECTSTATISTICS.methods_by_name['GetTrainingPhraseCount']._options = None
    _PROJECTSTATISTICS.methods_by_name['GetTrainingPhraseCount']._serialized_options = b'\202\323\344\223\002:\0228/{name=projects/*/agent/intents/*}/trainingPhrases:count'
    _PROJECTSTATISTICS.methods_by_name['GetResponseCount']._options = None
    _PROJECTSTATISTICS.methods_by_name['GetResponseCount']._serialized_options = b'\202\323\344\223\0024\0222/{name=projects/*/agent/intents/*}/responses:count'
    _PROJECTSTATISTICS.methods_by_name['GetEntityValueCount']._options = None
    _PROJECTSTATISTICS.methods_by_name['GetEntityValueCount']._serialized_options = b'\202\323\344\223\0027\0225/{name=projects/*/agent/entityTypes/*}/entities:count'
    _PROJECTSTATISTICS.methods_by_name['GetEntitySynonymCount']._options = None
    _PROJECTSTATISTICS.methods_by_name['GetEntitySynonymCount']._serialized_options = b'\202\323\344\223\002L\022J/{name=projects/*/agent/entityTypes/*/entityValues/*}/entitySynonyms:count'
    _GETINTENTCOUNTREQUEST._serialized_start=161
    _GETINTENTCOUNTREQUEST._serialized_end=256
    _GETENTITYTYPECOUNTREQUEST._serialized_start=258
    _GETENTITYTYPECOUNTREQUEST._serialized_end=361
    _GETPROJECTSTATREQUEST._serialized_start=363
    _GETPROJECTSTATREQUEST._serialized_end=402
    _GETPROJECTELEMENTSTATREQUEST._serialized_start=404
    _GETPROJECTELEMENTSTATREQUEST._serialized_end=471
    _PROJECTSTATISTICS._serialized_start=474
    _PROJECTSTATISTICS._serialized_end=1664
# @@protoc_insertion_point(module_scope)
