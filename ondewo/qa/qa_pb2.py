# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/qa/qa.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ondewo.nlu import session_pb2 as ondewo_dot_nlu_dot_session__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ondewo/qa/qa.proto',
  package='ondewo.qa',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12ondewo/qa/qa.proto\x12\tondewo.qa\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x18ondewo/nlu/session.proto\"\xd1\x01\n\x10GetAnswerRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12#\n\x04text\x18\x02 \x01(\x0b\x32\x15.ondewo.nlu.TextInput\x12\x17\n\x0fmax_num_answers\x18\x03 \x01(\x05\x12\x18\n\x10threshold_reader\x18\x04 \x01(\x02\x12\x1b\n\x13threshold_retriever\x18\x05 \x01(\x02\x12\x19\n\x11threshold_overall\x18\x06 \x01(\x02\x12\x19\n\x11reader_model_name\x18\x07 \x01(\t\"K\n\x11GetAnswerResponse\x12\x36\n\x0cquery_result\x18\x02 \x01(\x0b\x32 .ondewo.nlu.DetectIntentResponse\"B\n\x12RunScraperResponse\x12\x16\n\x0e\x63ontainer_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontainer_id\x18\x02 \x01(\t\"3\n\x13RunTrainingResponse\x12\n\n\x02\x66\x31\x18\x01 \x01(\x02\x12\x10\n\x08\x61\x63\x63uracy\x18\x02 \x01(\x02\x32\x99\x02\n\x02QA\x12V\n\tGetAnswer\x12\x1b.ondewo.qa.GetAnswerRequest\x1a\x1c.ondewo.qa.GetAnswerResponse\"\x0e\x82\xd3\xe4\x93\x02\x08\"\x03/qa:\x01*\x12[\n\nRunScraper\x12\x16.google.protobuf.Empty\x1a\x1d.ondewo.qa.RunScraperResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/qa:RunScraper\x12^\n\x0bRunTraining\x12\x16.google.protobuf.Empty\x1a\x1e.ondewo.qa.RunTrainingResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/qa:RunTrainingb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,ondewo_dot_nlu_dot_session__pb2.DESCRIPTOR,])




_GETANSWERREQUEST = _descriptor.Descriptor(
  name='GetAnswerRequest',
  full_name='ondewo.qa.GetAnswerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='ondewo.qa.GetAnswerRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='ondewo.qa.GetAnswerRequest.text', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_num_answers', full_name='ondewo.qa.GetAnswerRequest.max_num_answers', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threshold_reader', full_name='ondewo.qa.GetAnswerRequest.threshold_reader', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threshold_retriever', full_name='ondewo.qa.GetAnswerRequest.threshold_retriever', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threshold_overall', full_name='ondewo.qa.GetAnswerRequest.threshold_overall', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reader_model_name', full_name='ondewo.qa.GetAnswerRequest.reader_model_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=119,
  serialized_end=328,
)


_GETANSWERRESPONSE = _descriptor.Descriptor(
  name='GetAnswerResponse',
  full_name='ondewo.qa.GetAnswerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_result', full_name='ondewo.qa.GetAnswerResponse.query_result', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=330,
  serialized_end=405,
)


_RUNSCRAPERRESPONSE = _descriptor.Descriptor(
  name='RunScraperResponse',
  full_name='ondewo.qa.RunScraperResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_name', full_name='ondewo.qa.RunScraperResponse.container_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='container_id', full_name='ondewo.qa.RunScraperResponse.container_id', index=1,
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
  serialized_start=407,
  serialized_end=473,
)


_RUNTRAININGRESPONSE = _descriptor.Descriptor(
  name='RunTrainingResponse',
  full_name='ondewo.qa.RunTrainingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='ondewo.qa.RunTrainingResponse.f1', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='ondewo.qa.RunTrainingResponse.accuracy', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=475,
  serialized_end=526,
)

_GETANSWERREQUEST.fields_by_name['text'].message_type = ondewo_dot_nlu_dot_session__pb2._TEXTINPUT
_GETANSWERRESPONSE.fields_by_name['query_result'].message_type = ondewo_dot_nlu_dot_session__pb2._DETECTINTENTRESPONSE
DESCRIPTOR.message_types_by_name['GetAnswerRequest'] = _GETANSWERREQUEST
DESCRIPTOR.message_types_by_name['GetAnswerResponse'] = _GETANSWERRESPONSE
DESCRIPTOR.message_types_by_name['RunScraperResponse'] = _RUNSCRAPERRESPONSE
DESCRIPTOR.message_types_by_name['RunTrainingResponse'] = _RUNTRAININGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAnswerRequest = _reflection.GeneratedProtocolMessageType('GetAnswerRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETANSWERREQUEST,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.GetAnswerRequest)
  })
_sym_db.RegisterMessage(GetAnswerRequest)

GetAnswerResponse = _reflection.GeneratedProtocolMessageType('GetAnswerResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETANSWERRESPONSE,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.GetAnswerResponse)
  })
_sym_db.RegisterMessage(GetAnswerResponse)

RunScraperResponse = _reflection.GeneratedProtocolMessageType('RunScraperResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNSCRAPERRESPONSE,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.RunScraperResponse)
  })
_sym_db.RegisterMessage(RunScraperResponse)

RunTrainingResponse = _reflection.GeneratedProtocolMessageType('RunTrainingResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNTRAININGRESPONSE,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.RunTrainingResponse)
  })
_sym_db.RegisterMessage(RunTrainingResponse)



_QA = _descriptor.ServiceDescriptor(
  name='QA',
  full_name='ondewo.qa.QA',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=529,
  serialized_end=810,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAnswer',
    full_name='ondewo.qa.QA.GetAnswer',
    index=0,
    containing_service=None,
    input_type=_GETANSWERREQUEST,
    output_type=_GETANSWERRESPONSE,
    serialized_options=b'\202\323\344\223\002\010\"\003/qa:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunScraper',
    full_name='ondewo.qa.QA.RunScraper',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_RUNSCRAPERRESPONSE,
    serialized_options=b'\202\323\344\223\002\020\022\016/qa:RunScraper',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunTraining',
    full_name='ondewo.qa.QA.RunTraining',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_RUNTRAININGRESPONSE,
    serialized_options=b'\202\323\344\223\002\021\022\017/qa:RunTraining',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QA)

DESCRIPTOR.services_by_name['QA'] = _QA

# @@protoc_insertion_point(module_scope)