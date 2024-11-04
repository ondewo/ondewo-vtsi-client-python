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
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import ondewo.nlu.entity_type_pb2
import ondewo.nlu.intent_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ReannotateEntitiesOptions:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ReannotateEntitiesOptionsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ReannotateEntitiesOptions.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    REANNOTATE_NEVER: _ReannotateEntitiesOptions.ValueType  # 0
    """Never re-annotate training phrases"""
    REANNOTATE_ALWAYS: _ReannotateEntitiesOptions.ValueType  # 1
    """Always re-annotate training phrases"""
    REANNOTATE_IF_EMPTY: _ReannotateEntitiesOptions.ValueType  # 2
    """Re-annotate training phrases if there are no annotations"""
    REANNOTATE_AFTER_DELETION: _ReannotateEntitiesOptions.ValueType  # 3
    """Re-annotate if training phrases have been deleted"""
    REANNOTATE_IF_EMPTY_OR_AFTER_DELETION: _ReannotateEntitiesOptions.ValueType  # 4
    """Re-annotate if there are no annotations or if training phrases have been deleted"""

class ReannotateEntitiesOptions(_ReannotateEntitiesOptions, metaclass=_ReannotateEntitiesOptionsEnumTypeWrapper):
    """Encapsulates entity re-annotation options"""

REANNOTATE_NEVER: ReannotateEntitiesOptions.ValueType  # 0
"""Never re-annotate training phrases"""
REANNOTATE_ALWAYS: ReannotateEntitiesOptions.ValueType  # 1
"""Always re-annotate training phrases"""
REANNOTATE_IF_EMPTY: ReannotateEntitiesOptions.ValueType  # 2
"""Re-annotate training phrases if there are no annotations"""
REANNOTATE_AFTER_DELETION: ReannotateEntitiesOptions.ValueType  # 3
"""Re-annotate if training phrases have been deleted"""
REANNOTATE_IF_EMPTY_OR_AFTER_DELETION: ReannotateEntitiesOptions.ValueType  # 4
"""Re-annotate if there are no annotations or if training phrases have been deleted"""
global___ReannotateEntitiesOptions = ReannotateEntitiesOptions

@typing.final
class ValidateRegexRequest(google.protobuf.message.Message):
    """The request to validate regexes."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGEX_FIELD_NUMBER: builtins.int
    regex: builtins.str
    """String containing the regex."""
    def __init__(
        self,
        *,
        regex: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["regex", b"regex"]) -> None: ...

global___ValidateRegexRequest = ValidateRegexRequest

@typing.final
class ValidateRegexResponse(google.protobuf.message.Message):
    """The response of the regex validation"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_MESSAGES_FIELD_NUMBER: builtins.int
    @property
    def error_messages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Error messages"""

    def __init__(
        self,
        *,
        error_messages: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["error_messages", b"error_messages"]) -> None: ...

global___ValidateRegexResponse = ValidateRegexResponse

@typing.final
class ValidateEmbeddedRegexRequest(google.protobuf.message.Message):
    """Validation request for entity type values"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENTITY_TYPE_FIELD_NUMBER: builtins.int
    @property
    def entity_type(self) -> ondewo.nlu.entity_type_pb2.EntityType.Entity: ...
    def __init__(
        self,
        *,
        entity_type: ondewo.nlu.entity_type_pb2.EntityType.Entity | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["entity_type", b"entity_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["entity_type", b"entity_type"]) -> None: ...

global___ValidateEmbeddedRegexRequest = ValidateEmbeddedRegexRequest

@typing.final
class ValidateEmbeddedRegexResponse(google.protobuf.message.Message):
    """Response of the entity type validation"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_MESSAGES_FIELD_NUMBER: builtins.int
    @property
    def error_messages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of error message from the validation"""

    def __init__(
        self,
        *,
        error_messages: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["error_messages", b"error_messages"]) -> None: ...

global___ValidateEmbeddedRegexResponse = ValidateEmbeddedRegexResponse

@typing.final
class CleanAllIntentsRequest(google.protobuf.message.Message):
    """The request to clean the all intents."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    SPECIAL_CHARACTERS_FIELD_NUMBER: builtins.int
    SUBSTRING_WHITE_LIST_FIELD_NUMBER: builtins.int
    DRY_RUN_FIELD_NUMBER: builtins.int
    TRAINING_PHRASE_CLEANER_OPTIONS_FIELD_NUMBER: builtins.int
    REANNOTATE_ENTITIES_OPTIONS_FIELD_NUMBER: builtins.int
    NUMBER_OF_WORKERS_FIELD_NUMBER: builtins.int
    parent: builtins.str
    """Required. The agent to list all intents from.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent</code></pre>
    """
    language_code: builtins.str
    """Optional. The language to list training phrases, parameters and rich
    messages for. If not specified, the agent's default language is used.
    Note: languages must be enabled in the agent before they can be used.
    """
    special_characters: builtins.str
    """Optional. Characters to be recognized as special characters for cleaning.
    Overrides the default: '.,;!?:'
    """
    dry_run: builtins.bool
    """Required. Do not apply changes to the database if set to True"""
    reannotate_entities_options: global___ReannotateEntitiesOptions.ValueType
    """Optional. Options for re-annotation of entities (default = REANNOTATE_NEVER)"""
    number_of_workers: builtins.int
    """Optional. Number of threads used to accomplish the task"""
    @property
    def substring_white_list(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional. List of substring that shall not be cleaned/deleted.
        Example: ['St.', 'U.S.', 'sys.', '24.12.', 'Nr.', 'TelNr.']
        Default = None
        """

    @property
    def training_phrase_cleaner_options(self) -> global___TrainingPhraseCleanerOptions:
        """Optional. Options for the cleaning of the training phrases."""

    def __init__(
        self,
        *,
        parent: builtins.str = ...,
        language_code: builtins.str = ...,
        special_characters: builtins.str = ...,
        substring_white_list: collections.abc.Iterable[builtins.str] | None = ...,
        dry_run: builtins.bool = ...,
        training_phrase_cleaner_options: global___TrainingPhraseCleanerOptions | None = ...,
        reannotate_entities_options: global___ReannotateEntitiesOptions.ValueType = ...,
        number_of_workers: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["training_phrase_cleaner_options", b"training_phrase_cleaner_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["dry_run", b"dry_run", "language_code", b"language_code", "number_of_workers", b"number_of_workers", "parent", b"parent", "reannotate_entities_options", b"reannotate_entities_options", "special_characters", b"special_characters", "substring_white_list", b"substring_white_list", "training_phrase_cleaner_options", b"training_phrase_cleaner_options"]) -> None: ...

global___CleanAllIntentsRequest = CleanAllIntentsRequest

@typing.final
class CleanAllIntentsResponse(google.protobuf.message.Message):
    """Response corresponding to the CleanAllIntents Request"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLEANED_INTENTS_FIELD_NUMBER: builtins.int
    INTENT_UPDATE_LIST_FIELD_NUMBER: builtins.int
    @property
    def cleaned_intents(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ondewo.nlu.intent_pb2.Intent]:
        """Required. List of updates performed on intents"""

    @property
    def intent_update_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___IntentUpdate]:
        """Optional. List of updates applied to intents"""

    def __init__(
        self,
        *,
        cleaned_intents: collections.abc.Iterable[ondewo.nlu.intent_pb2.Intent] | None = ...,
        intent_update_list: collections.abc.Iterable[global___IntentUpdate] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cleaned_intents", b"cleaned_intents", "intent_update_list", b"intent_update_list"]) -> None: ...

global___CleanAllIntentsResponse = CleanAllIntentsResponse

@typing.final
class CleanIntentRequest(google.protobuf.message.Message):
    """The request message to clean a single intents."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_FIELD_NUMBER: builtins.int
    INTENT_NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    SPECIAL_CHARACTERS_FIELD_NUMBER: builtins.int
    SUBSTRING_WHITE_LIST_FIELD_NUMBER: builtins.int
    DRY_RUN_FIELD_NUMBER: builtins.int
    TRAINING_PHRASE_CLEANER_OPTIONS_FIELD_NUMBER: builtins.int
    REANNOTATE_ENTITIES_OPTIONS_FIELD_NUMBER: builtins.int
    parent: builtins.str
    """Required. The agent to list all intents from.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent</code></pre>
    """
    intent_name: builtins.str
    """Required. The name of the intent.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent/intents/&lt;intent_uuid&gt;</code></pre>
    """
    language_code: builtins.str
    """Optional. The language to list training phrases, parameters and rich
    messages for. If not specified, the agent's default language is used.
    Note: languages must be enabled in the agent before they can be used.
    """
    special_characters: builtins.str
    """Optional. Characters to be recognized as special characters for cleaning.
    Overrides the default: '.,;!?:'
    """
    dry_run: builtins.bool
    """Required. Do not apply changes to the database if set to True"""
    reannotate_entities_options: global___ReannotateEntitiesOptions.ValueType
    """Optional. Options for re-annotation of entities (default = REANNOTATE_NEVER)"""
    @property
    def substring_white_list(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional. List of substring that shall not be cleaned/deleted.
        Example: ['St.', 'U.S.', 'sys.', '24.12.', 'Nr.', 'TelNr.']
        Default = None
        """

    @property
    def training_phrase_cleaner_options(self) -> global___TrainingPhraseCleanerOptions:
        """Optional. Options for the cleaning of the training phrases."""

    def __init__(
        self,
        *,
        parent: builtins.str = ...,
        intent_name: builtins.str = ...,
        language_code: builtins.str = ...,
        special_characters: builtins.str = ...,
        substring_white_list: collections.abc.Iterable[builtins.str] | None = ...,
        dry_run: builtins.bool = ...,
        training_phrase_cleaner_options: global___TrainingPhraseCleanerOptions | None = ...,
        reannotate_entities_options: global___ReannotateEntitiesOptions.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["training_phrase_cleaner_options", b"training_phrase_cleaner_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["dry_run", b"dry_run", "intent_name", b"intent_name", "language_code", b"language_code", "parent", b"parent", "reannotate_entities_options", b"reannotate_entities_options", "special_characters", b"special_characters", "substring_white_list", b"substring_white_list", "training_phrase_cleaner_options", b"training_phrase_cleaner_options"]) -> None: ...

global___CleanIntentRequest = CleanIntentRequest

@typing.final
class CleanIntentResponse(google.protobuf.message.Message):
    """The response message to clean a single intents."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLEANED_INTENT_FIELD_NUMBER: builtins.int
    INTENT_UPDATE_FIELD_NUMBER: builtins.int
    @property
    def cleaned_intent(self) -> ondewo.nlu.intent_pb2.Intent:
        """Required. Cleaned Intent"""

    @property
    def intent_update(self) -> global___IntentUpdate:
        """Optional. Updates applied to intent"""

    def __init__(
        self,
        *,
        cleaned_intent: ondewo.nlu.intent_pb2.Intent | None = ...,
        intent_update: global___IntentUpdate | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cleaned_intent", b"cleaned_intent", "intent_update", b"intent_update"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cleaned_intent", b"cleaned_intent", "intent_update", b"intent_update"]) -> None: ...

global___CleanIntentResponse = CleanIntentResponse

@typing.final
class TrainingPhraseCleanerOptions(google.protobuf.message.Message):
    """Options for cleaning the training phrases"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELETE_REPEATED_WHITESPACES_FIELD_NUMBER: builtins.int
    DELETE_LEADING_SPECIAL_CHARACTERS_FIELD_NUMBER: builtins.int
    DELETE_TRAILING_SPECIAL_CHARACTERS_FIELD_NUMBER: builtins.int
    delete_repeated_whitespaces: builtins.bool
    """Whether or not to delete repeated whitespaces"""
    delete_leading_special_characters: builtins.bool
    """Whether of not to delete leading special characters"""
    delete_trailing_special_characters: builtins.bool
    """Whether of not to delete trailing special characters"""
    def __init__(
        self,
        *,
        delete_repeated_whitespaces: builtins.bool = ...,
        delete_leading_special_characters: builtins.bool = ...,
        delete_trailing_special_characters: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["delete_leading_special_characters", b"delete_leading_special_characters", "delete_repeated_whitespaces", b"delete_repeated_whitespaces", "delete_trailing_special_characters", b"delete_trailing_special_characters"]) -> None: ...

global___TrainingPhraseCleanerOptions = TrainingPhraseCleanerOptions

@typing.final
class StringUpdate(google.protobuf.message.Message):
    """Message to keep track of updated strings"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NEW_FIELD_NUMBER: builtins.int
    OLD_FIELD_NUMBER: builtins.int
    new: builtins.str
    """New version of the string"""
    old: builtins.str
    """Old version of the string"""
    def __init__(
        self,
        *,
        new: builtins.str = ...,
        old: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["new", b"new", "old", b"old"]) -> None: ...

global___StringUpdate = StringUpdate

@typing.final
class IntentUpdate(google.protobuf.message.Message):
    """Stores updates applied to an intent"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class TrainingPhraseUpdate(google.protobuf.message.Message):
        """Message to track the updates made to a training phrase"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TRAINING_PHRASE_UPDATE_FIELD_NUMBER: builtins.int
        ENTITY_UPDATES_FIELD_NUMBER: builtins.int
        ENTITIES_REANNOTATED_FIELD_NUMBER: builtins.int
        CONTAINS_UPDATE_VARIABLE_FIELD_NUMBER: builtins.int
        contains_update_variable: builtins.bool
        """Will be switched to True if at least one update has been performed"""
        @property
        def training_phrase_update(self) -> global___StringUpdate:
            """Stores updates of training phrases"""

        @property
        def entity_updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StringUpdate]:
            """Stores updates of entity strings"""

        @property
        def entities_reannotated(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """Stores re-annotated entity strings"""

        def __init__(
            self,
            *,
            training_phrase_update: global___StringUpdate | None = ...,
            entity_updates: collections.abc.Iterable[global___StringUpdate] | None = ...,
            entities_reannotated: collections.abc.Iterable[builtins.str] | None = ...,
            contains_update_variable: builtins.bool = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["training_phrase_update", b"training_phrase_update"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["contains_update_variable", b"contains_update_variable", "entities_reannotated", b"entities_reannotated", "entity_updates", b"entity_updates", "training_phrase_update", b"training_phrase_update"]) -> None: ...

    INTENT_DISPLAY_NAME_FIELD_NUMBER: builtins.int
    TRAINING_PHRASE_UPDATE_LIST_FIELD_NUMBER: builtins.int
    DELETED_PARAMETERS_FIELD_NUMBER: builtins.int
    intent_display_name: builtins.str
    """The display name of the intent"""
    @property
    def training_phrase_update_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___IntentUpdate.TrainingPhraseUpdate]:
        """List of the updated training phrases"""

    @property
    def deleted_parameters(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of the deleted parameters"""

    def __init__(
        self,
        *,
        intent_display_name: builtins.str = ...,
        training_phrase_update_list: collections.abc.Iterable[global___IntentUpdate.TrainingPhraseUpdate] | None = ...,
        deleted_parameters: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["deleted_parameters", b"deleted_parameters", "intent_display_name", b"intent_display_name", "training_phrase_update_list", b"training_phrase_update_list"]) -> None: ...

global___IntentUpdate = IntentUpdate

@typing.final
class EntityTypeUpdate(google.protobuf.message.Message):
    """Stores updates applied to an entity type"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class EntityUpdate(google.protobuf.message.Message):
        """Stores updates applied to an entity"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ENTITY_VALUE_UPDATE_FIELD_NUMBER: builtins.int
        ENTITY_SYNONYM_UPDATES_FIELD_NUMBER: builtins.int
        @property
        def entity_value_update(self) -> global___StringUpdate:
            """Updates made to the entity value"""

        @property
        def entity_synonym_updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StringUpdate]:
            """Updates made to the entity synonyms"""

        def __init__(
            self,
            *,
            entity_value_update: global___StringUpdate | None = ...,
            entity_synonym_updates: collections.abc.Iterable[global___StringUpdate] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["entity_value_update", b"entity_value_update"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["entity_synonym_updates", b"entity_synonym_updates", "entity_value_update", b"entity_value_update"]) -> None: ...

    ENTITY_TYPE_NAME_FIELD_NUMBER: builtins.int
    VALUES_UPDATE_LIST_FIELD_NUMBER: builtins.int
    entity_type_name: builtins.str
    """The entity type name"""
    @property
    def values_update_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityTypeUpdate.EntityUpdate]:
        """List of the updated entities"""

    def __init__(
        self,
        *,
        entity_type_name: builtins.str = ...,
        values_update_list: collections.abc.Iterable[global___EntityTypeUpdate.EntityUpdate] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["entity_type_name", b"entity_type_name", "values_update_list", b"values_update_list"]) -> None: ...

global___EntityTypeUpdate = EntityTypeUpdate

@typing.final
class CleanAllEntityTypesRequest(google.protobuf.message.Message):
    """Request to clean the entity types"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    SPECIAL_CHARACTERS_FIELD_NUMBER: builtins.int
    SUBSTRING_WHITE_LIST_FIELD_NUMBER: builtins.int
    MAX_ENTITY_COUNT_UPDATE_FIELD_NUMBER: builtins.int
    FORBIDDEN_ENTITY_TYPE_PATTERNS_FIELD_NUMBER: builtins.int
    DRY_RUN_FIELD_NUMBER: builtins.int
    NUMBER_OF_WORKERS_FIELD_NUMBER: builtins.int
    parent: builtins.str
    """Required. The agent to list all intents from.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent</code></pre>
    """
    language_code: builtins.str
    """Optional. The language to list training phrases, parameters and rich
    messages for. If not specified, the agent's default language is used.
    Note: languages must be enabled in the agent before they can be used.
    """
    special_characters: builtins.str
    """Optional. Characters to be recognized as special characters for cleaning.
    Overrides the default: '.,;!?:'
    """
    max_entity_count_update: builtins.int
    """Optional. Entity type that contain more than max_entity_count_update entities will
    not be cleaned. Relevant for auto-generated entity values (e.g. City Names)
    Default = 10000
    """
    dry_run: builtins.bool
    """Required. Do not apply changes to the database if set to True"""
    number_of_workers: builtins.int
    """Optional. Number of threads used to accomplish the task"""
    @property
    def substring_white_list(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional. List of substring that shall not be cleaned/deleted.
        Example: ['St.', 'U.S.', 'sys.', '24.12.', 'Nr.', 'TelNr.']
        """

    @property
    def forbidden_entity_type_patterns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional. List of strings or regexes. Entity types will be deleted if their display
        name matches an element of this list
        Example: ['sys.ignore.'] -> would delete entity types with display names sys.ignore.*
        """

    def __init__(
        self,
        *,
        parent: builtins.str = ...,
        language_code: builtins.str = ...,
        special_characters: builtins.str = ...,
        substring_white_list: collections.abc.Iterable[builtins.str] | None = ...,
        max_entity_count_update: builtins.int = ...,
        forbidden_entity_type_patterns: collections.abc.Iterable[builtins.str] | None = ...,
        dry_run: builtins.bool = ...,
        number_of_workers: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dry_run", b"dry_run", "forbidden_entity_type_patterns", b"forbidden_entity_type_patterns", "language_code", b"language_code", "max_entity_count_update", b"max_entity_count_update", "number_of_workers", b"number_of_workers", "parent", b"parent", "special_characters", b"special_characters", "substring_white_list", b"substring_white_list"]) -> None: ...

global___CleanAllEntityTypesRequest = CleanAllEntityTypesRequest

@typing.final
class CleanAllEntityTypesResponse(google.protobuf.message.Message):
    """Response from entity type cleaner"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLEANED_ENTITY_TYPES_FIELD_NUMBER: builtins.int
    DELETED_ENTITY_TYPES_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_UPDATES_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_DELETIONS_FIELD_NUMBER: builtins.int
    @property
    def cleaned_entity_types(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ondewo.nlu.entity_type_pb2.EntityType]:
        """Required. List of updated entity types"""

    @property
    def deleted_entity_types(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ondewo.nlu.entity_type_pb2.EntityType]:
        """Optional. List of updated entity types"""

    @property
    def entity_type_updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityTypeUpdate]:
        """Optional. List of updates performed on entity types"""

    @property
    def entity_type_deletions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityTypeUpdate]:
        """Optional. List of the deleted entity types"""

    def __init__(
        self,
        *,
        cleaned_entity_types: collections.abc.Iterable[ondewo.nlu.entity_type_pb2.EntityType] | None = ...,
        deleted_entity_types: collections.abc.Iterable[ondewo.nlu.entity_type_pb2.EntityType] | None = ...,
        entity_type_updates: collections.abc.Iterable[global___EntityTypeUpdate] | None = ...,
        entity_type_deletions: collections.abc.Iterable[global___EntityTypeUpdate] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cleaned_entity_types", b"cleaned_entity_types", "deleted_entity_types", b"deleted_entity_types", "entity_type_deletions", b"entity_type_deletions", "entity_type_updates", b"entity_type_updates"]) -> None: ...

global___CleanAllEntityTypesResponse = CleanAllEntityTypesResponse

@typing.final
class CleanEntityTypeRequest(google.protobuf.message.Message):
    """Request to clean a single entity type"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    SPECIAL_CHARACTERS_FIELD_NUMBER: builtins.int
    SUBSTRING_WHITE_LIST_FIELD_NUMBER: builtins.int
    MAX_ENTITY_COUNT_UPDATE_FIELD_NUMBER: builtins.int
    DRY_RUN_FIELD_NUMBER: builtins.int
    parent: builtins.str
    """Required. The agent to list all intents from.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent</code></pre>
    """
    entity_type_name: builtins.str
    """Required. The name of the entity_type"""
    language_code: builtins.str
    """Optional. The language to list training phrases, parameters and rich
    messages for. If not specified, the agent's default language is used.
    Note: languages must be enabled in the agent before they can be used.
    """
    special_characters: builtins.str
    """Optional. Characters to be recognized as special characters for cleaning.
    Overrides the default: '.,;!?:'
    """
    max_entity_count_update: builtins.int
    """Optional. Entity type that contain more than max_entity_count_update entities will
    not be cleaned. Relevant for auto-generated entity values (e.g. City Names)
    Default = 10000
    """
    dry_run: builtins.bool
    """Required. Do not apply changes to the database if set to True"""
    @property
    def substring_white_list(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional. List of substring that shall not be cleaned/deleted.
        Example: ['St.', 'U.S.', 'sys.', '24.12.', 'Nr.', 'TelNr.']
        """

    def __init__(
        self,
        *,
        parent: builtins.str = ...,
        entity_type_name: builtins.str = ...,
        language_code: builtins.str = ...,
        special_characters: builtins.str = ...,
        substring_white_list: collections.abc.Iterable[builtins.str] | None = ...,
        max_entity_count_update: builtins.int = ...,
        dry_run: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dry_run", b"dry_run", "entity_type_name", b"entity_type_name", "language_code", b"language_code", "max_entity_count_update", b"max_entity_count_update", "parent", b"parent", "special_characters", b"special_characters", "substring_white_list", b"substring_white_list"]) -> None: ...

global___CleanEntityTypeRequest = CleanEntityTypeRequest

@typing.final
class CleanEntityTypeResponse(google.protobuf.message.Message):
    """Response from entity type cleaner"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLEANED_ENTITY_TYPE_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_UPDATE_FIELD_NUMBER: builtins.int
    @property
    def cleaned_entity_type(self) -> ondewo.nlu.entity_type_pb2.EntityType:
        """Required. The cleaned entity type"""

    @property
    def entity_type_update(self) -> global___EntityTypeUpdate:
        """Optional. The updated entity type"""

    def __init__(
        self,
        *,
        cleaned_entity_type: ondewo.nlu.entity_type_pb2.EntityType | None = ...,
        entity_type_update: global___EntityTypeUpdate | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cleaned_entity_type", b"cleaned_entity_type", "entity_type_update", b"entity_type_update"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cleaned_entity_type", b"cleaned_entity_type", "entity_type_update", b"entity_type_update"]) -> None: ...

global___CleanEntityTypeResponse = CleanEntityTypeResponse

@typing.final
class AddTrainingPhrasesRequest(google.protobuf.message.Message):
    """Request message to AddTrainingPhrase rpc"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class TrainingPhraseForIntent(google.protobuf.message.Message):
        """Message that contains the new training phrase, together with the intent display name
        and, optionally the entity annotations
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TRAINING_PHRASE_FIELD_NUMBER: builtins.int
        INTENT_DISPLAY_NAME_FIELD_NUMBER: builtins.int
        ENTITIES_FIELD_NUMBER: builtins.int
        training_phrase: builtins.str
        """Required. New training phrase to be added"""
        intent_display_name: builtins.str
        """Required. Corresponding display name of the intent"""
        @property
        def entities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ondewo.nlu.intent_pb2.Intent.TrainingPhrase.Entity]:
            """Optional. Entity annotations"""

        def __init__(
            self,
            *,
            training_phrase: builtins.str = ...,
            intent_display_name: builtins.str = ...,
            entities: collections.abc.Iterable[ondewo.nlu.intent_pb2.Intent.TrainingPhrase.Entity] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["entities", b"entities", "intent_display_name", b"intent_display_name", "training_phrase", b"training_phrase"]) -> None: ...

    PARENT_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    TRAINING_PHRASE_LIST_FIELD_NUMBER: builtins.int
    EXTRACT_ENTITIES_FIELD_NUMBER: builtins.int
    SPECIAL_CHARACTERS_FIELD_NUMBER: builtins.int
    TRAINING_PHRASE_CLEANER_OPTIONS_FIELD_NUMBER: builtins.int
    NUMBER_OF_WORKERS_FIELD_NUMBER: builtins.int
    parent: builtins.str
    """Required. The agent to list all intents from.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent</code></pre>
    """
    language_code: builtins.str
    """Required. The language to list training phrases, parameters and rich
    messages for. If not specified, the agent's default language is used.
    Note: languages must be enabled in the agent before they can be used.
    """
    extract_entities: builtins.bool
    """Optional. Whether or not to extract entities for the new training phrases"""
    special_characters: builtins.str
    """Optional. Characters to be recognized as special characters for cleaning
    the training phrases. Overrides the default: '.,;!?:'
    """
    number_of_workers: builtins.int
    """Optional. Number of threads used to accomplish the task"""
    @property
    def training_phrase_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AddTrainingPhrasesRequest.TrainingPhraseForIntent]:
        """Required. List of training phrases to be added to the intent"""

    @property
    def training_phrase_cleaner_options(self) -> global___TrainingPhraseCleanerOptions:
        """Optional. Options for the training phrase cleaner to override the default settings"""

    def __init__(
        self,
        *,
        parent: builtins.str = ...,
        language_code: builtins.str = ...,
        training_phrase_list: collections.abc.Iterable[global___AddTrainingPhrasesRequest.TrainingPhraseForIntent] | None = ...,
        extract_entities: builtins.bool = ...,
        special_characters: builtins.str = ...,
        training_phrase_cleaner_options: global___TrainingPhraseCleanerOptions | None = ...,
        number_of_workers: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["training_phrase_cleaner_options", b"training_phrase_cleaner_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["extract_entities", b"extract_entities", "language_code", b"language_code", "number_of_workers", b"number_of_workers", "parent", b"parent", "special_characters", b"special_characters", "training_phrase_cleaner_options", b"training_phrase_cleaner_options", "training_phrase_list", b"training_phrase_list"]) -> None: ...

global___AddTrainingPhrasesRequest = AddTrainingPhrasesRequest

@typing.final
class AddTrainingPhrasesResponse(google.protobuf.message.Message):
    """Response message to AddTrainingPhrase rpc"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_MESSAGES_FIELD_NUMBER: builtins.int
    @property
    def error_messages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Required. If something goes wrong, error messages will be conveyed via a repeated string"""

    def __init__(
        self,
        *,
        error_messages: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["error_messages", b"error_messages"]) -> None: ...

global___AddTrainingPhrasesResponse = AddTrainingPhrasesResponse

@typing.final
class AddTrainingPhrasesFromCSVRequest(google.protobuf.message.Message):
    """Request message to AddTrainingPhraseFromCSV rpc"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    CSV_CONTENTS_FIELD_NUMBER: builtins.int
    EXTRACT_ENTITIES_FIELD_NUMBER: builtins.int
    SPECIAL_CHARACTERS_FIELD_NUMBER: builtins.int
    TRAINING_PHRASE_CLEANER_OPTIONS_FIELD_NUMBER: builtins.int
    NUMBER_OF_WORKERS_FIELD_NUMBER: builtins.int
    parent: builtins.str
    """Required. The agent to list all intents from.
    Format: <pre><code>projects/&lt;project_uuid&gt;/agent</code></pre>
    """
    language_code: builtins.str
    """Required. The language to list training phrases, parameters and rich
    messages for. If not specified, the agent's default language is used.
    Note: languages must be enabled in the agent before they can be used.
    """
    csv_contents: builtins.bytes
    """Required. Contents of the .csv file containing training phrases to be added to the intents"""
    extract_entities: builtins.bool
    """Optional. Whether or not to extract entities for the new training phrases"""
    special_characters: builtins.str
    """Optional. Before new training phrases are added to their corresponding intent,
    they are cleaned with cleaning scripts. These cleaning scripts remove certain special characters,
    if they are found at the beginning of the text or if they appear in annotations.
    Overrides the default: '.,;!?:'
    """
    number_of_workers: builtins.int
    """Optional. Number of threads used to accomplish the task"""
    @property
    def training_phrase_cleaner_options(self) -> global___TrainingPhraseCleanerOptions:
        """Optional. Options for the training phrase cleaner to override the default settings"""

    def __init__(
        self,
        *,
        parent: builtins.str = ...,
        language_code: builtins.str = ...,
        csv_contents: builtins.bytes = ...,
        extract_entities: builtins.bool = ...,
        special_characters: builtins.str = ...,
        training_phrase_cleaner_options: global___TrainingPhraseCleanerOptions | None = ...,
        number_of_workers: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["training_phrase_cleaner_options", b"training_phrase_cleaner_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["csv_contents", b"csv_contents", "extract_entities", b"extract_entities", "language_code", b"language_code", "number_of_workers", b"number_of_workers", "parent", b"parent", "special_characters", b"special_characters", "training_phrase_cleaner_options", b"training_phrase_cleaner_options"]) -> None: ...

global___AddTrainingPhrasesFromCSVRequest = AddTrainingPhrasesFromCSVRequest
