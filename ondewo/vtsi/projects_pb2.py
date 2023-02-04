# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/vtsi/projects.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aondewo/vtsi/projects.proto\x12\x0bondewo.vtsi\"\x95\x01\n\x0bVtsiProject\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0bmax_callers\x18\x03 \x01(\x05\x12\x15\n\rmax_listeners\x18\x04 \x01(\x05\x12\x36\n\x10\x61sterisk_configs\x18\x05 \x01(\x0b\x32\x1c.ondewo.vtsi.AsteriskConfigs\"\xc1\x01\n\x18\x41steriskConfigsVariables\x12\x1a\n\x12sip_trunk_username\x18\x01 \x01(\t\x12\x1a\n\x12sip_trunk_password\x18\x02 \x01(\t\x12\x16\n\x0esip_trunk_host\x18\x03 \x01(\t\x12\x17\n\x0ftransfer_number\x18\x04 \x01(\t\x12\x1c\n\x14transfer_number_host\x18\x05 \x01(\t\x12\x1e\n\x16sip_trunk_phone_number\x18\x06 \x01(\t\"\x9c\x01\n\x14\x41steriskConfigsFiles\x12\x1c\n\x14sip_conf_file_string\x18\x01 \x01(\t\x12#\n\x1b\x65xtensions_conf_file_string\x18\x02 \x01(\t\x12\x1f\n\x17queues_conf_file_string\x18\x03 \x01(\t\x12 \n\x18modules_conf_file_string\x18\x04 \x01(\t\"\x86\x02\n\x0f\x41steriskConfigs\x12K\n\x1a\x61sterisk_configs_variables\x18\x01 \x01(\x0b\x32%.ondewo.vtsi.AsteriskConfigsVariablesH\x00\x12\x43\n\x16\x61sterisk_configs_files\x18\x02 \x01(\x0b\x32!.ondewo.vtsi.AsteriskConfigsFilesH\x00\x12\x30\n&asterisk_configs_target_directory_name\x18\x03 \x01(\tH\x00\x12\x15\n\rasterisk_port\x18\x04 \x01(\x05\x42\x18\n\x16\x61sterisk_configs_oneof\"a\n\x18\x43reateVtsiProjectRequest\x12.\n\x0cvtsi_project\x18\x01 \x01(\x0b\x32\x18.ondewo.vtsi.VtsiProject\x12\x15\n\rerror_message\x18\x02 \x01(\t\"b\n\x19\x43reateVtsiProjectResponse\x12.\n\x0cvtsi_project\x18\x01 \x01(\x0b\x32\x18.ondewo.vtsi.VtsiProject\x12\x15\n\rerror_message\x18\x02 \x01(\t\"%\n\x15GetVtsiProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"J\n\x18UpdateVtsiProjectRequest\x12.\n\x0cvtsi_project\x18\x01 \x01(\x0b\x32\x18.ondewo.vtsi.VtsiProject\"@\n\x19UpdateVtsiProjectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\"(\n\x18\x44\x65leteVtsiProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"@\n\x19\x44\x65leteVtsiProjectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\"(\n\x18\x44\x65ployVtsiProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"@\n\x19\x44\x65ployVtsiProjectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\"*\n\x1aUndeployVtsiProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"B\n\x1bUndeployVtsiProjectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t2\xd4\x04\n\x08Projects\x12\x62\n\x11\x43reateVtsiProject\x12%.ondewo.vtsi.CreateVtsiProjectRequest\x1a&.ondewo.vtsi.CreateVtsiProjectResponse\x12N\n\x0eGetVtsiProject\x12\".ondewo.vtsi.GetVtsiProjectRequest\x1a\x18.ondewo.vtsi.VtsiProject\x12\x62\n\x11UpdateVtsiProject\x12%.ondewo.vtsi.UpdateVtsiProjectRequest\x1a&.ondewo.vtsi.UpdateVtsiProjectResponse\x12\x62\n\x11\x44\x65leteVtsiProject\x12%.ondewo.vtsi.DeleteVtsiProjectRequest\x1a&.ondewo.vtsi.DeleteVtsiProjectResponse\x12\x62\n\x11\x44\x65ployVtsiProject\x12%.ondewo.vtsi.DeployVtsiProjectRequest\x1a&.ondewo.vtsi.DeployVtsiProjectResponse\x12h\n\x13UndeployVtsiProject\x12\'.ondewo.vtsi.UndeployVtsiProjectRequest\x1a(.ondewo.vtsi.UndeployVtsiProjectResponseb\x06proto3')


_VTSIPROJECT = DESCRIPTOR.message_types_by_name['VtsiProject']
_ASTERISKCONFIGSVARIABLES = DESCRIPTOR.message_types_by_name['AsteriskConfigsVariables']
_ASTERISKCONFIGSFILES = DESCRIPTOR.message_types_by_name['AsteriskConfigsFiles']
_ASTERISKCONFIGS = DESCRIPTOR.message_types_by_name['AsteriskConfigs']
_CREATEVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['CreateVtsiProjectRequest']
_CREATEVTSIPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['CreateVtsiProjectResponse']
_GETVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['GetVtsiProjectRequest']
_UPDATEVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['UpdateVtsiProjectRequest']
_UPDATEVTSIPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateVtsiProjectResponse']
_DELETEVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['DeleteVtsiProjectRequest']
_DELETEVTSIPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['DeleteVtsiProjectResponse']
_DEPLOYVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['DeployVtsiProjectRequest']
_DEPLOYVTSIPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['DeployVtsiProjectResponse']
_UNDEPLOYVTSIPROJECTREQUEST = DESCRIPTOR.message_types_by_name['UndeployVtsiProjectRequest']
_UNDEPLOYVTSIPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['UndeployVtsiProjectResponse']
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
    _VTSIPROJECT._serialized_start = 44
    _VTSIPROJECT._serialized_end = 193
    _ASTERISKCONFIGSVARIABLES._serialized_start = 196
    _ASTERISKCONFIGSVARIABLES._serialized_end = 389
    _ASTERISKCONFIGSFILES._serialized_start = 392
    _ASTERISKCONFIGSFILES._serialized_end = 548
    _ASTERISKCONFIGS._serialized_start = 551
    _ASTERISKCONFIGS._serialized_end = 813
    _CREATEVTSIPROJECTREQUEST._serialized_start = 815
    _CREATEVTSIPROJECTREQUEST._serialized_end = 912
    _CREATEVTSIPROJECTRESPONSE._serialized_start = 914
    _CREATEVTSIPROJECTRESPONSE._serialized_end = 1012
    _GETVTSIPROJECTREQUEST._serialized_start = 1014
    _GETVTSIPROJECTREQUEST._serialized_end = 1051
    _UPDATEVTSIPROJECTREQUEST._serialized_start = 1053
    _UPDATEVTSIPROJECTREQUEST._serialized_end = 1127
    _UPDATEVTSIPROJECTRESPONSE._serialized_start = 1129
    _UPDATEVTSIPROJECTRESPONSE._serialized_end = 1193
    _DELETEVTSIPROJECTREQUEST._serialized_start = 1195
    _DELETEVTSIPROJECTREQUEST._serialized_end = 1235
    _DELETEVTSIPROJECTRESPONSE._serialized_start = 1237
    _DELETEVTSIPROJECTRESPONSE._serialized_end = 1301
    _DEPLOYVTSIPROJECTREQUEST._serialized_start = 1303
    _DEPLOYVTSIPROJECTREQUEST._serialized_end = 1343
    _DEPLOYVTSIPROJECTRESPONSE._serialized_start = 1345
    _DEPLOYVTSIPROJECTRESPONSE._serialized_end = 1409
    _UNDEPLOYVTSIPROJECTREQUEST._serialized_start = 1411
    _UNDEPLOYVTSIPROJECTREQUEST._serialized_end = 1453
    _UNDEPLOYVTSIPROJECTRESPONSE._serialized_start = 1455
    _UNDEPLOYVTSIPROJECTRESPONSE._serialized_end = 1521
    _PROJECTS._serialized_start = 1524
    _PROJECTS._serialized_end = 2120
# @@protoc_insertion_point(module_scope)