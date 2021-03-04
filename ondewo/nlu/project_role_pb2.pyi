# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.field_mask_pb2 import (
    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class DefaultProjectRole(builtin___int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> 'DefaultProjectRole': ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List['DefaultProjectRole']: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, 'DefaultProjectRole']]: ...
    PROJECT_UNSPECIFIED = typing___cast('DefaultProjectRole', 0)
    PROJECT_USER = typing___cast('DefaultProjectRole', 1)
    PROJECT_EXECUTOR = typing___cast('DefaultProjectRole', 2)
    PROJECT_DEVELOPER = typing___cast('DefaultProjectRole', 3)
    PROJECT_ADMIN = typing___cast('DefaultProjectRole', 4)
    PROJECT_INACTIVE = typing___cast('DefaultProjectRole', 5)
PROJECT_UNSPECIFIED = typing___cast('DefaultProjectRole', 0)
PROJECT_USER = typing___cast('DefaultProjectRole', 1)
PROJECT_EXECUTOR = typing___cast('DefaultProjectRole', 2)
PROJECT_DEVELOPER = typing___cast('DefaultProjectRole', 3)
PROJECT_ADMIN = typing___cast('DefaultProjectRole', 4)
PROJECT_INACTIVE = typing___cast('DefaultProjectRole', 5)
global___DefaultProjectRole = DefaultProjectRole

class ProjectRoleView(builtin___int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> 'ProjectRoleView': ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List['ProjectRoleView']: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, 'ProjectRoleView']]: ...
    PROJECT_ROLE_VIEW_UNSPECIFIED = typing___cast('ProjectRoleView', 0)
    PROJECT_ROLE_VIEW_SHALLOW = typing___cast('ProjectRoleView', 1)
    PROJECT_ROLE_VIEW_FULL = typing___cast('ProjectRoleView', 2)
PROJECT_ROLE_VIEW_UNSPECIFIED = typing___cast('ProjectRoleView', 0)
PROJECT_ROLE_VIEW_SHALLOW = typing___cast('ProjectRoleView', 1)
PROJECT_ROLE_VIEW_FULL = typing___cast('ProjectRoleView', 2)
global___ProjectRoleView = ProjectRoleView

class ProjectRole(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    role_id = ... # type: builtin___int
    name = ... # type: typing___Text
    permissions = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        role_id : typing___Optional[builtin___int] = None,
        name : typing___Optional[typing___Text] = None,
        permissions : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ProjectRole: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ProjectRole: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"permissions",b"permissions",u"role_id",b"role_id"]) -> None: ...
global___ProjectRole = ProjectRole

class CreateProjectRoleRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    parent = ... # type: typing___Text
    project_role_view = ... # type: global___ProjectRoleView

    @property
    def role(self) -> global___ProjectRole: ...

    def __init__(self,
        *,
        parent : typing___Optional[typing___Text] = None,
        role : typing___Optional[global___ProjectRole] = None,
        project_role_view : typing___Optional[global___ProjectRoleView] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateProjectRoleRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateProjectRoleRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"role",b"role"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"parent",b"parent",u"project_role_view",b"project_role_view",u"role",b"role"]) -> None: ...
global___CreateProjectRoleRequest = CreateProjectRoleRequest

class UpdateProjectRoleRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    parent = ... # type: typing___Text
    project_role_view = ... # type: global___ProjectRoleView

    @property
    def role(self) -> global___ProjectRole: ...

    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...

    def __init__(self,
        *,
        parent : typing___Optional[typing___Text] = None,
        role : typing___Optional[global___ProjectRole] = None,
        update_mask : typing___Optional[google___protobuf___field_mask_pb2___FieldMask] = None,
        project_role_view : typing___Optional[global___ProjectRoleView] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateProjectRoleRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateProjectRoleRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"role",b"role",u"update_mask",b"update_mask"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"parent",b"parent",u"project_role_view",b"project_role_view",u"role",b"role",u"update_mask",b"update_mask"]) -> None: ...
global___UpdateProjectRoleRequest = UpdateProjectRoleRequest

class GetProjectRoleRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    parent = ... # type: typing___Text
    role_id = ... # type: builtin___int
    role_name = ... # type: typing___Text
    project_role_view = ... # type: global___ProjectRoleView

    def __init__(self,
        *,
        parent : typing___Optional[typing___Text] = None,
        role_id : typing___Optional[builtin___int] = None,
        role_name : typing___Optional[typing___Text] = None,
        project_role_view : typing___Optional[global___ProjectRoleView] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetProjectRoleRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetProjectRoleRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"project_role_identifier",b"project_role_identifier",u"role_id",b"role_id",u"role_name",b"role_name"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"parent",b"parent",u"project_role_identifier",b"project_role_identifier",u"project_role_view",b"project_role_view",u"role_id",b"role_id",u"role_name",b"role_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"project_role_identifier",b"project_role_identifier"]) -> typing_extensions___Literal["role_id","role_name"]: ...
global___GetProjectRoleRequest = GetProjectRoleRequest

class DeleteProjectRoleRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    parent = ... # type: typing___Text
    role_id = ... # type: builtin___int

    def __init__(self,
        *,
        parent : typing___Optional[typing___Text] = None,
        role_id : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DeleteProjectRoleRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeleteProjectRoleRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"parent",b"parent",u"role_id",b"role_id"]) -> None: ...
global___DeleteProjectRoleRequest = DeleteProjectRoleRequest

class ListProjectRolesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    parent = ... # type: typing___Text
    page_token = ... # type: typing___Text
    project_role_view = ... # type: global___ProjectRoleView

    def __init__(self,
        *,
        parent : typing___Optional[typing___Text] = None,
        page_token : typing___Optional[typing___Text] = None,
        project_role_view : typing___Optional[global___ProjectRoleView] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListProjectRolesRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListProjectRolesRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"page_token",b"page_token",u"parent",b"parent",u"project_role_view",b"project_role_view"]) -> None: ...
global___ListProjectRolesRequest = ListProjectRolesRequest

class ListProjectRolesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    next_page_token = ... # type: typing___Text

    @property
    def project_roles(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___ProjectRole]: ...

    def __init__(self,
        *,
        project_roles : typing___Optional[typing___Iterable[global___ProjectRole]] = None,
        next_page_token : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListProjectRolesResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListProjectRolesResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"next_page_token",b"next_page_token",u"project_roles",b"project_roles"]) -> None: ...
global___ListProjectRolesResponse = ListProjectRolesResponse