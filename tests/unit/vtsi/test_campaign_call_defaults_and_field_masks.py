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
The ondewo-vtsi-api 9.1.0 campaign contract, read from the generated messages.

Campaign-level call defaults (``campaign_common_services_config`` / ``campaign_sip_caller_config``), the
plain-string ``display_name`` selectors that replace the removed ``CampaignDisplayName`` message, and the
``field_mask`` every campaign CRUD request and every ``List*`` request now carries.
"""

from types import ModuleType
from typing import (
    Any,
    List,
    Tuple,
)

import pytest
from google.protobuf.field_mask_pb2 import FieldMask

from ondewo.vtsi import (
    call_configs_pb2,
    calls_pb2,
    campaigns_pb2,
    events_pb2,
    logs_pb2,
    projects_pb2,
    softphones_pb2,
)

# The requests that select ONE campaign by resource name or display name, with the number the removed
# ``CampaignDisplayName`` member used to occupy.
CAMPAIGN_SELECTOR_REQUESTS: List[Tuple[Any, int]] = [
    (campaigns_pb2.GetCampaignRequest, 2),
    (campaigns_pb2.DeleteCampaignRequest, 2),
    (campaigns_pb2.GetCampaignStatisticsRequest, 2),
    (campaigns_pb2.StartCampaignRequest, 2),
    (campaigns_pb2.StopCampaignRequest, 2),
    (campaigns_pb2.HardStopCampaignRequest, 2),
    (campaigns_pb2.ResumeCampaignRequest, 2),
    (campaigns_pb2.ListCampaignCallsRequest, 7),
]

CAMPAIGN_CRUD_REQUESTS_WITH_A_FIELD_MASK: List[Any] = [
    campaigns_pb2.CreateCampaignRequest,
    campaigns_pb2.GetCampaignRequest,
    campaigns_pb2.UpdateCampaignRequest,
    campaigns_pb2.DeleteCampaignRequest,
    campaigns_pb2.ListCampaignsRequest,
    campaigns_pb2.ListCampaignCallsRequest,
]

VTSI_MODULES: List[ModuleType] = [calls_pb2, campaigns_pb2, events_pb2, logs_pb2, projects_pb2, softphones_pb2]

# A stream, not a listing: it has no page and no returned resource for a mask to narrow.
NOT_A_LISTING: List[str] = ["ListenCallAudioRequest"]


def _list_requests() -> List[Any]:
    """Every ``List*Request`` message of the vtsi modules that is a listing."""
    return [
        descriptor
        for module in VTSI_MODULES
        for name, descriptor in module.DESCRIPTOR.message_types_by_name.items()
        if name.startswith("List") and name.endswith("Request") and name not in NOT_A_LISTING
    ]


class TestTheCallConfigsModule:
    """``CommonServicesConfig`` / ``SipCallerConfig`` moved to ``call_configs.proto`` without moving on the wire."""

    def test_calls_pb2_still_exposes_the_moved_messages(self) -> None:
        """``import public`` keeps ``calls_pb2.CommonServicesConfig`` the very same class."""
        assert calls_pb2.CommonServicesConfig is call_configs_pb2.CommonServicesConfig
        assert calls_pb2.SipCallerConfig is call_configs_pb2.SipCallerConfig

    def test_the_fully_qualified_names_are_unchanged(self) -> None:
        """The package stays ``ondewo.vtsi``, so type URLs and the wire do not move."""
        assert call_configs_pb2.CommonServicesConfig.DESCRIPTOR.full_name == "ondewo.vtsi.CommonServicesConfig"
        assert call_configs_pb2.SipCallerConfig.DESCRIPTOR.full_name == "ondewo.vtsi.SipCallerConfig"
        assert call_configs_pb2.DESCRIPTOR.name == "ondewo/vtsi/call_configs.proto"

    def test_the_start_caller_request_still_uses_them(self) -> None:
        """``StartCallerRequest`` refers to the moved descriptors."""
        fields: Any = calls_pb2.StartCallerRequest.DESCRIPTOR.fields_by_name
        assert fields["sip_caller_config"].message_type is call_configs_pb2.SipCallerConfig.DESCRIPTOR
        assert fields["common_services_config"].message_type is call_configs_pb2.CommonServicesConfig.DESCRIPTOR


class TestTheCampaignCallDefaults:
    """A campaign carries the defaults of every one of its calls."""

    def test_the_two_new_fields_have_their_numbers_and_types(self) -> None:
        """Field 18 is the common-services default, 19 the SIP-caller default."""
        fields: Any = campaigns_pb2.Campaign.DESCRIPTOR.fields_by_name
        assert fields["campaign_common_services_config"].number == 18
        assert fields["campaign_common_services_config"].message_type is (
            call_configs_pb2.CommonServicesConfig.DESCRIPTOR
        )
        assert fields["campaign_sip_caller_config"].number == 19
        assert fields["campaign_sip_caller_config"].message_type is call_configs_pb2.SipCallerConfig.DESCRIPTOR

    def test_unset_defaults_are_absent_and_cost_nothing_on_the_wire(self) -> None:
        """A campaign that sets neither serialises exactly as before."""
        campaign: campaigns_pb2.Campaign = campaigns_pb2.Campaign(display_name="spring")
        assert not campaign.HasField("campaign_common_services_config")
        assert not campaign.HasField("campaign_sip_caller_config")
        assert campaign.SerializeToString() == campaigns_pb2.Campaign(display_name="spring").SerializeToString()

    def test_a_campaign_with_defaults_round_trips_in_a_create_request(self) -> None:
        """The defaults survive serialisation inside ``CreateCampaignRequest``."""
        campaign: campaigns_pb2.Campaign = campaigns_pb2.Campaign(
            display_name="spring",
            campaign_common_services_config=call_configs_pb2.CommonServicesConfig(),
            campaign_sip_caller_config=call_configs_pb2.SipCallerConfig(callee_id="+43123456789"),
        )
        request: campaigns_pb2.CreateCampaignRequest = campaigns_pb2.CreateCampaignRequest(
            vtsi_project_name="projects/p/project", campaign=campaign
        )
        parsed: campaigns_pb2.CreateCampaignRequest = campaigns_pb2.CreateCampaignRequest.FromString(
            request.SerializeToString()
        )
        assert parsed == request
        assert parsed.campaign.HasField("campaign_common_services_config")
        assert parsed.campaign.campaign_sip_caller_config.callee_id == "+43123456789"

    def test_a_new_campaign_of_an_assignment_carries_the_defaults(self) -> None:
        """``CampaignAssignment.new_campaign`` is a full ``Campaign``, defaults included."""
        assignment: campaigns_pb2.CampaignAssignment = campaigns_pb2.CampaignAssignment(
            new_campaign=campaigns_pb2.Campaign(
                display_name="spring",
                campaign_sip_caller_config=call_configs_pb2.SipCallerConfig(callee_id="+43123"),
            )
        )
        assert assignment.new_campaign.campaign_sip_caller_config.callee_id == "+43123"

    @pytest.mark.parametrize("path", ["campaign_common_services_config", "campaign_sip_caller_config"])
    def test_the_update_mask_accepts_the_new_paths(self, path: str) -> None:
        """``FieldMask.IsValidForDescriptor`` accepts the two paths on ``Campaign``."""
        assert FieldMask(paths=[path]).IsValidForDescriptor(campaigns_pb2.Campaign.DESCRIPTOR)

    def test_the_update_request_keeps_its_update_mask(self) -> None:
        """``UpdateCampaignRequest`` has both the ``update_mask`` and the partial-response ``field_mask``."""
        fields: Any = campaigns_pb2.UpdateCampaignRequest.DESCRIPTOR.fields_by_name
        assert fields["update_mask"].message_type is FieldMask.DESCRIPTOR
        assert fields["field_mask"].message_type is FieldMask.DESCRIPTOR


class TestTheDisplayNameSelectorIsAPlainString:
    """``CampaignDisplayName`` is gone; every selector is a ``string display_name``."""

    def test_the_message_is_removed(self) -> None:
        """Neither the module attribute nor the descriptor exists any more."""
        assert not hasattr(campaigns_pb2, "CampaignDisplayName")
        assert "CampaignDisplayName" not in campaigns_pb2.DESCRIPTOR.message_types_by_name

    @pytest.mark.parametrize("request_type,old_number", CAMPAIGN_SELECTOR_REQUESTS)
    def test_every_selector_is_a_string_with_a_project(self, request_type: Any, old_number: int) -> None:
        """A string ``display_name`` in the oneof, a top-level ``vtsi_project_name``, the old number unused."""
        descriptor: Any = request_type.DESCRIPTOR
        display_name: Any = descriptor.fields_by_name["display_name"]
        assert display_name.type == display_name.TYPE_STRING
        assert display_name.containing_oneof is not None
        assert [field.name for field in display_name.containing_oneof.fields if field is not display_name] in (
            ["name"],
            ["campaign_name"],
        )
        project: Any = descriptor.fields_by_name["vtsi_project_name"]
        assert project.type == project.TYPE_STRING
        assert project.containing_oneof is None
        assert old_number not in descriptor.fields_by_number
        assert display_name.number != old_number
        assert "campaign_display_name" not in descriptor.fields_by_name

    def test_the_assignment_selector_is_a_string_and_field_4_stays_unused(self) -> None:
        """``CampaignAssignment.display_name`` is field 5; the old message-typed 4 is reserved."""
        descriptor: Any = campaigns_pb2.CampaignAssignment.DESCRIPTOR
        assert descriptor.fields_by_name["display_name"].number == 5
        assert descriptor.fields_by_name["display_name"].type == descriptor.fields_by_name["display_name"].TYPE_STRING
        assert 4 not in descriptor.fields_by_number

    def test_a_display_name_selector_round_trips(self) -> None:
        """Setting the string selects it in the oneof and survives serialisation."""
        request: campaigns_pb2.GetCampaignRequest = campaigns_pb2.GetCampaignRequest(
            vtsi_project_name="projects/p/project", display_name="spring"
        )
        assert request.WhichOneof("campaign") == "display_name"
        assert campaigns_pb2.GetCampaignRequest.FromString(request.SerializeToString()) == request


class TestFieldMasks:
    """Partial responses on every campaign CRUD request and every listing."""

    @pytest.mark.parametrize("request_type", CAMPAIGN_CRUD_REQUESTS_WITH_A_FIELD_MASK)
    def test_every_campaign_crud_request_has_a_field_mask(self, request_type: Any) -> None:
        """``field_mask`` is a ``google.protobuf.FieldMask``."""
        assert request_type.DESCRIPTOR.fields_by_name["field_mask"].message_type is FieldMask.DESCRIPTOR

    def test_every_listing_has_a_field_mask(self) -> None:
        """No ``List*Request`` of the vtsi modules lacks one."""
        listings: List[Any] = _list_requests()
        assert len(listings) >= 13
        missing: List[str] = [
            descriptor.full_name
            for descriptor in listings
            if "field_mask" not in descriptor.fields_by_name
            or descriptor.fields_by_name["field_mask"].message_type is not FieldMask.DESCRIPTOR
        ]
        assert missing == []

    def test_a_masked_list_request_round_trips(self) -> None:
        """A ``ListCallsRequest`` with a mask survives serialisation."""
        request: calls_pb2.ListCallsRequest = calls_pb2.ListCallsRequest(field_mask=FieldMask(paths=["name", "status"]))
        assert list(calls_pb2.ListCallsRequest.FromString(request.SerializeToString()).field_mask.paths) == [
            "name",
            "status",
        ]
