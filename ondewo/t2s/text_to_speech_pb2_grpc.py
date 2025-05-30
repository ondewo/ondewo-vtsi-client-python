# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ondewo.t2s import text_to_speech_pb2 as ondewo_dot_t2s_dot_text__to__speech__pb2

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
        f' but the generated code in ondewo/t2s/text_to_speech_pb2_grpc.py depends on' +
        f' grpcio>={GRPC_GENERATED_VERSION}.' +
        f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' +
        f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class Text2SpeechStub(object):
    """Text2Speech service provides endpoints for text-to-speech generation.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Synthesize = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/Synthesize',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeResponse.FromString,
            _registered_method=True)
        self.BatchSynthesize = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/BatchSynthesize',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeResponse.FromString,
            _registered_method=True)
        self.NormalizeText = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/NormalizeText',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextResponse.FromString,
            _registered_method=True)
        self.GetT2sPipeline = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/GetT2sPipeline',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.FromString,
            _registered_method=True)
        self.CreateT2sPipeline = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/CreateT2sPipeline',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.FromString,
            _registered_method=True)
        self.DeleteT2sPipeline = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/DeleteT2sPipeline',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            _registered_method=True)
        self.UpdateT2sPipeline = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/UpdateT2sPipeline',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            _registered_method=True)
        self.ListT2sPipelines = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/ListT2sPipelines',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesResponse.FromString,
            _registered_method=True)
        self.ListT2sLanguages = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/ListT2sLanguages',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesResponse.FromString,
            _registered_method=True)
        self.ListT2sDomains = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/ListT2sDomains',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsResponse.FromString,
            _registered_method=True)
        self.GetServiceInfo = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/GetServiceInfo',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2SGetServiceInfoResponse.FromString,
            _registered_method=True)
        self.GetCustomPhonemizer = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/GetCustomPhonemizer',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.FromString,
            _registered_method=True)
        self.CreateCustomPhonemizer = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/CreateCustomPhonemizer',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CreateCustomPhonemizerRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.FromString,
            _registered_method=True)
        self.DeleteCustomPhonemizer = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/DeleteCustomPhonemizer',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            _registered_method=True)
        self.UpdateCustomPhonemizer = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/UpdateCustomPhonemizer',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.UpdateCustomPhonemizerRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.FromString,
            _registered_method=True)
        self.ListCustomPhonemizer = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/ListCustomPhonemizer',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerResponse.FromString,
            _registered_method=True)


class Text2SpeechServicer(object):
    """Text2Speech service provides endpoints for text-to-speech generation.
    """

    def Synthesize(self, request, context):
        """Synthesize RPC

        Synthesizes a specific text sent in the request with the provided configuration requirements
        and retrieves a response that includes the synthesized text as audio and the requested configuration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchSynthesize(self, request, context):
        """BatchSynthesize RPC

        Performs batch synthesis by accepting a batch of synthesis requests and returning a batch response.
        This can be more efficient for generating predictions on the AI model in bulk.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NormalizeText(self, request, context):
        """NormalizeText RPC

        Normalizes a text according to the specific pipeline's normalization rules.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetT2sPipeline(self, request, context):
        """GetT2sPipeline RPC

        Retrieves the configuration of the specified text-to-speech pipeline.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateT2sPipeline(self, request, context):
        """CreateT2sPipeline RPC

        Creates a new text-to-speech pipeline with the provided configuration and returns its pipeline ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteT2sPipeline(self, request, context):
        """DeleteT2sPipeline RPC

        Deletes the specified text-to-speech pipeline.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateT2sPipeline(self, request, context):
        """UpdateT2sPipeline RPC

        Updates the specified text-to-speech pipeline with the given configuration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListT2sPipelines(self, request, context):
        """ListT2sPipelines RPC

        Retrieves a list of text-to-speech pipelines based on specific requirements.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListT2sLanguages(self, request, context):
        """ListT2sLanguages RPC

        Retrieves a list of languages available based on specific configuration requirements.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListT2sDomains(self, request, context):
        """ListT2sDomains RPC

        Retrieves a list of domains available based on specific configuration requirements.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceInfo(self, request, context):
        """GetServiceInfo RPC

        Retrieves the version information of the running text-to-speech server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomPhonemizer(self, request, context):
        """GetCustomPhonemizer RPC

        Retrieves a custom phonemizer based on the provided PhonemizerId.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCustomPhonemizer(self, request, context):
        """CreateCustomPhonemizer RPC

        Creates a custom phonemizer based on the provided CreateCustomPhonemizerRequest.
        Returns the PhonemizerId associated with the created custom phonemizer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCustomPhonemizer(self, request, context):
        """DeleteCustomPhonemizer RPC

        Deletes a custom phonemizer based on the provided PhonemizerId.
        Returns an Empty response upon successful deletion.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCustomPhonemizer(self, request, context):
        """UpdateCustomPhonemizer RPC

        Updates the specified custom phonemizer with the provided configuration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCustomPhonemizer(self, request, context):
        """ListCustomPhonemizer RPC

        Retrieves a list of custom phonemizers based on specific requirements.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Text2SpeechServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Synthesize': grpc.unary_unary_rpc_method_handler(
            servicer.Synthesize,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeResponse.SerializeToString,
        ),
        'BatchSynthesize': grpc.unary_unary_rpc_method_handler(
            servicer.BatchSynthesize,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeResponse.SerializeToString,
        ),
        'NormalizeText': grpc.unary_unary_rpc_method_handler(
            servicer.NormalizeText,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextResponse.SerializeToString,
        ),
        'GetT2sPipeline': grpc.unary_unary_rpc_method_handler(
            servicer.GetT2sPipeline,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.SerializeToString,
        ),
        'CreateT2sPipeline': grpc.unary_unary_rpc_method_handler(
            servicer.CreateT2sPipeline,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.SerializeToString,
        ),
        'DeleteT2sPipeline': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteT2sPipeline,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'UpdateT2sPipeline': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateT2sPipeline,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'ListT2sPipelines': grpc.unary_unary_rpc_method_handler(
            servicer.ListT2sPipelines,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesResponse.SerializeToString,
        ),
        'ListT2sLanguages': grpc.unary_unary_rpc_method_handler(
            servicer.ListT2sLanguages,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesResponse.SerializeToString,
        ),
        'ListT2sDomains': grpc.unary_unary_rpc_method_handler(
            servicer.ListT2sDomains,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsResponse.SerializeToString,
        ),
        'GetServiceInfo': grpc.unary_unary_rpc_method_handler(
            servicer.GetServiceInfo,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2SGetServiceInfoResponse.SerializeToString,
        ),
        'GetCustomPhonemizer': grpc.unary_unary_rpc_method_handler(
            servicer.GetCustomPhonemizer,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.SerializeToString,
        ),
        'CreateCustomPhonemizer': grpc.unary_unary_rpc_method_handler(
            servicer.CreateCustomPhonemizer,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CreateCustomPhonemizerRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.SerializeToString,
        ),
        'DeleteCustomPhonemizer': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteCustomPhonemizer,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'UpdateCustomPhonemizer': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateCustomPhonemizer,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.UpdateCustomPhonemizerRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.SerializeToString,
        ),
        'ListCustomPhonemizer': grpc.unary_unary_rpc_method_handler(
            servicer.ListCustomPhonemizer,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ondewo.t2s.Text2Speech', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ondewo.t2s.Text2Speech', rpc_method_handlers)

 # This class is part of an EXPERIMENTAL API.


class Text2Speech(object):
    """Text2Speech service provides endpoints for text-to-speech generation.
    """

    @staticmethod
    def Synthesize(request,
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
            '/ondewo.t2s.Text2Speech/Synthesize',
            ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeRequest.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeResponse.FromString,
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
    def BatchSynthesize(request,
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
            '/ondewo.t2s.Text2Speech/BatchSynthesize',
            ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeRequest.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeResponse.FromString,
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
    def NormalizeText(request,
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
            '/ondewo.t2s.Text2Speech/NormalizeText',
            ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextRequest.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextResponse.FromString,
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
    def GetT2sPipeline(request,
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
            '/ondewo.t2s.Text2Speech/GetT2sPipeline',
            ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.FromString,
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
    def CreateT2sPipeline(request,
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
            '/ondewo.t2s.Text2Speech/CreateT2sPipeline',
            ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.FromString,
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
    def DeleteT2sPipeline(request,
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
            '/ondewo.t2s.Text2Speech/DeleteT2sPipeline',
            ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.SerializeToString,
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
    def UpdateT2sPipeline(request,
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
            '/ondewo.t2s.Text2Speech/UpdateT2sPipeline',
            ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.SerializeToString,
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
    def ListT2sPipelines(request,
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
            '/ondewo.t2s.Text2Speech/ListT2sPipelines',
            ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesRequest.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesResponse.FromString,
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
    def ListT2sLanguages(request,
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
            '/ondewo.t2s.Text2Speech/ListT2sLanguages',
            ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesRequest.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesResponse.FromString,
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
    def ListT2sDomains(request,
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
            '/ondewo.t2s.Text2Speech/ListT2sDomains',
            ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsRequest.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsResponse.FromString,
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
    def GetServiceInfo(request,
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
            '/ondewo.t2s.Text2Speech/GetServiceInfo',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.T2SGetServiceInfoResponse.FromString,
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
    def GetCustomPhonemizer(request,
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
            '/ondewo.t2s.Text2Speech/GetCustomPhonemizer',
            ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.FromString,
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
    def CreateCustomPhonemizer(request,
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
            '/ondewo.t2s.Text2Speech/CreateCustomPhonemizer',
            ondewo_dot_t2s_dot_text__to__speech__pb2.CreateCustomPhonemizerRequest.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.FromString,
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
    def DeleteCustomPhonemizer(request,
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
            '/ondewo.t2s.Text2Speech/DeleteCustomPhonemizer',
            ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.SerializeToString,
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
    def UpdateCustomPhonemizer(request,
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
            '/ondewo.t2s.Text2Speech/UpdateCustomPhonemizer',
            ondewo_dot_t2s_dot_text__to__speech__pb2.UpdateCustomPhonemizerRequest.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.FromString,
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
    def ListCustomPhonemizer(request,
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
            '/ondewo.t2s.Text2Speech/ListCustomPhonemizer',
            ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerRequest.SerializeToString,
            ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
