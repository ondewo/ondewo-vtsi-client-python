# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ondewo.vtsi import voip_pb2 as ondewo_dot_vtsi_dot_voip__pb2


class VoipSessionsStub(object):
    """session manager for phone calls
    endpoints of voip server that manages instances of ondewo-sip-sim, which handle individual calls
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LoadManifest = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/LoadManifest',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.VoipManifest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.VoipManifestResponse.FromString,
                )
        self.RunManifest = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/RunManifest',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.ManifestRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.RunManifestResponse.FromString,
                )
        self.RemoveManifest = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/RemoveManifest',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.ManifestRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.RemoveManifestResponse.FromString,
                )
        self.GetManifestIDs = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/GetManifestIDs',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.GetManifestIDsRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.GetManifestIDsResponse.FromString,
                )
        self.PerformCall = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/PerformCall',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.PerformCallRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.PerformCallResponse.FromString,
                )
        self.StopCall = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/StopCall',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.StopCallRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.StopCallResponse.FromString,
                )
        self.StartListener = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/StartListener',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.StartListenerRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.StartListenerResponse.FromString,
                )
        self.StopListener = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/StopListener',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.StopCallRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.StopListenerResponse.FromString,
                )
        self.GetCallIDs = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/GetCallIDs',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.GetCallIDsRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.GetCallIDsResponse.FromString,
                )
        self.ShutdownUnhealthyCalls = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/ShutdownUnhealthyCalls',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.ShutdownUnhealthyCallsRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.ShutdownUnhealthyCallsResponse.FromString,
                )
        self.GetManifestStatus = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/GetManifestStatus',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.VoipManifestStatusRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.VoipManifestStatus.FromString,
                )
        self.GetInstanceStatus = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/GetInstanceStatus',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.GetVoipStatusRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.VoipStatus.FromString,
                )
        self.UpdateServicesStatus = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/UpdateServicesStatus',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.UpdateServicesStatusRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.UpdateServicesStatusResponse.FromString,
                )
        self.DeployPreconditionForWorkingSetup = channel.unary_unary(
                '/ondewo.nlu.VoipSessions/DeployPreconditionForWorkingSetup',
                request_serializer=ondewo_dot_vtsi_dot_voip__pb2.DeployPreconditionRequest.SerializeToString,
                response_deserializer=ondewo_dot_vtsi_dot_voip__pb2.DeployPreconditionResponse.FromString,
                )


class VoipSessionsServicer(object):
    """session manager for phone calls
    endpoints of voip server that manages instances of ondewo-sip-sim, which handle individual calls
    """

    def LoadManifest(self, request, context):
        """////////////
        MANIFEST //
        ////////////

        load a manifest of calls to perform and listener-instances to start
        includes configurations of services: ondewo-cai, speech-to-text & text-to-speech
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunManifest(self, request, context):
        """run a manifest by its ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveManifest(self, request, context):
        """remove a manifest by its ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetManifestIDs(self, request, context):
        """get all active manifests
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PerformCall(self, request, context):
        """///////////
        CALLERS //
        ///////////

        perform a single call with the given parameters in the request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopCall(self, request, context):
        """stop an ongoing call
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartListener(self, request, context):
        """/////////////
        LISTENERS //
        /////////////

        start an ondewo-sip-sim instance that listens for calls with the given parameters
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopListener(self, request, context):
        """stop/kill an ondewo-sip-sim listener instance
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCallIDs(self, request, context):
        """///////////
        GENERAL //
        ///////////

        get all call IDs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShutdownUnhealthyCalls(self, request, context):
        """shutdown any deployed call with unhealthy status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetManifestStatus(self, request, context):
        """//////////
        STATUS //
        //////////

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInstanceStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateServicesStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeployPreconditionForWorkingSetup(self, request, context):
        """////////////////
        PRECONDITION //
        ////////////////

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VoipSessionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LoadManifest': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadManifest,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.VoipManifest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.VoipManifestResponse.SerializeToString,
            ),
            'RunManifest': grpc.unary_unary_rpc_method_handler(
                    servicer.RunManifest,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.ManifestRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.RunManifestResponse.SerializeToString,
            ),
            'RemoveManifest': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveManifest,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.ManifestRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.RemoveManifestResponse.SerializeToString,
            ),
            'GetManifestIDs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetManifestIDs,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.GetManifestIDsRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.GetManifestIDsResponse.SerializeToString,
            ),
            'PerformCall': grpc.unary_unary_rpc_method_handler(
                    servicer.PerformCall,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.PerformCallRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.PerformCallResponse.SerializeToString,
            ),
            'StopCall': grpc.unary_unary_rpc_method_handler(
                    servicer.StopCall,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.StopCallRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.StopCallResponse.SerializeToString,
            ),
            'StartListener': grpc.unary_unary_rpc_method_handler(
                    servicer.StartListener,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.StartListenerRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.StartListenerResponse.SerializeToString,
            ),
            'StopListener': grpc.unary_unary_rpc_method_handler(
                    servicer.StopListener,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.StopCallRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.StopListenerResponse.SerializeToString,
            ),
            'GetCallIDs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCallIDs,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.GetCallIDsRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.GetCallIDsResponse.SerializeToString,
            ),
            'ShutdownUnhealthyCalls': grpc.unary_unary_rpc_method_handler(
                    servicer.ShutdownUnhealthyCalls,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.ShutdownUnhealthyCallsRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.ShutdownUnhealthyCallsResponse.SerializeToString,
            ),
            'GetManifestStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetManifestStatus,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.VoipManifestStatusRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.VoipManifestStatus.SerializeToString,
            ),
            'GetInstanceStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInstanceStatus,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.GetVoipStatusRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.VoipStatus.SerializeToString,
            ),
            'UpdateServicesStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateServicesStatus,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.UpdateServicesStatusRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.UpdateServicesStatusResponse.SerializeToString,
            ),
            'DeployPreconditionForWorkingSetup': grpc.unary_unary_rpc_method_handler(
                    servicer.DeployPreconditionForWorkingSetup,
                    request_deserializer=ondewo_dot_vtsi_dot_voip__pb2.DeployPreconditionRequest.FromString,
                    response_serializer=ondewo_dot_vtsi_dot_voip__pb2.DeployPreconditionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ondewo.nlu.VoipSessions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VoipSessions(object):
    """session manager for phone calls
    endpoints of voip server that manages instances of ondewo-sip-sim, which handle individual calls
    """

    @staticmethod
    def LoadManifest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/LoadManifest',
            ondewo_dot_vtsi_dot_voip__pb2.VoipManifest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.VoipManifestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RunManifest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/RunManifest',
            ondewo_dot_vtsi_dot_voip__pb2.ManifestRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.RunManifestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveManifest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/RemoveManifest',
            ondewo_dot_vtsi_dot_voip__pb2.ManifestRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.RemoveManifestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetManifestIDs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/GetManifestIDs',
            ondewo_dot_vtsi_dot_voip__pb2.GetManifestIDsRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.GetManifestIDsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PerformCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/PerformCall',
            ondewo_dot_vtsi_dot_voip__pb2.PerformCallRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.PerformCallResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/StopCall',
            ondewo_dot_vtsi_dot_voip__pb2.StopCallRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.StopCallResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/StartListener',
            ondewo_dot_vtsi_dot_voip__pb2.StartListenerRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.StartListenerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopListener(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/StopListener',
            ondewo_dot_vtsi_dot_voip__pb2.StopCallRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.StopListenerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCallIDs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/GetCallIDs',
            ondewo_dot_vtsi_dot_voip__pb2.GetCallIDsRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.GetCallIDsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ShutdownUnhealthyCalls(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/ShutdownUnhealthyCalls',
            ondewo_dot_vtsi_dot_voip__pb2.ShutdownUnhealthyCallsRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.ShutdownUnhealthyCallsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetManifestStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/GetManifestStatus',
            ondewo_dot_vtsi_dot_voip__pb2.VoipManifestStatusRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.VoipManifestStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInstanceStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/GetInstanceStatus',
            ondewo_dot_vtsi_dot_voip__pb2.GetVoipStatusRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.VoipStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateServicesStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/UpdateServicesStatus',
            ondewo_dot_vtsi_dot_voip__pb2.UpdateServicesStatusRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.UpdateServicesStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeployPreconditionForWorkingSetup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.VoipSessions/DeployPreconditionForWorkingSetup',
            ondewo_dot_vtsi_dot_voip__pb2.DeployPreconditionRequest.SerializeToString,
            ondewo_dot_vtsi_dot_voip__pb2.DeployPreconditionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
