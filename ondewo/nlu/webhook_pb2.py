# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/nlu/webhook.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ondewo.nlu import context_pb2 as ondewo_dot_nlu_dot_context__pb2
from ondewo.nlu import intent_pb2 as ondewo_dot_nlu_dot_intent__pb2
from ondewo.nlu import session_pb2 as ondewo_dot_nlu_dot_session__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ondewo/nlu/webhook.proto',
  package='ondewo.nlu',
  syntax='proto3',
  serialized_options=b'\n\036com.google.cloud.dialogflow.v2B\014WebhookProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\370\001\001\242\002\002DF\252\002\032Google.Cloud.Dialogflow.V2',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18ondewo/nlu/webhook.proto\x12\nondewo.nlu\x1a\x1cgoogle/api/annotations.proto\x1a\x18ondewo/nlu/context.proto\x1a\x17ondewo/nlu/intent.proto\x1a\x18ondewo/nlu/session.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x1e\n\x0bPingRequest\x12\x0f\n\x07session\x18\x01 \x01(\t\"\xe0\x01\n\x0eWebhookRequest\x12\x0f\n\x07session\x18\x04 \x01(\t\x12\x13\n\x0bresponse_id\x18\x01 \x01(\t\x12-\n\x0cquery_result\x18\x02 \x01(\x0b\x32\x17.ondewo.nlu.QueryResult\x12O\n\x1eoriginal_detect_intent_request\x18\x03 \x01(\x0b\x32\'.ondewo.nlu.OriginalDetectIntentRequest\x12(\n\x07headers\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x83\x02\n\x0fWebhookResponse\x12\x18\n\x10\x66ulfillment_text\x18\x01 \x01(\t\x12\x38\n\x14\x66ulfillment_messages\x18\x02 \x03(\x0b\x32\x1a.ondewo.nlu.Intent.Message\x12\x0e\n\x06source\x18\x03 \x01(\t\x12(\n\x07payload\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0foutput_contexts\x18\x05 \x03(\x0b\x32\x13.ondewo.nlu.Context\x12\x34\n\x14\x66ollowup_event_input\x18\x06 \x01(\x0b\x32\x16.ondewo.nlu.EventInput\"W\n\x1bOriginalDetectIntentRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12(\n\x07payload\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"$\n\x0cPingResponse\x12\x14\n\x0cis_reachable\x18\x01 \x01(\x08\x32\x8a\x03\n\x07Webhook\x12\x93\x01\n\x12ResponseRefinement\x12\x1a.ondewo.nlu.WebhookRequest\x1a\x1b.ondewo.nlu.WebhookResponse\"D\x82\xd3\xe4\x93\x02>\"9/{session=projects/*/agent/sessions/*}:responseRefinement:\x01*\x12\x85\x01\n\x0bSlotFilling\x12\x1a.ondewo.nlu.WebhookRequest\x1a\x1b.ondewo.nlu.WebhookResponse\"=\x82\xd3\xe4\x93\x02\x37\"2/{session=projects/*/agent/sessions/*}:slotFilling:\x01*\x12\x61\n\x04Ping\x12\x17.ondewo.nlu.PingRequest\x1a\x18.ondewo.nlu.PingResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/projects/*/agent/webhook:pingB\x9b\x01\n\x1e\x63om.google.cloud.dialogflow.v2B\x0cWebhookProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,ondewo_dot_nlu_dot_context__pb2.DESCRIPTOR,ondewo_dot_nlu_dot_intent__pb2.DESCRIPTOR,ondewo_dot_nlu_dot_session__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='ondewo.nlu.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='ondewo.nlu.PingRequest.session', index=0,
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
  serialized_start=177,
  serialized_end=207,
)


_WEBHOOKREQUEST = _descriptor.Descriptor(
  name='WebhookRequest',
  full_name='ondewo.nlu.WebhookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='ondewo.nlu.WebhookRequest.session', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_id', full_name='ondewo.nlu.WebhookRequest.response_id', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_result', full_name='ondewo.nlu.WebhookRequest.query_result', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='original_detect_intent_request', full_name='ondewo.nlu.WebhookRequest.original_detect_intent_request', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='headers', full_name='ondewo.nlu.WebhookRequest.headers', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=210,
  serialized_end=434,
)


_WEBHOOKRESPONSE = _descriptor.Descriptor(
  name='WebhookResponse',
  full_name='ondewo.nlu.WebhookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fulfillment_text', full_name='ondewo.nlu.WebhookResponse.fulfillment_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fulfillment_messages', full_name='ondewo.nlu.WebhookResponse.fulfillment_messages', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='ondewo.nlu.WebhookResponse.source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='ondewo.nlu.WebhookResponse.payload', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_contexts', full_name='ondewo.nlu.WebhookResponse.output_contexts', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='followup_event_input', full_name='ondewo.nlu.WebhookResponse.followup_event_input', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=437,
  serialized_end=696,
)


_ORIGINALDETECTINTENTREQUEST = _descriptor.Descriptor(
  name='OriginalDetectIntentRequest',
  full_name='ondewo.nlu.OriginalDetectIntentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='ondewo.nlu.OriginalDetectIntentRequest.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='ondewo.nlu.OriginalDetectIntentRequest.payload', index=1,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=698,
  serialized_end=785,
)


_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='ondewo.nlu.PingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_reachable', full_name='ondewo.nlu.PingResponse.is_reachable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=787,
  serialized_end=823,
)

_WEBHOOKREQUEST.fields_by_name['query_result'].message_type = ondewo_dot_nlu_dot_session__pb2._QUERYRESULT
_WEBHOOKREQUEST.fields_by_name['original_detect_intent_request'].message_type = _ORIGINALDETECTINTENTREQUEST
_WEBHOOKREQUEST.fields_by_name['headers'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_WEBHOOKRESPONSE.fields_by_name['fulfillment_messages'].message_type = ondewo_dot_nlu_dot_intent__pb2._INTENT_MESSAGE
_WEBHOOKRESPONSE.fields_by_name['payload'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_WEBHOOKRESPONSE.fields_by_name['output_contexts'].message_type = ondewo_dot_nlu_dot_context__pb2._CONTEXT
_WEBHOOKRESPONSE.fields_by_name['followup_event_input'].message_type = ondewo_dot_nlu_dot_session__pb2._EVENTINPUT
_ORIGINALDETECTINTENTREQUEST.fields_by_name['payload'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['WebhookRequest'] = _WEBHOOKREQUEST
DESCRIPTOR.message_types_by_name['WebhookResponse'] = _WEBHOOKRESPONSE
DESCRIPTOR.message_types_by_name['OriginalDetectIntentRequest'] = _ORIGINALDETECTINTENTREQUEST
DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'ondewo.nlu.webhook_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.PingRequest)
  })
_sym_db.RegisterMessage(PingRequest)

WebhookRequest = _reflection.GeneratedProtocolMessageType('WebhookRequest', (_message.Message,), {
  'DESCRIPTOR' : _WEBHOOKREQUEST,
  '__module__' : 'ondewo.nlu.webhook_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.WebhookRequest)
  })
_sym_db.RegisterMessage(WebhookRequest)

WebhookResponse = _reflection.GeneratedProtocolMessageType('WebhookResponse', (_message.Message,), {
  'DESCRIPTOR' : _WEBHOOKRESPONSE,
  '__module__' : 'ondewo.nlu.webhook_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.WebhookResponse)
  })
_sym_db.RegisterMessage(WebhookResponse)

OriginalDetectIntentRequest = _reflection.GeneratedProtocolMessageType('OriginalDetectIntentRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORIGINALDETECTINTENTREQUEST,
  '__module__' : 'ondewo.nlu.webhook_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.OriginalDetectIntentRequest)
  })
_sym_db.RegisterMessage(OriginalDetectIntentRequest)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), {
  'DESCRIPTOR' : _PINGRESPONSE,
  '__module__' : 'ondewo.nlu.webhook_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.PingResponse)
  })
_sym_db.RegisterMessage(PingResponse)


DESCRIPTOR._options = None

_WEBHOOK = _descriptor.ServiceDescriptor(
  name='Webhook',
  full_name='ondewo.nlu.Webhook',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=826,
  serialized_end=1220,
  methods=[
  _descriptor.MethodDescriptor(
    name='ResponseRefinement',
    full_name='ondewo.nlu.Webhook.ResponseRefinement',
    index=0,
    containing_service=None,
    input_type=_WEBHOOKREQUEST,
    output_type=_WEBHOOKRESPONSE,
    serialized_options=b'\202\323\344\223\002>\"9/{session=projects/*/agent/sessions/*}:responseRefinement:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SlotFilling',
    full_name='ondewo.nlu.Webhook.SlotFilling',
    index=1,
    containing_service=None,
    input_type=_WEBHOOKREQUEST,
    output_type=_WEBHOOKRESPONSE,
    serialized_options=b'\202\323\344\223\0027\"2/{session=projects/*/agent/sessions/*}:slotFilling:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='ondewo.nlu.Webhook.Ping',
    index=2,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGRESPONSE,
    serialized_options=b'\202\323\344\223\002 \022\036/projects/*/agent/webhook:ping',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WEBHOOK)

DESCRIPTOR.services_by_name['Webhook'] = _WEBHOOK

# @@protoc_insertion_point(module_scope)
