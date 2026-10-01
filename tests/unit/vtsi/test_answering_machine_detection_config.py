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
The answering machine detection (AMD) surface of the GENERATED code.

Three contracts the VTSI server and the SIP/CSI containers rely on:

* every singular ``AnsweringMachineDetectionConfig`` field carries EXPLICIT PRESENCE, because an unset field
  means "use the CSI container default" and must stay distinguishable from an explicit ``false`` / ``0``;
* the field and enum numbers are the ones the server maps (``VoiceInteractionConfig`` field 4,
  ``Call`` fields 19, 20 and 21);
* the vendored ``ondewo/sip`` stubs carry the same sip-api AMD surface as ``ondewo-sip-client`` (the
  non-terminal status 22 ``OUTGOING_CALL_ANSWERING_MACHINE_DETECTED``, ``SipStatus.amd_result``, the
  voice-message action and end reason, ``SipReportAnsweringMachineDetected``), because the last installed copy
  of ``ondewo/sip`` wins.

Dropping an ``optional`` keyword, renumbering a field, or regenerating against a sip-api without AMD makes these
tests fail.
"""

from typing import Dict, List

import pytest
from google.protobuf.descriptor import Descriptor, FieldDescriptor
from google.protobuf.message import Message

from ondewo.sip import sip_pb2
from ondewo.vtsi import calls_pb2

#: Singular AMD fields and their numbers; each must have explicit presence.
OPTIONAL_AMD_FIELDS: Dict[str, int] = {
    "active": 1,
    "action": 2,
    "sensitivity": 3,
    "max_decision_time_ms": 4,
    "max_machine_wait_ms": 5,
    "beep_wait_after_greeting_ms": 6,
    "initial_silence_ms": 7,
    "max_human_greeting_ms": 8,
    "greeting_end_silence_ms": 9,
    "beep_detection_active": 10,
    "hang_up_on_fax": 13,
    "hang_up_on_network_announcement": 14,
    "hang_up_on_ivr": 15,
    "hang_up_on_call_screening": 16,
    "voice_message_intent": 17,
    "voice_message_max_beep_wait_ms": 18,
    "voice_message_timeout_ms": 19,
    "keyword_detection_active": 20,
    "cadence_detection_active": 21,
}

#: Repeated AMD phrase-list fields and their numbers.
REPEATED_AMD_FIELDS: Dict[str, int] = {
    "additional_machine_phrases": 11,
    "additional_human_phrases": 12,
}

AMD_DESCRIPTOR: Descriptor = calls_pb2.AnsweringMachineDetectionConfig.DESCRIPTOR


def _has_field(message: Message, field_name: str) -> bool:
    """Ask ``HasField`` for a field name only known at run time (the generated stubs type it as a Literal)."""
    return message.HasField(field_name)


class TestAnsweringMachineDetectionConfig:
    def test_the_message_has_exactly_the_planned_fields(self) -> None:
        numbers: Dict[str, int] = {field.name: field.number for field in AMD_DESCRIPTOR.fields}
        assert numbers == {**OPTIONAL_AMD_FIELDS, **REPEATED_AMD_FIELDS}

    @pytest.mark.parametrize("field_name", sorted(OPTIONAL_AMD_FIELDS))
    def test_every_singular_field_has_explicit_presence(self, field_name: str) -> None:
        field: FieldDescriptor = AMD_DESCRIPTOR.fields_by_name[field_name]
        assert field.has_presence is True
        config: calls_pb2.AnsweringMachineDetectionConfig = calls_pb2.AnsweringMachineDetectionConfig()
        assert _has_field(config, field_name) is False

    def test_an_explicit_false_is_present_and_not_the_same_as_unset(self) -> None:
        config: calls_pb2.AnsweringMachineDetectionConfig = calls_pb2.AnsweringMachineDetectionConfig(
            hang_up_on_fax=False,
        )
        assert config.HasField("hang_up_on_fax") is True
        assert config.SerializeToString() != b""

    @pytest.mark.parametrize("field_name", sorted(REPEATED_AMD_FIELDS))
    def test_the_phrase_lists_are_repeated_strings(self, field_name: str) -> None:
        field: FieldDescriptor = AMD_DESCRIPTOR.fields_by_name[field_name]
        assert field.is_repeated is True
        assert field.type == FieldDescriptor.TYPE_STRING

    def test_the_enums_have_an_unspecified_zero_and_the_planned_values(self) -> None:
        action: Dict[str, int] = dict(calls_pb2.AnsweringMachineDetectionConfig.AmdAction.items())
        sensitivity: Dict[str, int] = dict(calls_pb2.AnsweringMachineDetectionConfig.AmdSensitivity.items())
        assert action == {"AMD_ACTION_UNSPECIFIED": 0, "HANG_UP": 1, "DETECT_ONLY": 2, "LEAVE_VOICE_MESSAGE": 3}
        assert sensitivity == {"AMD_SENSITIVITY_UNSPECIFIED": 0, "LOW": 1, "MEDIUM": 2, "HIGH": 3}

    def test_it_is_field_4_of_voice_interaction_config(self) -> None:
        field: FieldDescriptor = calls_pb2.VoiceInteractionConfig.DESCRIPTOR.fields_by_name[
            "answering_machine_detection_config"
        ]
        assert field.number == 4
        assert field.message_type is AMD_DESCRIPTOR


class TestCallRedialMarker:
    @pytest.mark.parametrize(
        ("field_name", "number"),
        [
            ("redial_recommended", 19),
            ("redial_reason", 20),
            ("answering_machine_detection_end_description", 21),
        ],
    )
    def test_the_redial_fields_have_presence_and_their_numbers(self, field_name: str, number: int) -> None:
        field: FieldDescriptor = calls_pb2.Call.DESCRIPTOR.fields_by_name[field_name]
        assert field.number == number
        assert field.has_presence is True
        assert _has_field(calls_pb2.Call(), field_name) is False

    def test_the_amd_verdict_is_reachable_through_call_sip_status(self) -> None:
        call: calls_pb2.Call = calls_pb2.Call(
            sip_status=sip_pb2.SipStatus(
                status_type=sip_pb2.SipStatus.StatusType.OUTGOING_CALL_FINISHED,
                description="Answering machine detected with hang up",
                amd_result=sip_pb2.AnsweringMachineDetectionResult(
                    verdict=sip_pb2.AnsweringMachineDetectionResult.Verdict.MACHINE,
                ),
            ),
            redial_recommended=True,
            redial_reason="answering_machine",
            answering_machine_detection_end_description="Answering machine detected with hang up",
        )
        parsed: calls_pb2.Call = calls_pb2.Call.FromString(call.SerializeToString())
        assert parsed.sip_status.amd_result.verdict == sip_pb2.AnsweringMachineDetectionResult.Verdict.MACHINE
        assert parsed.redial_recommended is True
        assert parsed.answering_machine_detection_end_description == "Answering machine detected with hang up"


class TestVendoredSipProtoCarriesAmd:
    def test_status_22_is_the_answering_machine_detected_status(self) -> None:
        assert sip_pb2.SipStatus.StatusType.Value("OUTGOING_CALL_ANSWERING_MACHINE_DETECTED") == 22
        assert "OUTGOING_CALL_ANSWERING_MACHINE" not in sip_pb2.SipStatus.StatusType.keys()

    def test_the_voice_message_action_and_end_reason_exist(self) -> None:
        assert sip_pb2.AnsweringMachineDetectionResult.ActionTaken.Value("LEFT_VOICE_MESSAGE") == 4
        assert sip_pb2.SipEndCallRequest.EndCallReason.Value("ANSWERING_MACHINE_VOICE_MESSAGE_LEFT") == 2

    def test_the_detected_report_rpc_exists(self) -> None:
        method_names: List[str] = [method.name for method in sip_pb2.DESCRIPTOR.services_by_name["Sip"].methods]
        assert "SipReportAnsweringMachineDetected" in method_names

    def test_end_call_request_carries_the_reason_and_the_result(self) -> None:
        names: List[str] = [field.name for field in sip_pb2.SipEndCallRequest.DESCRIPTOR.fields]
        assert "end_reason" in names
        assert "amd_result" in names
