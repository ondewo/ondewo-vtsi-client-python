# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/nlu/context.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ondewo/nlu/context.proto',
  package='ondewo.nlu',
  syntax='proto3',
  serialized_options=b'\n\036com.google.cloud.dialogflow.v2B\014ContextProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\370\001\001\242\002\002DF\252\002\032Google.Cloud.Dialogflow.V2',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18ondewo/nlu/context.proto\x12\nondewo.nlu\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"\xa9\x02\n\x07\x43ontext\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0elifespan_count\x18\x02 \x01(\x05\x12\x37\n\nparameters\x18\x03 \x03(\x0b\x32#.ondewo.nlu.Context.ParametersEntry\x12\x15\n\rlifespan_time\x18\x04 \x01(\x02\x1aV\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x16\n\x0evalue_original\x18\x04 \x01(\t\x1aP\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.ondewo.nlu.Context.Parameter:\x02\x38\x01\"9\n\x13ListContextsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\"V\n\x14ListContextsResponse\x12%\n\x08\x63ontexts\x18\x01 \x03(\x0b\x32\x13.ondewo.nlu.Context\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"!\n\x11GetContextRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"L\n\x14\x43reateContextRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12$\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x13.ondewo.nlu.Context\"m\n\x14UpdateContextRequest\x12$\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x13.ondewo.nlu.Context\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"$\n\x14\x44\x65leteContextRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"*\n\x18\x44\x65leteAllContextsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t2\xce\x06\n\x08\x43ontexts\x12\x8c\x01\n\x0cListContexts\x12\x1f.ondewo.nlu.ListContextsRequest\x1a .ondewo.nlu.ListContextsResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v2/{parent=projects/*/agent/sessions/*}/contexts\x12{\n\nGetContext\x12\x1d.ondewo.nlu.GetContextRequest\x1a\x13.ondewo.nlu.Context\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v2/{name=projects/*/agent/sessions/*/contexts/*}\x12\x8a\x01\n\rCreateContext\x12 .ondewo.nlu.CreateContextRequest\x1a\x13.ondewo.nlu.Context\"B\x82\xd3\xe4\x93\x02<\"1/v2/{parent=projects/*/agent/sessions/*}/contexts:\x07\x63ontext\x12\x92\x01\n\rUpdateContext\x12 .ondewo.nlu.UpdateContextRequest\x1a\x13.ondewo.nlu.Context\"J\x82\xd3\xe4\x93\x02\x44\x32\x39/v2/{context.name=projects/*/agent/sessions/*/contexts/*}:\x07\x63ontext\x12\x84\x01\n\rDeleteContext\x12 .ondewo.nlu.DeleteContextRequest\x1a\x16.google.protobuf.Empty\"9\x82\xd3\xe4\x93\x02\x33*1/v2/{name=projects/*/agent/sessions/*/contexts/*}\x12\x8c\x01\n\x11\x44\x65leteAllContexts\x12$.ondewo.nlu.DeleteAllContextsRequest\x1a\x16.google.protobuf.Empty\"9\x82\xd3\xe4\x93\x02\x33*1/v2/{parent=projects/*/agent/sessions/*}/contextsB\x9b\x01\n\x1e\x63om.google.cloud.dialogflow.v2B\x0c\x43ontextProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_CONTEXT_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='ondewo.nlu.Context.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ondewo.nlu.Context.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='ondewo.nlu.Context.Parameter.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ondewo.nlu.Context.Parameter.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value_original', full_name='ondewo.nlu.Context.Parameter.value_original', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=263,
  serialized_end=349,
)

_CONTEXT_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='ondewo.nlu.Context.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ondewo.nlu.Context.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ondewo.nlu.Context.ParametersEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=431,
)

_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='ondewo.nlu.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ondewo.nlu.Context.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lifespan_count', full_name='ondewo.nlu.Context.lifespan_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='ondewo.nlu.Context.parameters', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lifespan_time', full_name='ondewo.nlu.Context.lifespan_time', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONTEXT_PARAMETER, _CONTEXT_PARAMETERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=431,
)


_LISTCONTEXTSREQUEST = _descriptor.Descriptor(
  name='ListContextsRequest',
  full_name='ondewo.nlu.ListContextsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='ondewo.nlu.ListContextsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ondewo.nlu.ListContextsRequest.page_token', index=1,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=433,
  serialized_end=490,
)


_LISTCONTEXTSRESPONSE = _descriptor.Descriptor(
  name='ListContextsResponse',
  full_name='ondewo.nlu.ListContextsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contexts', full_name='ondewo.nlu.ListContextsResponse.contexts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ondewo.nlu.ListContextsResponse.next_page_token', index=1,
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
  serialized_start=492,
  serialized_end=578,
)


_GETCONTEXTREQUEST = _descriptor.Descriptor(
  name='GetContextRequest',
  full_name='ondewo.nlu.GetContextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ondewo.nlu.GetContextRequest.name', index=0,
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
  serialized_start=580,
  serialized_end=613,
)


_CREATECONTEXTREQUEST = _descriptor.Descriptor(
  name='CreateContextRequest',
  full_name='ondewo.nlu.CreateContextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='ondewo.nlu.CreateContextRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='context', full_name='ondewo.nlu.CreateContextRequest.context', index=1,
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
  serialized_start=615,
  serialized_end=691,
)


_UPDATECONTEXTREQUEST = _descriptor.Descriptor(
  name='UpdateContextRequest',
  full_name='ondewo.nlu.UpdateContextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='ondewo.nlu.UpdateContextRequest.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='ondewo.nlu.UpdateContextRequest.update_mask', index=1,
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
  serialized_start=693,
  serialized_end=802,
)


_DELETECONTEXTREQUEST = _descriptor.Descriptor(
  name='DeleteContextRequest',
  full_name='ondewo.nlu.DeleteContextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ondewo.nlu.DeleteContextRequest.name', index=0,
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
  serialized_start=804,
  serialized_end=840,
)


_DELETEALLCONTEXTSREQUEST = _descriptor.Descriptor(
  name='DeleteAllContextsRequest',
  full_name='ondewo.nlu.DeleteAllContextsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='ondewo.nlu.DeleteAllContextsRequest.parent', index=0,
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
  serialized_start=842,
  serialized_end=884,
)

_CONTEXT_PARAMETER.containing_type = _CONTEXT
_CONTEXT_PARAMETERSENTRY.fields_by_name['value'].message_type = _CONTEXT_PARAMETER
_CONTEXT_PARAMETERSENTRY.containing_type = _CONTEXT
_CONTEXT.fields_by_name['parameters'].message_type = _CONTEXT_PARAMETERSENTRY
_LISTCONTEXTSRESPONSE.fields_by_name['contexts'].message_type = _CONTEXT
_CREATECONTEXTREQUEST.fields_by_name['context'].message_type = _CONTEXT
_UPDATECONTEXTREQUEST.fields_by_name['context'].message_type = _CONTEXT
_UPDATECONTEXTREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
DESCRIPTOR.message_types_by_name['ListContextsRequest'] = _LISTCONTEXTSREQUEST
DESCRIPTOR.message_types_by_name['ListContextsResponse'] = _LISTCONTEXTSRESPONSE
DESCRIPTOR.message_types_by_name['GetContextRequest'] = _GETCONTEXTREQUEST
DESCRIPTOR.message_types_by_name['CreateContextRequest'] = _CREATECONTEXTREQUEST
DESCRIPTOR.message_types_by_name['UpdateContextRequest'] = _UPDATECONTEXTREQUEST
DESCRIPTOR.message_types_by_name['DeleteContextRequest'] = _DELETECONTEXTREQUEST
DESCRIPTOR.message_types_by_name['DeleteAllContextsRequest'] = _DELETEALLCONTEXTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), {

  'Parameter' : _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), {
    'DESCRIPTOR' : _CONTEXT_PARAMETER,
    '__module__' : 'ondewo.nlu.context_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.Context.Parameter)
    })
  ,

  'ParametersEntry' : _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONTEXT_PARAMETERSENTRY,
    '__module__' : 'ondewo.nlu.context_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.Context.ParametersEntry)
    })
  ,
  'DESCRIPTOR' : _CONTEXT,
  '__module__' : 'ondewo.nlu.context_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.Context)
  })
_sym_db.RegisterMessage(Context)
_sym_db.RegisterMessage(Context.Parameter)
_sym_db.RegisterMessage(Context.ParametersEntry)

ListContextsRequest = _reflection.GeneratedProtocolMessageType('ListContextsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONTEXTSREQUEST,
  '__module__' : 'ondewo.nlu.context_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.ListContextsRequest)
  })
_sym_db.RegisterMessage(ListContextsRequest)

ListContextsResponse = _reflection.GeneratedProtocolMessageType('ListContextsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONTEXTSRESPONSE,
  '__module__' : 'ondewo.nlu.context_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.ListContextsResponse)
  })
_sym_db.RegisterMessage(ListContextsResponse)

GetContextRequest = _reflection.GeneratedProtocolMessageType('GetContextRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONTEXTREQUEST,
  '__module__' : 'ondewo.nlu.context_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.GetContextRequest)
  })
_sym_db.RegisterMessage(GetContextRequest)

CreateContextRequest = _reflection.GeneratedProtocolMessageType('CreateContextRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONTEXTREQUEST,
  '__module__' : 'ondewo.nlu.context_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.CreateContextRequest)
  })
_sym_db.RegisterMessage(CreateContextRequest)

UpdateContextRequest = _reflection.GeneratedProtocolMessageType('UpdateContextRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONTEXTREQUEST,
  '__module__' : 'ondewo.nlu.context_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.UpdateContextRequest)
  })
_sym_db.RegisterMessage(UpdateContextRequest)

DeleteContextRequest = _reflection.GeneratedProtocolMessageType('DeleteContextRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECONTEXTREQUEST,
  '__module__' : 'ondewo.nlu.context_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.DeleteContextRequest)
  })
_sym_db.RegisterMessage(DeleteContextRequest)

DeleteAllContextsRequest = _reflection.GeneratedProtocolMessageType('DeleteAllContextsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALLCONTEXTSREQUEST,
  '__module__' : 'ondewo.nlu.context_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.DeleteAllContextsRequest)
  })
_sym_db.RegisterMessage(DeleteAllContextsRequest)


DESCRIPTOR._options = None
_CONTEXT_PARAMETERSENTRY._options = None

_CONTEXTS = _descriptor.ServiceDescriptor(
  name='Contexts',
  full_name='ondewo.nlu.Contexts',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=887,
  serialized_end=1733,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListContexts',
    full_name='ondewo.nlu.Contexts.ListContexts',
    index=0,
    containing_service=None,
    input_type=_LISTCONTEXTSREQUEST,
    output_type=_LISTCONTEXTSRESPONSE,
    serialized_options=b'\202\323\344\223\0023\0221/v2/{parent=projects/*/agent/sessions/*}/contexts',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetContext',
    full_name='ondewo.nlu.Contexts.GetContext',
    index=1,
    containing_service=None,
    input_type=_GETCONTEXTREQUEST,
    output_type=_CONTEXT,
    serialized_options=b'\202\323\344\223\0023\0221/v2/{name=projects/*/agent/sessions/*/contexts/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateContext',
    full_name='ondewo.nlu.Contexts.CreateContext',
    index=2,
    containing_service=None,
    input_type=_CREATECONTEXTREQUEST,
    output_type=_CONTEXT,
    serialized_options=b'\202\323\344\223\002<\"1/v2/{parent=projects/*/agent/sessions/*}/contexts:\007context',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateContext',
    full_name='ondewo.nlu.Contexts.UpdateContext',
    index=3,
    containing_service=None,
    input_type=_UPDATECONTEXTREQUEST,
    output_type=_CONTEXT,
    serialized_options=b'\202\323\344\223\002D29/v2/{context.name=projects/*/agent/sessions/*/contexts/*}:\007context',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteContext',
    full_name='ondewo.nlu.Contexts.DeleteContext',
    index=4,
    containing_service=None,
    input_type=_DELETECONTEXTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\0023*1/v2/{name=projects/*/agent/sessions/*/contexts/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteAllContexts',
    full_name='ondewo.nlu.Contexts.DeleteAllContexts',
    index=5,
    containing_service=None,
    input_type=_DELETEALLCONTEXTSREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\0023*1/v2/{parent=projects/*/agent/sessions/*}/contexts',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTEXTS)

DESCRIPTOR.services_by_name['Contexts'] = _CONTEXTS

# @@protoc_insertion_point(module_scope)