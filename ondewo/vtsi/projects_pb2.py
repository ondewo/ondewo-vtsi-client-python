# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/vtsi/projects.proto
"""Generated protocol buffer code."""
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aondewo/vtsi/projects.proto\x12\x0bondewo.vtsi\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa5\x03\n\x0bVtsiProject\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0bmax_callers\x18\x03 \x01(\x05\x12\x15\n\rmax_listeners\x18\x04 \x01(\x05\x12\x36\n\x10\x61sterisk_configs\x18\x05 \x01(\x0b\x32\x1c.ondewo.vtsi.AsteriskConfigs\x12;\n\x13vtsi_project_status\x18\x06 \x01(\x0e\x32\x1e.ondewo.vtsi.VtsiProjectStatus\x12\x12\n\ncreated_by\x18\x07 \x01(\t\x12.\n\ncreated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bmodified_by\x18\t \x01(\t\x12/\n\x0bmodified_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0e\x61\x63tive_callers\x18\x0b \x01(\x05\x12\x18\n\x10\x61\x63tive_listeners\x18\x0c \x01(\x05\x12\x15\n\rasterisk_port\x18\r \x01(\x05\"\xc1\x01\n\x18\x41steriskConfigsVariables\x12\x1a\n\x12sip_trunk_username\x18\x01 \x01(\t\x12\x1a\n\x12sip_trunk_password\x18\x02 \x01(\t\x12\x16\n\x0esip_trunk_host\x18\x03 \x01(\t\x12\x17\n\x0ftransfer_number\x18\x04 \x01(\t\x12\x1c\n\x14transfer_number_host\x18\x05 \x01(\t\x12\x1e\n\x16sip_trunk_phone_number\x18\x06 \x01(\t\"\x9c\x01\n\x14\x41steriskConfigsFiles\x12\x1c\n\x14sip_conf_file_string\x18\x01 \x01(\t\x12#\n\x1b\x65xtensions_conf_file_string\x18\x02 \x01(\t\x12\x1f\n\x17queues_conf_file_string\x18\x03 \x01(\t\x12 \n\x18modules_conf_file_string\x18\x04 \x01(\t\"\x86\x02\n\x0f\x41steriskConfigs\x12K\n\x1a\x61sterisk_configs_variables\x18\x01 \x01(\x0b\x32%.ondewo.vtsi.AsteriskConfigsVariablesH\x00\x12\x43\n\x16\x61sterisk_configs_files\x18\x02 \x01(\x0b\x32!.ondewo.vtsi.AsteriskConfigsFilesH\x00\x12\x30\n&asterisk_configs_target_directory_name\x18\x03 \x01(\tH\x00\x12\x15\n\rasterisk_port\x18\x04 \x01(\x05\x42\x18\n\x16\x61sterisk_configs_oneof\"a\n\x18\x43reateVtsiProjectRequest\x12.\n\x0cvtsi_project\x18\x01 \x01(\x0b\x32\x18.ondewo.vtsi.VtsiProject\x12\x15\n\rerror_message\x18\x02 \x01(\t\"b\n\x19\x43reateVtsiProjectResponse\x12.\n\x0cvtsi_project\x18\x01 \x01(\x0b\x32\x18.ondewo.vtsi.VtsiProject\x12\x15\n\rerror_message\x18\x02 \x01(\t\"%\n\x15GetVtsiProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xa5\x01\n\x17ListVtsiProjectsRequest\x12\x37\n\x11vtsi_project_view\x18\x01 \x01(\x0e\x32\x1c.ondewo.vtsi.VtsiProjectView\x12\x12\n\npage_token\x18\x02 \x01(\t\x12=\n\x14vtsi_project_sorting\x18\x03 \x01(\x0b\x32\x1f.ondewo.vtsi.VtsiProjectSorting\"d\n\x18ListVtsiProjectsResponse\x12/\n\rvtsi_projects\x18\x01 \x03(\x0b\x32\x18.ondewo.vtsi.VtsiProject\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xee\x02\n\x12VtsiProjectSorting\x12N\n\rsorting_field\x18\x01 \x01(\x0e\x32\x37.ondewo.vtsi.VtsiProjectSorting.VtsiProjectSortingField\x12\x39\n\x0csorting_mode\x18\x02 \x01(\x0e\x32#.ondewo.vtsi.VtsiProjectSortingMode\"\xcc\x01\n\x17VtsiProjectSortingField\x12\x1b\n\x17NO_VTSI_PROJECT_SORTING\x10\x00\x12\x1d\n\x19SORT_VTSI_PROJECT_BY_NAME\x10\x01\x12%\n!SORT_VTSI_PROJECT_BY_DISPLAY_NAME\x10\x02\x12&\n\"SORT_VTSI_PROJECT_BY_CREATION_DATE\x10\x03\x12&\n\"SORT_VTSI_PROJECT_BY_LAST_MODIFIED\x10\x04\"J\n\x18UpdateVtsiProjectRequest\x12.\n\x0cvtsi_project\x18\x01 \x01(\x0b\x32\x18.ondewo.vtsi.VtsiProject\"@\n\x19UpdateVtsiProjectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\"(\n\x18\x44\x65leteVtsiProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"@\n\x19\x44\x65leteVtsiProjectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\"(\n\x18\x44\x65ployVtsiProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"@\n\x19\x44\x65ployVtsiProjectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\"*\n\x1aUndeployVtsiProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"B\n\x1bUndeployVtsiProjectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t*\x8b\x01\n\x11VtsiProjectStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0e\n\nUNDEPLOYED\x10\x01\x12\x0c\n\x08UPDATING\x10\x02\x12\r\n\tDEPLOYING\x10\x03\x12\x0c\n\x08\x44\x45PLOYED\x10\x04\x12\x0f\n\x0bUNDEPLOYING\x10\x05\x12\x0c\n\x08\x44\x45LETING\x10\x06\x12\x0b\n\x07\x44\x45LETED\x10\x07*7\n\x16VtsiProjectSortingMode\x12\r\n\tASCENDING\x10\x00\x12\x0e\n\nDESCENDING\x10\x01*\x8e\x01\n\x0fVtsiProjectView\x12!\n\x1dVTSI_PROJECT_VIEW_UNSPECIFIED\x10\x00\x12\x1a\n\x16VTSI_PROJECT_VIEW_FULL\x10\x01\x12\x1d\n\x19VTSI_PROJECT_VIEW_SHALLOW\x10\x02\x12\x1d\n\x19VTSI_PROJECT_VIEW_MINIMUM\x10\x03\x32\xb5\x05\n\x08Projects\x12\x62\n\x11\x43reateVtsiProject\x12%.ondewo.vtsi.CreateVtsiProjectRequest\x1a&.ondewo.vtsi.CreateVtsiProjectResponse\x12N\n\x0eGetVtsiProject\x12\".ondewo.vtsi.GetVtsiProjectRequest\x1a\x18.ondewo.vtsi.VtsiProject\x12\x62\n\x11UpdateVtsiProject\x12%.ondewo.vtsi.UpdateVtsiProjectRequest\x1a&.ondewo.vtsi.UpdateVtsiProjectResponse\x12\x62\n\x11\x44\x65leteVtsiProject\x12%.ondewo.vtsi.DeleteVtsiProjectRequest\x1a&.ondewo.vtsi.DeleteVtsiProjectResponse\x12\x62\n\x11\x44\x65ployVtsiProject\x12%.ondewo.vtsi.DeployVtsiProjectRequest\x1a&.ondewo.vtsi.DeployVtsiProjectResponse\x12h\n\x13UndeployVtsiProject\x12\'.ondewo.vtsi.UndeployVtsiProjectRequest\x1a(.ondewo.vtsi.UndeployVtsiProjectResponse\x12_\n\x10ListVtsiProjects\x12$.ondewo.vtsi.ListVtsiProjectsRequest\x1a%.ondewo.vtsi.ListVtsiProjectsResponseb\x06proto3')

_VTSIPROJECTSTATUS = DESCRIPTOR.enum_types_by_name['VtsiProjectStatus']
VtsiProjectStatus = enum_type_wrapper.EnumTypeWrapper(_VTSIPROJECTSTATUS)
_VTSIPROJECTSORTINGMODE = DESCRIPTOR.enum_types_by_name['VtsiProjectSortingMode']
VtsiProjectSortingMode = enum_type_wrapper.EnumTypeWrapper(_VTSIPROJECTSORTINGMODE)
_VTSIPROJECTVIEW = DESCRIPTOR.enum_types_by_name['VtsiProjectView']
VtsiProjectView = enum_type_wrapper.EnumTypeWrapper(_VTSIPROJECTVIEW)
UNSPECIFIED = 0
UNDEPLOYED = 1
UPDATING = 2
DEPLOYING = 3
DEPLOYED = 4
UNDEPLOYING = 5
DELETING = 6
DELETED = 7
ASCENDING = 0
DESCENDING = 1
VTSI_PROJECT_VIEW_UNSPECIFIED = 0
VTSI_PROJECT_VIEW_FULL = 1
VTSI_PROJECT_VIEW_SHALLOW = 2
VTSI_PROJECT_VIEW_MINIMUM = 3


_VTSIPROJECT = DESCRIPTOR.message_types_by_name['VtsiProject']
_ASTERISKCONFIGSVARIABLES = DESCRIPTOR.message_types_by_name['AsteriskConfigsVariables']
_ASTERISKCONFIGSFILES = DESCRIPTOR.message_types_by_name['AsteriskConfigsFiles']
_ASTERISKCONFIGS = DESCRIPTOR.message_types_by_name['AsteriskConfigs']
_CREATEVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['CreateVtsiProjectRequest']
_CREATEVTSIPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['CreateVtsiProjectResponse']
_GETVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['GetVtsiProjectRequest']
_LISTVTSIPROJECTSREQUEST = DESCRIPTOR.message_types_by_name['ListVtsiProjectsRequest']
_LISTVTSIPROJECTSRESPONSE = DESCRIPTOR.message_types_by_name['ListVtsiProjectsResponse']
_VTSIPROJECTSORTING = DESCRIPTOR.message_types_by_name['VtsiProjectSorting']
_UPDATEVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['UpdateVtsiProjectRequest']
_UPDATEVTSIPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateVtsiProjectResponse']
_DELETEVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['DeleteVtsiProjectRequest']
_DELETEVTSIPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['DeleteVtsiProjectResponse']
_DEPLOYVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['DeployVtsiProjectRequest']
_DEPLOYVTSIPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['DeployVtsiProjectResponse']
_UNDEPLOYVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['UndeployVtsiProjectRequest']
_UNDEPLOYVTSIPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['UndeployVtsiProjectResponse']
_VTSIPROJECTSORTING_VTSIPROJECTSORTINGFIELD = _VTSIPROJECTSORTING.enum_types_by_name['VtsiProjectSortingField']
VtsiProject = _reflection.GeneratedProtocolMessageType('VtsiProject', (_message.Message,), {
    'DESCRIPTOR': _VTSIPROJECT,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.VtsiProject)
})
_sym_db.RegisterMessage(VtsiProject)

AsteriskConfigsVariables = _reflection.GeneratedProtocolMessageType('AsteriskConfigsVariables', (_message.Message,), {
    'DESCRIPTOR': _ASTERISKCONFIGSVARIABLES,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.AsteriskConfigsVariables)
})
_sym_db.RegisterMessage(AsteriskConfigsVariables)

AsteriskConfigsFiles = _reflection.GeneratedProtocolMessageType('AsteriskConfigsFiles', (_message.Message,), {
    'DESCRIPTOR': _ASTERISKCONFIGSFILES,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.AsteriskConfigsFiles)
})
_sym_db.RegisterMessage(AsteriskConfigsFiles)

AsteriskConfigs = _reflection.GeneratedProtocolMessageType('AsteriskConfigs', (_message.Message,), {
    'DESCRIPTOR': _ASTERISKCONFIGS,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.AsteriskConfigs)
})
_sym_db.RegisterMessage(AsteriskConfigs)

CreateVtsiProjectRequest = _reflection.GeneratedProtocolMessageType('CreateVtsiProjectRequest', (_message.Message,), {
    'DESCRIPTOR': _CREATEVTSIPROJECTREQUEST,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.CreateVtsiProjectRequest)
})
_sym_db.RegisterMessage(CreateVtsiProjectRequest)

CreateVtsiProjectResponse = _reflection.GeneratedProtocolMessageType('CreateVtsiProjectResponse', (_message.Message,), {
    'DESCRIPTOR': _CREATEVTSIPROJECTRESPONSE,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.CreateVtsiProjectResponse)
})
_sym_db.RegisterMessage(CreateVtsiProjectResponse)

GetVtsiProjectRequest = _reflection.GeneratedProtocolMessageType('GetVtsiProjectRequest', (_message.Message,), {
    'DESCRIPTOR': _GETVTSIPROJECTREQUEST,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetVtsiProjectRequest)
})
_sym_db.RegisterMessage(GetVtsiProjectRequest)

ListVtsiProjectsRequest = _reflection.GeneratedProtocolMessageType('ListVtsiProjectsRequest', (_message.Message,), {
    'DESCRIPTOR': _LISTVTSIPROJECTSREQUEST,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.ListVtsiProjectsRequest)
})
_sym_db.RegisterMessage(ListVtsiProjectsRequest)

ListVtsiProjectsResponse = _reflection.GeneratedProtocolMessageType('ListVtsiProjectsResponse', (_message.Message,), {
    'DESCRIPTOR': _LISTVTSIPROJECTSRESPONSE,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.ListVtsiProjectsResponse)
})
_sym_db.RegisterMessage(ListVtsiProjectsResponse)

VtsiProjectSorting = _reflection.GeneratedProtocolMessageType('VtsiProjectSorting', (_message.Message,), {
    'DESCRIPTOR': _VTSIPROJECTSORTING,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.VtsiProjectSorting)
})
_sym_db.RegisterMessage(VtsiProjectSorting)

UpdateVtsiProjectRequest = _reflection.GeneratedProtocolMessageType('UpdateVtsiProjectRequest', (_message.Message,), {
    'DESCRIPTOR': _UPDATEVTSIPROJECTREQUEST,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.UpdateVtsiProjectRequest)
})
_sym_db.RegisterMessage(UpdateVtsiProjectRequest)

UpdateVtsiProjectResponse = _reflection.GeneratedProtocolMessageType('UpdateVtsiProjectResponse', (_message.Message,), {
    'DESCRIPTOR': _UPDATEVTSIPROJECTRESPONSE,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.UpdateVtsiProjectResponse)
})
_sym_db.RegisterMessage(UpdateVtsiProjectResponse)

DeleteVtsiProjectRequest = _reflection.GeneratedProtocolMessageType('DeleteVtsiProjectRequest', (_message.Message,), {
    'DESCRIPTOR': _DELETEVTSIPROJECTREQUEST,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.DeleteVtsiProjectRequest)
})
_sym_db.RegisterMessage(DeleteVtsiProjectRequest)

DeleteVtsiProjectResponse = _reflection.GeneratedProtocolMessageType('DeleteVtsiProjectResponse', (_message.Message,), {
    'DESCRIPTOR': _DELETEVTSIPROJECTRESPONSE,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.DeleteVtsiProjectResponse)
})
_sym_db.RegisterMessage(DeleteVtsiProjectResponse)

DeployVtsiProjectRequest = _reflection.GeneratedProtocolMessageType('DeployVtsiProjectRequest', (_message.Message,), {
    'DESCRIPTOR': _DEPLOYVTSIPROJECTREQUEST,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.DeployVtsiProjectRequest)
})
_sym_db.RegisterMessage(DeployVtsiProjectRequest)

DeployVtsiProjectResponse = _reflection.GeneratedProtocolMessageType('DeployVtsiProjectResponse', (_message.Message,), {
    'DESCRIPTOR': _DEPLOYVTSIPROJECTRESPONSE,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.DeployVtsiProjectResponse)
})
_sym_db.RegisterMessage(DeployVtsiProjectResponse)

UndeployVtsiProjectRequest = _reflection.GeneratedProtocolMessageType('UndeployVtsiProjectRequest', (_message.Message,), {
    'DESCRIPTOR': _UNDEPLOYVTSIPROJECTREQUEST,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.UndeployVtsiProjectRequest)
})
_sym_db.RegisterMessage(UndeployVtsiProjectRequest)

UndeployVtsiProjectResponse = _reflection.GeneratedProtocolMessageType('UndeployVtsiProjectResponse', (_message.Message,), {
    'DESCRIPTOR': _UNDEPLOYVTSIPROJECTRESPONSE,
    '__module__': 'ondewo.vtsi.projects_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.vtsi.UndeployVtsiProjectResponse)
})
_sym_db.RegisterMessage(UndeployVtsiProjectResponse)

_PROJECTS = DESCRIPTOR.services_by_name['Projects']
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _VTSIPROJECTSTATUS._serialized_start=2498
    _VTSIPROJECTSTATUS._serialized_end=2637
    _VTSIPROJECTSORTINGMODE._serialized_start=2639
    _VTSIPROJECTSORTINGMODE._serialized_end=2694
    _VTSIPROJECTVIEW._serialized_start=2697
    _VTSIPROJECTVIEW._serialized_end=2839
    _VTSIPROJECT._serialized_start=107
    _VTSIPROJECT._serialized_end=528
    _ASTERISKCONFIGSVARIABLES._serialized_start=531
    _ASTERISKCONFIGSVARIABLES._serialized_end=724
    _ASTERISKCONFIGSFILES._serialized_start=727
    _ASTERISKCONFIGSFILES._serialized_end=883
    _ASTERISKCONFIGS._serialized_start=886
    _ASTERISKCONFIGS._serialized_end=1148
    _CREATEVTSIPROJECTREQUEST._serialized_start=1150
    _CREATEVTSIPROJECTREQUEST._serialized_end=1247
    _CREATEVTSIPROJECTRESPONSE._serialized_start=1249
    _CREATEVTSIPROJECTRESPONSE._serialized_end=1347
    _GETVTSIPROJECTREQUEST._serialized_start=1349
    _GETVTSIPROJECTREQUEST._serialized_end=1386
    _LISTVTSIPROJECTSREQUEST._serialized_start=1389
    _LISTVTSIPROJECTSREQUEST._serialized_end=1554
    _LISTVTSIPROJECTSRESPONSE._serialized_start=1556
    _LISTVTSIPROJECTSRESPONSE._serialized_end=1656
    _VTSIPROJECTSORTING._serialized_start=1659
    _VTSIPROJECTSORTING._serialized_end=2025
    _VTSIPROJECTSORTING_VTSIPROJECTSORTINGFIELD._serialized_start=1821
    _VTSIPROJECTSORTING_VTSIPROJECTSORTINGFIELD._serialized_end=2025
    _UPDATEVTSIPROJECTREQUEST._serialized_start=2027
    _UPDATEVTSIPROJECTREQUEST._serialized_end=2101
    _UPDATEVTSIPROJECTRESPONSE._serialized_start=2103
    _UPDATEVTSIPROJECTRESPONSE._serialized_end=2167
    _DELETEVTSIPROJECTREQUEST._serialized_start=2169
    _DELETEVTSIPROJECTREQUEST._serialized_end=2209
    _DELETEVTSIPROJECTRESPONSE._serialized_start=2211
    _DELETEVTSIPROJECTRESPONSE._serialized_end=2275
    _DEPLOYVTSIPROJECTREQUEST._serialized_start=2277
    _DEPLOYVTSIPROJECTREQUEST._serialized_end=2317
    _DEPLOYVTSIPROJECTRESPONSE._serialized_start=2319
    _DEPLOYVTSIPROJECTRESPONSE._serialized_end=2383
    _UNDEPLOYVTSIPROJECTREQUEST._serialized_start=2385
    _UNDEPLOYVTSIPROJECTREQUEST._serialized_end=2427
    _UNDEPLOYVTSIPROJECTRESPONSE._serialized_start=2429
    _UNDEPLOYVTSIPROJECTRESPONSE._serialized_end=2495
    _PROJECTS._serialized_start=2842
    _PROJECTS._serialized_end=3535
# @@protoc_insertion_point(module_scope)
