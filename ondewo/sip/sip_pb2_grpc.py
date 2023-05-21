# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ondewo.sip import sip_pb2 as ondewo_dot_sip_dot_sip__pb2


class SipStub(object):
    """ONDEWO-SIP API available at <a href="https://github.com/ondewo/ondewo-sip-api>">GitHub</a>
    SIP LifeCycle is explained at <a href="https://thanhloi2603.wordpress.com/2017/06/10/sip-lifecycle-overview/">here</a>
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SipStartSession = channel.unary_unary(
            '/ondewo.sip.Sip/SipStartSession',
            request_serializer=ondewo_dot_sip_dot_sip__pb2.SipStartSessionRequest.SerializeToString,
            response_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
        )
        self.SipEndSession = channel.unary_unary(
            '/ondewo.sip.Sip/SipEndSession',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
        )
        self.SipStartCall = channel.unary_unary(
            '/ondewo.sip.Sip/SipStartCall',
            request_serializer=ondewo_dot_sip_dot_sip__pb2.SipStartCallRequest.SerializeToString,
            response_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
        )
        self.SipEndCall = channel.unary_unary(
            '/ondewo.sip.Sip/SipEndCall',
            request_serializer=ondewo_dot_sip_dot_sip__pb2.SipEndCallRequest.SerializeToString,
            response_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
        )
        self.SipTransferCall = channel.unary_unary(
            '/ondewo.sip.Sip/SipTransferCall',
            request_serializer=ondewo_dot_sip_dot_sip__pb2.SipTransferCallRequest.SerializeToString,
            response_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
        )
        self.SipRegisterAccount = channel.unary_unary(
            '/ondewo.sip.Sip/SipRegisterAccount',
            request_serializer=ondewo_dot_sip_dot_sip__pb2.SipRegisterAccountRequest.SerializeToString,
            response_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
        )
        self.SipGetSipStatus = channel.unary_unary(
            '/ondewo.sip.Sip/SipGetSipStatus',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
        )
        self.SipGetSipStatusHistory = channel.unary_unary(
            '/ondewo.sip.Sip/SipGetSipStatusHistory',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStatusHistoryResponse.FromString,
        )
        self.SipPlayWavFiles = channel.unary_unary(
            '/ondewo.sip.Sip/SipPlayWavFiles',
            request_serializer=ondewo_dot_sip_dot_sip__pb2.SipPlayWavFilesRequest.SerializeToString,
            response_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
        )
        self.SipMute = channel.unary_unary(
            '/ondewo.sip.Sip/SipMute',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
        )
        self.SipUnMute = channel.unary_unary(
            '/ondewo.sip.Sip/SipUnMute',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
        )


class SipServicer(object):
    """ONDEWO-SIP API available at <a href="https://github.com/ondewo/ondewo-sip-api>">GitHub</a>
    SIP LifeCycle is explained at <a href="https://thanhloi2603.wordpress.com/2017/06/10/sip-lifecycle-overview/">here</a>
    """

    def SipStartSession(self, request, context):
        """Starts a new SIP session for an account registered at a SIP server. <code>RegisterAccount</code> need to be called before.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SipEndSession(self, request, context):
        """Ends a SIP session for an account registered at a SIP server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SipStartCall(self, request, context):
        """Starts a call in an active SIP session for an account registered at a SIP server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SipEndCall(self, request, context):
        """Ends a call in an active SIP session for an account registered at a SIP server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SipTransferCall(self, request, context):
        """Transfers a call in an active SIP session for an account registered at a SIP server to
        another SIP account or phone number specified by <code>transfer_id</code>
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SipRegisterAccount(self, request, context):
        """Registers s SIP account at a SIP server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SipGetSipStatus(self, request, context):
        """Gets the current SIP status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SipGetSipStatusHistory(self, request, context):
        """Gets the history of SIP status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SipPlayWavFiles(self, request, context):
        """Plays wav files during an ongoing call of an active SIP session
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SipMute(self, request, context):
        """Mutes the microphone in an ongoing call of an active SIP session
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SipUnMute(self, request, context):
        """Un-mutes the microphone in an ongoing call of an active SIP session
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SipServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SipStartSession': grpc.unary_unary_rpc_method_handler(
            servicer.SipStartSession,
            request_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStartSessionRequest.FromString,
            response_serializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.SerializeToString,
        ),
        'SipEndSession': grpc.unary_unary_rpc_method_handler(
            servicer.SipEndSession,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.SerializeToString,
        ),
        'SipStartCall': grpc.unary_unary_rpc_method_handler(
            servicer.SipStartCall,
            request_deserializer=ondewo_dot_sip_dot_sip__pb2.SipStartCallRequest.FromString,
            response_serializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.SerializeToString,
        ),
        'SipEndCall': grpc.unary_unary_rpc_method_handler(
            servicer.SipEndCall,
            request_deserializer=ondewo_dot_sip_dot_sip__pb2.SipEndCallRequest.FromString,
            response_serializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.SerializeToString,
        ),
        'SipTransferCall': grpc.unary_unary_rpc_method_handler(
            servicer.SipTransferCall,
            request_deserializer=ondewo_dot_sip_dot_sip__pb2.SipTransferCallRequest.FromString,
            response_serializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.SerializeToString,
        ),
        'SipRegisterAccount': grpc.unary_unary_rpc_method_handler(
            servicer.SipRegisterAccount,
            request_deserializer=ondewo_dot_sip_dot_sip__pb2.SipRegisterAccountRequest.FromString,
            response_serializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.SerializeToString,
        ),
        'SipGetSipStatus': grpc.unary_unary_rpc_method_handler(
            servicer.SipGetSipStatus,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.SerializeToString,
        ),
        'SipGetSipStatusHistory': grpc.unary_unary_rpc_method_handler(
            servicer.SipGetSipStatusHistory,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ondewo_dot_sip_dot_sip__pb2.SipStatusHistoryResponse.SerializeToString,
        ),
        'SipPlayWavFiles': grpc.unary_unary_rpc_method_handler(
            servicer.SipPlayWavFiles,
            request_deserializer=ondewo_dot_sip_dot_sip__pb2.SipPlayWavFilesRequest.FromString,
            response_serializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.SerializeToString,
        ),
        'SipMute': grpc.unary_unary_rpc_method_handler(
            servicer.SipMute,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.SerializeToString,
        ),
        'SipUnMute': grpc.unary_unary_rpc_method_handler(
            servicer.SipUnMute,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ondewo_dot_sip_dot_sip__pb2.SipStatus.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ondewo.sip.Sip', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Sip(object):
    """ONDEWO-SIP API available at <a href="https://github.com/ondewo/ondewo-sip-api>">GitHub</a>
    SIP LifeCycle is explained at <a href="https://thanhloi2603.wordpress.com/2017/06/10/sip-lifecycle-overview/">here</a>
    """

    @staticmethod
    def SipStartSession(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.sip.Sip/SipStartSession',
                                             ondewo_dot_sip_dot_sip__pb2.SipStartSessionRequest.SerializeToString,
                                             ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SipEndSession(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.sip.Sip/SipEndSession',
                                             google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                                             ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SipStartCall(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.sip.Sip/SipStartCall',
                                             ondewo_dot_sip_dot_sip__pb2.SipStartCallRequest.SerializeToString,
                                             ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SipEndCall(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.sip.Sip/SipEndCall',
                                             ondewo_dot_sip_dot_sip__pb2.SipEndCallRequest.SerializeToString,
                                             ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SipTransferCall(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.sip.Sip/SipTransferCall',
                                             ondewo_dot_sip_dot_sip__pb2.SipTransferCallRequest.SerializeToString,
                                             ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SipRegisterAccount(request,
                           target,
                           options=(),
                           channel_credentials=None,
                           call_credentials=None,
                           insecure=False,
                           compression=None,
                           wait_for_ready=None,
                           timeout=None,
                           metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.sip.Sip/SipRegisterAccount',
                                             ondewo_dot_sip_dot_sip__pb2.SipRegisterAccountRequest.SerializeToString,
                                             ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SipGetSipStatus(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.sip.Sip/SipGetSipStatus',
                                             google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                                             ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SipGetSipStatusHistory(request,
                               target,
                               options=(),
                               channel_credentials=None,
                               call_credentials=None,
                               insecure=False,
                               compression=None,
                               wait_for_ready=None,
                               timeout=None,
                               metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.sip.Sip/SipGetSipStatusHistory',
                                             google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                                             ondewo_dot_sip_dot_sip__pb2.SipStatusHistoryResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SipPlayWavFiles(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.sip.Sip/SipPlayWavFiles',
                                             ondewo_dot_sip_dot_sip__pb2.SipPlayWavFilesRequest.SerializeToString,
                                             ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SipMute(request,
                target,
                options=(),
                channel_credentials=None,
                call_credentials=None,
                insecure=False,
                compression=None,
                wait_for_ready=None,
                timeout=None,
                metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.sip.Sip/SipMute',
                                             google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                                             ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SipUnMute(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.sip.Sip/SipUnMute',
                                             google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                                             ondewo_dot_sip_dot_sip__pb2.SipStatus.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
