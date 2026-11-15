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
from ondewo.vtsi import ivr_menus_pb2
from ondewo.vtsi.client.services_interface import ServicesInterface
from ondewo.vtsi.ivr_menus_pb2_grpc import IvrMenusStub


class IvrMenus(ServicesInterface):
    """
    A class representing the IvrMenus service interface.

    This class provides methods to build, validate, publish and test the IVR menus of a VTSI project: DTMF and
    speech menus rendered into the project's Asterisk, their revisions, their test calls and their dialplan.

    Inherits from ServicesInterface.
    """

    @property
    def stub(self) -> IvrMenusStub:
        """
        Get the gRPC stub for the IvrMenus service.

        Returns:
            IvrMenusStub: The gRPC stub for the IvrMenus service.
        """
        stub: IvrMenusStub = IvrMenusStub(channel=self.grpc_channel)
        return stub

    def create_ivr_menu(
        self,
        request: ivr_menus_pb2.CreateIvrMenuRequest,
    ) -> ivr_menus_pb2.IvrMenu:
        """
        Create an IVR menu as a DRAFT (revision 1); nothing routes until it is published.

        Args:
            request (ivr_menus_pb2.CreateIvrMenuRequest):
                The request specifying the project and the menu to create.

        Returns:
            ivr_menus_pb2.IvrMenu:
                The created menu.
        """
        response: ivr_menus_pb2.IvrMenu = self.stub.CreateIvrMenu(
            request=request,
            metadata=self.metadata,
        )
        return response

    def get_ivr_menu(
        self,
        request: ivr_menus_pb2.GetIvrMenuRequest,
    ) -> ivr_menus_pb2.IvrMenu:
        """
        Get an IVR menu at its current revision.

        Args:
            request (ivr_menus_pb2.GetIvrMenuRequest):
                The request specifying the menu name and the optional field mask.

        Returns:
            ivr_menus_pb2.IvrMenu:
                The menu.
        """
        response: ivr_menus_pb2.IvrMenu = self.stub.GetIvrMenu(
            request=request,
            metadata=self.metadata,
        )
        return response

    def update_ivr_menu(
        self,
        request: ivr_menus_pb2.UpdateIvrMenuRequest,
    ) -> ivr_menus_pb2.IvrMenu:
        """
        Update the fields named in ``update_mask``; a changed graph field saves a new DRAFT revision.

        Args:
            request (ivr_menus_pb2.UpdateIvrMenuRequest):
                The request carrying the menu, the update mask and the optional expected revision.

        Returns:
            ivr_menus_pb2.IvrMenu:
                The updated menu.
        """
        response: ivr_menus_pb2.IvrMenu = self.stub.UpdateIvrMenu(
            request=request,
            metadata=self.metadata,
        )
        return response

    def delete_ivr_menu(
        self,
        request: ivr_menus_pb2.DeleteIvrMenuRequest,
    ) -> ivr_menus_pb2.DeleteIvrMenuResponse:
        """
        Delete an IVR menu and all its revisions.

        Args:
            request (ivr_menus_pb2.DeleteIvrMenuRequest):
                The request specifying the menu name and whether to force the deletion.

        Returns:
            ivr_menus_pb2.DeleteIvrMenuResponse:
                The deletion response.
        """
        response: ivr_menus_pb2.DeleteIvrMenuResponse = self.stub.DeleteIvrMenu(
            request=request,
            metadata=self.metadata,
        )
        return response

    def list_ivr_menus(
        self,
        request: ivr_menus_pb2.ListIvrMenusRequest,
    ) -> ivr_menus_pb2.ListIvrMenusResponse:
        """
        List the IVR menus of a project.

        Args:
            request (ivr_menus_pb2.ListIvrMenusRequest):
                The request specifying the project and the page.

        Returns:
            ivr_menus_pb2.ListIvrMenusResponse:
                One page of menus.
        """
        response: ivr_menus_pb2.ListIvrMenusResponse = self.stub.ListIvrMenus(
            request=request,
            metadata=self.metadata,
        )
        return response

    def validate_ivr_menu(
        self,
        request: ivr_menus_pb2.ValidateIvrMenuRequest,
    ) -> ivr_menus_pb2.ValidateIvrMenuResponse:
        """
        Validate a draft menu and return ALL its issues with their node paths; writes nothing.

        Args:
            request (ivr_menus_pb2.ValidateIvrMenuRequest):
                The request carrying the draft menu.

        Returns:
            ivr_menus_pb2.ValidateIvrMenuResponse:
                Every issue found.
        """
        response: ivr_menus_pb2.ValidateIvrMenuResponse = self.stub.ValidateIvrMenu(
            request=request,
            metadata=self.metadata,
        )
        return response

    def publish_ivr_menu(
        self,
        request: ivr_menus_pb2.PublishIvrMenuRequest,
    ) -> ivr_menus_pb2.IvrMenu:
        """
        Publish a revision of a menu into the project's Asterisk and switch its bound phone numbers to it.

        Args:
            request (ivr_menus_pb2.PublishIvrMenuRequest):
                The request specifying the menu and the revision to publish.

        Returns:
            ivr_menus_pb2.IvrMenu:
                The menu after the publication.
        """
        response: ivr_menus_pb2.IvrMenu = self.stub.PublishIvrMenu(
            request=request,
            metadata=self.metadata,
        )
        return response

    def clone_ivr_menu(
        self,
        request: ivr_menus_pb2.CloneIvrMenuRequest,
    ) -> ivr_menus_pb2.IvrMenu:
        """
        Copy a menu (its current or a given revision) into a new DRAFT menu without phone numbers.

        Args:
            request (ivr_menus_pb2.CloneIvrMenuRequest):
                The request specifying the source menu and the new display name.

        Returns:
            ivr_menus_pb2.IvrMenu:
                The new draft menu.
        """
        response: ivr_menus_pb2.IvrMenu = self.stub.CloneIvrMenu(
            request=request,
            metadata=self.metadata,
        )
        return response

    def list_ivr_menu_revisions(
        self,
        request: ivr_menus_pb2.ListIvrMenuRevisionsRequest,
    ) -> ivr_menus_pb2.ListIvrMenuRevisionsResponse:
        """
        List the saved revisions of a menu, newest first.

        Args:
            request (ivr_menus_pb2.ListIvrMenuRevisionsRequest):
                The request specifying the menu and the page.

        Returns:
            ivr_menus_pb2.ListIvrMenuRevisionsResponse:
                One page of revisions.
        """
        response: ivr_menus_pb2.ListIvrMenuRevisionsResponse = self.stub.ListIvrMenuRevisions(
            request=request,
            metadata=self.metadata,
        )
        return response

    def test_ivr_menu(
        self,
        request: ivr_menus_pb2.TestIvrMenuRequest,
    ) -> ivr_menus_pb2.IvrMenuTest:
        """
        Start a test call through the PUBLISHED revision of a menu; returns at once with the test RUNNING.

        Poll ``get_ivr_menu_test`` for the result. A test never dials a listener, a softphone or a phone number.

        Args:
            request (ivr_menus_pb2.TestIvrMenuRequest):
                The request specifying the menu, the scripted steps and the optional maximum duration.

        Returns:
            ivr_menus_pb2.IvrMenuTest:
                The started test, in ``IVR_MENU_TEST_STATE_RUNNING``.
        """
        response: ivr_menus_pb2.IvrMenuTest = self.stub.TestIvrMenu(
            request=request,
            metadata=self.metadata,
        )
        return response

    def get_ivr_menu_test(
        self,
        request: ivr_menus_pb2.GetIvrMenuTestRequest,
    ) -> ivr_menus_pb2.IvrMenuTest:
        """
        Get a test started by ``test_ivr_menu``: its state and the path traversed so far.

        Args:
            request (ivr_menus_pb2.GetIvrMenuTestRequest):
                The request specifying the test name.

        Returns:
            ivr_menus_pb2.IvrMenuTest:
                The test.
        """
        response: ivr_menus_pb2.IvrMenuTest = self.stub.GetIvrMenuTest(
            request=request,
            metadata=self.metadata,
        )
        return response

    def get_ivr_menu_dialplan(
        self,
        request: ivr_menus_pb2.GetIvrMenuDialplanRequest,
    ) -> ivr_menus_pb2.GetIvrMenuDialplanResponse:
        """
        Get the rendered dialplan of one revision, read-only, for support.

        Args:
            request (ivr_menus_pb2.GetIvrMenuDialplanRequest):
                The request specifying the menu and the revision.

        Returns:
            ivr_menus_pb2.GetIvrMenuDialplanResponse:
                The rendered dialplan.
        """
        response: ivr_menus_pb2.GetIvrMenuDialplanResponse = self.stub.GetIvrMenuDialplan(
            request=request,
            metadata=self.metadata,
        )
        return response
