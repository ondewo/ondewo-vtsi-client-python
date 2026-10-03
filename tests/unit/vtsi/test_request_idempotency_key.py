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
"""
The optional ``idempotency_key`` on the five batch requests of ``Calls``, read from the generated descriptors.

A plain proto3 ``string``: no presence, so the empty default is the documented "no deduplication".
"""

from typing import (
    Any,
    List,
    Tuple,
)

import pytest
from google.protobuf.descriptor import FieldDescriptor

from ondewo.vtsi import calls_pb2

# (request message, field number of idempotency_key)
IDEMPOTENT_REQUESTS: List[Tuple[Any, int]] = [
    (calls_pb2.StartCallersRequest, 4),
    (calls_pb2.StartListenersRequest, 3),
    (calls_pb2.StartScheduledCallersRequest, 4),
    (calls_pb2.AddCallersToCampaignRequest, 4),
    (calls_pb2.AddScheduledCallersToCampaignRequest, 4),
]


@pytest.mark.parametrize(
    "message_type, number",
    IDEMPOTENT_REQUESTS,
    ids=[message_type.DESCRIPTOR.name for message_type, _ in IDEMPOTENT_REQUESTS],
)
def test_the_batch_request_carries_an_idempotency_key(message_type: Any, number: int) -> None:
    """The field has the published name, number and type, and survives a round trip."""
    field: Any = message_type.DESCRIPTOR.fields_by_name["idempotency_key"]
    assert field.number == number
    assert field.type == FieldDescriptor.TYPE_STRING
    assert not field.has_presence
    assert message_type().idempotency_key == ""
    request: Any = message_type(idempotency_key="retry-0001")
    assert message_type.FromString(request.SerializeToString()).idempotency_key == "retry-0001"
