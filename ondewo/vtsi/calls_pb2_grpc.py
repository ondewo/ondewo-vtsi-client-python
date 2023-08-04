# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ondewo.vtsi import calls_pb2 as ondewo_dot_vtsi_dot_calls__pb2


class CallsStub(object):
    """ONDEWO VTSI API
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartCaller = channel.unary_unary(
            '/ondewo.vtsi.Calls/StartCaller',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartCallerRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartCallerResponse.FromString,
        )
        self.StartCallers = channel.unary_unary(
            '/ondewo.vtsi.Calls/StartCallers',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartCallersRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartCallersResponse.FromString,
        )
        self.ListCallers = channel.unary_unary(
            '/ondewo.vtsi.Calls/ListCallers',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.ListCallersRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.ListCallersResponse.FromString,
        )
        self.GetCaller = channel.unary_unary(
            '/ondewo.vtsi.Calls/GetCaller',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.GetCallerRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.Caller.FromString,
        )
        self.StartListener = channel.unary_unary(
            '/ondewo.vtsi.Calls/StartListener',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartListenerRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartListenerResponse.FromString,
        )
        self.StartListeners = channel.unary_unary(
            '/ondewo.vtsi.Calls/StartListeners',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartListenersRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartListenersResponse.FromString,
        )
        self.ListListeners = channel.unary_unary(
            '/ondewo.vtsi.Calls/ListListeners',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.ListListenersRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.ListListenersResponse.FromString,
        )
        self.GetListener = channel.unary_unary(
            '/ondewo.vtsi.Calls/GetListener',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.GetListenerRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.Listener.FromString,
        )
        self.StartScheduledCaller = channel.unary_unary(
            '/ondewo.vtsi.Calls/StartScheduledCaller',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallerRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallerResponse.FromString,
        )
        self.StartScheduledCallers = channel.unary_unary(
            '/ondewo.vtsi.Calls/StartScheduledCallers',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallersRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallersResponse.FromString,
        )
        self.StopCall = channel.unary_unary(
            '/ondewo.vtsi.Calls/StopCall',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.StopCallRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StopCallResponse.FromString,
        )
        self.StopCalls = channel.unary_unary(
            '/ondewo.vtsi.Calls/StopCalls',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.StopCallsRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StopCallsResponse.FromString,
        )
        self.StopAllCalls = channel.unary_unary(
            '/ondewo.vtsi.Calls/StopAllCalls',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.StopAllCallsRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StopCallsResponse.FromString,
        )
        self.TransferCall = channel.unary_unary(
            '/ondewo.vtsi.Calls/TransferCall',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.TransferCallRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.TransferCallResponse.FromString,
        )
        self.TransferCalls = channel.unary_unary(
            '/ondewo.vtsi.Calls/TransferCalls',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.TransferCallsRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.TransferCallsResponse.FromString,
        )
        self.GetCall = channel.unary_unary(
            '/ondewo.vtsi.Calls/GetCall',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.GetCallRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.Call.FromString,
        )
        self.ListCalls = channel.unary_unary(
            '/ondewo.vtsi.Calls/ListCalls',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.ListCallsRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.ListCallsResponse.FromString,
        )
        self.GetAudioFile = channel.unary_unary(
            '/ondewo.vtsi.Calls/GetAudioFile',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.GetAudioFileRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.GetAudioFileResponse.FromString,
        )
        self.GetFullConversationAudioFile = channel.unary_unary(
            '/ondewo.vtsi.Calls/GetFullConversationAudioFile',
            request_serializer=ondewo_dot_vtsi_dot_calls__pb2.GetFullConversationAudioFileRequest.SerializeToString,
            response_deserializer=ondewo_dot_vtsi_dot_calls__pb2.GetFullConversationAudioFileResponse.FromString,
        )


class CallsServicer(object):
    """ONDEWO VTSI API
    """

    def StartCaller(self, request, context):
        """////////////////////////////////////////////////////////////////////////////
        Caller and Listener endpoints
        ////////////////////////////////////////////////////////////////////////////

        start single caller instance for a specific nlu-project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartCallers(self, request, context):
        """start multiple ondewo-sip callers instances for a specific nlu-project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCallers(self, request, context):
        """lists all available callers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCaller(self, request, context):
        """gets a caller
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartListener(self, request, context):
        """start single listener instance for a specific nlu-project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartListeners(self, request, context):
        """start multiple ondewo-sip listeners instances for a specific nlu-project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListListeners(self, request, context):
        """lists all available listeners
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListener(self, request, context):
        """gets a listener
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartScheduledCaller(self, request, context):
        """start multiple ondewo-sip callers instances with schedules
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartScheduledCallers(self, request, context):
        """start multiple ondewo-sip callers instances with schedules
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopCall(self, request, context):
        """stop/kill a ondewo-sip listener or caller instance for a specific vtsi-project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopCalls(self, request, context):
        """stop/kill a list of ondewo-sip listener or caller instances for a specific vtsi-project.
        "stops both Listener and Caller calls"
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopAllCalls(self, request, context):
        """stop/kill all ondewo-sip listener or caller instance for a specific nlu-project.
        "stops all Listener and Caller calls"
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferCall(self, request, context):
        """Transfer a call from a listener to another
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferCalls(self, request, context):
        """Transfer a call from a listener to another
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCall(self, request, context):
        """get call log for single call instance
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCalls(self, request, context):
        """get call log for all call instances
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAudioFile(self, request, context):
        """Get a s2t or t2s audio file for this conversation if it exists in Minio
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFullConversationAudioFile(self, request, context):
        """Get The whole conversation in an audio file
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CallsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'StartCaller': grpc.unary_unary_rpc_method_handler(
            servicer.StartCaller,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartCallerRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartCallerResponse.SerializeToString,
        ),
        'StartCallers': grpc.unary_unary_rpc_method_handler(
            servicer.StartCallers,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartCallersRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartCallersResponse.SerializeToString,
        ),
        'ListCallers': grpc.unary_unary_rpc_method_handler(
            servicer.ListCallers,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.ListCallersRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.ListCallersResponse.SerializeToString,
        ),
        'GetCaller': grpc.unary_unary_rpc_method_handler(
            servicer.GetCaller,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.GetCallerRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.Caller.SerializeToString,
        ),
        'StartListener': grpc.unary_unary_rpc_method_handler(
            servicer.StartListener,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartListenerRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartListenerResponse.SerializeToString,
        ),
        'StartListeners': grpc.unary_unary_rpc_method_handler(
            servicer.StartListeners,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartListenersRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartListenersResponse.SerializeToString,
        ),
        'ListListeners': grpc.unary_unary_rpc_method_handler(
            servicer.ListListeners,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.ListListenersRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.ListListenersResponse.SerializeToString,
        ),
        'GetListener': grpc.unary_unary_rpc_method_handler(
            servicer.GetListener,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.GetListenerRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.Listener.SerializeToString,
        ),
        'StartScheduledCaller': grpc.unary_unary_rpc_method_handler(
            servicer.StartScheduledCaller,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallerRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallerResponse.SerializeToString,
        ),
        'StartScheduledCallers': grpc.unary_unary_rpc_method_handler(
            servicer.StartScheduledCallers,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallersRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallersResponse.SerializeToString,
        ),
        'StopCall': grpc.unary_unary_rpc_method_handler(
            servicer.StopCall,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StopCallRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.StopCallResponse.SerializeToString,
        ),
        'StopCalls': grpc.unary_unary_rpc_method_handler(
            servicer.StopCalls,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StopCallsRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.StopCallsResponse.SerializeToString,
        ),
        'StopAllCalls': grpc.unary_unary_rpc_method_handler(
            servicer.StopAllCalls,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.StopAllCallsRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.StopCallsResponse.SerializeToString,
        ),
        'TransferCall': grpc.unary_unary_rpc_method_handler(
            servicer.TransferCall,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.TransferCallRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.TransferCallResponse.SerializeToString,
        ),
        'TransferCalls': grpc.unary_unary_rpc_method_handler(
            servicer.TransferCalls,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.TransferCallsRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.TransferCallsResponse.SerializeToString,
        ),
        'GetCall': grpc.unary_unary_rpc_method_handler(
            servicer.GetCall,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.GetCallRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.Call.SerializeToString,
        ),
        'ListCalls': grpc.unary_unary_rpc_method_handler(
            servicer.ListCalls,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.ListCallsRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.ListCallsResponse.SerializeToString,
        ),
        'GetAudioFile': grpc.unary_unary_rpc_method_handler(
            servicer.GetAudioFile,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.GetAudioFileRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.GetAudioFileResponse.SerializeToString,
        ),
        'GetFullConversationAudioFile': grpc.unary_unary_rpc_method_handler(
            servicer.GetFullConversationAudioFile,
            request_deserializer=ondewo_dot_vtsi_dot_calls__pb2.GetFullConversationAudioFileRequest.FromString,
            response_serializer=ondewo_dot_vtsi_dot_calls__pb2.GetFullConversationAudioFileResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ondewo.vtsi.Calls', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Calls(object):
    """ONDEWO VTSI API
    """

    @staticmethod
    def StartCaller(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/StartCaller',
                                             ondewo_dot_vtsi_dot_calls__pb2.StartCallerRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.StartCallerResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartCallers(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/StartCallers',
                                             ondewo_dot_vtsi_dot_calls__pb2.StartCallersRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.StartCallersResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCallers(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/ListCallers',
                                             ondewo_dot_vtsi_dot_calls__pb2.ListCallersRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.ListCallersResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCaller(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/GetCaller',
                                             ondewo_dot_vtsi_dot_calls__pb2.GetCallerRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.Caller.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartListener(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/StartListener',
                                             ondewo_dot_vtsi_dot_calls__pb2.StartListenerRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.StartListenerResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartListeners(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/StartListeners',
                                             ondewo_dot_vtsi_dot_calls__pb2.StartListenersRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.StartListenersResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListListeners(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/ListListeners',
                                             ondewo_dot_vtsi_dot_calls__pb2.ListListenersRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.ListListenersResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListener(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/GetListener',
                                             ondewo_dot_vtsi_dot_calls__pb2.GetListenerRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.Listener.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartScheduledCaller(request,
                             target,
                             options=(),
                             channel_credentials=None,
                             call_credentials=None,
                             insecure=False,
                             compression=None,
                             wait_for_ready=None,
                             timeout=None,
                             metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/StartScheduledCaller',
                                             ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallerRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallerResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartScheduledCallers(request,
                              target,
                              options=(),
                              channel_credentials=None,
                              call_credentials=None,
                              insecure=False,
                              compression=None,
                              wait_for_ready=None,
                              timeout=None,
                              metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/StartScheduledCallers',
                                             ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallersRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.StartScheduledCallersResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopCall(request,
                 target,
                 options=(),
                 channel_credentials=None,
                 call_credentials=None,
                 insecure=False,
                 compression=None,
                 wait_for_ready=None,
                 timeout=None,
                 metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/StopCall',
                                             ondewo_dot_vtsi_dot_calls__pb2.StopCallRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.StopCallResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopCalls(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/StopCalls',
                                             ondewo_dot_vtsi_dot_calls__pb2.StopCallsRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.StopCallsResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopAllCalls(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/StopAllCalls',
                                             ondewo_dot_vtsi_dot_calls__pb2.StopAllCallsRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.StopCallsResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransferCall(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/TransferCall',
                                             ondewo_dot_vtsi_dot_calls__pb2.TransferCallRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.TransferCallResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransferCalls(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/TransferCalls',
                                             ondewo_dot_vtsi_dot_calls__pb2.TransferCallsRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.TransferCallsResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCall(request,
                target,
                options=(),
                channel_credentials=None,
                call_credentials=None,
                insecure=False,
                compression=None,
                wait_for_ready=None,
                timeout=None,
                metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/GetCall',
                                             ondewo_dot_vtsi_dot_calls__pb2.GetCallRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.Call.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCalls(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/ListCalls',
                                             ondewo_dot_vtsi_dot_calls__pb2.ListCallsRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.ListCallsResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAudioFile(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/GetAudioFile',
                                             ondewo_dot_vtsi_dot_calls__pb2.GetAudioFileRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.GetAudioFileResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFullConversationAudioFile(request,
                                     target,
                                     options=(),
                                     channel_credentials=None,
                                     call_credentials=None,
                                     insecure=False,
                                     compression=None,
                                     wait_for_ready=None,
                                     timeout=None,
                                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.vtsi.Calls/GetFullConversationAudioFile',
                                             ondewo_dot_vtsi_dot_calls__pb2.GetFullConversationAudioFileRequest.SerializeToString,
                                             ondewo_dot_vtsi_dot_calls__pb2.GetFullConversationAudioFileResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
