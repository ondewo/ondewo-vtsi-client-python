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
import google.protobuf.descriptor
import google.protobuf.message
import ondewo.nlu.entity_type_pb2
import ondewo.nlu.intent_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetIntentCountRequest(google.protobuf.message.Message):
    """Request to get the intent count"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_FIELD_NUMBER: builtins.int
    FILTER_BY_CATEGORY_FIELD_NUMBER: builtins.int
    parent: builtins.str
    """Required. The project that the agent to fetch is associated with.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agents</code></pre>
    """
    filter_by_category: ondewo.nlu.intent_pb2.IntentCategory.ValueType
    """Optional. Applies a filter to the list to be counted. Default, no filter."""
    def __init__(
        self,
        *,
        parent: builtins.str = ...,
        filter_by_category: ondewo.nlu.intent_pb2.IntentCategory.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter_by_category", b"filter_by_category", "parent", b"parent"]) -> None: ...

global___GetIntentCountRequest = GetIntentCountRequest

@typing.final
class GetEntityTypeCountRequest(google.protobuf.message.Message):
    """Request to get entity type count"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_FIELD_NUMBER: builtins.int
    FILTER_BY_CATEGORY_FIELD_NUMBER: builtins.int
    parent: builtins.str
    """Required. The project that the agent to fetch is associated with.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agents</code></pre>
    """
    filter_by_category: ondewo.nlu.entity_type_pb2.EntityTypeCategory.ValueType
    """Optional. Applies a filter to the list to be counted. Default, no filter."""
    def __init__(
        self,
        *,
        parent: builtins.str = ...,
        filter_by_category: ondewo.nlu.entity_type_pb2.EntityTypeCategory.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter_by_category", b"filter_by_category", "parent", b"parent"]) -> None: ...

global___GetEntityTypeCountRequest = GetEntityTypeCountRequest

@typing.final
class GetProjectStatRequest(google.protobuf.message.Message):
    """Request to get project statistics"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_FIELD_NUMBER: builtins.int
    parent: builtins.str
    """Required. The project that the agent to fetch is associated with.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agents</code></pre>
    """
    def __init__(
        self,
        *,
        parent: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["parent", b"parent"]) -> None: ...

global___GetProjectStatRequest = GetProjectStatRequest

@typing.final
class GetProjectElementStatRequest(google.protobuf.message.Message):
    """Request to get project element statistics"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Required. The name/path of the concept to get the statistic from.
    Example:
    <pre><code>
    * projects/&lt;project_uuid&gt;/agent/intents/&lt;intent_uuid&gt;
    * projects/&lt;project_uuid&gt;/agent/entityTypes/&lt;entity_type_uuid&gt;
    * projects/&lt;project_uuid&gt;/agent/entityTypes/&lt;entity_type_uuid&gt;/entityValues&lt;entity_value_uuid&gt;
    </code></pre>
    """
    language_code: builtins.str
    """Language code"""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        language_code: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["language_code", b"language_code", "name", b"name"]) -> None: ...

global___GetProjectElementStatRequest = GetProjectElementStatRequest
