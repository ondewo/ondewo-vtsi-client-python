# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/nlu/project_statistics.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ondewo.nlu import intent_pb2 as ondewo_dot_nlu_dot_intent__pb2
from ondewo.nlu import common_pb2 as ondewo_dot_nlu_dot_common__pb2
from ondewo.nlu import entity_type_pb2 as ondewo_dot_nlu_dot_entity__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ondewo/nlu/project_statistics.proto',
  package='ondewo.nlu',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#ondewo/nlu/project_statistics.proto\x12\nondewo.nlu\x1a\x1cgoogle/api/annotations.proto\x1a\x17ondewo/nlu/intent.proto\x1a\x17ondewo/nlu/common.proto\x1a\x1condewo/nlu/entity_type.proto\"_\n\x15GetIntentCountRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x36\n\x12\x66ilter_by_category\x18\x02 \x01(\x0e\x32\x1a.ondewo.nlu.IntentCategory\"g\n\x19GetEntityTypeCountRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12:\n\x12\x66ilter_by_category\x18\x02 \x01(\x0e\x32\x1e.ondewo.nlu.EntityTypeCategory\"\'\n\x15GetProjectStatRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\"C\n\x1cGetProjectElementStatRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t2\xa6\t\n\x11ProjectStatistics\x12\x7f\n\x0eGetIntentCount\x12!.ondewo.nlu.GetIntentCountRequest\x1a\x18.ondewo.nlu.StatResponse\"0\x82\xd3\xe4\x93\x02*\x12(/{parent=projects/*/agent}/intents:count\x12\x8b\x01\n\x12GetEntityTypeCount\x12%.ondewo.nlu.GetEntityTypeCountRequest\x1a\x18.ondewo.nlu.StatResponse\"4\x82\xd3\xe4\x93\x02.\x12,/{parent=projects/*/agent}/entityTypes:count\x12{\n\x0cGetUserCount\x12!.ondewo.nlu.GetProjectStatRequest\x1a\x18.ondewo.nlu.StatResponse\".\x82\xd3\xe4\x93\x02(\x12&/{parent=projects/*/agent}/users:count\x12\x81\x01\n\x0fGetSessionCount\x12!.ondewo.nlu.GetProjectStatRequest\x1a\x18.ondewo.nlu.StatResponse\"1\x82\xd3\xe4\x93\x02+\x12)/{parent=projects/*/agent}/sessions:count\x12\x9e\x01\n\x16GetTrainingPhraseCount\x12(.ondewo.nlu.GetProjectElementStatRequest\x1a\x18.ondewo.nlu.StatResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/{name=projects/*/agent/intents/*}/trainingPhrases:count\x12\x92\x01\n\x10GetResponseCount\x12(.ondewo.nlu.GetProjectElementStatRequest\x1a\x18.ondewo.nlu.StatResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/{name=projects/*/agent/intents/*}/responses:count\x12\x98\x01\n\x13GetEntityValueCount\x12(.ondewo.nlu.GetProjectElementStatRequest\x1a\x18.ondewo.nlu.StatResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/{name=projects/*/agent/entityTypes/*}/entities:count\x12\xaf\x01\n\x15GetEntitySynonymCount\x12(.ondewo.nlu.GetProjectElementStatRequest\x1a\x18.ondewo.nlu.StatResponse\"R\x82\xd3\xe4\x93\x02L\x12J/{name=projects/*/agent/entityTypes/*/entityValues/*}/entitySynonyms:countb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,ondewo_dot_nlu_dot_intent__pb2.DESCRIPTOR,ondewo_dot_nlu_dot_common__pb2.DESCRIPTOR,ondewo_dot_nlu_dot_entity__type__pb2.DESCRIPTOR,])




_GETINTENTCOUNTREQUEST = _descriptor.Descriptor(
  name='GetIntentCountRequest',
  full_name='ondewo.nlu.GetIntentCountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='ondewo.nlu.GetIntentCountRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter_by_category', full_name='ondewo.nlu.GetIntentCountRequest.filter_by_category', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=256,
)


_GETENTITYTYPECOUNTREQUEST = _descriptor.Descriptor(
  name='GetEntityTypeCountRequest',
  full_name='ondewo.nlu.GetEntityTypeCountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='ondewo.nlu.GetEntityTypeCountRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter_by_category', full_name='ondewo.nlu.GetEntityTypeCountRequest.filter_by_category', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=361,
)


_GETPROJECTSTATREQUEST = _descriptor.Descriptor(
  name='GetProjectStatRequest',
  full_name='ondewo.nlu.GetProjectStatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='ondewo.nlu.GetProjectStatRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=363,
  serialized_end=402,
)


_GETPROJECTELEMENTSTATREQUEST = _descriptor.Descriptor(
  name='GetProjectElementStatRequest',
  full_name='ondewo.nlu.GetProjectElementStatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ondewo.nlu.GetProjectElementStatRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='ondewo.nlu.GetProjectElementStatRequest.language_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=404,
  serialized_end=471,
)

_GETINTENTCOUNTREQUEST.fields_by_name['filter_by_category'].enum_type = ondewo_dot_nlu_dot_intent__pb2._INTENTCATEGORY
_GETENTITYTYPECOUNTREQUEST.fields_by_name['filter_by_category'].enum_type = ondewo_dot_nlu_dot_entity__type__pb2._ENTITYTYPECATEGORY
DESCRIPTOR.message_types_by_name['GetIntentCountRequest'] = _GETINTENTCOUNTREQUEST
DESCRIPTOR.message_types_by_name['GetEntityTypeCountRequest'] = _GETENTITYTYPECOUNTREQUEST
DESCRIPTOR.message_types_by_name['GetProjectStatRequest'] = _GETPROJECTSTATREQUEST
DESCRIPTOR.message_types_by_name['GetProjectElementStatRequest'] = _GETPROJECTELEMENTSTATREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetIntentCountRequest = _reflection.GeneratedProtocolMessageType('GetIntentCountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINTENTCOUNTREQUEST,
  '__module__' : 'ondewo.nlu.project_statistics_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.GetIntentCountRequest)
  })
_sym_db.RegisterMessage(GetIntentCountRequest)

GetEntityTypeCountRequest = _reflection.GeneratedProtocolMessageType('GetEntityTypeCountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETENTITYTYPECOUNTREQUEST,
  '__module__' : 'ondewo.nlu.project_statistics_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.GetEntityTypeCountRequest)
  })
_sym_db.RegisterMessage(GetEntityTypeCountRequest)

GetProjectStatRequest = _reflection.GeneratedProtocolMessageType('GetProjectStatRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTSTATREQUEST,
  '__module__' : 'ondewo.nlu.project_statistics_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.GetProjectStatRequest)
  })
_sym_db.RegisterMessage(GetProjectStatRequest)

GetProjectElementStatRequest = _reflection.GeneratedProtocolMessageType('GetProjectElementStatRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTELEMENTSTATREQUEST,
  '__module__' : 'ondewo.nlu.project_statistics_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.GetProjectElementStatRequest)
  })
_sym_db.RegisterMessage(GetProjectElementStatRequest)



_PROJECTSTATISTICS = _descriptor.ServiceDescriptor(
  name='ProjectStatistics',
  full_name='ondewo.nlu.ProjectStatistics',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=474,
  serialized_end=1664,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetIntentCount',
    full_name='ondewo.nlu.ProjectStatistics.GetIntentCount',
    index=0,
    containing_service=None,
    input_type=_GETINTENTCOUNTREQUEST,
    output_type=ondewo_dot_nlu_dot_common__pb2._STATRESPONSE,
    serialized_options=b'\202\323\344\223\002*\022(/{parent=projects/*/agent}/intents:count',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetEntityTypeCount',
    full_name='ondewo.nlu.ProjectStatistics.GetEntityTypeCount',
    index=1,
    containing_service=None,
    input_type=_GETENTITYTYPECOUNTREQUEST,
    output_type=ondewo_dot_nlu_dot_common__pb2._STATRESPONSE,
    serialized_options=b'\202\323\344\223\002.\022,/{parent=projects/*/agent}/entityTypes:count',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserCount',
    full_name='ondewo.nlu.ProjectStatistics.GetUserCount',
    index=2,
    containing_service=None,
    input_type=_GETPROJECTSTATREQUEST,
    output_type=ondewo_dot_nlu_dot_common__pb2._STATRESPONSE,
    serialized_options=b'\202\323\344\223\002(\022&/{parent=projects/*/agent}/users:count',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSessionCount',
    full_name='ondewo.nlu.ProjectStatistics.GetSessionCount',
    index=3,
    containing_service=None,
    input_type=_GETPROJECTSTATREQUEST,
    output_type=ondewo_dot_nlu_dot_common__pb2._STATRESPONSE,
    serialized_options=b'\202\323\344\223\002+\022)/{parent=projects/*/agent}/sessions:count',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTrainingPhraseCount',
    full_name='ondewo.nlu.ProjectStatistics.GetTrainingPhraseCount',
    index=4,
    containing_service=None,
    input_type=_GETPROJECTELEMENTSTATREQUEST,
    output_type=ondewo_dot_nlu_dot_common__pb2._STATRESPONSE,
    serialized_options=b'\202\323\344\223\002:\0228/{name=projects/*/agent/intents/*}/trainingPhrases:count',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetResponseCount',
    full_name='ondewo.nlu.ProjectStatistics.GetResponseCount',
    index=5,
    containing_service=None,
    input_type=_GETPROJECTELEMENTSTATREQUEST,
    output_type=ondewo_dot_nlu_dot_common__pb2._STATRESPONSE,
    serialized_options=b'\202\323\344\223\0024\0222/{name=projects/*/agent/intents/*}/responses:count',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetEntityValueCount',
    full_name='ondewo.nlu.ProjectStatistics.GetEntityValueCount',
    index=6,
    containing_service=None,
    input_type=_GETPROJECTELEMENTSTATREQUEST,
    output_type=ondewo_dot_nlu_dot_common__pb2._STATRESPONSE,
    serialized_options=b'\202\323\344\223\0027\0225/{name=projects/*/agent/entityTypes/*}/entities:count',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetEntitySynonymCount',
    full_name='ondewo.nlu.ProjectStatistics.GetEntitySynonymCount',
    index=7,
    containing_service=None,
    input_type=_GETPROJECTELEMENTSTATREQUEST,
    output_type=ondewo_dot_nlu_dot_common__pb2._STATRESPONSE,
    serialized_options=b'\202\323\344\223\002L\022J/{name=projects/*/agent/entityTypes/*/entityValues/*}/entitySynonyms:count',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROJECTSTATISTICS)

DESCRIPTOR.services_by_name['ProjectStatistics'] = _PROJECTSTATISTICS

# @@protoc_insertion_point(module_scope)
