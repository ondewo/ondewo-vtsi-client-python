# Copyright 2021-2024 ONDEWO GmbH
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
from ondewo.utils.async_base_services_interface import AsyncBaseServicesInterface

from ondewo.vtsi import projects_pb2
from ondewo.vtsi.projects_pb2_grpc import ProjectsStub


class Projects(AsyncBaseServicesInterface):
    """
    A class representing the Projects service interface.

    This class provides methods to interact with the Projects service, which allows managing VtsiProjects.

    Inherits from BaseServicesInterface.
    """

    @property
    def stub(self) -> ProjectsStub:
        """
        Get the gRPC stub for the Projects service.

        Returns:
            ProjectsStub: The gRPC stub for the Projects service.
        """
        stub: ProjectsStub = ProjectsStub(channel=self.grpc_channel)
        return stub

    async def create_vtsi_project(
        self, request: projects_pb2.CreateVtsiProjectRequest
    ) -> projects_pb2.CreateVtsiProjectResponse:
        """
        Create a new VtsiProject.

        Args:
            request (projects_pb2.CreateVtsiProjectRequest): The request message to create a new VtsiProject.

        Returns:
            projects_pb2.CreateVtsiProjectResponse:
                The response message containing the details of the created VtsiProject.
        """
        return await self.stub.CreateVtsiProject(request=request)

    async def get_vtsi_project(self, request: projects_pb2.GetVtsiProjectRequest) -> projects_pb2.VtsiProject:
        """
        Get details of a specific VtsiProject.

        Args:
            request (projects_pb2.GetVtsiProjectRequest): The request message to get details of a VtsiProject.

        Returns:
            projects_pb2.VtsiProject: The response message containing the details of the specified VtsiProject.
        """
        return await self.stub.GetVtsiProject(request=request)

    async def update_vtsi_project(
        self, request: projects_pb2.UpdateVtsiProjectRequest
    ) -> projects_pb2.UpdateVtsiProjectResponse:
        """
        Update an existing VtsiProject.

        Args:
            request (projects_pb2.UpdateVtsiProjectRequest): The request message to update an existing VtsiProject.

        Returns:
            projects_pb2.UpdateVtsiProjectResponse:
                The response message containing the details of the updated VtsiProject.
        """
        return await self.stub.UpdateVtsiProject(request=request)

    async def delete_vtsi_project(
        self, request: projects_pb2.DeleteVtsiProjectRequest
    ) -> projects_pb2.DeleteVtsiProjectResponse:
        """
        Delete an existing VtsiProject.

        Args:
            request (projects_pb2.DeleteVtsiProjectRequest):
                The request message to delete an existing VtsiProject.

        Returns:
            projects_pb2.DeleteVtsiProjectResponse:
                The response message containing the details of the deleted VtsiProject.
        """
        return await self.stub.DeleteVtsiProject(request=request)

    async def deploy_vtsi_project(
        self, request: projects_pb2.DeployVtsiProjectRequest
    ) -> projects_pb2.DeployVtsiProjectResponse:
        """
        Deploy a VtsiProject.

        Args:
            request (projects_pb2.DeployVtsiProjectRequest):
                The request message to deploy a VtsiProject.

        Returns:
            projects_pb2.DeployVtsiProjectResponse:
                The response message containing the details of the deployed VtsiProject.
        """
        return await self.stub.DeployVtsiProject(request=request)

    async def undeploy_vtsi_project(
        self, request: projects_pb2.UndeployVtsiProjectRequest
    ) -> projects_pb2.UndeployVtsiProjectResponse:
        """
        Undeploy a VtsiProject.

        Args:
            request (projects_pb2.UndeployVtsiProjectRequest):
                The request message to undeploy a VtsiProject.

        Returns:
            projects_pb2.UndeployVtsiProjectResponse:
                The response message containing the details of the undeployed VtsiProject.
        """
        return await self.stub.UndeployVtsiProject(request=request)

    async def list_vtsi_projects(
        self, request: projects_pb2.ListVtsiProjectsRequest
    ) -> projects_pb2.ListVtsiProjectsResponse:
        """
        List all VtsiProjects.

        Args:
            request (projects_pb2.ListVtsiProjectsRequest): The request message to list all VtsiProjects.

        Returns:
            projects_pb2.ListVtsiProjectsResponse: The response message containing a list of all VtsiProjects.
        """
        return await self.stub.ListVtsiProjects(request=request)
