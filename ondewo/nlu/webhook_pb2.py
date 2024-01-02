# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/nlu/webhook.proto
"""Generated protocol buffer code."""
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ondewo.nlu import session_pb2 as ondewo_dot_nlu_dot_session__pb2
from ondewo.nlu import intent_pb2 as ondewo_dot_nlu_dot_intent__pb2
from ondewo.nlu import context_pb2 as ondewo_dot_nlu_dot_context__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18ondewo/nlu/webhook.proto\x12\nondewo.nlu\x1a\x1cgoogle/api/annotations.proto\x1a\x18ondewo/nlu/context.proto\x1a\x17ondewo/nlu/intent.proto\x1a\x18ondewo/nlu/session.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x1e\n\x0bPingRequest\x12\x0f\n\x07session\x18\x01 \x01(\t\"\xe0\x01\n\x0eWebhookRequest\x12\x0f\n\x07session\x18\x04 \x01(\t\x12\x13\n\x0bresponse_id\x18\x01 \x01(\t\x12-\n\x0cquery_result\x18\x02 \x01(\x0b\x32\x17.ondewo.nlu.QueryResult\x12O\n\x1eoriginal_detect_intent_request\x18\x03 \x01(\x0b\x32\'.ondewo.nlu.OriginalDetectIntentRequest\x12(\n\x07headers\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x83\x02\n\x0fWebhookResponse\x12\x18\n\x10\x66ulfillment_text\x18\x01 \x01(\t\x12\x38\n\x14\x66ulfillment_messages\x18\x02 \x03(\x0b\x32\x1a.ondewo.nlu.Intent.Message\x12\x0e\n\x06source\x18\x03 \x01(\t\x12(\n\x07payload\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0foutput_contexts\x18\x05 \x03(\x0b\x32\x13.ondewo.nlu.Context\x12\x34\n\x14\x66ollowup_event_input\x18\x06 \x01(\x0b\x32\x16.ondewo.nlu.EventInput\"W\n\x1bOriginalDetectIntentRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12(\n\x07payload\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"$\n\x0cPingResponse\x12\x14\n\x0cis_reachable\x18\x01 \x01(\x08\x32\x8a\x03\n\x07Webhook\x12\x93\x01\n\x12ResponseRefinement\x12\x1a.ondewo.nlu.WebhookRequest\x1a\x1b.ondewo.nlu.WebhookResponse\"D\x82\xd3\xe4\x93\x02>\"9/{session=projects/*/agent/sessions/*}:responseRefinement:\x01*\x12\x85\x01\n\x0bSlotFilling\x12\x1a.ondewo.nlu.WebhookRequest\x1a\x1b.ondewo.nlu.WebhookResponse\"=\x82\xd3\xe4\x93\x02\x37\"2/{session=projects/*/agent/sessions/*}:slotFilling:\x01*\x12\x61\n\x04Ping\x12\x17.ondewo.nlu.PingRequest\x1a\x18.ondewo.nlu.PingResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/projects/*/agent/webhook:pingB\x9b\x01\n\x1e\x63om.google.cloud.dialogflow.v2B\x0cWebhookProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ondewo.nlu.webhook_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\036com.google.cloud.dialogflow.v2B\014WebhookProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\370\001\001\242\002\002DF\252\002\032Google.Cloud.Dialogflow.V2'
    _WEBHOOK.methods_by_name['ResponseRefinement']._options = None
    _WEBHOOK.methods_by_name['ResponseRefinement']._serialized_options = b'\202\323\344\223\002>\"9/{session=projects/*/agent/sessions/*}:responseRefinement:\001*'
    _WEBHOOK.methods_by_name['SlotFilling']._options = None
    _WEBHOOK.methods_by_name['SlotFilling']._serialized_options = b'\202\323\344\223\0027\"2/{session=projects/*/agent/sessions/*}:slotFilling:\001*'
    _WEBHOOK.methods_by_name['Ping']._options = None
    _WEBHOOK.methods_by_name['Ping']._serialized_options = b'\202\323\344\223\002 \022\036/projects/*/agent/webhook:ping'
    _globals['_PINGREQUEST']._serialized_start=177
    _globals['_PINGREQUEST']._serialized_end=207
    _globals['_WEBHOOKREQUEST']._serialized_start=210
    _globals['_WEBHOOKREQUEST']._serialized_end=434
    _globals['_WEBHOOKRESPONSE']._serialized_start=437
    _globals['_WEBHOOKRESPONSE']._serialized_end=696
    _globals['_ORIGINALDETECTINTENTREQUEST']._serialized_start=698
    _globals['_ORIGINALDETECTINTENTREQUEST']._serialized_end=785
    _globals['_PINGRESPONSE']._serialized_start=787
    _globals['_PINGRESPONSE']._serialized_end=823
    _globals['_WEBHOOK']._serialized_start=826
    _globals['_WEBHOOK']._serialized_end=1220
# @@protoc_insertion_point(module_scope)
