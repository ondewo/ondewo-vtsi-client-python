# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from ondewo.nlu import ccai_project_pb2 as ondewo_dot_nlu_dot_ccai__project__pb2

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
        f' but the generated code in ondewo/nlu/ccai_project_pb2_grpc.py depends on' +
        f' grpcio>={GRPC_GENERATED_VERSION}.' +
        f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' +
        f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CcaiProjectsStub(object):
    """Service to manage Call Center AI (CCAI) Projects.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCcaiProject = channel.unary_unary(
            '/ondewo.nlu.CcaiProjects/GetCcaiProject',
            request_serializer=ondewo_dot_nlu_dot_ccai__project__pb2.GetCcaiProjectRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_ccai__project__pb2.CcaiProject.FromString,
            _registered_method=True)
        self.CreateCcaiProject = channel.unary_unary(
            '/ondewo.nlu.CcaiProjects/CreateCcaiProject',
            request_serializer=ondewo_dot_nlu_dot_ccai__project__pb2.CreateCcaiProjectRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_ccai__project__pb2.CreateCcaiProjectResponse.FromString,
            _registered_method=True)
        self.DeleteCcaiProject = channel.unary_unary(
            '/ondewo.nlu.CcaiProjects/DeleteCcaiProject',
            request_serializer=ondewo_dot_nlu_dot_ccai__project__pb2.DeleteCcaiProjectRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_ccai__project__pb2.DeleteCcaiProjectResponse.FromString,
            _registered_method=True)
        self.ListCcaiProjects = channel.unary_unary(
            '/ondewo.nlu.CcaiProjects/ListCcaiProjects',
            request_serializer=ondewo_dot_nlu_dot_ccai__project__pb2.ListCcaiProjectsRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_ccai__project__pb2.ListCcaiProjectsResponse.FromString,
            _registered_method=True)
        self.UpdateCcaiProject = channel.unary_unary(
            '/ondewo.nlu.CcaiProjects/UpdateCcaiProject',
            request_serializer=ondewo_dot_nlu_dot_ccai__project__pb2.UpdateCcaiProjectRequest.SerializeToString,
            response_deserializer=ondewo_dot_nlu_dot_ccai__project__pb2.UpdateCcaiProjectResponse.FromString,
            _registered_method=True)


class CcaiProjectsServicer(object):
    """Service to manage Call Center AI (CCAI) Projects.
    """

    def GetCcaiProject(self, request, context):
        """Retrieves information about a specific CCAI project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCcaiProject(self, request, context):
        """Creates a new CCAI project based on the provided request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCcaiProject(self, request, context):
        """Deletes a CCAI project identified by the provided request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCcaiProjects(self, request, context):
        """Lists all CCAI projects based on the provided request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCcaiProject(self, request, context):
        """Updates the information of an existing CCAI project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CcaiProjectsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetCcaiProject': grpc.unary_unary_rpc_method_handler(
            servicer.GetCcaiProject,
            request_deserializer=ondewo_dot_nlu_dot_ccai__project__pb2.GetCcaiProjectRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_ccai__project__pb2.CcaiProject.SerializeToString,
        ),
        'CreateCcaiProject': grpc.unary_unary_rpc_method_handler(
            servicer.CreateCcaiProject,
            request_deserializer=ondewo_dot_nlu_dot_ccai__project__pb2.CreateCcaiProjectRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_ccai__project__pb2.CreateCcaiProjectResponse.SerializeToString,
        ),
        'DeleteCcaiProject': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteCcaiProject,
            request_deserializer=ondewo_dot_nlu_dot_ccai__project__pb2.DeleteCcaiProjectRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_ccai__project__pb2.DeleteCcaiProjectResponse.SerializeToString,
        ),
        'ListCcaiProjects': grpc.unary_unary_rpc_method_handler(
            servicer.ListCcaiProjects,
            request_deserializer=ondewo_dot_nlu_dot_ccai__project__pb2.ListCcaiProjectsRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_ccai__project__pb2.ListCcaiProjectsResponse.SerializeToString,
        ),
        'UpdateCcaiProject': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateCcaiProject,
            request_deserializer=ondewo_dot_nlu_dot_ccai__project__pb2.UpdateCcaiProjectRequest.FromString,
            response_serializer=ondewo_dot_nlu_dot_ccai__project__pb2.UpdateCcaiProjectResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ondewo.nlu.CcaiProjects', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ondewo.nlu.CcaiProjects', rpc_method_handlers)

 # This class is part of an EXPERIMENTAL API.


class CcaiProjects(object):
    """Service to manage Call Center AI (CCAI) Projects.
    """

    @staticmethod
    def GetCcaiProject(request,
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
            '/ondewo.nlu.CcaiProjects/GetCcaiProject',
            ondewo_dot_nlu_dot_ccai__project__pb2.GetCcaiProjectRequest.SerializeToString,
            ondewo_dot_nlu_dot_ccai__project__pb2.CcaiProject.FromString,
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
    def CreateCcaiProject(request,
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
            '/ondewo.nlu.CcaiProjects/CreateCcaiProject',
            ondewo_dot_nlu_dot_ccai__project__pb2.CreateCcaiProjectRequest.SerializeToString,
            ondewo_dot_nlu_dot_ccai__project__pb2.CreateCcaiProjectResponse.FromString,
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
    def DeleteCcaiProject(request,
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
            '/ondewo.nlu.CcaiProjects/DeleteCcaiProject',
            ondewo_dot_nlu_dot_ccai__project__pb2.DeleteCcaiProjectRequest.SerializeToString,
            ondewo_dot_nlu_dot_ccai__project__pb2.DeleteCcaiProjectResponse.FromString,
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
    def ListCcaiProjects(request,
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
            '/ondewo.nlu.CcaiProjects/ListCcaiProjects',
            ondewo_dot_nlu_dot_ccai__project__pb2.ListCcaiProjectsRequest.SerializeToString,
            ondewo_dot_nlu_dot_ccai__project__pb2.ListCcaiProjectsResponse.FromString,
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
    def UpdateCcaiProject(request,
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
            '/ondewo.nlu.CcaiProjects/UpdateCcaiProject',
            ondewo_dot_nlu_dot_ccai__project__pb2.UpdateCcaiProjectRequest.SerializeToString,
            ondewo_dot_nlu_dot_ccai__project__pb2.UpdateCcaiProjectResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
