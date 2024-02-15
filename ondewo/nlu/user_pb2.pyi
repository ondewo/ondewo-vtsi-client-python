"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2020-2023 ONDEWO GmbH

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import ondewo.nlu.common_pb2
import ondewo.nlu.project_role_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DefaultServerRole:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DefaultServerRoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DefaultServerRole.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SERVER_UNSPECIFIED: _DefaultServerRole.ValueType  # 0
    """unspecified server role"""
    SERVER_USER: _DefaultServerRole.ValueType  # 1
    """read-only access"""
    SERVER_MANAGER: _DefaultServerRole.ValueType  # 2
    """SERVER_USER's permissions + CRUD of projects and Users"""
    SERVER_ADMIN: _DefaultServerRole.ValueType  # 3
    """this role can do everything"""
    SERVER_INACTIVE: _DefaultServerRole.ValueType  # 4
    """this role can do nothing. Used to set a user as inactive in the server."""

class DefaultServerRole(_DefaultServerRole, metaclass=_DefaultServerRoleEnumTypeWrapper):
    """Structure of server role"""

SERVER_UNSPECIFIED: DefaultServerRole.ValueType  # 0
"""unspecified server role"""
SERVER_USER: DefaultServerRole.ValueType  # 1
"""read-only access"""
SERVER_MANAGER: DefaultServerRole.ValueType  # 2
"""SERVER_USER's permissions + CRUD of projects and Users"""
SERVER_ADMIN: DefaultServerRole.ValueType  # 3
"""this role can do everything"""
SERVER_INACTIVE: DefaultServerRole.ValueType  # 4
"""this role can do nothing. Used to set a user as inactive in the server."""
global___DefaultServerRole = DefaultServerRole

@typing_extensions.final
class User(google.protobuf.message.Message):
    """User messages

    this message contains all the fields that required for user db
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ID_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    SERVER_ROLE_ID_FIELD_NUMBER: builtins.int
    USER_EMAIL_FIELD_NUMBER: builtins.int
    USER_PROFILE_PICTURE_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    MODIFIED_BY_FIELD_NUMBER: builtins.int
    user_id: builtins.str
    """when creating user user_id is empty, then it will be generated on creation time on backend"""
    display_name: builtins.str
    """Optional field display_name is the name that will be used on the frontend to interact with the user
    it shouldn't be unique. If not provided user_name will also be used as display name
    """
    server_role_id: builtins.int
    """server role type of the given user. If nothing is provided, the user is set to USER (minimum access)"""
    user_email: builtins.str
    """user e-mail should be a valid e-mail and unique"""
    user_profile_picture: builtins.bytes
    """user profile picture"""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation date and time. Read-only field."""
    @property
    def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Modification date and time. Read-only field."""
    created_by: builtins.str
    """User id in form of a valid UUID."""
    modified_by: builtins.str
    """User id in form of a valid UUID."""
    def __init__(
        self,
        *,
        user_id: builtins.str = ...,
        display_name: builtins.str = ...,
        server_role_id: builtins.int = ...,
        user_email: builtins.str = ...,
        user_profile_picture: builtins.bytes = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_by: builtins.str = ...,
        modified_by: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "modified_at", b"modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "created_by", b"created_by", "display_name", b"display_name", "modified_at", b"modified_at", "modified_by", b"modified_by", "server_role_id", b"server_role_id", "user_email", b"user_email", "user_id", b"user_id", "user_profile_picture", b"user_profile_picture"]) -> None: ...

global___User = User

@typing_extensions.final
class UserInfo(google.protobuf.message.Message):
    """This message contains information about user"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ProjectRolesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> ondewo.nlu.project_role_pb2.ProjectRole: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: ondewo.nlu.project_role_pb2.ProjectRole | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    USER_FIELD_NUMBER: builtins.int
    PROJECT_ROLES_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """user object"""
    @property
    def project_roles(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, ondewo.nlu.project_role_pb2.ProjectRole]:
        """If in GetUser, ListUser requests UserView is FULL, then the mapping is additionally provided
        of parent of the project and corresponding ProjectRole of the user
        """
    def __init__(
        self,
        *,
        user: global___User | None = ...,
        project_roles: collections.abc.Mapping[builtins.str, ondewo.nlu.project_role_pb2.ProjectRole] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["project_roles", b"project_roles", "user", b"user"]) -> None: ...

global___UserInfo = UserInfo

@typing_extensions.final
class CreateUserRequest(google.protobuf.message.Message):
    """Request to create user"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """user_id in the User message should be given, if empty will throw an error in the backend"""
    password: builtins.str
    """password"""
    def __init__(
        self,
        *,
        user: global___User | None = ...,
        password: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["password", b"password", "user", b"user"]) -> None: ...

global___CreateUserRequest = CreateUserRequest

@typing_extensions.final
class UpdateUserRequest(google.protobuf.message.Message):
    """Request to update user"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """user_id in the User message should be given, if empty will throw an error in the backend
        password and other fields in the User are optional. Only the fields to be updated should be provided
        """
    password: builtins.str
    """Password of the user"""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. The mask to control which fields get updated."""
    def __init__(
        self,
        *,
        user: global___User | None = ...,
        password: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask", b"update_mask", "user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["password", b"password", "update_mask", b"update_mask", "user", b"user"]) -> None: ...

global___UpdateUserRequest = UpdateUserRequest

@typing_extensions.final
class GetUserRequest(google.protobuf.message.Message):
    """Request to get user"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ID_FIELD_NUMBER: builtins.int
    USER_EMAIL_FIELD_NUMBER: builtins.int
    user_id: builtins.str
    """the user is identified by user id"""
    user_email: builtins.str
    """the user can identified by their email"""
    def __init__(
        self,
        *,
        user_id: builtins.str = ...,
        user_email: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user_email", b"user_email", "user_id", b"user_id", "user_identifier", b"user_identifier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["user_email", b"user_email", "user_id", b"user_id", "user_identifier", b"user_identifier"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["user_identifier", b"user_identifier"]) -> typing_extensions.Literal["user_id", "user_email"] | None: ...

global___GetUserRequest = GetUserRequest

@typing_extensions.final
class DeleteUserRequest(google.protobuf.message.Message):
    """Request to delete user"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ID_FIELD_NUMBER: builtins.int
    user_id: builtins.str
    """user is identified by user id, if empty will throw an error in the backend"""
    def __init__(
        self,
        *,
        user_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["user_id", b"user_id"]) -> None: ...

global___DeleteUserRequest = DeleteUserRequest

@typing_extensions.final
class ListUsersRequest(google.protobuf.message.Message):
    """Request to list user"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_token: builtins.str
    """Optional: The page token to support pagination.
    Pagination allows you to retrieve a large result set in smaller, more manageable portions.
    The page token is a string representing the current index and page size.

    Valid page token strings:
    * "" (empty string) - Retrieves the first page.
    * "current_index-0--page_size-20" - Retrieves the first page with a page size of 20.
    * "current_index-1--page_size-20" - Retrieves the second page with a page size of 20.

    Index starts at 0.

    Examples of valid page token strings:
    * ""
    * "current_index-0--page_size-20"
    * "current_index-1--page_size-20"
    * "current_index-10--page_size-20"

    Examples of invalid page token strings:
    * "1"
    * "current_index-0--page_size-20"
    * "current_index--1--page_size-20"
    * "current_index1--page_size-20"
    * "current_index-1--page_size--20"
    """
    def __init__(
        self,
        *,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_token", b"page_token"]) -> None: ...

global___ListUsersRequest = ListUsersRequest

@typing_extensions.final
class ListUsersResponse(google.protobuf.message.Message):
    """Response containing list of users"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___User]:
        """The list of users. There will be a maximum number of items
        returned based on the page_token field in the request.
        """
    next_page_token: builtins.str
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """
    def __init__(
        self,
        *,
        users: collections.abc.Iterable[global___User] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "users", b"users"]) -> None: ...

global___ListUsersResponse = ListUsersResponse

@typing_extensions.final
class ListUserInfosResponse(google.protobuf.message.Message):
    """Response containing list of users"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UserInfo]:
        """The list of server roles. There will be a maximum number of items
        returned based on the page_token field in the request.
        """
    next_page_token: builtins.str
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """
    def __init__(
        self,
        *,
        users: collections.abc.Iterable[global___UserInfo] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "users", b"users"]) -> None: ...

global___ListUserInfosResponse = ListUserInfosResponse

@typing_extensions.final
class ServerRole(google.protobuf.message.Message):
    """Server Role messages"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    MODIFIED_BY_FIELD_NUMBER: builtins.int
    role_id: builtins.int
    """unique identifier of the role"""
    name: builtins.str
    """unique name of the role"""
    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """defines the permissions for the given role (the strings can be gotten from the ListServerPermissions)"""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation date and time. Read-only field."""
    @property
    def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Modification date and time. Read-only field."""
    created_by: builtins.str
    """User id in form of a valid UUID."""
    modified_by: builtins.str
    """User id in form of a valid UUID."""
    def __init__(
        self,
        *,
        role_id: builtins.int = ...,
        name: builtins.str = ...,
        permissions: collections.abc.Iterable[builtins.str] | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_by: builtins.str = ...,
        modified_by: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "modified_at", b"modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "created_by", b"created_by", "modified_at", b"modified_at", "modified_by", b"modified_by", "name", b"name", "permissions", b"permissions", "role_id", b"role_id"]) -> None: ...

global___ServerRole = ServerRole

@typing_extensions.final
class CreateServerRoleRequest(google.protobuf.message.Message):
    """Request to create server role"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_FIELD_NUMBER: builtins.int
    @property
    def role(self) -> global___ServerRole:
        """If the role_id is not provided, an incremental value will be assigned
        The "name" and "role_type" are mandatory values
        The permissions all default to False if not provided specifically
        """
    def __init__(
        self,
        *,
        role: global___ServerRole | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["role", b"role"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["role", b"role"]) -> None: ...

global___CreateServerRoleRequest = CreateServerRoleRequest

@typing_extensions.final
class UpdateServerRoleRequest(google.protobuf.message.Message):
    """Request to update server role"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def role(self) -> global___ServerRole:
        """role_id in the Role message should be given, if empty will throw an error in the backend
        other fields in the Role are optional. Only the fields to be updated should be provided
        """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. The mask to control which fields get updated."""
    def __init__(
        self,
        *,
        role: global___ServerRole | None = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["role", b"role", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["role", b"role", "update_mask", b"update_mask"]) -> None: ...

global___UpdateServerRoleRequest = UpdateServerRoleRequest

@typing_extensions.final
class DeleteServerRoleRequest(google.protobuf.message.Message):
    """Request to delete server role"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_ID_FIELD_NUMBER: builtins.int
    role_id: builtins.int
    """role is identified by role id, if empty will throw an error in the backend"""
    def __init__(
        self,
        *,
        role_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["role_id", b"role_id"]) -> None: ...

global___DeleteServerRoleRequest = DeleteServerRoleRequest

@typing_extensions.final
class GetServerRoleRequest(google.protobuf.message.Message):
    """Request to get server role"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_ID_FIELD_NUMBER: builtins.int
    ROLE_NAME_FIELD_NUMBER: builtins.int
    role_id: builtins.int
    """role is identified by role id"""
    role_name: builtins.str
    """role can also be uniquely identified by its name"""
    def __init__(
        self,
        *,
        role_id: builtins.int = ...,
        role_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["role_id", b"role_id", "role_name", b"role_name", "server_role_identifier", b"server_role_identifier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["role_id", b"role_id", "role_name", b"role_name", "server_role_identifier", b"server_role_identifier"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["server_role_identifier", b"server_role_identifier"]) -> typing_extensions.Literal["role_id", "role_name"] | None: ...

global___GetServerRoleRequest = GetServerRoleRequest

@typing_extensions.final
class ListServerRolesRequest(google.protobuf.message.Message):
    """Request to list server roles"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_token: builtins.str
    """Optional: The page token to support pagination.
    Pagination allows you to retrieve a large result set in smaller, more manageable portions.
    The page token is a string representing the current index and page size.

    Valid page token strings:
    * "" (empty string) - Retrieves the first page.
    * "current_index-0--page_size-20" - Retrieves the first page with a page size of 20.
    * "current_index-1--page_size-20" - Retrieves the second page with a page size of 20.

    Index starts at 0.

    Examples of valid page token strings:
    * ""
    * "current_index-0--page_size-20"
    * "current_index-1--page_size-20"
    * "current_index-10--page_size-20"

    Examples of invalid page token strings:
    * "1"
    * "current_index-0--page_size-20"
    * "current_index--1--page_size-20"
    * "current_index1--page_size-20"
    * "current_index-1--page_size--20"
    """
    def __init__(
        self,
        *,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_token", b"page_token"]) -> None: ...

global___ListServerRolesRequest = ListServerRolesRequest

@typing_extensions.final
class ListServerRolesResponse(google.protobuf.message.Message):
    """Response containing list of server roles"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ROLES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def server_roles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServerRole]:
        """The list of server roles. There will be a maximum number of items
        returned based on the page_token field in the request.
        """
    next_page_token: builtins.str
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """
    def __init__(
        self,
        *,
        server_roles: collections.abc.Iterable[global___ServerRole] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "server_roles", b"server_roles"]) -> None: ...

global___ListServerRolesResponse = ListServerRolesResponse

@typing_extensions.final
class ListServerPermissionsRequest(google.protobuf.message.Message):
    """Server permissions"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_token: builtins.str
    """Optional: The page token to support pagination.
    Pagination allows you to retrieve a large result set in smaller, more manageable portions.
    The page token is a string representing the current index and page size.

    Valid page token strings:
    * "" (empty string) - Retrieves the first page.
    * "current_index-0--page_size-20" - Retrieves the first page with a page size of 20.
    * "current_index-1--page_size-20" - Retrieves the second page with a page size of 20.

    Index starts at 0.

    Examples of valid page token strings:
    * ""
    * "current_index-0--page_size-20"
    * "current_index-1--page_size-20"
    * "current_index-10--page_size-20"

    Examples of invalid page token strings:
    * "1"
    * "current_index-0--page_size-20"
    * "current_index--1--page_size-20"
    * "current_index1--page_size-20"
    * "current_index-1--page_size--20"
    """
    def __init__(
        self,
        *,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_token", b"page_token"]) -> None: ...

global___ListServerPermissionsRequest = ListServerPermissionsRequest

@typing_extensions.final
class ListServerPermissionsResponse(google.protobuf.message.Message):
    """Response containing list of server permissions"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PERMISSIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The list of server permissions. There will be a maximum number of items
        returned based on the page_token field in the request.
        """
    next_page_token: builtins.str
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """
    def __init__(
        self,
        *,
        permissions: collections.abc.Iterable[builtins.str] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "permissions", b"permissions"]) -> None: ...

global___ListServerPermissionsResponse = ListServerPermissionsResponse

@typing_extensions.final
class LoginRequest(google.protobuf.message.Message):
    """Authentication messages"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_EMAIL_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    user_email: builtins.str
    """user email"""
    password: builtins.str
    """user password"""
    def __init__(
        self,
        *,
        user_email: builtins.str = ...,
        password: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["password", b"password", "user_email", b"user_email"]) -> None: ...

global___LoginRequest = LoginRequest

@typing_extensions.final
class LoginResponse(google.protobuf.message.Message):
    """This message is a response of logging"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    AUTH_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """user object - user_id must be there"""
    auth_token: builtins.str
    """authentication token after successful login of the user to access NLU services"""
    def __init__(
        self,
        *,
        user: global___User | None = ...,
        auth_token: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["auth_token", b"auth_token", "user", b"user"]) -> None: ...

global___LoginResponse = LoginResponse

@typing_extensions.final
class GetUserPreferencesRequest(google.protobuf.message.Message):
    """Request to get user preferences."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_NAME_FIELD_NUMBER: builtins.int
    KEYS_FIELD_NUMBER: builtins.int
    REGEX_INCLUDE_FIELD_NUMBER: builtins.int
    user_name: builtins.str
    """The name of the user.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/users/&lt;user_uuid&gt;</code></pre>
    """
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Specific keys to retrieve from user preferences.
        If keys are specified multiple times then only one KeyValue pair is returned
        """
    regex_include: builtins.str
    """Optional: In addition to the keys specified also include all <pre>keys</pre> that match the provided
    <pre>regex_include</pre> regular expression.
    If user does not add regex_filter, then only the keys specified in the keys field are returned.
    If both, a key in the keys field and in the regex_include will be matched than only a single
    <pre>KeyValuePair</pre> is returned.
    """
    def __init__(
        self,
        *,
        user_name: builtins.str = ...,
        keys: collections.abc.Iterable[builtins.str] | None = ...,
        regex_include: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keys", b"keys", "regex_include", b"regex_include", "user_name", b"user_name"]) -> None: ...

global___GetUserPreferencesRequest = GetUserPreferencesRequest

@typing_extensions.final
class GetUserPreferencesResponse(google.protobuf.message.Message):
    """Response containing user preferences."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_NAME_FIELD_NUMBER: builtins.int
    KEY_VALUE_PAIRS_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    user_name: builtins.str
    """The name of the user.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/users/&lt;user_uuid&gt;</code></pre>
    """
    @property
    def key_value_pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ondewo.nlu.common_pb2.KeyValuePair]:
        """List of key-value pairs representing user preferences."""
    error_message: builtins.str
    """error message if there are any."""
    def __init__(
        self,
        *,
        user_name: builtins.str = ...,
        key_value_pairs: collections.abc.Iterable[ondewo.nlu.common_pb2.KeyValuePair] | None = ...,
        error_message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message", b"error_message", "key_value_pairs", b"key_value_pairs", "user_name", b"user_name"]) -> None: ...

global___GetUserPreferencesResponse = GetUserPreferencesResponse

@typing_extensions.final
class SetUserPreferencesRequest(google.protobuf.message.Message):
    """Request to set or update user preferences."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_NAME_FIELD_NUMBER: builtins.int
    KEY_VALUE_PAIRS_FIELD_NUMBER: builtins.int
    user_name: builtins.str
    """The name of the user.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/users/&lt;user_uuid&gt;</code></pre>
    """
    @property
    def key_value_pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ondewo.nlu.common_pb2.KeyValuePair]:
        """List of key-value pairs to set or update."""
    def __init__(
        self,
        *,
        user_name: builtins.str = ...,
        key_value_pairs: collections.abc.Iterable[ondewo.nlu.common_pb2.KeyValuePair] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_value_pairs", b"key_value_pairs", "user_name", b"user_name"]) -> None: ...

global___SetUserPreferencesRequest = SetUserPreferencesRequest

@typing_extensions.final
class SetUserPreferencesResponse(google.protobuf.message.Message):
    """Response to set or update user preferences."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_NAME_FIELD_NUMBER: builtins.int
    KEYS_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    user_name: builtins.str
    """The name of the user.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/users/&lt;user_uuid&gt;</code></pre>
    """
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of keys to delete from user preferences."""
    error_message: builtins.str
    """error message if there are any."""
    def __init__(
        self,
        *,
        user_name: builtins.str = ...,
        keys: collections.abc.Iterable[builtins.str] | None = ...,
        error_message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message", b"error_message", "keys", b"keys", "user_name", b"user_name"]) -> None: ...

global___SetUserPreferencesResponse = SetUserPreferencesResponse

@typing_extensions.final
class DeleteUserPreferencesRequest(google.protobuf.message.Message):
    """Request to delete specific user preferences."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_NAME_FIELD_NUMBER: builtins.int
    KEYS_FIELD_NUMBER: builtins.int
    REGEX_INCLUDE_FIELD_NUMBER: builtins.int
    user_name: builtins.str
    """The name of the user.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/users/&lt;user_uuid&gt;</code></pre>
    """
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of keys to delete from user preferences."""
    regex_include: builtins.str
    """Optional: In addition to the keys specified also include all <pre>keys</pre> that match the provided
    <pre>regex_include</pre> regular expression.
    If user does not add regex_filter, then only the keys specified in the keys field are deleted.
    If both, a key in the keys field and in the regex_include is matched then the key is deleted without raising an error.
    """
    def __init__(
        self,
        *,
        user_name: builtins.str = ...,
        keys: collections.abc.Iterable[builtins.str] | None = ...,
        regex_include: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keys", b"keys", "regex_include", b"regex_include", "user_name", b"user_name"]) -> None: ...

global___DeleteUserPreferencesRequest = DeleteUserPreferencesRequest

@typing_extensions.final
class DeleteUserPreferencesResponse(google.protobuf.message.Message):
    """Response to delete specific user preferences."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_NAME_FIELD_NUMBER: builtins.int
    KEYS_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    user_name: builtins.str
    """The name of the user.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/users/&lt;user_uuid&gt;</code></pre>
    """
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of keys to delete from user preferences."""
    error_message: builtins.str
    """error message if there are any."""
    def __init__(
        self,
        *,
        user_name: builtins.str = ...,
        keys: collections.abc.Iterable[builtins.str] | None = ...,
        error_message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message", b"error_message", "keys", b"keys", "user_name", b"user_name"]) -> None: ...

global___DeleteUserPreferencesResponse = DeleteUserPreferencesResponse

@typing_extensions.final
class DeleteAllUserPreferencesRequest(google.protobuf.message.Message):
    """Request to delete all user preferences with an optional filter substring."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_NAME_FIELD_NUMBER: builtins.int
    REGEX_FILTER_FIELD_NUMBER: builtins.int
    user_name: builtins.str
    """The name of the user.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/users/&lt;user_uuid&gt;</code></pre>
    """
    regex_filter: builtins.str
    """Optional: Only delete keys that match the provided regular expression.
    If user does not add regex_filter, then all user preferences will be deleted
    Example:
    Only delete keys starting with DE: <code>^DE_</code>
    Only delete keys matching: <code>.*user.*</code>
    """
    def __init__(
        self,
        *,
        user_name: builtins.str = ...,
        regex_filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["regex_filter", b"regex_filter", "user_name", b"user_name"]) -> None: ...

global___DeleteAllUserPreferencesRequest = DeleteAllUserPreferencesRequest

@typing_extensions.final
class ListUserPreferencesRequest(google.protobuf.message.Message):
    """Request to list all user preferences for a specific user."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_NAME_FIELD_NUMBER: builtins.int
    REGEX_FILTER_FIELD_NUMBER: builtins.int
    user_name: builtins.str
    """The name of the user.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/users/&lt;user_uuid&gt;</code></pre>
    """
    regex_filter: builtins.str
    """Optional: Only list keys that match the provided regular expression"""
    def __init__(
        self,
        *,
        user_name: builtins.str = ...,
        regex_filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["regex_filter", b"regex_filter", "user_name", b"user_name"]) -> None: ...

global___ListUserPreferencesRequest = ListUserPreferencesRequest

@typing_extensions.final
class ListUserPreferencesResponse(google.protobuf.message.Message):
    """Response containing a list of user preferences for a specific user with an optional filter substring."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_NAME_FIELD_NUMBER: builtins.int
    KEY_VALUE_PAIRS_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    user_name: builtins.str
    """The name of the user."""
    @property
    def key_value_pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ondewo.nlu.common_pb2.KeyValuePair]:
        """List of key-value pairs representing user preferences."""
    error_message: builtins.str
    """error message if there are any."""
    def __init__(
        self,
        *,
        user_name: builtins.str = ...,
        key_value_pairs: collections.abc.Iterable[ondewo.nlu.common_pb2.KeyValuePair] | None = ...,
        error_message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message", b"error_message", "key_value_pairs", b"key_value_pairs", "user_name", b"user_name"]) -> None: ...

global___ListUserPreferencesResponse = ListUserPreferencesResponse
