"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import ondewo.nlu.entity_type_pb2
import ondewo.nlu.intent_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetIntentCountRequest(google.protobuf.message.Message):
    """Request to get the intent count"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_BY_CATEGORY_FIELD_NUMBER: builtins.int
    parent: typing.Text
    """Required. The project that the agent to fetch is associated with.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agents</code></pre>
    """

    filter_by_category: ondewo.nlu.intent_pb2.IntentCategory.ValueType
    """Optional. Applies a filter to the list to be counted. Default, no filter."""

    def __init__(self,
        *,
        parent: typing.Text = ...,
        filter_by_category: ondewo.nlu.intent_pb2.IntentCategory.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter_by_category",b"filter_by_category","parent",b"parent"]) -> None: ...
global___GetIntentCountRequest = GetIntentCountRequest

class GetEntityTypeCountRequest(google.protobuf.message.Message):
    """Request to get entity type count"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_BY_CATEGORY_FIELD_NUMBER: builtins.int
    parent: typing.Text
    """Required. The project that the agent to fetch is associated with.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agents</code></pre>
    """

    filter_by_category: ondewo.nlu.entity_type_pb2.EntityTypeCategory.ValueType
    """Optional. Applies a filter to the list to be counted. Default, no filter."""

    def __init__(self,
        *,
        parent: typing.Text = ...,
        filter_by_category: ondewo.nlu.entity_type_pb2.EntityTypeCategory.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter_by_category",b"filter_by_category","parent",b"parent"]) -> None: ...
global___GetEntityTypeCountRequest = GetEntityTypeCountRequest

class GetProjectStatRequest(google.protobuf.message.Message):
    """Request to get project statistics"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    parent: typing.Text
    """Required. The project that the agent to fetch is associated with.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agents</code></pre>
    """

    def __init__(self,
        *,
        parent: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent"]) -> None: ...
global___GetProjectStatRequest = GetProjectStatRequest

class GetProjectElementStatRequest(google.protobuf.message.Message):
    """Request to get project element statistics"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Required. The name/path of the concept to get the statistic from.

    Example:
         * `projects/<Project ID>/agent/intents/<Intent ID>`
         * `projects/<Project ID>/agent/entityTypes/<Entity Type ID>`
         * `projects/<Project ID>/agent/entityTypes/<Entity Type ID>/entityValues/<Entity Value ID>`
    """

    language_code: typing.Text
    def __init__(self,
        *,
        name: typing.Text = ...,
        language_code: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","name",b"name"]) -> None: ...
global___GetProjectElementStatRequest = GetProjectElementStatRequest
