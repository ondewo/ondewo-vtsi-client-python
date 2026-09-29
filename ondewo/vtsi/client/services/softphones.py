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
from ondewo.vtsi import softphones_pb2
from ondewo.vtsi.client.services_interface import ServicesInterface
from ondewo.vtsi.softphones_pb2_grpc import SoftphonesStub


class Softphones(ServicesInterface):
    """
    A class representing the Softphones service interface.

    This class provides methods to manage the softphone accounts of a VTSI project: SIP accounts on the
    project's Asterisk for humans using a softphone such as Zoiper, their client certificates, credential
    rotation and softphone provisioning.

    Inherits from ServicesInterface.
    """

    @property
    def stub(self) -> SoftphonesStub:
        """
        Get the gRPC stub for the Softphones service.

        Returns:
            SoftphonesStub: The gRPC stub for the Softphones service.
        """
        stub: SoftphonesStub = SoftphonesStub(channel=self.grpc_channel)
        return stub

    def create_softphone_account(
        self,
        request: softphones_pb2.CreateSoftphoneAccountRequest,
    ) -> softphones_pb2.CreateSoftphoneAccountResponse:
        """
        Create a softphone account and return it with its ONE-TIME credentials.

        The response is the only place the SIP password and the PKCS#12 bundle ever appear; store them
        immediately and never log the response.

        Args:
            request (softphones_pb2.CreateSoftphoneAccountRequest):
                The request specifying the project and the account to create.

        Returns:
            softphones_pb2.CreateSoftphoneAccountResponse:
                The created account plus its one-time credentials.
        """
        response: softphones_pb2.CreateSoftphoneAccountResponse = self.stub.CreateSoftphoneAccount(
            request=request,
            metadata=self.metadata,
        )
        return response

    def get_softphone_account(
        self,
        request: softphones_pb2.GetSoftphoneAccountRequest,
    ) -> softphones_pb2.SoftphoneAccount:
        """
        Get a softphone account, optionally as a partial response selected by a field mask.

        Args:
            request (softphones_pb2.GetSoftphoneAccountRequest):
                The request specifying the account name and the optional field mask.

        Returns:
            softphones_pb2.SoftphoneAccount:
                The softphone account (never a secret).
        """
        response: softphones_pb2.SoftphoneAccount = self.stub.GetSoftphoneAccount(
            request=request,
            metadata=self.metadata,
        )
        return response

    def update_softphone_account(
        self,
        request: softphones_pb2.UpdateSoftphoneAccountRequest,
    ) -> softphones_pb2.SoftphoneAccount:
        """
        Update the fields of a softphone account named by the update mask.

        Args:
            request (softphones_pb2.UpdateSoftphoneAccountRequest):
                The request carrying the account and the required update mask.

        Returns:
            softphones_pb2.SoftphoneAccount:
                The updated softphone account.
        """
        response: softphones_pb2.SoftphoneAccount = self.stub.UpdateSoftphoneAccount(
            request=request,
            metadata=self.metadata,
        )
        return response

    def delete_softphone_account(
        self,
        request: softphones_pb2.DeleteSoftphoneAccountRequest,
    ) -> softphones_pb2.DeleteSoftphoneAccountResponse:
        """
        Delete a softphone account and revoke every certificate it holds.

        Args:
            request (softphones_pb2.DeleteSoftphoneAccountRequest):
                The request specifying the account to delete.

        Returns:
            softphones_pb2.DeleteSoftphoneAccountResponse:
                The deleted account name and the number of revoked certificates.
        """
        response: softphones_pb2.DeleteSoftphoneAccountResponse = self.stub.DeleteSoftphoneAccount(
            request=request,
            metadata=self.metadata,
        )
        return response

    def list_softphone_accounts(
        self,
        request: softphones_pb2.ListSoftphoneAccountsRequest,
    ) -> softphones_pb2.ListSoftphoneAccountsResponse:
        """
        List the softphone accounts of a project, filtered, sorted and paged.

        Args:
            request (softphones_pb2.ListSoftphoneAccountsRequest):
                The request specifying the project, filter, field mask, paging and sorting.

        Returns:
            softphones_pb2.ListSoftphoneAccountsResponse:
                One page of softphone accounts plus the next page token.
        """
        response: softphones_pb2.ListSoftphoneAccountsResponse = self.stub.ListSoftphoneAccounts(
            request=request,
            metadata=self.metadata,
        )
        return response

    def rotate_softphone_credentials(
        self,
        request: softphones_pb2.RotateSoftphoneCredentialsRequest,
    ) -> softphones_pb2.RotateSoftphoneCredentialsResponse:
        """
        Rotate the SIP password and/or the client certificate of a softphone account.

        The response carries the new ONE-TIME secrets; store them immediately and never log the response.

        Args:
            request (softphones_pb2.RotateSoftphoneCredentialsRequest):
                The request specifying the account and what to rotate.

        Returns:
            softphones_pb2.RotateSoftphoneCredentialsResponse:
                The account after rotation plus the rotated one-time credentials.
        """
        response: softphones_pb2.RotateSoftphoneCredentialsResponse = self.stub.RotateSoftphoneCredentials(
            request=request,
            metadata=self.metadata,
        )
        return response

    def list_softphone_certificates(
        self,
        request: softphones_pb2.ListSoftphoneCertificatesRequest,
    ) -> softphones_pb2.ListSoftphoneCertificatesResponse:
        """
        List softphone client certificates of an account or of a whole project.

        Args:
            request (softphones_pb2.ListSoftphoneCertificatesRequest):
                The request specifying the scope, filter, field mask and paging.

        Returns:
            softphones_pb2.ListSoftphoneCertificatesResponse:
                One page of certificates (public material only) plus the next page token.
        """
        response: softphones_pb2.ListSoftphoneCertificatesResponse = self.stub.ListSoftphoneCertificates(
            request=request,
            metadata=self.metadata,
        )
        return response

    def get_softphone_certificate(
        self,
        request: softphones_pb2.GetSoftphoneCertificateRequest,
    ) -> softphones_pb2.SoftphoneCertificate:
        """
        Get one softphone client certificate.

        Args:
            request (softphones_pb2.GetSoftphoneCertificateRequest):
                The request specifying the certificate name and the optional field mask.

        Returns:
            softphones_pb2.SoftphoneCertificate:
                The certificate (public material only).
        """
        response: softphones_pb2.SoftphoneCertificate = self.stub.GetSoftphoneCertificate(
            request=request,
            metadata=self.metadata,
        )
        return response

    def revoke_softphone_certificate(
        self,
        request: softphones_pb2.RevokeSoftphoneCertificateRequest,
    ) -> softphones_pb2.SoftphoneCertificate:
        """
        Revoke a softphone client certificate so the project's Asterisk no longer accepts it.

        Args:
            request (softphones_pb2.RevokeSoftphoneCertificateRequest):
                The request specifying the certificate and an optional reason.

        Returns:
            softphones_pb2.SoftphoneCertificate:
                The revoked certificate.
        """
        response: softphones_pb2.SoftphoneCertificate = self.stub.RevokeSoftphoneCertificate(
            request=request,
            metadata=self.metadata,
        )
        return response

    def get_softphone_provisioning(
        self,
        request: softphones_pb2.GetSoftphoneProvisioningRequest,
    ) -> softphones_pb2.SoftphoneProvisioning:
        """
        Get everything needed to configure a softphone such as Zoiper for an account, without secrets.

        Args:
            request (softphones_pb2.GetSoftphoneProvisioningRequest):
                The request specifying the account to provision.

        Returns:
            softphones_pb2.SoftphoneProvisioning:
                The provisioning data, including step-by-step Zoiper instructions.
        """
        response: softphones_pb2.SoftphoneProvisioning = self.stub.GetSoftphoneProvisioning(
            request=request,
            metadata=self.metadata,
        )
        return response
