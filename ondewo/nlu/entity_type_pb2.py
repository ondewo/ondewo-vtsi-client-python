# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/nlu/entity_type.proto
"""Generated protocol buffer code."""
from ondewo.nlu import operations_pb2 as ondewo_dot_nlu_dot_operations__pb2
from ondewo.nlu import common_pb2 as ondewo_dot_nlu_dot_common__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1condewo/nlu/entity_type.proto\x12\nondewo.nlu\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x17ondewo/nlu/common.proto\x1a\x1bondewo/nlu/operations.proto\"\x93\x05\n\nEntityType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12)\n\x04kind\x18\x03 \x01(\x0e\x32\x1b.ondewo.nlu.EntityType.Kind\x12\x45\n\x13\x61uto_expansion_mode\x18\x04 \x01(\x0e\x32(.ondewo.nlu.EntityType.AutoExpansionMode\x12/\n\x08\x65ntities\x18\x06 \x03(\x0b\x32\x1d.ondewo.nlu.EntityType.Entity\x12\x17\n\x0fnext_page_token\x18\n \x01(\t\x12\x14\n\x0c\x65ntity_count\x18\x0b \x01(\x05\x12\x37\n\x06status\x18\x0c \x01(\x0e\x32\'.ondewo.nlu.EntityType.EntityTypeStatus\x12\x15\n\rsynonym_count\x18\r \x01(\x05\x1a{\n\x06\x45ntity\x12\r\n\x05value\x18\x01 \x01(\t\x12\x10\n\x08synonyms\x18\x02 \x03(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x04 \x01(\t\x12\x15\n\rsynonym_count\x18\x05 \x01(\x05\x12\x15\n\rlanguage_code\x18\x06 \x01(\t\"9\n\x04Kind\x12\x14\n\x10KIND_UNSPECIFIED\x10\x00\x12\x0c\n\x08KIND_MAP\x10\x01\x12\r\n\tKIND_LIST\x10\x02\",\n\x10\x45ntityTypeStatus\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\"Y\n\x11\x41utoExpansionMode\x12#\n\x1f\x41UTO_EXPANSION_MODE_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x41UTO_EXPANSION_MODE_DEFAULT\x10\x01\"\xfb\x01\n\x16ListEntityTypesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x34\n\x10\x65ntity_type_view\x18\x05 \x01(\x0e\x32\x1a.ondewo.nlu.EntityTypeView\x12:\n\x12\x66ilter_by_category\x18\x06 \x01(\x0e\x32\x1e.ondewo.nlu.EntityTypeCategory\x12\x34\n\rsort_by_field\x18\x07 \x01(\x0b\x32\x1d.ondewo.nlu.EntityTypeSorting\"`\n\x17ListEntityTypesResponse\x12,\n\x0c\x65ntity_types\x18\x01 \x03(\x0b\x32\x16.ondewo.nlu.EntityType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x85\x01\n\x14GetEntityTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x12\n\npage_token\x18\x05 \x01(\t\x12\x34\n\x10\x65ntity_type_view\x18\x06 \x01(\x0e\x32\x1a.ondewo.nlu.EntityTypeView\"\xa3\x01\n\x17\x43reateEntityTypeRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12+\n\x0b\x65ntity_type\x18\x02 \x01(\x0b\x32\x16.ondewo.nlu.EntityType\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x12\x34\n\x10\x65ntity_type_view\x18\x06 \x01(\x0e\x32\x1a.ondewo.nlu.EntityTypeView\"\xc4\x01\n\x17UpdateEntityTypeRequest\x12+\n\x0b\x65ntity_type\x18\x01 \x01(\x0b\x32\x16.ondewo.nlu.EntityType\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x34\n\x10\x65ntity_type_view\x18\x06 \x01(\x0e\x32\x1a.ondewo.nlu.EntityTypeView\"\'\n\x17\x44\x65leteEntityTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xee\x01\n\x1d\x42\x61tchUpdateEntityTypesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x1f\n\x15\x65ntity_type_batch_uri\x18\x02 \x01(\tH\x00\x12?\n\x18\x65ntity_type_batch_inline\x18\x03 \x01(\x0b\x32\x1b.ondewo.nlu.EntityTypeBatchH\x00\x12\x15\n\rlanguage_code\x18\x04 \x01(\t\x12/\n\x0bupdate_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x13\n\x11\x65ntity_type_batch\"N\n\x1e\x42\x61tchUpdateEntityTypesResponse\x12,\n\x0c\x65ntity_types\x18\x01 \x03(\x0b\x32\x16.ondewo.nlu.EntityType\"J\n\x1d\x42\x61tchDeleteEntityTypesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x19\n\x11\x65ntity_type_names\x18\x02 \x03(\t\"?\n\x0f\x45ntityTypeBatch\x12,\n\x0c\x65ntity_types\x18\x01 \x03(\x0b\x32\x16.ondewo.nlu.EntityType\"\x84\x03\n\x11\x45ntityTypeSorting\x12K\n\rsorting_field\x18\x01 \x01(\x0e\x32\x34.ondewo.nlu.EntityTypeSorting.EntityTypeSortingField\x12-\n\x0csorting_mode\x18\x02 \x01(\x0e\x32\x17.ondewo.nlu.SortingMode\"\xf2\x01\n\x16\x45ntityTypeSortingField\x12\x1a\n\x16NO_ENTITY_TYPE_SORTING\x10\x00\x12\x1c\n\x18SORT_ENTITY_TYPE_BY_NAME\x10\x01\x12%\n!SORT_ENTITY_TYPE_BY_CREATION_DATE\x10\x02\x12$\n SORT_ENTITY_TYPE_BY_LAST_UPDATED\x10\x03\x12*\n&SORT_ENTITY_TYPE_BY_ENTITY_VALUE_COUNT\x10\x04\x12%\n!SORT_ENTITY_TYPE_BY_SYNONYM_COUNT\x10\x05\"l\n\x0c\x45ntityStatus\x12/\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x1d.ondewo.nlu.EntityType.EntityH\x00\x12\x17\n\rerror_message\x18\x02 \x01(\tH\x00\x42\x12\n\x10\x65ntity_or_status\"^\n\x15\x42\x61tchEntitiesResponse\x12\x31\n\x0f\x65ntity_statuses\x18\x01 \x03(\x0b\x32\x18.ondewo.nlu.EntityStatus\x12\x12\n\nhas_errors\x18\x02 \x01(\x08\"^\n\x13\x43reateEntityRequest\x12\x18\n\x10\x65ntity_type_name\x18\x01 \x01(\t\x12-\n\x06\x65ntity\x18\x02 \x01(\x0b\x32\x1d.ondewo.nlu.EntityType.Entity\"]\n\x1a\x42\x61tchCreateEntitiesRequest\x12?\n\x16\x63reate_entity_requests\x18\x01 \x03(\x0b\x32\x1f.ondewo.nlu.CreateEntityRequest\"M\n\x1a\x42\x61tchUpdateEntitiesRequest\x12/\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x1d.ondewo.nlu.EntityType.Entity\"D\n\x13UpdateEntityRequest\x12-\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x1d.ondewo.nlu.EntityType.Entity\" \n\x10GetEntityRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"(\n\x17\x42\x61tchGetEntitiesRequest\x12\r\n\x05names\x18\x01 \x03(\t\"+\n\x1a\x42\x61tchDeleteEntitiesRequest\x12\r\n\x05names\x18\x01 \x03(\t\"#\n\x13\x44\x65leteEntityRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"v\n\x12\x44\x65leteEntityStatus\x12\x36\n\x14successfully_deleted\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x17\n\rerror_message\x18\x02 \x01(\tH\x00\x42\x0f\n\rdelete_status\"j\n\x1b\x42\x61tchDeleteEntitiesResponse\x12\x37\n\x0f\x64\x65lete_statuses\x18\x01 \x03(\x0b\x32\x1e.ondewo.nlu.DeleteEntityStatus\x12\x12\n\nhas_errors\x18\x02 \x01(\x08\"\xac\x01\n\x13ListEntitiesRequest\x12\x18\n\x10\x65ntity_type_name\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x35\n\rsort_by_field\x18\x05 \x01(\x0b\x32\x1e.ondewo.nlu.EntityValueSorting\x12\x19\n\x11search_by_pattern\x18\x06 \x01(\t\"`\n\x14ListEntitiesResponse\x12/\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x1d.ondewo.nlu.EntityType.Entity\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xba\x02\n\x12\x45ntityValueSorting\x12M\n\rsorting_field\x18\x07 \x01(\x0e\x32\x36.ondewo.nlu.EntityValueSorting.EntityValueSortingField\x12-\n\x0csorting_mode\x18\x08 \x01(\x0e\x32\x17.ondewo.nlu.SortingMode\"\xa5\x01\n\x17\x45ntityValueSortingField\x12\x1b\n\x17NO_ENTITY_VALUE_SORTING\x10\x00\x12%\n!SORT_ENTITY_VALUE_BY_DISPLAY_NAME\x10\x01\x12\x1e\n\x1aSORT_ENTITY_VALUE_BY_VALUE\x10\x02\x12&\n\"SORT_ENTITY_VALUE_BY_SYNONYM_COUNT\x10\x03*\xa7\x01\n\x0e\x45ntityTypeView\x12 \n\x1c\x45NTITY_TYPE_VIEW_UNSPECIFIED\x10\x00\x12\x19\n\x15\x45NTITY_TYPE_VIEW_FULL\x10\x01\x12\x1c\n\x18\x45NTITY_TYPE_VIEW_PARTIAL\x10\x02\x12\x1c\n\x18\x45NTITY_TYPE_VIEW_SHALLOW\x10\x03\x12\x1c\n\x18\x45NTITY_TYPE_VIEW_MINIMUM\x10\x04*c\n\x12\x45ntityTypeCategory\x12\x14\n\x10\x41LL_ENTITY_TYPES\x10\x00\x12\x18\n\x14\x44\x45\x46\x41ULT_ENTITY_TYPES\x10\x01\x12\x1d\n\x19USER_DEFINED_ENTITY_TYPES\x10\x02\x32\x9b\x10\n\x0b\x45ntityTypes\x12\x8d\x01\n\x0fListEntityTypes\x12\".ondewo.nlu.ListEntityTypesRequest\x1a#.ondewo.nlu.ListEntityTypesResponse\"1\x82\xd3\xe4\x93\x02+\x12)/v2/{parent=projects/*/agent}/entityTypes\x12|\n\rGetEntityType\x12 .ondewo.nlu.GetEntityTypeRequest\x1a\x16.ondewo.nlu.EntityType\"1\x82\xd3\xe4\x93\x02+\x12)/v2/{name=projects/*/agent/entityTypes/*}\x12\x85\x01\n\x10\x43reateEntityType\x12#.ondewo.nlu.CreateEntityTypeRequest\x1a\x16.ondewo.nlu.EntityType\"4\x82\xd3\xe4\x93\x02.\")/v2/{parent=projects/*/agent}/entityTypes:\x01*\x12\x91\x01\n\x10UpdateEntityType\x12#.ondewo.nlu.UpdateEntityTypeRequest\x1a\x16.ondewo.nlu.EntityType\"@\x82\xd3\xe4\x93\x02:25/v2/{entity_type.name=projects/*/agent/entityTypes/*}:\x01*\x12\x82\x01\n\x10\x44\x65leteEntityType\x12#.ondewo.nlu.DeleteEntityTypeRequest\x1a\x16.google.protobuf.Empty\"1\x82\xd3\xe4\x93\x02+*)/v2/{name=projects/*/agent/entityTypes/*}\x12\x9c\x01\n\x16\x42\x61tchUpdateEntityTypes\x12).ondewo.nlu.BatchUpdateEntityTypesRequest\x1a\x15.ondewo.nlu.Operation\"@\x82\xd3\xe4\x93\x02:\"5/v2/{parent=projects/*/agent}/entityTypes:batchUpdate:\x01*\x12\x9c\x01\n\x16\x42\x61tchDeleteEntityTypes\x12).ondewo.nlu.BatchDeleteEntityTypesRequest\x1a\x15.ondewo.nlu.Operation\"@\x82\xd3\xe4\x93\x02:\"5/v2/{parent=projects/*/agent}/entityTypes:batchDelete:\x01*\x12\x86\x01\n\tGetEntity\x12\x1c.ondewo.nlu.GetEntityRequest\x1a\x1d.ondewo.nlu.EntityType.Entity\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/v2/{name=projects/*/agent/entityTypes/*/entities/*}\x12\x90\x01\n\x0c\x43reateEntity\x12\x1f.ondewo.nlu.CreateEntityRequest\x1a\x1d.ondewo.nlu.EntityType.Entity\"@\x82\xd3\xe4\x93\x02:\"5/v2/{parent=projects/*/agent}/entityTypes/*/entities/:\x01*\x12\x97\x01\n\x0cUpdateEntity\x12\x1f.ondewo.nlu.UpdateEntityRequest\x1a\x1d.ondewo.nlu.EntityType.Entity\"G\x82\xd3\xe4\x93\x02\x41\x32</v2/{entity_.name=projects/*/agent/entityTypes/*/entities/*}:\x01*\x12\x8d\x01\n\x0c\x44\x65leteEntity\x12\x1f.ondewo.nlu.DeleteEntityRequest\x1a\x1e.ondewo.nlu.DeleteEntityStatus\"<\x82\xd3\xe4\x93\x02\x36*4/v2/{name=projects/*/agent/entityTypes/*/entities/*}\x12`\n\x13\x42\x61tchCreateEntities\x12&.ondewo.nlu.BatchCreateEntitiesRequest\x1a!.ondewo.nlu.BatchEntitiesResponse\x12`\n\x13\x42\x61tchUpdateEntities\x12&.ondewo.nlu.BatchUpdateEntitiesRequest\x1a!.ondewo.nlu.BatchEntitiesResponse\x12Z\n\x10\x42\x61tchGetEntities\x12#.ondewo.nlu.BatchGetEntitiesRequest\x1a!.ondewo.nlu.BatchEntitiesResponse\x12\x66\n\x13\x42\x61tchDeleteEntities\x12&.ondewo.nlu.BatchDeleteEntitiesRequest\x1a\'.ondewo.nlu.BatchDeleteEntitiesResponse\x12Q\n\x0cListEntities\x12\x1f.ondewo.nlu.ListEntitiesRequest\x1a .ondewo.nlu.ListEntitiesResponseB\x9e\x01\n\x1e\x63om.google.cloud.dialogflow.v2B\x0f\x45ntityTypeProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')

_ENTITYTYPEVIEW = DESCRIPTOR.enum_types_by_name['EntityTypeView']
EntityTypeView = enum_type_wrapper.EnumTypeWrapper(_ENTITYTYPEVIEW)
_ENTITYTYPECATEGORY = DESCRIPTOR.enum_types_by_name['EntityTypeCategory']
EntityTypeCategory = enum_type_wrapper.EnumTypeWrapper(_ENTITYTYPECATEGORY)
ENTITY_TYPE_VIEW_UNSPECIFIED = 0
ENTITY_TYPE_VIEW_FULL = 1
ENTITY_TYPE_VIEW_PARTIAL = 2
ENTITY_TYPE_VIEW_SHALLOW = 3
ENTITY_TYPE_VIEW_MINIMUM = 4
ALL_ENTITY_TYPES = 0
DEFAULT_ENTITY_TYPES = 1
USER_DEFINED_ENTITY_TYPES = 2


_ENTITYTYPE = DESCRIPTOR.message_types_by_name['EntityType']
_ENTITYTYPE_ENTITY = _ENTITYTYPE.nested_types_by_name['Entity']
_LISTENTITYTYPESREQUEST = DESCRIPTOR.message_types_by_name['ListEntityTypesRequest']
_LISTENTITYTYPESRESPONSE = DESCRIPTOR.message_types_by_name['ListEntityTypesResponse']
_GETENTITYTYPEREQUEST = DESCRIPTOR.message_types_by_name['GetEntityTypeRequest']
_CREATEENTITYTYPEREQUEST = DESCRIPTOR.message_types_by_name['CreateEntityTypeRequest']
_UPDATEENTITYTYPEREQUEST = DESCRIPTOR.message_types_by_name['UpdateEntityTypeRequest']
_DELETEENTITYTYPEREQUEST = DESCRIPTOR.message_types_by_name['DeleteEntityTypeRequest']
_BATCHUPDATEENTITYTYPESREQUEST = DESCRIPTOR.message_types_by_name['BatchUpdateEntityTypesRequest']
_BATCHUPDATEENTITYTYPESRESPONSE = DESCRIPTOR.message_types_by_name['BatchUpdateEntityTypesResponse']
_BATCHDELETEENTITYTYPESREQUEST = DESCRIPTOR.message_types_by_name['BatchDeleteEntityTypesRequest']
_ENTITYTYPEBATCH = DESCRIPTOR.message_types_by_name['EntityTypeBatch']
_ENTITYTYPESORTING = DESCRIPTOR.message_types_by_name['EntityTypeSorting']
_ENTITYSTATUS = DESCRIPTOR.message_types_by_name['EntityStatus']
_BATCHENTITIESRESPONSE = DESCRIPTOR.message_types_by_name['BatchEntitiesResponse']
_CREATEENTITYREQUEST = DESCRIPTOR.message_types_by_name['CreateEntityRequest']
_BATCHCREATEENTITIESREQUEST = DESCRIPTOR.message_types_by_name['BatchCreateEntitiesRequest']
_BATCHUPDATEENTITIESREQUEST = DESCRIPTOR.message_types_by_name['BatchUpdateEntitiesRequest']
_UPDATEENTITYREQUEST = DESCRIPTOR.message_types_by_name['UpdateEntityRequest']
_GETENTITYREQUEST = DESCRIPTOR.message_types_by_name['GetEntityRequest']
_BATCHGETENTITIESREQUEST = DESCRIPTOR.message_types_by_name['BatchGetEntitiesRequest']
_BATCHDELETEENTITIESREQUEST = DESCRIPTOR.message_types_by_name['BatchDeleteEntitiesRequest']
_DELETEENTITYREQUEST = DESCRIPTOR.message_types_by_name['DeleteEntityRequest']
_DELETEENTITYSTATUS = DESCRIPTOR.message_types_by_name['DeleteEntityStatus']
_BATCHDELETEENTITIESRESPONSE = DESCRIPTOR.message_types_by_name['BatchDeleteEntitiesResponse']
_LISTENTITIESREQUEST = DESCRIPTOR.message_types_by_name['ListEntitiesRequest']
_LISTENTITIESRESPONSE = DESCRIPTOR.message_types_by_name['ListEntitiesResponse']
_ENTITYVALUESORTING = DESCRIPTOR.message_types_by_name['EntityValueSorting']
_ENTITYTYPE_KIND = _ENTITYTYPE.enum_types_by_name['Kind']
_ENTITYTYPE_ENTITYTYPESTATUS = _ENTITYTYPE.enum_types_by_name['EntityTypeStatus']
_ENTITYTYPE_AUTOEXPANSIONMODE = _ENTITYTYPE.enum_types_by_name['AutoExpansionMode']
_ENTITYTYPESORTING_ENTITYTYPESORTINGFIELD = _ENTITYTYPESORTING.enum_types_by_name['EntityTypeSortingField']
_ENTITYVALUESORTING_ENTITYVALUESORTINGFIELD = _ENTITYVALUESORTING.enum_types_by_name['EntityValueSortingField']
EntityType = _reflection.GeneratedProtocolMessageType('EntityType', (_message.Message,), {

    'Entity': _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
        'DESCRIPTOR': _ENTITYTYPE_ENTITY,
        '__module__': 'ondewo.nlu.entity_type_pb2'
        # @@protoc_insertion_point(class_scope:ondewo.nlu.EntityType.Entity)
    }),
    'DESCRIPTOR': _ENTITYTYPE,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.EntityType)
})
_sym_db.RegisterMessage(EntityType)
_sym_db.RegisterMessage(EntityType.Entity)

ListEntityTypesRequest = _reflection.GeneratedProtocolMessageType('ListEntityTypesRequest', (_message.Message,), {
    'DESCRIPTOR': _LISTENTITYTYPESREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.ListEntityTypesRequest)
})
_sym_db.RegisterMessage(ListEntityTypesRequest)

ListEntityTypesResponse = _reflection.GeneratedProtocolMessageType('ListEntityTypesResponse', (_message.Message,), {
    'DESCRIPTOR': _LISTENTITYTYPESRESPONSE,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.ListEntityTypesResponse)
})
_sym_db.RegisterMessage(ListEntityTypesResponse)

GetEntityTypeRequest = _reflection.GeneratedProtocolMessageType('GetEntityTypeRequest', (_message.Message,), {
    'DESCRIPTOR': _GETENTITYTYPEREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.GetEntityTypeRequest)
})
_sym_db.RegisterMessage(GetEntityTypeRequest)

CreateEntityTypeRequest = _reflection.GeneratedProtocolMessageType('CreateEntityTypeRequest', (_message.Message,), {
    'DESCRIPTOR': _CREATEENTITYTYPEREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.CreateEntityTypeRequest)
})
_sym_db.RegisterMessage(CreateEntityTypeRequest)

UpdateEntityTypeRequest = _reflection.GeneratedProtocolMessageType('UpdateEntityTypeRequest', (_message.Message,), {
    'DESCRIPTOR': _UPDATEENTITYTYPEREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.UpdateEntityTypeRequest)
})
_sym_db.RegisterMessage(UpdateEntityTypeRequest)

DeleteEntityTypeRequest = _reflection.GeneratedProtocolMessageType('DeleteEntityTypeRequest', (_message.Message,), {
    'DESCRIPTOR': _DELETEENTITYTYPEREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.DeleteEntityTypeRequest)
})
_sym_db.RegisterMessage(DeleteEntityTypeRequest)

BatchUpdateEntityTypesRequest = _reflection.GeneratedProtocolMessageType('BatchUpdateEntityTypesRequest', (_message.Message,), {
    'DESCRIPTOR': _BATCHUPDATEENTITYTYPESREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.BatchUpdateEntityTypesRequest)
})
_sym_db.RegisterMessage(BatchUpdateEntityTypesRequest)

BatchUpdateEntityTypesResponse = _reflection.GeneratedProtocolMessageType('BatchUpdateEntityTypesResponse', (_message.Message,), {
    'DESCRIPTOR': _BATCHUPDATEENTITYTYPESRESPONSE,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.BatchUpdateEntityTypesResponse)
})
_sym_db.RegisterMessage(BatchUpdateEntityTypesResponse)

BatchDeleteEntityTypesRequest = _reflection.GeneratedProtocolMessageType('BatchDeleteEntityTypesRequest', (_message.Message,), {
    'DESCRIPTOR': _BATCHDELETEENTITYTYPESREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.BatchDeleteEntityTypesRequest)
})
_sym_db.RegisterMessage(BatchDeleteEntityTypesRequest)

EntityTypeBatch = _reflection.GeneratedProtocolMessageType('EntityTypeBatch', (_message.Message,), {
    'DESCRIPTOR': _ENTITYTYPEBATCH,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.EntityTypeBatch)
})
_sym_db.RegisterMessage(EntityTypeBatch)

EntityTypeSorting = _reflection.GeneratedProtocolMessageType('EntityTypeSorting', (_message.Message,), {
    'DESCRIPTOR': _ENTITYTYPESORTING,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.EntityTypeSorting)
})
_sym_db.RegisterMessage(EntityTypeSorting)

EntityStatus = _reflection.GeneratedProtocolMessageType('EntityStatus', (_message.Message,), {
    'DESCRIPTOR': _ENTITYSTATUS,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.EntityStatus)
})
_sym_db.RegisterMessage(EntityStatus)

BatchEntitiesResponse = _reflection.GeneratedProtocolMessageType('BatchEntitiesResponse', (_message.Message,), {
    'DESCRIPTOR': _BATCHENTITIESRESPONSE,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.BatchEntitiesResponse)
})
_sym_db.RegisterMessage(BatchEntitiesResponse)

CreateEntityRequest = _reflection.GeneratedProtocolMessageType('CreateEntityRequest', (_message.Message,), {
    'DESCRIPTOR': _CREATEENTITYREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.CreateEntityRequest)
})
_sym_db.RegisterMessage(CreateEntityRequest)

BatchCreateEntitiesRequest = _reflection.GeneratedProtocolMessageType('BatchCreateEntitiesRequest', (_message.Message,), {
    'DESCRIPTOR': _BATCHCREATEENTITIESREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.BatchCreateEntitiesRequest)
})
_sym_db.RegisterMessage(BatchCreateEntitiesRequest)

BatchUpdateEntitiesRequest = _reflection.GeneratedProtocolMessageType('BatchUpdateEntitiesRequest', (_message.Message,), {
    'DESCRIPTOR': _BATCHUPDATEENTITIESREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.BatchUpdateEntitiesRequest)
})
_sym_db.RegisterMessage(BatchUpdateEntitiesRequest)

UpdateEntityRequest = _reflection.GeneratedProtocolMessageType('UpdateEntityRequest', (_message.Message,), {
    'DESCRIPTOR': _UPDATEENTITYREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.UpdateEntityRequest)
})
_sym_db.RegisterMessage(UpdateEntityRequest)

GetEntityRequest = _reflection.GeneratedProtocolMessageType('GetEntityRequest', (_message.Message,), {
    'DESCRIPTOR': _GETENTITYREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.GetEntityRequest)
})
_sym_db.RegisterMessage(GetEntityRequest)

BatchGetEntitiesRequest = _reflection.GeneratedProtocolMessageType('BatchGetEntitiesRequest', (_message.Message,), {
    'DESCRIPTOR': _BATCHGETENTITIESREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.BatchGetEntitiesRequest)
})
_sym_db.RegisterMessage(BatchGetEntitiesRequest)

BatchDeleteEntitiesRequest = _reflection.GeneratedProtocolMessageType('BatchDeleteEntitiesRequest', (_message.Message,), {
    'DESCRIPTOR': _BATCHDELETEENTITIESREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.BatchDeleteEntitiesRequest)
})
_sym_db.RegisterMessage(BatchDeleteEntitiesRequest)

DeleteEntityRequest = _reflection.GeneratedProtocolMessageType('DeleteEntityRequest', (_message.Message,), {
    'DESCRIPTOR': _DELETEENTITYREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.DeleteEntityRequest)
})
_sym_db.RegisterMessage(DeleteEntityRequest)

DeleteEntityStatus = _reflection.GeneratedProtocolMessageType('DeleteEntityStatus', (_message.Message,), {
    'DESCRIPTOR': _DELETEENTITYSTATUS,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.DeleteEntityStatus)
})
_sym_db.RegisterMessage(DeleteEntityStatus)

BatchDeleteEntitiesResponse = _reflection.GeneratedProtocolMessageType('BatchDeleteEntitiesResponse', (_message.Message,), {
    'DESCRIPTOR': _BATCHDELETEENTITIESRESPONSE,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.BatchDeleteEntitiesResponse)
})
_sym_db.RegisterMessage(BatchDeleteEntitiesResponse)

ListEntitiesRequest = _reflection.GeneratedProtocolMessageType('ListEntitiesRequest', (_message.Message,), {
    'DESCRIPTOR': _LISTENTITIESREQUEST,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.ListEntitiesRequest)
})
_sym_db.RegisterMessage(ListEntitiesRequest)

ListEntitiesResponse = _reflection.GeneratedProtocolMessageType('ListEntitiesResponse', (_message.Message,), {
    'DESCRIPTOR': _LISTENTITIESRESPONSE,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.ListEntitiesResponse)
})
_sym_db.RegisterMessage(ListEntitiesResponse)

EntityValueSorting = _reflection.GeneratedProtocolMessageType('EntityValueSorting', (_message.Message,), {
    'DESCRIPTOR': _ENTITYVALUESORTING,
    '__module__': 'ondewo.nlu.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.EntityValueSorting)
})
_sym_db.RegisterMessage(EntityValueSorting)

_ENTITYTYPES = DESCRIPTOR.services_by_name['EntityTypes']
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\036com.google.cloud.dialogflow.v2B\017EntityTypeProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\370\001\001\242\002\002DF\252\002\032Google.Cloud.Dialogflow.V2'
    _ENTITYTYPES.methods_by_name['ListEntityTypes']._options = None
    _ENTITYTYPES.methods_by_name['ListEntityTypes']._serialized_options = b'\202\323\344\223\002+\022)/v2/{parent=projects/*/agent}/entityTypes'
    _ENTITYTYPES.methods_by_name['GetEntityType']._options = None
    _ENTITYTYPES.methods_by_name['GetEntityType']._serialized_options = b'\202\323\344\223\002+\022)/v2/{name=projects/*/agent/entityTypes/*}'
    _ENTITYTYPES.methods_by_name['CreateEntityType']._options = None
    _ENTITYTYPES.methods_by_name['CreateEntityType']._serialized_options = b'\202\323\344\223\002.\")/v2/{parent=projects/*/agent}/entityTypes:\001*'
    _ENTITYTYPES.methods_by_name['UpdateEntityType']._options = None
    _ENTITYTYPES.methods_by_name['UpdateEntityType']._serialized_options = b'\202\323\344\223\002:25/v2/{entity_type.name=projects/*/agent/entityTypes/*}:\001*'
    _ENTITYTYPES.methods_by_name['DeleteEntityType']._options = None
    _ENTITYTYPES.methods_by_name['DeleteEntityType']._serialized_options = b'\202\323\344\223\002+*)/v2/{name=projects/*/agent/entityTypes/*}'
    _ENTITYTYPES.methods_by_name['BatchUpdateEntityTypes']._options = None
    _ENTITYTYPES.methods_by_name['BatchUpdateEntityTypes']._serialized_options = b'\202\323\344\223\002:\"5/v2/{parent=projects/*/agent}/entityTypes:batchUpdate:\001*'
    _ENTITYTYPES.methods_by_name['BatchDeleteEntityTypes']._options = None
    _ENTITYTYPES.methods_by_name['BatchDeleteEntityTypes']._serialized_options = b'\202\323\344\223\002:\"5/v2/{parent=projects/*/agent}/entityTypes:batchDelete:\001*'
    _ENTITYTYPES.methods_by_name['GetEntity']._options = None
    _ENTITYTYPES.methods_by_name['GetEntity']._serialized_options = b'\202\323\344\223\0026\0224/v2/{name=projects/*/agent/entityTypes/*/entities/*}'
    _ENTITYTYPES.methods_by_name['CreateEntity']._options = None
    _ENTITYTYPES.methods_by_name['CreateEntity']._serialized_options = b'\202\323\344\223\002:\"5/v2/{parent=projects/*/agent}/entityTypes/*/entities/:\001*'
    _ENTITYTYPES.methods_by_name['UpdateEntity']._options = None
    _ENTITYTYPES.methods_by_name['UpdateEntity']._serialized_options = b'\202\323\344\223\002A2</v2/{entity_.name=projects/*/agent/entityTypes/*/entities/*}:\001*'
    _ENTITYTYPES.methods_by_name['DeleteEntity']._options = None
    _ENTITYTYPES.methods_by_name['DeleteEntity']._serialized_options = b'\202\323\344\223\0026*4/v2/{name=projects/*/agent/entityTypes/*/entities/*}'
    _ENTITYTYPEVIEW._serialized_start=4123
    _ENTITYTYPEVIEW._serialized_end=4290
    _ENTITYTYPECATEGORY._serialized_start=4292
    _ENTITYTYPECATEGORY._serialized_end=4391
    _ENTITYTYPE._serialized_start=192
    _ENTITYTYPE._serialized_end=851
    _ENTITYTYPE_ENTITY._serialized_start=532
    _ENTITYTYPE_ENTITY._serialized_end=655
    _ENTITYTYPE_KIND._serialized_start=657
    _ENTITYTYPE_KIND._serialized_end=714
    _ENTITYTYPE_ENTITYTYPESTATUS._serialized_start=716
    _ENTITYTYPE_ENTITYTYPESTATUS._serialized_end=760
    _ENTITYTYPE_AUTOEXPANSIONMODE._serialized_start=762
    _ENTITYTYPE_AUTOEXPANSIONMODE._serialized_end=851
    _LISTENTITYTYPESREQUEST._serialized_start=854
    _LISTENTITYTYPESREQUEST._serialized_end=1105
    _LISTENTITYTYPESRESPONSE._serialized_start=1107
    _LISTENTITYTYPESRESPONSE._serialized_end=1203
    _GETENTITYTYPEREQUEST._serialized_start=1206
    _GETENTITYTYPEREQUEST._serialized_end=1339
    _CREATEENTITYTYPEREQUEST._serialized_start=1342
    _CREATEENTITYTYPEREQUEST._serialized_end=1505
    _UPDATEENTITYTYPEREQUEST._serialized_start=1508
    _UPDATEENTITYTYPEREQUEST._serialized_end=1704
    _DELETEENTITYTYPEREQUEST._serialized_start=1706
    _DELETEENTITYTYPEREQUEST._serialized_end=1745
    _BATCHUPDATEENTITYTYPESREQUEST._serialized_start=1748
    _BATCHUPDATEENTITYTYPESREQUEST._serialized_end=1986
    _BATCHUPDATEENTITYTYPESRESPONSE._serialized_start=1988
    _BATCHUPDATEENTITYTYPESRESPONSE._serialized_end=2066
    _BATCHDELETEENTITYTYPESREQUEST._serialized_start=2068
    _BATCHDELETEENTITYTYPESREQUEST._serialized_end=2142
    _ENTITYTYPEBATCH._serialized_start=2144
    _ENTITYTYPEBATCH._serialized_end=2207
    _ENTITYTYPESORTING._serialized_start=2210
    _ENTITYTYPESORTING._serialized_end=2598
    _ENTITYTYPESORTING_ENTITYTYPESORTINGFIELD._serialized_start=2356
    _ENTITYTYPESORTING_ENTITYTYPESORTINGFIELD._serialized_end=2598
    _ENTITYSTATUS._serialized_start=2600
    _ENTITYSTATUS._serialized_end=2708
    _BATCHENTITIESRESPONSE._serialized_start=2710
    _BATCHENTITIESRESPONSE._serialized_end=2804
    _CREATEENTITYREQUEST._serialized_start=2806
    _CREATEENTITYREQUEST._serialized_end=2900
    _BATCHCREATEENTITIESREQUEST._serialized_start=2902
    _BATCHCREATEENTITIESREQUEST._serialized_end=2995
    _BATCHUPDATEENTITIESREQUEST._serialized_start=2997
    _BATCHUPDATEENTITIESREQUEST._serialized_end=3074
    _UPDATEENTITYREQUEST._serialized_start=3076
    _UPDATEENTITYREQUEST._serialized_end=3144
    _GETENTITYREQUEST._serialized_start=3146
    _GETENTITYREQUEST._serialized_end=3178
    _BATCHGETENTITIESREQUEST._serialized_start=3180
    _BATCHGETENTITIESREQUEST._serialized_end=3220
    _BATCHDELETEENTITIESREQUEST._serialized_start=3222
    _BATCHDELETEENTITIESREQUEST._serialized_end=3265
    _DELETEENTITYREQUEST._serialized_start=3267
    _DELETEENTITYREQUEST._serialized_end=3302
    _DELETEENTITYSTATUS._serialized_start=3304
    _DELETEENTITYSTATUS._serialized_end=3422
    _BATCHDELETEENTITIESRESPONSE._serialized_start=3424
    _BATCHDELETEENTITIESRESPONSE._serialized_end=3530
    _LISTENTITIESREQUEST._serialized_start=3533
    _LISTENTITIESREQUEST._serialized_end=3705
    _LISTENTITIESRESPONSE._serialized_start=3707
    _LISTENTITIESRESPONSE._serialized_end=3803
    _ENTITYVALUESORTING._serialized_start=3806
    _ENTITYVALUESORTING._serialized_end=4120
    _ENTITYVALUESORTING_ENTITYVALUESORTINGFIELD._serialized_start=3955
    _ENTITYVALUESORTING_ENTITYVALUESORTINGFIELD._serialized_end=4120
    _ENTITYTYPES._serialized_start=4394
    _ENTITYTYPES._serialized_end=6469
# @@protoc_insertion_point(module_scope)
