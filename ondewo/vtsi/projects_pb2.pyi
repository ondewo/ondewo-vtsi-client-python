"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _VtsiProjectStatus:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _VtsiProjectStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VtsiProjectStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNSPECIFIED: _VtsiProjectStatus.ValueType  # 0
    """No status specified"""

    UNDEPLOYED: _VtsiProjectStatus.ValueType  # 1
    """Project successfully created and undeployed"""

    UPDATING: _VtsiProjectStatus.ValueType  # 2
    """Project configuration is updating"""

    DEPLOYING: _VtsiProjectStatus.ValueType  # 3
    """Project is deploying"""

    DEPLOYED: _VtsiProjectStatus.ValueType  # 4
    """Project is deployed"""

    UNDEPLOYING: _VtsiProjectStatus.ValueType  # 5
    """Project is un-deploying"""

    DELETING: _VtsiProjectStatus.ValueType  # 6
    """Project is currently deleting"""

    DELETED: _VtsiProjectStatus.ValueType  # 7
    """Project is deleted"""

class VtsiProjectStatus(_VtsiProjectStatus, metaclass=_VtsiProjectStatusEnumTypeWrapper):
    """Status of a VtsiProject."""
    pass

UNSPECIFIED: VtsiProjectStatus.ValueType  # 0
"""No status specified"""

UNDEPLOYED: VtsiProjectStatus.ValueType  # 1
"""Project successfully created and undeployed"""

UPDATING: VtsiProjectStatus.ValueType  # 2
"""Project configuration is updating"""

DEPLOYING: VtsiProjectStatus.ValueType  # 3
"""Project is deploying"""

DEPLOYED: VtsiProjectStatus.ValueType  # 4
"""Project is deployed"""

UNDEPLOYING: VtsiProjectStatus.ValueType  # 5
"""Project is un-deploying"""

DELETING: VtsiProjectStatus.ValueType  # 6
"""Project is currently deleting"""

DELETED: VtsiProjectStatus.ValueType  # 7
"""Project is deleted"""

global___VtsiProjectStatus = VtsiProjectStatus


class _VtsiProjectSortingMode:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _VtsiProjectSortingModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VtsiProjectSortingMode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ASCENDING: _VtsiProjectSortingMode.ValueType  # 0
    """The ascending sorting mode.
    When sorting using this mode, VtsiProject objects will be arranged
    in ascending order based on the specified criteria.
    """

    DESCENDING: _VtsiProjectSortingMode.ValueType  # 1
    """The descending sorting mode.
    When sorting using this mode, VtsiProject objects will be arranged
    in descending order based on the specified criteria.
    """

class VtsiProjectSortingMode(_VtsiProjectSortingMode, metaclass=_VtsiProjectSortingModeEnumTypeWrapper):
    """Sorting mode"""
    pass

ASCENDING: VtsiProjectSortingMode.ValueType  # 0
"""The ascending sorting mode.
When sorting using this mode, VtsiProject objects will be arranged
in ascending order based on the specified criteria.
"""

DESCENDING: VtsiProjectSortingMode.ValueType  # 1
"""The descending sorting mode.
When sorting using this mode, VtsiProject objects will be arranged
in descending order based on the specified criteria.
"""

global___VtsiProjectSortingMode = VtsiProjectSortingMode


class _VtsiProjectView:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _VtsiProjectViewEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VtsiProjectView.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    VTSI_PROJECT_VIEW_UNSPECIFIED: _VtsiProjectView.ValueType  # 0
    """Unspecified VTSI_PROJECT view: the view is defined by the call:
    - CreateVTSI_PROJECT: VTSI_PROJECT_VIEW_SHALLOW
    - UpdateVTSI_PROJECT: VTSI_PROJECT_VIEW_SHALLOW
    - GetVTSI_PROJECT: VTSI_PROJECT_VIEW_FULL
    - ListVTSI_PROJECTs: VTSI_PROJECT_VIEW_SHALLOW
    """

    VTSI_PROJECT_VIEW_FULL: _VtsiProjectView.ValueType  # 1
    """Full VTSI_PROJECT view: populate all the fields of the VTSI_PROJECT message including configs."""

    VTSI_PROJECT_VIEW_SHALLOW: _VtsiProjectView.ValueType  # 2
    """Shallow VTSI_PROJECT view: populates all the fields except configs."""

    VTSI_PROJECT_VIEW_MINIMUM: _VtsiProjectView.ValueType  # 3
    """Minimum view including only VTSI_PROJECT UUID and VTSI_PROJECT display name"""

class VtsiProjectView(_VtsiProjectView, metaclass=_VtsiProjectViewEnumTypeWrapper):
    """Structure of VTSI_PROJECT view"""
    pass

VTSI_PROJECT_VIEW_UNSPECIFIED: VtsiProjectView.ValueType  # 0
"""Unspecified VTSI_PROJECT view: the view is defined by the call:
- CreateVTSI_PROJECT: VTSI_PROJECT_VIEW_SHALLOW
- UpdateVTSI_PROJECT: VTSI_PROJECT_VIEW_SHALLOW
- GetVTSI_PROJECT: VTSI_PROJECT_VIEW_FULL
- ListVTSI_PROJECTs: VTSI_PROJECT_VIEW_SHALLOW
"""

VTSI_PROJECT_VIEW_FULL: VtsiProjectView.ValueType  # 1
"""Full VTSI_PROJECT view: populate all the fields of the VTSI_PROJECT message including configs."""

VTSI_PROJECT_VIEW_SHALLOW: VtsiProjectView.ValueType  # 2
"""Shallow VTSI_PROJECT view: populates all the fields except configs."""

VTSI_PROJECT_VIEW_MINIMUM: VtsiProjectView.ValueType  # 3
"""Minimum view including only VTSI_PROJECT UUID and VTSI_PROJECT display name"""

global___VtsiProjectView = VtsiProjectView


class VtsiProject(google.protobuf.message.Message):
    """The VTSI project with its configuration setting"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    MAX_CALLERS_FIELD_NUMBER: builtins.int
    MAX_LISTENERS_FIELD_NUMBER: builtins.int
    ASTERISK_CONFIGS_FIELD_NUMBER: builtins.int
    VTSI_PROJECT_STATUS_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    MODIFIED_BY_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FIELD_NUMBER: builtins.int
    ACTIVE_CALLERS_FIELD_NUMBER: builtins.int
    ACTIVE_LISTENERS_FIELD_NUMBER: builtins.int
    ASTERISK_PORT_FIELD_NUMBER: builtins.int
    NLU_AGENT_NAMES_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Required. The project name. Format: <pre><code>projects/&lt;project_uuid&gt;/project</code></pre>
    Only when a new VtsiProject is created the name can be undefined/empty
    """

    display_name: typing.Text
    """OPTIONAL: The display name of the project"""

    max_callers: builtins.int
    """The maximum number of callers that this project can have."""

    max_listeners: builtins.int
    """The maximum number of listeners that this project can have."""

    @property
    def asterisk_configs(self) -> global___AsteriskConfigs:
        """Configs to start the asterisk server."""
        pass
    vtsi_project_status: global___VtsiProjectStatus.ValueType
    """The status of the VTSI project."""

    created_by: typing.Text
    """The user who created the vtsi project. Readonly."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation time of the vtsi project. Readonly."""
        pass
    modified_by: typing.Text
    """The user who modified the vtsi project. Readonly."""

    @property
    def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Modification time of the vtsi project. Readonly."""
        pass
    active_callers: builtins.int
    """The number of active callers in this project."""

    active_listeners: builtins.int
    """The number of active listeners in this project."""

    asterisk_port: builtins.int
    """The port of the asterisk server"""

    @property
    def nlu_agent_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """associated NLU agents
        Format: `projects/<Project ID>/agent`.
        """
        pass
    def __init__(self,
        *,
        name: typing.Text = ...,
        display_name: typing.Text = ...,
        max_callers: builtins.int = ...,
        max_listeners: builtins.int = ...,
        asterisk_configs: typing.Optional[global___AsteriskConfigs] = ...,
        vtsi_project_status: global___VtsiProjectStatus.ValueType = ...,
        created_by: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        modified_by: typing.Text = ...,
        modified_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        active_callers: builtins.int = ...,
        active_listeners: builtins.int = ...,
        asterisk_port: builtins.int = ...,
        nlu_agent_names: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["asterisk_configs",b"asterisk_configs","created_at",b"created_at","modified_at",b"modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["active_callers",b"active_callers","active_listeners",b"active_listeners","asterisk_configs",b"asterisk_configs","asterisk_port",b"asterisk_port","created_at",b"created_at","created_by",b"created_by","display_name",b"display_name","max_callers",b"max_callers","max_listeners",b"max_listeners","modified_at",b"modified_at","modified_by",b"modified_by","name",b"name","nlu_agent_names",b"nlu_agent_names","vtsi_project_status",b"vtsi_project_status"]) -> None: ...
global___VtsiProject = VtsiProject

class AsteriskConfigsVariables(google.protobuf.message.Message):
    """Configuration variables for the Asterisk server"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SIP_TRUNK_USERNAME_FIELD_NUMBER: builtins.int
    SIP_TRUNK_PASSWORD_FIELD_NUMBER: builtins.int
    SIP_TRUNK_HOST_FIELD_NUMBER: builtins.int
    TRANSFER_NUMBER_FIELD_NUMBER: builtins.int
    TRANSFER_NUMBER_HOST_FIELD_NUMBER: builtins.int
    SIP_TRUNK_PHONE_NUMBER_FIELD_NUMBER: builtins.int
    sip_trunk_username: typing.Text
    """SIP trunk username."""

    sip_trunk_password: typing.Text
    """SIP trunk password."""

    sip_trunk_host: typing.Text
    """SIP trunk host."""

    transfer_number: typing.Text
    """Transfer number."""

    transfer_number_host: typing.Text
    """Transfer number host."""

    sip_trunk_phone_number: typing.Text
    """SIP trunk phone number."""

    def __init__(self,
        *,
        sip_trunk_username: typing.Text = ...,
        sip_trunk_password: typing.Text = ...,
        sip_trunk_host: typing.Text = ...,
        transfer_number: typing.Text = ...,
        transfer_number_host: typing.Text = ...,
        sip_trunk_phone_number: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["sip_trunk_host",b"sip_trunk_host","sip_trunk_password",b"sip_trunk_password","sip_trunk_phone_number",b"sip_trunk_phone_number","sip_trunk_username",b"sip_trunk_username","transfer_number",b"transfer_number","transfer_number_host",b"transfer_number_host"]) -> None: ...
global___AsteriskConfigsVariables = AsteriskConfigsVariables

class AsteriskConfigsFiles(google.protobuf.message.Message):
    """Configuration files for the Asterisk server"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SIP_CONF_FILE_STRING_FIELD_NUMBER: builtins.int
    EXTENSIONS_CONF_FILE_STRING_FIELD_NUMBER: builtins.int
    QUEUES_CONF_FILE_STRING_FIELD_NUMBER: builtins.int
    MODULES_CONF_FILE_STRING_FIELD_NUMBER: builtins.int
    sip_conf_file_string: typing.Text
    """sip.conf file as string"""

    extensions_conf_file_string: typing.Text
    """extensions.conf file as string"""

    queues_conf_file_string: typing.Text
    """queues.conf file as string"""

    modules_conf_file_string: typing.Text
    """modules.conf file as string"""

    def __init__(self,
        *,
        sip_conf_file_string: typing.Text = ...,
        extensions_conf_file_string: typing.Text = ...,
        queues_conf_file_string: typing.Text = ...,
        modules_conf_file_string: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["extensions_conf_file_string",b"extensions_conf_file_string","modules_conf_file_string",b"modules_conf_file_string","queues_conf_file_string",b"queues_conf_file_string","sip_conf_file_string",b"sip_conf_file_string"]) -> None: ...
global___AsteriskConfigsFiles = AsteriskConfigsFiles

class AsteriskConfigs(google.protobuf.message.Message):
    """Configurations object for the Asterisk server"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ASTERISK_CONFIGS_VARIABLES_FIELD_NUMBER: builtins.int
    ASTERISK_CONFIGS_FILES_FIELD_NUMBER: builtins.int
    ASTERISK_CONFIGS_TARGET_DIRECTORY_NAME_FIELD_NUMBER: builtins.int
    ASTERISK_PORT_FIELD_NUMBER: builtins.int
    @property
    def asterisk_configs_variables(self) -> global___AsteriskConfigsVariables:
        """Configs as variables which will fill those variables using a blue print."""
        pass
    @property
    def asterisk_configs_files(self) -> global___AsteriskConfigsFiles:
        """Configs as files which will set up the configs using those files."""
        pass
    asterisk_configs_target_directory_name: typing.Text
    """Configs will be mapped in from a preconfigured asterisk target directory."""

    asterisk_port: builtins.int
    """OPTIONAL: The port where Asterisk should start."""

    def __init__(self,
        *,
        asterisk_configs_variables: typing.Optional[global___AsteriskConfigsVariables] = ...,
        asterisk_configs_files: typing.Optional[global___AsteriskConfigsFiles] = ...,
        asterisk_configs_target_directory_name: typing.Text = ...,
        asterisk_port: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["asterisk_configs_files",b"asterisk_configs_files","asterisk_configs_oneof",b"asterisk_configs_oneof","asterisk_configs_target_directory_name",b"asterisk_configs_target_directory_name","asterisk_configs_variables",b"asterisk_configs_variables"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asterisk_configs_files",b"asterisk_configs_files","asterisk_configs_oneof",b"asterisk_configs_oneof","asterisk_configs_target_directory_name",b"asterisk_configs_target_directory_name","asterisk_configs_variables",b"asterisk_configs_variables","asterisk_port",b"asterisk_port"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["asterisk_configs_oneof",b"asterisk_configs_oneof"]) -> typing.Optional[typing_extensions.Literal["asterisk_configs_variables","asterisk_configs_files","asterisk_configs_target_directory_name"]]: ...
global___AsteriskConfigs = AsteriskConfigs

class CreateVtsiProjectRequest(google.protobuf.message.Message):
    """Request for creating a VTSI project"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VTSI_PROJECT_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    @property
    def vtsi_project(self) -> global___VtsiProject:
        """VTSI project
        Recommended is to leave "name" empty. The project name here is optional.
        If no name is given a new parent name is created. The parent has the format:
        <pre><code>projects/&lt;project_uuid&gt;/project</code></pre>.
        """
        pass
    error_message: typing.Text
    """error message if there are any."""

    def __init__(self,
        *,
        vtsi_project: typing.Optional[global___VtsiProject] = ...,
        error_message: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["vtsi_project",b"vtsi_project"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message",b"error_message","vtsi_project",b"vtsi_project"]) -> None: ...
global___CreateVtsiProjectRequest = CreateVtsiProjectRequest

class CreateVtsiProjectResponse(google.protobuf.message.Message):
    """Response of the create project"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VTSI_PROJECT_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    @property
    def vtsi_project(self) -> global___VtsiProject:
        """Vtsi project"""
        pass
    error_message: typing.Text
    """error message if there are any."""

    def __init__(self,
        *,
        vtsi_project: typing.Optional[global___VtsiProject] = ...,
        error_message: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["vtsi_project",b"vtsi_project"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message",b"error_message","vtsi_project",b"vtsi_project"]) -> None: ...
global___CreateVtsiProjectResponse = CreateVtsiProjectResponse

class GetVtsiProjectRequest(google.protobuf.message.Message):
    """Request to retrieve a VTSI project"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    """VTSI project name with which to perform the call of the form <pre><code>projects/&lt;project_uuid&gt;/project</code></pre>"""

    def __init__(self,
        *,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetVtsiProjectRequest = GetVtsiProjectRequest

class ListVtsiProjectsRequest(google.protobuf.message.Message):
    """Request to get the list of agents"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VTSI_PROJECT_VIEW_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    VTSI_PROJECT_SORTING_FIELD_NUMBER: builtins.int
    NLU_AGENT_NAMES_FIELD_NUMBER: builtins.int
    vtsi_project_view: global___VtsiProjectView.ValueType
    """Optional. Specify the view of the returned VtsiProject (full view by default)"""

    page_token: typing.Text
    """Optional. The next_page_token value returned from a previous list request.
    Example: "current_index-1--page_size-20"
    """

    @property
    def vtsi_project_sorting(self) -> global___VtsiProjectSorting:
        """Optional. Field to define the sorting of the list of VTSI projects in the response.
        If not specified, the default behavior is to have no sorting.
        """
        pass
    @property
    def nlu_agent_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Optional. Filter based on associated NLU agents
        Format: `projects/<Project ID>/agent`.
        """
        pass
    def __init__(self,
        *,
        vtsi_project_view: global___VtsiProjectView.ValueType = ...,
        page_token: typing.Optional[typing.Text] = ...,
        vtsi_project_sorting: typing.Optional[global___VtsiProjectSorting] = ...,
        nlu_agent_names: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_page_token",b"_page_token","_vtsi_project_sorting",b"_vtsi_project_sorting","page_token",b"page_token","vtsi_project_sorting",b"vtsi_project_sorting"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_page_token",b"_page_token","_vtsi_project_sorting",b"_vtsi_project_sorting","nlu_agent_names",b"nlu_agent_names","page_token",b"page_token","vtsi_project_sorting",b"vtsi_project_sorting","vtsi_project_view",b"vtsi_project_view"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_page_token",b"_page_token"]) -> typing.Optional[typing_extensions.Literal["page_token"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_vtsi_project_sorting",b"_vtsi_project_sorting"]) -> typing.Optional[typing_extensions.Literal["vtsi_project_sorting"]]: ...
global___ListVtsiProjectsRequest = ListVtsiProjectsRequest

class ListVtsiProjectsResponse(google.protobuf.message.Message):
    """This is a protobuf message definition for the response of getting a list of VTSI projects."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VTSI_PROJECTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def vtsi_projects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___VtsiProject]:
        """The list of VTSI projects returned in the response.
        Use the 'repeated' keyword to indicate that this field can contain multiple instances of VtsiProject.
        """
        pass
    next_page_token: typing.Text
    """Token to retrieve the next page of results.
    This field is a string that holds a token for fetching the next page of results.
    If there are no more results in the list, this field will be empty.
    """

    def __init__(self,
        *,
        vtsi_projects: typing.Optional[typing.Iterable[global___VtsiProject]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","vtsi_projects",b"vtsi_projects"]) -> None: ...
global___ListVtsiProjectsResponse = ListVtsiProjectsResponse

class VtsiProjectSorting(google.protobuf.message.Message):
    """This protobuf message defines the sorting order for VTSI (Virtual Test System Infrastructure) projects."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _VtsiProjectSortingField:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _VtsiProjectSortingFieldEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[VtsiProjectSorting._VtsiProjectSortingField.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NO_VTSI_PROJECT_SORTING: VtsiProjectSorting._VtsiProjectSortingField.ValueType  # 0
        """No sorting"""

        SORT_VTSI_PROJECT_BY_NAME: VtsiProjectSorting._VtsiProjectSortingField.ValueType  # 1
        """Sort by project name such as <pre><code>projects/&lt;project_uuid&gt;/project</code></pre>."""

        SORT_VTSI_PROJECT_BY_DISPLAY_NAME: VtsiProjectSorting._VtsiProjectSortingField.ValueType  # 2
        """Sort by display name"""

        SORT_VTSI_PROJECT_BY_CREATION_DATE: VtsiProjectSorting._VtsiProjectSortingField.ValueType  # 3
        """Sort by creation date"""

        SORT_VTSI_PROJECT_BY_LAST_MODIFIED: VtsiProjectSorting._VtsiProjectSortingField.ValueType  # 4
        """Sort by last modified date"""

    class VtsiProjectSortingField(_VtsiProjectSortingField, metaclass=_VtsiProjectSortingFieldEnumTypeWrapper):
        """Enum to specify the sorting field for VTSI projects."""
        pass

    NO_VTSI_PROJECT_SORTING: VtsiProjectSorting.VtsiProjectSortingField.ValueType  # 0
    """No sorting"""

    SORT_VTSI_PROJECT_BY_NAME: VtsiProjectSorting.VtsiProjectSortingField.ValueType  # 1
    """Sort by project name such as <pre><code>projects/&lt;project_uuid&gt;/project</code></pre>."""

    SORT_VTSI_PROJECT_BY_DISPLAY_NAME: VtsiProjectSorting.VtsiProjectSortingField.ValueType  # 2
    """Sort by display name"""

    SORT_VTSI_PROJECT_BY_CREATION_DATE: VtsiProjectSorting.VtsiProjectSortingField.ValueType  # 3
    """Sort by creation date"""

    SORT_VTSI_PROJECT_BY_LAST_MODIFIED: VtsiProjectSorting.VtsiProjectSortingField.ValueType  # 4
    """Sort by last modified date"""


    SORTING_FIELD_FIELD_NUMBER: builtins.int
    SORTING_MODE_FIELD_NUMBER: builtins.int
    sorting_field: global___VtsiProjectSorting.VtsiProjectSortingField.ValueType
    """sorting field for vtsi projects sorting"""

    sorting_mode: global___VtsiProjectSortingMode.ValueType
    """Sorting mode"""

    def __init__(self,
        *,
        sorting_field: typing.Optional[global___VtsiProjectSorting.VtsiProjectSortingField.ValueType] = ...,
        sorting_mode: typing.Optional[global___VtsiProjectSortingMode.ValueType] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_sorting_field",b"_sorting_field","_sorting_mode",b"_sorting_mode","sorting_field",b"sorting_field","sorting_mode",b"sorting_mode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_sorting_field",b"_sorting_field","_sorting_mode",b"_sorting_mode","sorting_field",b"sorting_field","sorting_mode",b"sorting_mode"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_sorting_field",b"_sorting_field"]) -> typing.Optional[typing_extensions.Literal["sorting_field"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_sorting_mode",b"_sorting_mode"]) -> typing.Optional[typing_extensions.Literal["sorting_mode"]]: ...
global___VtsiProjectSorting = VtsiProjectSorting

class UpdateVtsiProjectRequest(google.protobuf.message.Message):
    """Request to updated VTSI project"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VTSI_PROJECT_FIELD_NUMBER: builtins.int
    @property
    def vtsi_project(self) -> global___VtsiProject:
        """Project Configs."""
        pass
    def __init__(self,
        *,
        vtsi_project: typing.Optional[global___VtsiProject] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["vtsi_project",b"vtsi_project"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["vtsi_project",b"vtsi_project"]) -> None: ...
global___UpdateVtsiProjectRequest = UpdateVtsiProjectRequest

class UpdateVtsiProjectResponse(google.protobuf.message.Message):
    """Request to updated VTSI project"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    name: typing.Text
    """VTSI project name with which to perform the call of the form <pre><code>projects/&lt;project_uuid&gt;/project</code></pre>"""

    error_message: typing.Text
    """error message if there are any."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        error_message: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message",b"error_message","name",b"name"]) -> None: ...
global___UpdateVtsiProjectResponse = UpdateVtsiProjectResponse

class DeleteVtsiProjectRequest(google.protobuf.message.Message):
    """Request to delete a VTSI project
    If a deployed VTSI project was deleted then it was undeployed beforehand automatically
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    """VTSI project name with which to perform the call of the form <pre><code>projects/&lt;project_uuid&gt;/project</code></pre>"""

    def __init__(self,
        *,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteVtsiProjectRequest = DeleteVtsiProjectRequest

class DeleteVtsiProjectResponse(google.protobuf.message.Message):
    """Response to delete a VTSI project
    If a deployed VTSI project was deleted then it was undeployed beforehand automatically
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    name: typing.Text
    """VTSI project name with which to perform the call of the form <pre><code>projects/&lt;project_uuid&gt;/project</code></pre>"""

    error_message: typing.Text
    """error message if there are any."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        error_message: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message",b"error_message","name",b"name"]) -> None: ...
global___DeleteVtsiProjectResponse = DeleteVtsiProjectResponse

class DeployVtsiProjectRequest(google.protobuf.message.Message):
    """Request to deploy a vtsi project"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    """VTSI project name with which to perform the call of the form <pre><code>projects/&lt;project_uuid&gt;/project</code></pre>"""

    def __init__(self,
        *,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeployVtsiProjectRequest = DeployVtsiProjectRequest

class DeployVtsiProjectResponse(google.protobuf.message.Message):
    """Response to deploy a vtsi project"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    name: typing.Text
    """VTSI project name with which to perform the call of the form <pre><code>projects/&lt;project_uuid&gt;/project</code></pre>"""

    error_message: typing.Text
    """error message if there are any."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        error_message: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message",b"error_message","name",b"name"]) -> None: ...
global___DeployVtsiProjectResponse = DeployVtsiProjectResponse

class UndeployVtsiProjectRequest(google.protobuf.message.Message):
    """ Request to undeploy a vtsi project"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Project name of the VTSI project."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___UndeployVtsiProjectRequest = UndeployVtsiProjectRequest

class UndeployVtsiProjectResponse(google.protobuf.message.Message):
    """Response to undeploy a vtsi project"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    name: typing.Text
    """VTSI project name with which to perform the call of the form <pre><code>projects/&lt;project_uuid&gt;/project</code></pre>"""

    error_message: typing.Text
    """error message if there are any."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        error_message: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message",b"error_message","name",b"name"]) -> None: ...
global___UndeployVtsiProjectResponse = UndeployVtsiProjectResponse
