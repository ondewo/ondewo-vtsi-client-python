# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ondewo.nlu import entity_type_pb2 as ondewo_dot_nlu_dot_entity__type__pb2
from ondewo.nlu import operations_pb2 as ondewo_dot_nlu_dot_operations__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},' +
        f' but the generated code in ondewo/nlu/entity_type_pb2_grpc.py depends on' +
        f' grpcio>={GRPC_GENERATED_VERSION}.' +
        f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' +
        f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class EntityTypesStub(object):
    """Entities are extracted from user input and represent parameters that are
    meaningful to your application. For example, a date range, a proper name
    such as a geographic location or landmark, and so on. Entities represent
    actionable data for your application.

    When you define an entity, you can also include synonyms that all map to
    that entity. For example, "soft drink", "soda", "pop", and so on.

    There are three types of entities:

    *   **System** - entities that are defined by the Dialogflow API for common
    data types such as date, time, currency, and so on. A system entity is
    represented by the `EntityType` type.

    *   **Developer** - entities that are defined by you that represent
    actionable data that is meaningful to your application. For example,
    you could define a `pizza.sauce` entity for red or white pizza sauce,
    a `pizza.cheese` entity for the different types of cheese on a pizza,
    a `pizza.topping` entity for different toppings, and so on. A developer
    entity is represented by the `EntityType` type.

    *   **User** - entities that are built for an individual user such as
    favorites, preferences, playlists, and so on. A user entity is
    represented by the [SessionEntityType][google.cloud.dialogflow.v2.SessionEntityType] type.

    For more information about entity types, see the
    [Dialogflow documentation](https://dialogflow.com/docs/entities).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListEntityTypes = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/ListEntityTypes',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.ListEntityTypesRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.ListEntityTypesResponse.FromString,
            _registered_method=True)
        self.GetEntityType = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/GetEntityType',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.GetEntityTypeRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.FromString,
            _registered_method=True)
        self.CreateEntityType = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/CreateEntityType',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.CreateEntityTypeRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.FromString,
            _registered_method=True)
        self.UpdateEntityType = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/UpdateEntityType',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.UpdateEntityTypeRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.FromString,
            _registered_method=True)
        self.DeleteEntityType = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/DeleteEntityType',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.DeleteEntityTypeRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            _registered_method=True)
        self.BatchUpdateEntityTypes = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/BatchUpdateEntityTypes',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchUpdateEntityTypesRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_operations__pb2.Operation.FromString,
            _registered_method=True)
        self.BatchDeleteEntityTypes = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/BatchDeleteEntityTypes',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchDeleteEntityTypesRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_operations__pb2.Operation.FromString,
            _registered_method=True)
        self.GetEntity = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/GetEntity',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.GetEntityRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.Entity.FromString,
            _registered_method=True)
        self.CreateEntity = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/CreateEntity',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.CreateEntityRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.Entity.FromString,
            _registered_method=True)
        self.UpdateEntity = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/UpdateEntity',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.UpdateEntityRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.Entity.FromString,
            _registered_method=True)
        self.DeleteEntity = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/DeleteEntity',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.DeleteEntityRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.DeleteEntityStatus.FromString,
            _registered_method=True)
        self.BatchCreateEntities = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/BatchCreateEntities',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchCreateEntitiesRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchEntitiesResponse.FromString,
            _registered_method=True)
        self.BatchUpdateEntities = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/BatchUpdateEntities',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchUpdateEntitiesRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchEntitiesResponse.FromString,
            _registered_method=True)
        self.BatchGetEntities = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/BatchGetEntities',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchGetEntitiesRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchEntitiesResponse.FromString,
            _registered_method=True)
        self.BatchDeleteEntities = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/BatchDeleteEntities',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchDeleteEntitiesRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchDeleteEntitiesResponse.FromString,
            _registered_method=True)
        self.ListEntities = channel.unary_unary(
            '/ondewo.nlu.EntityTypes/ListEntities',
            request_serializer=ondewo_dot_nlu_dot_entity__type__pb2.ListEntitiesRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.ListEntitiesResponse.FromString,
            _registered_method=True)


class EntityTypesServicer(object):
    """Entities are extracted from user input and represent parameters that are
    meaningful to your application. For example, a date range, a proper name
    such as a geographic location or landmark, and so on. Entities represent
    actionable data for your application.

    When you define an entity, you can also include synonyms that all map to
    that entity. For example, "soft drink", "soda", "pop", and so on.

    There are three types of entities:

    *   **System** - entities that are defined by the Dialogflow API for common
    data types such as date, time, currency, and so on. A system entity is
    represented by the `EntityType` type.

    *   **Developer** - entities that are defined by you that represent
    actionable data that is meaningful to your application. For example,
    you could define a `pizza.sauce` entity for red or white pizza sauce,
    a `pizza.cheese` entity for the different types of cheese on a pizza,
    a `pizza.topping` entity for different toppings, and so on. A developer
    entity is represented by the `EntityType` type.

    *   **User** - entities that are built for an individual user such as
    favorites, preferences, playlists, and so on. A user entity is
    represented by the [SessionEntityType][google.cloud.dialogflow.v2.SessionEntityType] type.

    For more information about entity types, see the
    [Dialogflow documentation](https://dialogflow.com/docs/entities).
    """

    def ListEntityTypes(self, request, context):
        """Returns the list of all entity types in the specified agent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEntityType(self, request, context):
        """Retrieves the specified entity type.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEntityType(self, request, context):
        """Creates an entity type in the specified agent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEntityType(self, request, context):
        """Updates the specified entity type.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEntityType(self, request, context):
        """Deletes the specified entity type.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchUpdateEntityTypes(self, request, context):
        """Updates/Creates multiple entity types in the specified agent.

        Operation <response: [BatchUpdateEntityTypesResponse][google.cloud.dialogflow.v2.BatchUpdateEntityTypesResponse],
        metadata: [google.protobuf.Struct][google.protobuf.Struct]>
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchDeleteEntityTypes(self, request, context):
        """Deletes entity types in the specified agent.

        Operation <response: [google.protobuf.Empty][google.protobuf.Empty],
        metadata: [google.protobuf.Struct][google.protobuf.Struct]>
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEntity(self, request, context):
        """Retrieves the specified entity .
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEntity(self, request, context):
        """Creates an entity  in the specified agent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEntity(self, request, context):
        """Updates the specified entity .
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEntity(self, request, context):
        """Deletes the specified entity .
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchCreateEntities(self, request, context):
        """Creates an entity value in an entity type.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchUpdateEntities(self, request, context):
        """Updates a specific entity value.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetEntities(self, request, context):
        """Gets a specific entity value.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchDeleteEntities(self, request, context):
        """Deletes the specified entity value.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEntities(self, request, context):
        """List entities of an entity type
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EntityTypesServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ListEntityTypes': grpc.unary_unary_rpc_method_handler(
            servicer.ListEntityTypes,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.ListEntityTypesRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.ListEntityTypesResponse.SerializeToString,
        ),
        'GetEntityType': grpc.unary_unary_rpc_method_handler(
            servicer.GetEntityType,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.GetEntityTypeRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.SerializeToString,
        ),
        'CreateEntityType': grpc.unary_unary_rpc_method_handler(
            servicer.CreateEntityType,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.CreateEntityTypeRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.SerializeToString,
        ),
        'UpdateEntityType': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateEntityType,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.UpdateEntityTypeRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.SerializeToString,
        ),
        'DeleteEntityType': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteEntityType,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.DeleteEntityTypeRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'BatchUpdateEntityTypes': grpc.unary_unary_rpc_method_handler(
            servicer.BatchUpdateEntityTypes,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchUpdateEntityTypesRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_operations__pb2.Operation.SerializeToString,
        ),
        'BatchDeleteEntityTypes': grpc.unary_unary_rpc_method_handler(
            servicer.BatchDeleteEntityTypes,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchDeleteEntityTypesRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_operations__pb2.Operation.SerializeToString,
        ),
        'GetEntity': grpc.unary_unary_rpc_method_handler(
            servicer.GetEntity,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.GetEntityRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.Entity.SerializeToString,
        ),
        'CreateEntity': grpc.unary_unary_rpc_method_handler(
            servicer.CreateEntity,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.CreateEntityRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.Entity.SerializeToString,
        ),
        'UpdateEntity': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateEntity,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.UpdateEntityRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.EntityType.Entity.SerializeToString,
        ),
        'DeleteEntity': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteEntity,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.DeleteEntityRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.DeleteEntityStatus.SerializeToString,
        ),
        'BatchCreateEntities': grpc.unary_unary_rpc_method_handler(
            servicer.BatchCreateEntities,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchCreateEntitiesRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchEntitiesResponse.SerializeToString,
        ),
        'BatchUpdateEntities': grpc.unary_unary_rpc_method_handler(
            servicer.BatchUpdateEntities,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchUpdateEntitiesRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchEntitiesResponse.SerializeToString,
        ),
        'BatchGetEntities': grpc.unary_unary_rpc_method_handler(
            servicer.BatchGetEntities,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchGetEntitiesRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchEntitiesResponse.SerializeToString,
        ),
        'BatchDeleteEntities': grpc.unary_unary_rpc_method_handler(
            servicer.BatchDeleteEntities,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchDeleteEntitiesRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.BatchDeleteEntitiesResponse.SerializeToString,
        ),
        'ListEntities': grpc.unary_unary_rpc_method_handler(
            servicer.ListEntities,
            request_deserializer=ondewo_dot_nlu_dot_entity__type__pb2.ListEntitiesRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_entity__type__pb2.ListEntitiesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ondewo.nlu.EntityTypes', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ondewo.nlu.EntityTypes', rpc_method_handlers)

 # This class is part of an EXPERIMENTAL API.


class EntityTypes(object):
    """Entities are extracted from user input and represent parameters that are
    meaningful to your application. For example, a date range, a proper name
    such as a geographic location or landmark, and so on. Entities represent
    actionable data for your application.

    When you define an entity, you can also include synonyms that all map to
    that entity. For example, "soft drink", "soda", "pop", and so on.

    There are three types of entities:

    *   **System** - entities that are defined by the Dialogflow API for common
    data types such as date, time, currency, and so on. A system entity is
    represented by the `EntityType` type.

    *   **Developer** - entities that are defined by you that represent
    actionable data that is meaningful to your application. For example,
    you could define a `pizza.sauce` entity for red or white pizza sauce,
    a `pizza.cheese` entity for the different types of cheese on a pizza,
    a `pizza.topping` entity for different toppings, and so on. A developer
    entity is represented by the `EntityType` type.

    *   **User** - entities that are built for an individual user such as
    favorites, preferences, playlists, and so on. A user entity is
    represented by the [SessionEntityType][google.cloud.dialogflow.v2.SessionEntityType] type.

    For more information about entity types, see the
    [Dialogflow documentation](https://dialogflow.com/docs/entities).
    """

    @staticmethod
    def ListEntityTypes(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/ListEntityTypes',
            ondewo_dot_nlu_dot_entity__type__pb2.ListEntityTypesRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.ListEntityTypesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetEntityType(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/GetEntityType',
            ondewo_dot_nlu_dot_entity__type__pb2.GetEntityTypeRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.EntityType.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateEntityType(request,
                         target,
                         options=(),
                         channel_credentials=None,
                         call_credentials=None,
                         insecure=False,
                         compression=None,
                         wait_for_ready=None,
                         timeout=None,
                         metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/CreateEntityType',
            ondewo_dot_nlu_dot_entity__type__pb2.CreateEntityTypeRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.EntityType.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateEntityType(request,
                         target,
                         options=(),
                         channel_credentials=None,
                         call_credentials=None,
                         insecure=False,
                         compression=None,
                         wait_for_ready=None,
                         timeout=None,
                         metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/UpdateEntityType',
            ondewo_dot_nlu_dot_entity__type__pb2.UpdateEntityTypeRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.EntityType.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteEntityType(request,
                         target,
                         options=(),
                         channel_credentials=None,
                         call_credentials=None,
                         insecure=False,
                         compression=None,
                         wait_for_ready=None,
                         timeout=None,
                         metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/DeleteEntityType',
            ondewo_dot_nlu_dot_entity__type__pb2.DeleteEntityTypeRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchUpdateEntityTypes(request,
                               target,
                               options=(),
                               channel_credentials=None,
                               call_credentials=None,
                               insecure=False,
                               compression=None,
                               wait_for_ready=None,
                               timeout=None,
                               metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/BatchUpdateEntityTypes',
            ondewo_dot_nlu_dot_entity__type__pb2.BatchUpdateEntityTypesRequest.SerializeToString,
            ondewo_dot_nlu_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchDeleteEntityTypes(request,
                               target,
                               options=(),
                               channel_credentials=None,
                               call_credentials=None,
                               insecure=False,
                               compression=None,
                               wait_for_ready=None,
                               timeout=None,
                               metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/BatchDeleteEntityTypes',
            ondewo_dot_nlu_dot_entity__type__pb2.BatchDeleteEntityTypesRequest.SerializeToString,
            ondewo_dot_nlu_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetEntity(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/GetEntity',
            ondewo_dot_nlu_dot_entity__type__pb2.GetEntityRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.EntityType.Entity.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateEntity(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/CreateEntity',
            ondewo_dot_nlu_dot_entity__type__pb2.CreateEntityRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.EntityType.Entity.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateEntity(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/UpdateEntity',
            ondewo_dot_nlu_dot_entity__type__pb2.UpdateEntityRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.EntityType.Entity.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteEntity(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/DeleteEntity',
            ondewo_dot_nlu_dot_entity__type__pb2.DeleteEntityRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.DeleteEntityStatus.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchCreateEntities(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/BatchCreateEntities',
            ondewo_dot_nlu_dot_entity__type__pb2.BatchCreateEntitiesRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.BatchEntitiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchUpdateEntities(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/BatchUpdateEntities',
            ondewo_dot_nlu_dot_entity__type__pb2.BatchUpdateEntitiesRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.BatchEntitiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchGetEntities(request,
                         target,
                         options=(),
                         channel_credentials=None,
                         call_credentials=None,
                         insecure=False,
                         compression=None,
                         wait_for_ready=None,
                         timeout=None,
                         metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/BatchGetEntities',
            ondewo_dot_nlu_dot_entity__type__pb2.BatchGetEntitiesRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.BatchEntitiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchDeleteEntities(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/BatchDeleteEntities',
            ondewo_dot_nlu_dot_entity__type__pb2.BatchDeleteEntitiesRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.BatchDeleteEntitiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListEntities(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ondewo.nlu.EntityTypes/ListEntities',
            ondewo_dot_nlu_dot_entity__type__pb2.ListEntitiesRequest.SerializeToString,
            ondewo_dot_nlu_dot_entity__type__pb2.ListEntitiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
