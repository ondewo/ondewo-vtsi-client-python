# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ondewo.nlu import common_pb2 as ondewo_dot_nlu_dot_common__pb2
from ondewo.nlu import server_statistics_pb2 as ondewo_dot_nlu_dot_server__statistics__pb2


class ServerStatisticsStub(object):
    """Server project statistics
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProjectCount = channel.unary_unary(
            '/ondewo.nlu.ServerStatistics/GetProjectCount',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_common__pb2.StatResponse.FromString,
        )
        self.GetUserProjectCount = channel.unary_unary(
            '/ondewo.nlu.ServerStatistics/GetUserProjectCount',
            request_serializer=ondewo_dot_nlu_dot_server__statistics__pb2.GetUserProjectCountRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_common__pb2.StatResponse.FromString,
        )
        self.GetUserCount = channel.unary_unary(
            '/ondewo.nlu.ServerStatistics/GetUserCount',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_common__pb2.StatResponse.FromString,
        )


class ServerStatisticsServicer(object):
    """Server project statistics
    """

    def GetProjectCount(self, request, context):
        """Returns the count of projects in the CAI server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserProjectCount(self, request, context):
        """Returns the count of projects of a user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserCount(self, request, context):
        """Returns the users count within a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerStatisticsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetProjectCount': grpc.unary_unary_rpc_method_handler(
            servicer.GetProjectCount,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ondewo_dot_nlu_dot_common__pb2.StatResponse.SerializeToString,
        ),
        'GetUserProjectCount': grpc.unary_unary_rpc_method_handler(
            servicer.GetUserProjectCount,
            request_deserializer=ondewo_dot_nlu_dot_server__statistics__pb2.GetUserProjectCountRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_common__pb2.StatResponse.SerializeToString,
        ),
        'GetUserCount': grpc.unary_unary_rpc_method_handler(
            servicer.GetUserCount,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ondewo_dot_nlu_dot_common__pb2.StatResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ondewo.nlu.ServerStatistics', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class ServerStatistics(object):
    """Server project statistics
    """

    @staticmethod
    def GetProjectCount(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.ServerStatistics/GetProjectCount',
                                             google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                                             ondewo_dot_nlu_dot_common__pb2.StatResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserProjectCount(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.ServerStatistics/GetUserProjectCount',
                                             ondewo_dot_nlu_dot_server__statistics__pb2.GetUserProjectCountRequest.SerializeToString,
                                             ondewo_dot_nlu_dot_common__pb2.StatResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserCount(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.nlu.ServerStatistics/GetUserCount',
                                             google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                                             ondewo_dot_nlu_dot_common__pb2.StatResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
