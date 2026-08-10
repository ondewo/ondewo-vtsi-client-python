# Copyright 2021-2025 ONDEWO GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Iterator

from ondewo.vtsi import logs_pb2
from ondewo.vtsi.client.services_interface import ServicesInterface
from ondewo.vtsi.logs_pb2_grpc import LogsStub


class Logs(ServicesInterface):
    """
    A class representing the Logs service interface.

    This class provides methods to read the container logs of the per-call ondewo-sip / ondewo-csi
    containers that ondewo-vtsi captured into its database: a live server-stream, a filtered history
    query, log-stream metadata, and an erasure call.

    Inherits from ServicesInterface.
    """

    @property
    def stub(self) -> LogsStub:
        """
        Get the gRPC stub for the Logs service.

        Returns:
            LogsStub: The gRPC stub for the Logs service.
        """
        stub: LogsStub = LogsStub(channel=self.grpc_channel)
        return stub

    def stream_call_logs(
        self,
        request: logs_pb2.StreamCallLogsRequest,
    ) -> Iterator[logs_pb2.StreamCallLogsResponse]:
        """
        Stream captured container log entries as they arrive.

        The returned iterator is the live gRPC stream: iterating it blocks until the next batch is
        available, and abandoning it cancels the RPC, which releases the server-side stream slot.

        Args:
            request (logs_pb2.StreamCallLogsRequest):
                The request specifying the project, the filter and where to resume from.

        Returns:
            Iterator[logs_pb2.StreamCallLogsResponse]:
                An iterator over the response envelopes.
        """
        response: Iterator[logs_pb2.StreamCallLogsResponse] = self.stub.StreamCallLogs(
            request=request,
            metadata=self.metadata,
        )
        return response

    def list_call_logs(
        self,
        request: logs_pb2.ListCallLogsRequest,
    ) -> logs_pb2.ListCallLogsResponse:
        """
        Return a bounded, filtered page of captured container log entries.

        Args:
            request (logs_pb2.ListCallLogsRequest):
                The request specifying the project, the filter and the paging cursor.

        Returns:
            logs_pb2.ListCallLogsResponse:
                The matching entries plus the cursor bounds.
        """
        response: logs_pb2.ListCallLogsResponse = self.stub.ListCallLogs(
            request=request,
            metadata=self.metadata,
        )
        return response

    def get_call_log_stream(
        self,
        request: logs_pb2.GetCallLogStreamRequest,
    ) -> logs_pb2.CallLogStream:
        """
        Get the capture state of a single log stream.

        Args:
            request (logs_pb2.GetCallLogStreamRequest):
                The request specifying the project and the log stream name.

        Returns:
            logs_pb2.CallLogStream:
                The log stream.
        """
        response: logs_pb2.CallLogStream = self.stub.GetCallLogStream(
            request=request,
            metadata=self.metadata,
        )
        return response

    def list_call_log_streams(
        self,
        request: logs_pb2.ListCallLogStreamsRequest,
    ) -> logs_pb2.ListCallLogStreamsResponse:
        """
        List the log streams ondewo-vtsi has captured for a project.

        Args:
            request (logs_pb2.ListCallLogStreamsRequest):
                The request specifying the project, the filter and the page token.

        Returns:
            logs_pb2.ListCallLogStreamsResponse:
                The matching log streams.
        """
        response: logs_pb2.ListCallLogStreamsResponse = self.stub.ListCallLogStreams(
            request=request,
            metadata=self.metadata,
        )
        return response

    def delete_call_logs(
        self,
        request: logs_pb2.DeleteCallLogsRequest,
    ) -> logs_pb2.DeleteCallLogsResponse:
        """
        Permanently delete captured log entries matching a filter.

        Args:
            request (logs_pb2.DeleteCallLogsRequest):
                The request specifying the project and which entries to delete.

        Returns:
            logs_pb2.DeleteCallLogsResponse:
                How many entries and streams were deleted.
        """
        response: logs_pb2.DeleteCallLogsResponse = self.stub.DeleteCallLogs(
            request=request,
            metadata=self.metadata,
        )
        return response
