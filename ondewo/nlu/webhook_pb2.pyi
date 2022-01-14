"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import ondewo.nlu.context_pb2
import ondewo.nlu.intent_pb2
import ondewo.nlu.session_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class PingRequest(google.protobuf.message.Message):
    """request sent for webhook ping"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SESSION_FIELD_NUMBER: builtins.int
    session: typing.Text = ...
    """session ID for webhook ping"""

    def __init__(self,
        *,
        session : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["session",b"session"]) -> None: ...
global___PingRequest = PingRequest

class WebhookRequest(google.protobuf.message.Message):
    """The request message for a webhook call."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SESSION_FIELD_NUMBER: builtins.int
    RESPONSE_ID_FIELD_NUMBER: builtins.int
    QUERY_RESULT_FIELD_NUMBER: builtins.int
    ORIGINAL_DETECT_INTENT_REQUEST_FIELD_NUMBER: builtins.int
    HEADERS_FIELD_NUMBER: builtins.int
    session: typing.Text = ...
    """The unique identifier of detectIntent request session.
    Can be used to identify end-user inside webhook implementation.
    Format: `projects/<Project ID>/agent/sessions/<Session ID>`.
    """

    response_id: typing.Text = ...
    """The unique identifier of the response. Contains the same value as
    `[Streaming]DetectIntentResponse.response_id`.
    """

    @property
    def query_result(self) -> ondewo.nlu.session_pb2.QueryResult:
        """The result of the conversational query or event processing. Contains the
        same value as `[Streaming]DetectIntentResponse.query_result`.
        """
        pass
    @property
    def original_detect_intent_request(self) -> global___OriginalDetectIntentRequest:
        """Optional. The contents of the original request that was passed to
        `[Streaming]DetectIntent` call.
        """
        pass
    @property
    def headers(self) -> google.protobuf.struct_pb2.Struct:
        """Optional. The headers of the request message"""
        pass
    def __init__(self,
        *,
        session : typing.Text = ...,
        response_id : typing.Text = ...,
        query_result : typing.Optional[ondewo.nlu.session_pb2.QueryResult] = ...,
        original_detect_intent_request : typing.Optional[global___OriginalDetectIntentRequest] = ...,
        headers : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers",b"headers","original_detect_intent_request",b"original_detect_intent_request","query_result",b"query_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers",b"headers","original_detect_intent_request",b"original_detect_intent_request","query_result",b"query_result","response_id",b"response_id","session",b"session"]) -> None: ...
global___WebhookRequest = WebhookRequest

class WebhookResponse(google.protobuf.message.Message):
    """The response message for a webhook call."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FULFILLMENT_TEXT_FIELD_NUMBER: builtins.int
    FULFILLMENT_MESSAGES_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    OUTPUT_CONTEXTS_FIELD_NUMBER: builtins.int
    FOLLOWUP_EVENT_INPUT_FIELD_NUMBER: builtins.int
    fulfillment_text: typing.Text = ...
    """Optional. The text to be shown on the screen. This value is passed directly
    to `QueryResult.fulfillment_text`.
    """

    @property
    def fulfillment_messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ondewo.nlu.intent_pb2.Intent.Message]:
        """Optional. The collection of rich messages to present to the user. This
        value is passed directly to `QueryResult.fulfillment_messages`.
        """
        pass
    source: typing.Text = ...
    """Optional. This value is passed directly to `QueryResult.webhook_source`."""

    @property
    def payload(self) -> google.protobuf.struct_pb2.Struct:
        """Optional. This value is passed directly to `QueryResult.webhook_payload`.
        See the related `fulfillment_messages[i].payload field`, which may be used
        as an alternative to this field.

        This field can be used for Actions on Google responses.
        It should have a structure similar to the JSON message shown here. For more
        information, see
        [Actions on Google Webhook
        Format](https://developers.google.com/actions/dialogflow/webhook)
        <pre>{
          "google": {
            "expectUserResponse": true,
            "richResponse": {
              "items": [
                {
                  "simpleResponse": {
                    "textToSpeech": "this is a simple response"
                  }
                }
              ]
            }
          }
        }</pre>
        """
        pass
    @property
    def output_contexts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ondewo.nlu.context_pb2.Context]:
        """Optional. The collection of output contexts. This value is passed directly
        to `QueryResult.output_contexts`.
        """
        pass
    @property
    def followup_event_input(self) -> ondewo.nlu.session_pb2.EventInput:
        """Optional. Makes the platform immediately invoke another `DetectIntent` call
        internally with the specified event as input.
        """
        pass
    def __init__(self,
        *,
        fulfillment_text : typing.Text = ...,
        fulfillment_messages : typing.Optional[typing.Iterable[ondewo.nlu.intent_pb2.Intent.Message]] = ...,
        source : typing.Text = ...,
        payload : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        output_contexts : typing.Optional[typing.Iterable[ondewo.nlu.context_pb2.Context]] = ...,
        followup_event_input : typing.Optional[ondewo.nlu.session_pb2.EventInput] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["followup_event_input",b"followup_event_input","payload",b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["followup_event_input",b"followup_event_input","fulfillment_messages",b"fulfillment_messages","fulfillment_text",b"fulfillment_text","output_contexts",b"output_contexts","payload",b"payload","source",b"source"]) -> None: ...
global___WebhookResponse = WebhookResponse

class OriginalDetectIntentRequest(google.protobuf.message.Message):
    """Represents the contents of the original request that was passed to
    the `[Streaming]DetectIntent` call.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SOURCE_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    source: typing.Text = ...
    """The source of this request, e.g., `google`, `facebook`, `slack`. It is set
    by Dialogflow-owned servers.
    """

    @property
    def payload(self) -> google.protobuf.struct_pb2.Struct:
        """Optional. This field is set to the value of `QueryParameters.payload` field
        passed in the request.
        """
        pass
    def __init__(self,
        *,
        source : typing.Text = ...,
        payload : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["payload",b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["payload",b"payload","source",b"source"]) -> None: ...
global___OriginalDetectIntentRequest = OriginalDetectIntentRequest

class PingResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IS_REACHABLE_FIELD_NUMBER: builtins.int
    is_reachable: builtins.bool = ...
    """This is the response message of a Ping request.
    It's purpose is to report the reachability of a Webhook server.
    """

    def __init__(self,
        *,
        is_reachable : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["is_reachable",b"is_reachable"]) -> None: ...
global___PingResponse = PingResponse
