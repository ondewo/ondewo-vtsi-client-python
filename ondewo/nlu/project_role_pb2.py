# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/nlu/project_role.proto
"""Generated protocol buffer code."""
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dondewo/nlu/project_role.proto\x12\nondewo.nlu\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1bgoogle/protobuf/empty.proto\"A\n\x0bProjectRole\x12\x0f\n\x07role_id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bpermissions\x18\x03 \x03(\t\"\x89\x01\n\x18\x43reateProjectRoleRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12%\n\x04role\x18\x02 \x01(\x0b\x32\x17.ondewo.nlu.ProjectRole\x12\x36\n\x11project_role_view\x18\x03 \x01(\x0e\x32\x1b.ondewo.nlu.ProjectRoleView\"\xba\x01\n\x18UpdateProjectRoleRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12%\n\x04role\x18\x02 \x01(\x0b\x32\x17.ondewo.nlu.ProjectRole\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x36\n\x11project_role_view\x18\x04 \x01(\x0e\x32\x1b.ondewo.nlu.ProjectRoleView\"\xa2\x01\n\x15GetProjectRoleRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\x07role_id\x18\x02 \x01(\rH\x00\x12\x13\n\trole_name\x18\x03 \x01(\tH\x00\x12\x36\n\x11project_role_view\x18\x04 \x01(\x0e\x32\x1b.ondewo.nlu.ProjectRoleViewB\x19\n\x17project_role_identifier\";\n\x18\x44\x65leteProjectRoleRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0f\n\x07role_id\x18\x02 \x01(\r\"u\n\x17ListProjectRolesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x36\n\x11project_role_view\x18\x03 \x01(\x0e\x32\x1b.ondewo.nlu.ProjectRoleView\"c\n\x18ListProjectRolesResponse\x12.\n\rproject_roles\x18\x01 \x03(\x0b\x32\x17.ondewo.nlu.ProjectRole\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*\x95\x01\n\x12\x44\x65\x66\x61ultProjectRole\x12\x17\n\x13PROJECT_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROJECT_USER\x10\x01\x12\x14\n\x10PROJECT_EXECUTOR\x10\x02\x12\x15\n\x11PROJECT_DEVELOPER\x10\x03\x12\x11\n\rPROJECT_ADMIN\x10\x04\x12\x14\n\x10PROJECT_INACTIVE\x10\x05*o\n\x0fProjectRoleView\x12!\n\x1dPROJECT_ROLE_VIEW_UNSPECIFIED\x10\x00\x12\x1d\n\x19PROJECT_ROLE_VIEW_SHALLOW\x10\x01\x12\x1a\n\x16PROJECT_ROLE_VIEW_FULL\x10\x02\x32\xe2\x05\n\x0cProjectRoles\x12\x8a\x01\n\x11\x43reateProjectRole\x12$.ondewo.nlu.CreateProjectRoleRequest\x1a\x17.ondewo.nlu.ProjectRole\"6\x82\xd3\xe4\x93\x02\x30\"+/v2/{parent=projects/*/agent}/project_roles:\x01*\x12\x8d\x01\n\x0eGetProjectRole\x12!.ondewo.nlu.GetProjectRoleRequest\x1a\x17.ondewo.nlu.ProjectRole\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/v2/{parent=projects/*/agent}/project_roles/{role_id=*}\x12\x92\x01\n\x11\x44\x65leteProjectRole\x12$.ondewo.nlu.DeleteProjectRoleRequest\x1a\x16.google.protobuf.Empty\"?\x82\xd3\xe4\x93\x02\x39*7/v2/{parent=projects/*/agent}/project_roles/{role_id=*}\x12\x8a\x01\n\x11UpdateProjectRole\x12$.ondewo.nlu.UpdateProjectRoleRequest\x1a\x17.ondewo.nlu.ProjectRole\"6\x82\xd3\xe4\x93\x02\x30\x32+/v2/{parent=projects/*/agent}/project_roles:\x01*\x12\x92\x01\n\x10ListProjectRoles\x12#.ondewo.nlu.ListProjectRolesRequest\x1a$.ondewo.nlu.ListProjectRolesResponse\"3\x82\xd3\xe4\x93\x02-\x12+/v2/{parent=projects/*/agent}/project_rolesb\x06proto3')

_DEFAULTPROJECTROLE = DESCRIPTOR.enum_types_by_name['DefaultProjectRole']
DefaultProjectRole = enum_type_wrapper.EnumTypeWrapper(_DEFAULTPROJECTROLE)
_PROJECTROLEVIEW = DESCRIPTOR.enum_types_by_name['ProjectRoleView']
ProjectRoleView = enum_type_wrapper.EnumTypeWrapper(_PROJECTROLEVIEW)
PROJECT_UNSPECIFIED = 0
PROJECT_USER = 1
PROJECT_EXECUTOR = 2
PROJECT_DEVELOPER = 3
PROJECT_ADMIN = 4
PROJECT_INACTIVE = 5
PROJECT_ROLE_VIEW_UNSPECIFIED = 0
PROJECT_ROLE_VIEW_SHALLOW = 1
PROJECT_ROLE_VIEW_FULL = 2


_PROJECTROLE = DESCRIPTOR.message_types_by_name['ProjectRole']
_CREATEPROJECTROLEREQUEST = DESCRIPTOR.message_types_by_name['CreateProjectRoleRequest']
_UPDATEPROJECTROLEREQUEST = DESCRIPTOR.message_types_by_name['UpdateProjectRoleRequest']
_GETPROJECTROLEREQUEST = DESCRIPTOR.message_types_by_name['GetProjectRoleRequest']
_DELETEPROJECTROLEREQUEST = DESCRIPTOR.message_types_by_name['DeleteProjectRoleRequest']
_LISTPROJECTROLESREQUEST = DESCRIPTOR.message_types_by_name['ListProjectRolesRequest']
_LISTPROJECTROLESRESPONSE = DESCRIPTOR.message_types_by_name['ListProjectRolesResponse']
ProjectRole = _reflection.GeneratedProtocolMessageType('ProjectRole', (_message.Message,), {
    'DESCRIPTOR': _PROJECTROLE,
    '__module__': 'ondewo.nlu.project_role_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.ProjectRole)
})
_sym_db.RegisterMessage(ProjectRole)

CreateProjectRoleRequest = _reflection.GeneratedProtocolMessageType('CreateProjectRoleRequest', (_message.Message,), {
    'DESCRIPTOR': _CREATEPROJECTROLEREQUEST,
    '__module__': 'ondewo.nlu.project_role_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.CreateProjectRoleRequest)
})
_sym_db.RegisterMessage(CreateProjectRoleRequest)

UpdateProjectRoleRequest = _reflection.GeneratedProtocolMessageType('UpdateProjectRoleRequest', (_message.Message,), {
    'DESCRIPTOR': _UPDATEPROJECTROLEREQUEST,
    '__module__': 'ondewo.nlu.project_role_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.UpdateProjectRoleRequest)
})
_sym_db.RegisterMessage(UpdateProjectRoleRequest)

GetProjectRoleRequest = _reflection.GeneratedProtocolMessageType('GetProjectRoleRequest', (_message.Message,), {
    'DESCRIPTOR': _GETPROJECTROLEREQUEST,
    '__module__': 'ondewo.nlu.project_role_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.GetProjectRoleRequest)
})
_sym_db.RegisterMessage(GetProjectRoleRequest)

DeleteProjectRoleRequest = _reflection.GeneratedProtocolMessageType('DeleteProjectRoleRequest', (_message.Message,), {
    'DESCRIPTOR': _DELETEPROJECTROLEREQUEST,
    '__module__': 'ondewo.nlu.project_role_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.DeleteProjectRoleRequest)
})
_sym_db.RegisterMessage(DeleteProjectRoleRequest)

ListProjectRolesRequest = _reflection.GeneratedProtocolMessageType('ListProjectRolesRequest', (_message.Message,), {
    'DESCRIPTOR': _LISTPROJECTROLESREQUEST,
    '__module__': 'ondewo.nlu.project_role_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.ListProjectRolesRequest)
})
_sym_db.RegisterMessage(ListProjectRolesRequest)

ListProjectRolesResponse = _reflection.GeneratedProtocolMessageType('ListProjectRolesResponse', (_message.Message,), {
    'DESCRIPTOR': _LISTPROJECTROLESRESPONSE,
    '__module__': 'ondewo.nlu.project_role_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.nlu.ListProjectRolesResponse)
})
_sym_db.RegisterMessage(ListProjectRolesResponse)

_PROJECTROLES = DESCRIPTOR.services_by_name['ProjectRoles']
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _PROJECTROLES.methods_by_name['CreateProjectRole']._options = None
    _PROJECTROLES.methods_by_name['CreateProjectRole']._serialized_options = b'\202\323\344\223\0020\"+/v2/{parent=projects/*/agent}/project_roles:\001*'
    _PROJECTROLES.methods_by_name['GetProjectRole']._options = None
    _PROJECTROLES.methods_by_name['GetProjectRole']._serialized_options = b'\202\323\344\223\0029\0227/v2/{parent=projects/*/agent}/project_roles/{role_id=*}'
    _PROJECTROLES.methods_by_name['DeleteProjectRole']._options = None
    _PROJECTROLES.methods_by_name['DeleteProjectRole']._serialized_options = b'\202\323\344\223\0029*7/v2/{parent=projects/*/agent}/project_roles/{role_id=*}'
    _PROJECTROLES.methods_by_name['UpdateProjectRole']._options = None
    _PROJECTROLES.methods_by_name['UpdateProjectRole']._serialized_options = b'\202\323\344\223\00202+/v2/{parent=projects/*/agent}/project_roles:\001*'
    _PROJECTROLES.methods_by_name['ListProjectRoles']._options = None
    _PROJECTROLES.methods_by_name['ListProjectRoles']._serialized_options = b'\202\323\344\223\002-\022+/v2/{parent=projects/*/agent}/project_roles'
    _DEFAULTPROJECTROLE._serialized_start=981
    _DEFAULTPROJECTROLE._serialized_end=1130
    _PROJECTROLEVIEW._serialized_start=1132
    _PROJECTROLEVIEW._serialized_end=1243
    _PROJECTROLE._serialized_start=138
    _PROJECTROLE._serialized_end=203
    _CREATEPROJECTROLEREQUEST._serialized_start=206
    _CREATEPROJECTROLEREQUEST._serialized_end=343
    _UPDATEPROJECTROLEREQUEST._serialized_start=346
    _UPDATEPROJECTROLEREQUEST._serialized_end=532
    _GETPROJECTROLEREQUEST._serialized_start=535
    _GETPROJECTROLEREQUEST._serialized_end=697
    _DELETEPROJECTROLEREQUEST._serialized_start=699
    _DELETEPROJECTROLEREQUEST._serialized_end=758
    _LISTPROJECTROLESREQUEST._serialized_start=760
    _LISTPROJECTROLESREQUEST._serialized_end=877
    _LISTPROJECTROLESRESPONSE._serialized_start=879
    _LISTPROJECTROLESRESPONSE._serialized_end=978
    _PROJECTROLES._serialized_start=1246
    _PROJECTROLES._serialized_end=1984
# @@protoc_insertion_point(module_scope)
