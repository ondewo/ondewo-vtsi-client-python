# Copyright 2021-2026 ONDEWO GmbH
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
The carrier TLS verification surface of the GENERATED code.

The VTSI server verifies the carrier's TLS certificate only when ``sip_trunk_verify_server`` is true AND
``sip_trunk_ca_certificates_pem`` is given, so both must keep their field numbers and their EXPLICIT PRESENCE:
an unset ``sip_trunk_verify_server`` means false, and an unset bundle must stay distinguishable from an empty one.
Dropping an ``optional`` keyword or renumbering either field makes these tests fail.
"""

from typing import Dict

import pytest
from google.protobuf.descriptor import FieldDescriptor

from ondewo.vtsi import projects_pb2

#: Field name -> field number.
TRUNK_TLS_FIELDS: Dict[str, int] = {
    "sip_trunk_ca_certificates_pem": 9,
    "sip_trunk_verify_server": 10,
}


@pytest.mark.parametrize("field_name,number", sorted(TRUNK_TLS_FIELDS.items()))
def test_trunk_tls_field_has_its_number_and_explicit_presence(field_name: str, number: int) -> None:
    field: FieldDescriptor = projects_pb2.AsteriskConfigsVariables.DESCRIPTOR.fields_by_name[field_name]
    assert field.number == number
    assert field.has_presence, f"{field_name} lost its `optional` keyword"


def test_unset_is_distinguishable_from_an_explicit_default() -> None:
    variables: projects_pb2.AsteriskConfigsVariables = projects_pb2.AsteriskConfigsVariables()
    assert not variables.HasField("sip_trunk_verify_server")
    assert not variables.HasField("sip_trunk_ca_certificates_pem")
    variables.sip_trunk_verify_server = False
    variables.sip_trunk_ca_certificates_pem = ""
    assert variables.HasField("sip_trunk_verify_server")
    assert variables.HasField("sip_trunk_ca_certificates_pem")
