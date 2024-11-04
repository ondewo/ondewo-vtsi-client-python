# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ondewo.nlu import context_pb2 as ondewo_dot_nlu_dot_context__pb2

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
        f' but the generated code in ondewo/nlu/context_pb2_grpc.py depends on' +
        f' grpcio>={GRPC_GENERATED_VERSION}.' +
        f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' +
        f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ContextsStub(object):
    """A context represents additional information included with user input or with
    an intent returned by the Dialogflow API. Contexts are helpful for
    differentiating user input which may be vague or have a different meaning
    depending on additional details from your application such as user setting
    and preferences, previous user input, where the user is in your application,
    geographic location, and so on.

    You can include contexts as input parameters of a
    [DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent] (or
    [StreamingDetectIntent][google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent]) request,
    or as output contexts included in the returned intent.
    Contexts expire when an intent is matched, after the number of `DetectIntent`
    requests specified by the `lifespan_count` parameter, or after 10 minutes
    if no intents are matched for a `DetectIntent` request.

    For more information about contexts, see the
    [Dialogflow documentation](https://dialogflow.com/docs/contexts).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListContexts = channel.unary_unary(
            '/ondewo.nlu.Contexts/ListContexts',
            request_serializer=ondewo_dot_nlu_dot_context__pb2.ListContextsRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_context__pb2.ListContextsResponse.FromString,
            _registered_method=True)
        self.GetContext = channel.unary_unary(
            '/ondewo.nlu.Contexts/GetContext',
            request_serializer=ondewo_dot_nlu_dot_context__pb2.GetContextRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_context__pb2.Context.FromString,
            _registered_method=True)
        self.CreateContext = channel.unary_unary(
            '/ondewo.nlu.Contexts/CreateContext',
            request_serializer=ondewo_dot_nlu_dot_context__pb2.CreateContextRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_context__pb2.Context.FromString,
            _registered_method=True)
        self.UpdateContext = channel.unary_unary(
            '/ondewo.nlu.Contexts/UpdateContext',
            request_serializer=ondewo_dot_nlu_dot_context__pb2.UpdateContextRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_context__pb2.Context.FromString,
            _registered_method=True)
        self.DeleteContext = channel.unary_unary(
            '/ondewo.nlu.Contexts/DeleteContext',
            request_serializer=ondewo_dot_nlu_dot_context__pb2.DeleteContextRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            _registered_method=True)
        self.DeleteAllContexts = channel.unary_unary(
            '/ondewo.nlu.Contexts/DeleteAllContexts',
            request_serializer=ondewo_dot_nlu_dot_context__pb2.DeleteAllContextsRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            _registered_method=True)


class ContextsServicer(object):
    """A context represents additional information included with user input or with
    an intent returned by the Dialogflow API. Contexts are helpful for
    differentiating user input which may be vague or have a different meaning
    depending on additional details from your application such as user setting
    and preferences, previous user input, where the user is in your application,
    geographic location, and so on.

    You can include contexts as input parameters of a
    [DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent] (or
    [StreamingDetectIntent][google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent]) request,
    or as output contexts included in the returned intent.
    Contexts expire when an intent is matched, after the number of `DetectIntent`
    requests specified by the `lifespan_count` parameter, or after 10 minutes
    if no intents are matched for a `DetectIntent` request.

    For more information about contexts, see the
    [Dialogflow documentation](https://dialogflow.com/docs/contexts).
    """

    def ListContexts(self, request, context):
        """Returns the list of all contexts in the specified session.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetContext(self, request, context):
        """Retrieves the specified context.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateContext(self, request, context):
        """Creates a context.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateContext(self, request, context):
        """Updates the specified context.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteContext(self, request, context):
        """Deletes the specified context.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllContexts(self, request, context):
        """Deletes all active contexts in the specified session.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ContextsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ListContexts': grpc.unary_unary_rpc_method_handler(
            servicer.ListContexts,
            request_deserializer=ondewo_dot_nlu_dot_context__pb2.ListContextsRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_context__pb2.ListContextsResponse.SerializeToString,
        ),
        'GetContext': grpc.unary_unary_rpc_method_handler(
            servicer.GetContext,
            request_deserializer=ondewo_dot_nlu_dot_context__pb2.GetContextRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_context__pb2.Context.SerializeToString,
        ),
        'CreateContext': grpc.unary_unary_rpc_method_handler(
            servicer.CreateContext,
            request_deserializer=ondewo_dot_nlu_dot_context__pb2.CreateContextRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_context__pb2.Context.SerializeToString,
        ),
        'UpdateContext': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateContext,
            request_deserializer=ondewo_dot_nlu_dot_context__pb2.UpdateContextRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_context__pb2.Context.SerializeToString,
        ),
        'DeleteContext': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteContext,
            request_deserializer=ondewo_dot_nlu_dot_context__pb2.DeleteContextRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'DeleteAllContexts': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteAllContexts,
            request_deserializer=ondewo_dot_nlu_dot_context__pb2.DeleteAllContextsRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ondewo.nlu.Contexts', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ondewo.nlu.Contexts', rpc_method_handlers)

 # This class is part of an EXPERIMENTAL API.


class Contexts(object):
    """A context represents additional information included with user input or with
    an intent returned by the Dialogflow API. Contexts are helpful for
    differentiating user input which may be vague or have a different meaning
    depending on additional details from your application such as user setting
    and preferences, previous user input, where the user is in your application,
    geographic location, and so on.

    You can include contexts as input parameters of a
    [DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent] (or
    [StreamingDetectIntent][google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent]) request,
    or as output contexts included in the returned intent.
    Contexts expire when an intent is matched, after the number of `DetectIntent`
    requests specified by the `lifespan_count` parameter, or after 10 minutes
    if no intents are matched for a `DetectIntent` request.

    For more information about contexts, see the
    [Dialogflow documentation](https://dialogflow.com/docs/contexts).
    """

    @staticmethod
    def ListContexts(request,
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
            '/ondewo.nlu.Contexts/ListContexts',
            ondewo_dot_nlu_dot_context__pb2.ListContextsRequest.SerializeToString,
            ondewo_dot_nlu_dot_context__pb2.ListContextsResponse.FromString,
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
    def GetContext(request,
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
            '/ondewo.nlu.Contexts/GetContext',
            ondewo_dot_nlu_dot_context__pb2.GetContextRequest.SerializeToString,
            ondewo_dot_nlu_dot_context__pb2.Context.FromString,
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
    def CreateContext(request,
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
            '/ondewo.nlu.Contexts/CreateContext',
            ondewo_dot_nlu_dot_context__pb2.CreateContextRequest.SerializeToString,
            ondewo_dot_nlu_dot_context__pb2.Context.FromString,
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
    def UpdateContext(request,
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
            '/ondewo.nlu.Contexts/UpdateContext',
            ondewo_dot_nlu_dot_context__pb2.UpdateContextRequest.SerializeToString,
            ondewo_dot_nlu_dot_context__pb2.Context.FromString,
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
    def DeleteContext(request,
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
            '/ondewo.nlu.Contexts/DeleteContext',
            ondewo_dot_nlu_dot_context__pb2.DeleteContextRequest.SerializeToString,
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
    def DeleteAllContexts(request,
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
            '/ondewo.nlu.Contexts/DeleteAllContexts',
            ondewo_dot_nlu_dot_context__pb2.DeleteAllContextsRequest.SerializeToString,
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
