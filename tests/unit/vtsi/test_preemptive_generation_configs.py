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
The per-call preemptive generation settings must reach the generated client with EXPLICIT PRESENCE.

``NluVtsiConfig.preemptive_generation_config``, ``T2sVtsiConfig.preemptive_synthesis_config`` and
``CsiVtsiConfig.preemptive_generation_config`` carry only ``optional`` scalars: an unset field keeps the
deployment's value, so "the caller said nothing" must stay distinguishable from an explicit ``0`` / ``false``
(``max_drafts_per_turn=0`` switches drafts off, ``enabled=false`` switches preemptive generation off). These
tests drive the generated ``call_configs_pb2`` directly, so a dropped ``optional`` keyword or a renumbered
field fails here after the regeneration.
"""

from typing import Dict, List, Tuple, Type

from google.protobuf.message import Message

from ondewo.vtsi import call_configs_pb2

#: (message, its scalar fields with their field numbers), as declared in ondewo-vtsi-api 9.4.0.
PREEMPTIVE_MESSAGES: List[Tuple[Type[Message], Dict[str, int]]] = [
    (
        call_configs_pb2.NluPreemptiveGenerationConfig,
        {"max_drafts_per_turn": 1, "min_stable_dwell_seconds": 2, "min_interval_seconds": 3},
    ),
    (call_configs_pb2.T2sPreemptiveSynthesisConfig, {"enabled": 1, "chunked": 2}),
    (call_configs_pb2.CsiPreemptiveGenerationConfig, {"enabled": 1, "commit_wait_timeout_seconds": 2}),
]

#: (container message, field name, field number) of the three sub-messages.
CONTAINERS: List[Tuple[Type[Message], str, int]] = [
    (call_configs_pb2.NluVtsiConfig, "preemptive_generation_config", 10),
    (call_configs_pb2.T2sVtsiConfig, "preemptive_synthesis_config", 3),
    (call_configs_pb2.CsiVtsiConfig, "preemptive_generation_config", 7),
]


class TestTheFieldsAreWhereTheApiDeclaresThem:
    def test_every_scalar_has_its_number_and_explicit_presence(self) -> None:
        for message_type, fields in PREEMPTIVE_MESSAGES:
            descriptor = message_type.DESCRIPTOR
            assert {field.name: field.number for field in descriptor.fields} == fields, descriptor.full_name
            for name in fields:
                assert descriptor.fields_by_name[name].has_presence, f"{descriptor.full_name}.{name}"

    def test_every_sub_message_hangs_off_its_service_config(self) -> None:
        for container_type, name, number in CONTAINERS:
            field = container_type.DESCRIPTOR.fields_by_name[name]
            assert field.number == number
            assert field.message_type is not None


class TestAZeroValueIsPresentAndSurvivesTheWire:
    def test_an_unset_field_is_absent_and_an_explicit_zero_is_present(self) -> None:
        nlu: call_configs_pb2.NluPreemptiveGenerationConfig = call_configs_pb2.NluPreemptiveGenerationConfig()
        assert not nlu.HasField("max_drafts_per_turn")
        nlu.max_drafts_per_turn = 0
        assert nlu.HasField("max_drafts_per_turn")

        csi: call_configs_pb2.CsiPreemptiveGenerationConfig = call_configs_pb2.CsiPreemptiveGenerationConfig()
        assert not csi.HasField("enabled")
        csi.enabled = False
        assert csi.HasField("enabled")

    def test_presence_survives_serialization_inside_the_common_services_config(self) -> None:
        sent = call_configs_pb2.CommonServicesConfig(
            nlu_vtsi_config=call_configs_pb2.NluVtsiConfig(
                preemptive_generation_config=call_configs_pb2.NluPreemptiveGenerationConfig(max_drafts_per_turn=0)
            ),
            t2s_vtsi_config=call_configs_pb2.T2sVtsiConfig(
                preemptive_synthesis_config=call_configs_pb2.T2sPreemptiveSynthesisConfig(chunked=False)
            ),
            csi_vtsi_config=call_configs_pb2.CsiVtsiConfig(
                preemptive_generation_config=call_configs_pb2.CsiPreemptiveGenerationConfig(enabled=False)
            ),
        )
        received = call_configs_pb2.CommonServicesConfig()
        received.ParseFromString(sent.SerializeToString())

        assert received.nlu_vtsi_config.preemptive_generation_config.HasField("max_drafts_per_turn")
        assert not received.nlu_vtsi_config.preemptive_generation_config.HasField("min_interval_seconds")
        assert received.t2s_vtsi_config.preemptive_synthesis_config.HasField("chunked")
        assert not received.t2s_vtsi_config.preemptive_synthesis_config.HasField("enabled")
        assert received.csi_vtsi_config.preemptive_generation_config.HasField("enabled")
        assert not received.csi_vtsi_config.preemptive_generation_config.HasField("commit_wait_timeout_seconds")
