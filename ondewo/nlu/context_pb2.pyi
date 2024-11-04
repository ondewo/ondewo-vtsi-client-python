"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2018 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Modifications Copyright 2020-2023 ONDEWO GmbH

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
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Context(google.protobuf.message.Message):
    """Represents a context."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Parameter(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        DISPLAY_NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        VALUE_ORIGINAL_FIELD_NUMBER: builtins.int
        CREATED_AT_FIELD_NUMBER: builtins.int
        MODIFIED_AT_FIELD_NUMBER: builtins.int
        CREATED_BY_FIELD_NUMBER: builtins.int
        MODIFIED_BY_FIELD_NUMBER: builtins.int
        name: builtins.str
        """The name of the context parameter."""
        display_name: builtins.str
        """The display name of the context parameter."""
        value: builtins.str
        """The value(s) of the context parameter."""
        value_original: builtins.str
        """The original value(s) of the context parameter."""
        created_by: builtins.str
        """User id in form of a valid UUID."""
        modified_by: builtins.str
        """User id in form of a valid UUID."""
        @property
        def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """Creation date and time. Read-only field."""

        @property
        def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """Modification date and time. Read-only field."""

        def __init__(
            self,
            *,
            name: builtins.str = ...,
            display_name: builtins.str = ...,
            value: builtins.str = ...,
            value_original: builtins.str = ...,
            created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
            modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
            created_by: builtins.str = ...,
            modified_by: builtins.str = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["created_at", b"created_at", "modified_at", b"modified_at"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "created_by", b"created_by", "display_name", b"display_name", "modified_at", b"modified_at", "modified_by", b"modified_by", "name", b"name", "value", b"value", "value_original", b"value_original"]) -> None: ...

    @typing.final
    class ParametersEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___Context.Parameter: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___Context.Parameter | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    LIFESPAN_COUNT_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    LIFESPAN_TIME_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    MODIFIED_BY_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Required. The display name of the context (must be unique per session).

    Note: we are deviating from the dialogflow format `projects/<Project ID>/agent/sessions/<Session ID>/contexts/<Context ID>`.

    - DetectIntent only returns
       - the short display name in the "name" field in query_result.output_contexts
       - only expects the short display name in the "name" field in query_parameters.contexts
    - Also inside the persisted session object only the short display name is used.
       - SessionStep.contexts only contains the short display name
       - SessionReviewStep.contexts only contains the short display name
    """
    lifespan_count: builtins.int
    """Optional. The number of conversational query requests after which the
    context expires. If set to `0` (the default) the context expires
    immediately. Contexts expire automatically after 10 minutes even if there
    are no matching queries.
    """
    lifespan_time: builtins.float
    """Optional. The time span in seconds after which the context expires. By default it does not expire."""
    created_by: builtins.str
    """User id in form of a valid UUID."""
    modified_by: builtins.str
    """User id in form of a valid UUID."""
    @property
    def parameters(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___Context.Parameter]:
        """Optional. The collection of parameters associated with this context.
        Refer to [this doc](https://dialogflow.com/docs/actions-and-parameters) for
        syntax.
        Keys are the display names of context parameters.
        """

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation date and time. Read-only field."""

    @property
    def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Modification date and time. Read-only field."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        lifespan_count: builtins.int = ...,
        parameters: collections.abc.Mapping[builtins.str, global___Context.Parameter] | None = ...,
        lifespan_time: builtins.float = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_by: builtins.str = ...,
        modified_by: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "modified_at", b"modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "created_by", b"created_by", "lifespan_count", b"lifespan_count", "lifespan_time", b"lifespan_time", "modified_at", b"modified_at", "modified_by", b"modified_by", "name", b"name", "parameters", b"parameters"]) -> None: ...

global___Context = Context

@typing.final
class ListContextsRequest(google.protobuf.message.Message):
    """The request message for [Contexts.ListContexts][google.cloud.dialogflow.v2.Contexts.ListContexts]."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_ID_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    session_id: builtins.str
    """Required. The session to list all contexts from.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/sessions/&lt;session_uuid&gt;</code></pre>
    """
    page_token: builtins.str
    """Optional. The next_page_token value returned from a previous list request.
    The page token to support pagination.
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
        session_id: builtins.str = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_token", b"page_token", "session_id", b"session_id"]) -> None: ...

global___ListContextsRequest = ListContextsRequest

@typing.final
class ListContextsResponse(google.protobuf.message.Message):
    """The response message for [Contexts.ListContexts][google.cloud.dialogflow.v2.Contexts.ListContexts]."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTEXTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """
    @property
    def contexts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Context]:
        """The list of contexts. There will be a maximum number of items
        returned based on the page_token field in the request.
        """

    def __init__(
        self,
        *,
        contexts: collections.abc.Iterable[global___Context] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["contexts", b"contexts", "next_page_token", b"next_page_token"]) -> None: ...

global___ListContextsResponse = ListContextsResponse

@typing.final
class GetContextRequest(google.protobuf.message.Message):
    """The request message for [Contexts.GetContext][google.cloud.dialogflow.v2.Contexts.GetContext]."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Required. The name of the context. Format:
    `projects/<Project ID>/agent/sessions/<Session ID>/contexts/<Context ID>`.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name"]) -> None: ...

global___GetContextRequest = GetContextRequest

@typing.final
class CreateContextRequest(google.protobuf.message.Message):
    """The request message for [Contexts.CreateContext][google.cloud.dialogflow.v2.Contexts.CreateContext]."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_ID_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    session_id: builtins.str
    """Required. The session to create a context for.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/sessions/&lt;session_uuid&gt;</code></pre>
    """
    @property
    def context(self) -> global___Context:
        """Required. The context to create."""

    def __init__(
        self,
        *,
        session_id: builtins.str = ...,
        context: global___Context | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["context", b"context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["context", b"context", "session_id", b"session_id"]) -> None: ...

global___CreateContextRequest = CreateContextRequest

@typing.final
class UpdateContextRequest(google.protobuf.message.Message):
    """The request message for [Contexts.UpdateContext][google.cloud.dialogflow.v2.Contexts.UpdateContext]."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTEXT_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def context(self) -> global___Context:
        """Required. The context to update."""

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. The mask to control which fields get updated."""

    def __init__(
        self,
        *,
        context: global___Context | None = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["context", b"context", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["context", b"context", "update_mask", b"update_mask"]) -> None: ...

global___UpdateContextRequest = UpdateContextRequest

@typing.final
class DeleteContextRequest(google.protobuf.message.Message):
    """The request message for [Contexts.DeleteContext][google.cloud.dialogflow.v2.Contexts.DeleteContext]."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Required. The name of the context to delete. Format:
    `projects/<Project ID>/agent/sessions/<Session ID>/contexts/<Context ID>`.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name"]) -> None: ...

global___DeleteContextRequest = DeleteContextRequest

@typing.final
class DeleteAllContextsRequest(google.protobuf.message.Message):
    """The request message for [Contexts.DeleteAllContexts][google.cloud.dialogflow.v2.Contexts.DeleteAllContexts].
    Required. The name of the session to delete all contexts from.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/sessions/&lt;session_uuid&gt;</code></pre>
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_ID_FIELD_NUMBER: builtins.int
    session_id: builtins.str
    def __init__(
        self,
        *,
        session_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["session_id", b"session_id"]) -> None: ...

global___DeleteAllContextsRequest = DeleteAllContextsRequest
