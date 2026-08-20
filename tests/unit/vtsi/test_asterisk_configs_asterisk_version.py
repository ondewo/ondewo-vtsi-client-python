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
``AsteriskConfigs.asterisk_version`` must carry EXPLICIT PRESENCE.

The field selects the docker image tag of the Asterisk image a VTSI project starts. The server
falls back to its own ``ONDEWO_VTSI_ASTERISK_IMAGE_TAG`` default when the caller says nothing, so
"the caller said nothing" and "the caller sent the empty string" have to stay distinguishable on
the wire -- the first is a fallback, the second is a caller error. A plain proto3 scalar cannot
express that difference: it reads back as ``''`` either way and ``HasField`` raises on it.

These assertions are about the GENERATED code, not about a hand-written wrapper, which is why they
drive ``projects_pb2`` directly: if the ``optional`` keyword is ever dropped from the ``.proto``,
the regenerated client still compiles and every one of these tests fails.
"""

from typing import Optional

from ondewo.vtsi import projects_pb2

#: A real ONDEWO Asterisk image tag, so the value is representative rather than a placeholder.
ASTERISK_VERSION: str = "alpine-3.18-18.20.2"


def _configs(**overrides: object) -> projects_pb2.AsteriskConfigs:
    """Build an otherwise-valid ``AsteriskConfigs`` -- the oneof is set, as the server requires."""
    configs: projects_pb2.AsteriskConfigs = projects_pb2.AsteriskConfigs(
        asterisk_configs_target_directory_name="asterisk_configs_dir",
        asterisk_port=5060,
    )
    for name, value in overrides.items():
        setattr(configs, name, value)
    return configs


class TestAsteriskVersionHasExplicitPresence:
    def test_an_unset_asterisk_version_is_reported_as_absent(self) -> None:
        configs: projects_pb2.AsteriskConfigs = _configs()
        assert configs.HasField("asterisk_version") is False
        # The read still yields the scalar default, which is exactly why HasField is the question
        # a caller has to ask.
        assert configs.asterisk_version == ""

    def test_a_set_asterisk_version_is_reported_as_present(self) -> None:
        configs: projects_pb2.AsteriskConfigs = _configs(asterisk_version=ASTERISK_VERSION)
        assert configs.HasField("asterisk_version") is True
        assert configs.asterisk_version == ASTERISK_VERSION

    def test_an_explicitly_empty_asterisk_version_is_present_and_not_the_same_as_unset(self) -> None:
        """The distinction the ``optional`` keyword exists for: both read back ``''``."""
        configs: projects_pb2.AsteriskConfigs = _configs(asterisk_version="")
        assert configs.HasField("asterisk_version") is True
        assert configs.asterisk_version == ""
        assert configs != _configs()

    def test_clearing_asterisk_version_restores_absence(self) -> None:
        configs: projects_pb2.AsteriskConfigs = _configs(asterisk_version=ASTERISK_VERSION)
        configs.ClearField("asterisk_version")
        assert configs.HasField("asterisk_version") is False


class TestAsteriskVersionSurvivesTheWire:
    def test_presence_survives_serialization(self) -> None:
        for value in (ASTERISK_VERSION, ""):
            sent: projects_pb2.AsteriskConfigs = _configs(asterisk_version=value)
            received: projects_pb2.AsteriskConfigs = projects_pb2.AsteriskConfigs()
            received.ParseFromString(sent.SerializeToString())
            assert received.HasField("asterisk_version") is True
            assert received.asterisk_version == value

    def test_absence_survives_serialization(self) -> None:
        sent: projects_pb2.AsteriskConfigs = _configs()
        received: projects_pb2.AsteriskConfigs = projects_pb2.AsteriskConfigs()
        received.ParseFromString(sent.SerializeToString())
        assert received.HasField("asterisk_version") is False


class TestAsteriskVersionDoesNotDisturbTheConfigsOneof:
    """
    ``optional`` compiles to a SYNTHETIC oneof (``_asterisk_version``).

    The server reads its configuration variant with ``WhichOneof("asterisk_configs_oneof")`` and
    raises a caller-facing ``ValueError`` when that returns ``None``. A synthetic oneof sitting
    next to the real one must not change that answer, in either direction.
    """

    def test_setting_the_version_does_not_select_a_configuration_variant(self) -> None:
        configs: projects_pb2.AsteriskConfigs = projects_pb2.AsteriskConfigs(
            asterisk_version=ASTERISK_VERSION,
        )
        assert configs.WhichOneof("asterisk_configs_oneof") is None

    def test_the_configuration_variant_is_unaffected_by_the_version(self) -> None:
        configs: projects_pb2.AsteriskConfigs = _configs(asterisk_version=ASTERISK_VERSION)
        selected: Optional[str] = configs.WhichOneof("asterisk_configs_oneof")
        assert selected == "asterisk_configs_target_directory_name"

    def test_the_version_is_not_a_member_of_the_configuration_oneof(self) -> None:
        members = {
            field.name
            for field in projects_pb2.AsteriskConfigs.DESCRIPTOR.oneofs_by_name["asterisk_configs_oneof"].fields
        }
        assert "asterisk_version" not in members
        assert members == {
            "asterisk_configs_variables",
            "asterisk_configs_files",
            "asterisk_configs_target_directory_name",
        }


class TestThePresenceAssertionsAreFalsifiable:
    """
    A premise test: prove the descriptor really distinguishes the two kinds of scalar.

    Without it, the assertions above could pass for a reason other than the ``optional`` keyword.
    ``asterisk_port`` is the plain proto3 scalar sitting one field number below and is the control:
    it must report NO presence, and the generated stub must not even accept it as a ``HasField``
    argument (mypy rejects such a call, which is why this is asserted through the descriptor rather
    than by making the call).

    Dropping ``optional`` from the ``.proto`` flips ``asterisk_version`` into the ``asterisk_port``
    column here, and turns every test above into a ``ValueError``.
    """

    def test_the_plain_scalar_control_has_no_presence(self) -> None:
        field = projects_pb2.AsteriskConfigs.DESCRIPTOR.fields_by_name["asterisk_port"]
        assert field.has_presence is False
        assert field.containing_oneof is None

    def test_the_version_has_presence_via_a_synthetic_oneof(self) -> None:
        field = projects_pb2.AsteriskConfigs.DESCRIPTOR.fields_by_name["asterisk_version"]
        assert field.has_presence is True
        # ``optional`` on a proto3 scalar compiles to a synthetic one-member oneof named after the
        # field. Naming it here is what makes the mechanism visible rather than incidental.
        assert field.containing_oneof is not None
        assert field.containing_oneof.name == "_asterisk_version"
