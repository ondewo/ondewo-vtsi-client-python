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
TLS and mutual TLS end to end: the SDK's real ``Client`` / ``AsyncClient`` against a real TLS server.

The channel is built by ``ondewo-client-utils`` (``ServicesInterface`` and ``build_shared_channel``
forward the config untouched); these tests prove that a ``ClientConfig`` carrying
``grpc_client_cert`` / ``grpc_client_key`` really completes a handshake with a server that requires
client certificates, per service and over the shared channel, sync and ``grpc.aio``.

The certificates are minted per test module (never committed). The servers have no servicers, so an
RPC answered ``UNIMPLEMENTED`` proves the request crossed the handshake; a refused handshake surfaces
as ``UNAVAILABLE``. ``DeleteCallers`` is used because it is not idempotent and so has no retry policy:
a refused handshake fails at once instead of being retried until the deadline.
"""

import datetime
from concurrent import futures
from typing import (
    Any,
    Callable,
    Iterator,
    List,
    Optional,
)

import grpc
import pytest
import pytest_asyncio
from cryptography import x509
from cryptography.hazmat.primitives import (
    hashes,
    serialization,
)
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import (
    ExtendedKeyUsageOID,
    NameOID,
)

from ondewo.vtsi import calls_pb2
from ondewo.vtsi.client.async_client import AsyncClient
from ondewo.vtsi.client.client import Client
from ondewo.vtsi.client.client_config import ClientConfig

SERVER_NAME: str = "localhost"
TIMEOUT_IN_S: float = 10.0


class Pki:
    """One throwaway CA with a server leaf (SAN ``localhost``) and a client leaf, all PEM bytes."""

    def __init__(self, name: str) -> None:
        self._ca_key: ec.EllipticCurvePrivateKey = ec.generate_private_key(ec.SECP256R1())
        self.ca_cert: bytes = self._issue(f"{name}-ca", self._ca_key.public_key(), ca=True, issuer=None)
        ca: x509.Certificate = x509.load_pem_x509_certificate(self.ca_cert)
        server_key: ec.EllipticCurvePrivateKey = ec.generate_private_key(ec.SECP256R1())
        self.server_key: bytes = _pem_key(server_key)
        self.server_cert: bytes = self._issue(
            f"{name}-server", server_key.public_key(), False, ca, ExtendedKeyUsageOID.SERVER_AUTH, SERVER_NAME
        )
        client_key: ec.EllipticCurvePrivateKey = ec.generate_private_key(ec.SECP256R1())
        self.client_key: bytes = _pem_key(client_key)
        self.client_cert: bytes = self._issue(
            f"{name}-client", client_key.public_key(), False, ca, ExtendedKeyUsageOID.CLIENT_AUTH
        )

    def _issue(
        self,
        subject: str,
        public_key: ec.EllipticCurvePublicKey,
        ca: bool,
        issuer: Optional[x509.Certificate],
        usage: Optional[x509.ObjectIdentifier] = None,
        san: Optional[str] = None,
    ) -> bytes:
        now: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
        name: x509.Name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, subject)])
        builder: x509.CertificateBuilder = (
            x509.CertificateBuilder()
            .subject_name(name)
            .issuer_name(name if issuer is None else issuer.subject)
            .public_key(public_key)
            .serial_number(x509.random_serial_number())
            .not_valid_before(now - datetime.timedelta(days=1))
            .not_valid_after(now + datetime.timedelta(days=30))
            .add_extension(x509.BasicConstraints(ca=ca, path_length=None), critical=True)
        )
        if usage is not None:
            builder = builder.add_extension(x509.ExtendedKeyUsage([usage]), critical=False)
        if san is not None:
            builder = builder.add_extension(x509.SubjectAlternativeName([x509.DNSName(san)]), critical=False)
        return builder.sign(self._ca_key, hashes.SHA256()).public_bytes(serialization.Encoding.PEM)


def _pem_key(key: ec.EllipticCurvePrivateKey) -> bytes:
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )


def _crlf(pem: bytes) -> str:
    return pem.replace(b"\n", b"\r\n").decode()


@pytest.fixture(scope="module")
def pki() -> Pki:
    return Pki("deployment")


@pytest.fixture(scope="module")
def foreign() -> Pki:
    return Pki("foreign")


def _credentials(pki: Pki, require_client_auth: bool) -> grpc.ServerCredentials:
    return grpc.ssl_server_credentials(
        [(pki.server_key, pki.server_cert)],
        root_certificates=pki.ca_cert if require_client_auth else None,
        require_client_auth=require_client_auth,
    )


@pytest.fixture
def server() -> Iterator[Callable[[Pki, bool], int]]:
    """Start a servicer-less sync TLS server; ``(pki, require_client_auth) -> port``."""
    servers: List[grpc.Server] = []

    def start(pki: Pki, require_client_auth: bool) -> int:
        grpc_server: grpc.Server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        port: int = grpc_server.add_secure_port(f"{SERVER_NAME}:0", _credentials(pki, require_client_auth))
        grpc_server.start()
        servers.append(grpc_server)
        return port

    yield start
    for grpc_server in servers:
        grpc_server.stop(grace=None)


@pytest_asyncio.fixture
async def async_server() -> Any:
    """Start a servicer-less ``grpc.aio`` TLS server; ``(pki, require_client_auth) -> port``."""
    servers: List[grpc.aio.Server] = []

    async def start(pki: Pki, require_client_auth: bool) -> int:
        grpc_server: grpc.aio.Server = grpc.aio.server()
        port: int = grpc_server.add_secure_port(f"{SERVER_NAME}:0", _credentials(pki, require_client_auth))
        await grpc_server.start()
        servers.append(grpc_server)
        return port

    yield start
    for grpc_server in servers:
        await grpc_server.stop(grace=None)


def _config(port: int, trusted: Pki, client: Optional[Pki] = None) -> ClientConfig:
    """A config trusting ``trusted``'s CA, presenting ``client``'s leaf when given (mutual TLS)."""
    return ClientConfig(
        host=SERVER_NAME,
        port=str(port),
        grpc_cert=trusted.ca_cert.decode(),
        grpc_client_cert=None if client is None else client.client_cert.decode(),
        grpc_client_key=None if client is None else client.client_key.decode(),
    )


def _call(config: ClientConfig, use_shared_channel: bool) -> grpc.StatusCode:
    """One real RPC through the SDK client; returns the status code it ended with."""
    client: Client = Client(config=config, use_shared_channel=use_shared_channel)
    try:
        with pytest.raises(grpc.RpcError) as error:
            client.services.calls.stub.DeleteCallers(
                calls_pb2.DeleteCallersRequest(), metadata=client.services.calls.metadata, timeout=TIMEOUT_IN_S
            )
        code: grpc.StatusCode = error.value.code()  # type: ignore[attr-defined]
        return code
    finally:
        client.disconnect()


async def _async_call(config: ClientConfig, use_shared_channel: bool) -> grpc.StatusCode:
    client: AsyncClient = AsyncClient(config=config, use_shared_channel=use_shared_channel)
    try:
        with pytest.raises(grpc.aio.AioRpcError) as error:
            await client.services.calls.stub.DeleteCallers(
                calls_pb2.DeleteCallersRequest(), metadata=client.services.calls.metadata, timeout=TIMEOUT_IN_S
            )
        return error.value.code()
    finally:
        await client.disconnect()


SHARED: Any = pytest.mark.parametrize("use_shared_channel", [False, True], ids=["per-service", "shared"])


@SHARED
class TestSyncClient:
    def test_plain_tls_reaches_the_server(self, server: Any, pki: Pki, use_shared_channel: bool) -> None:
        assert _call(_config(server(pki, False), pki), use_shared_channel) is grpc.StatusCode.UNIMPLEMENTED

    def test_mutual_tls_reaches_the_server(self, server: Any, pki: Pki, use_shared_channel: bool) -> None:
        assert _call(_config(server(pki, True), pki, pki), use_shared_channel) is grpc.StatusCode.UNIMPLEMENTED

    def test_no_identity_is_refused_by_a_client_auth_server(
        self, server: Any, pki: Pki, use_shared_channel: bool
    ) -> None:
        assert _call(_config(server(pki, True), pki), use_shared_channel) is grpc.StatusCode.UNAVAILABLE

    def test_an_identity_from_an_unrelated_ca_is_refused(
        self, server: Any, pki: Pki, foreign: Pki, use_shared_channel: bool
    ) -> None:
        assert _call(_config(server(pki, True), pki, foreign), use_shared_channel) is grpc.StatusCode.UNAVAILABLE

    def test_a_server_from_an_untrusted_ca_is_refused(
        self, server: Any, pki: Pki, foreign: Pki, use_shared_channel: bool
    ) -> None:
        assert _call(_config(server(pki, True), foreign, pki), use_shared_channel) is grpc.StatusCode.UNAVAILABLE

    def test_crlf_pems_complete_the_mutual_tls_handshake(self, server: Any, pki: Pki, use_shared_channel: bool) -> None:
        config: ClientConfig = ClientConfig(
            host=SERVER_NAME,
            port=str(server(pki, True)),
            grpc_cert=_crlf(pki.ca_cert),
            grpc_client_cert=_crlf(pki.client_cert),
            grpc_client_key=_crlf(pki.client_key),
        )
        assert _call(config, use_shared_channel) is grpc.StatusCode.UNIMPLEMENTED

    def test_an_empty_identity_on_both_is_plain_tls(self, server: Any, pki: Pki, use_shared_channel: bool) -> None:
        config: ClientConfig = ClientConfig(
            host=SERVER_NAME,
            port=str(server(pki, False)),
            grpc_cert=pki.ca_cert.decode(),
            grpc_client_cert="",
            grpc_client_key="",
        )
        assert _call(config, use_shared_channel) is grpc.StatusCode.UNIMPLEMENTED

    def test_insecure_with_an_identity_is_refused(self, pki: Pki, use_shared_channel: bool) -> None:
        with pytest.raises(ValueError, match="use a secure channel") as refusal:
            Client(config=_config(1, pki, pki), use_secure_channel=False, use_shared_channel=use_shared_channel)
        assert "PRIVATE KEY" not in str(refusal.value) and "CERTIFICATE" not in str(refusal.value)


@SHARED
@pytest.mark.asyncio
class TestAsyncClient:
    async def test_plain_tls_reaches_the_server(self, async_server: Any, pki: Pki, use_shared_channel: bool) -> None:
        config: ClientConfig = _config(await async_server(pki, False), pki)
        assert await _async_call(config, use_shared_channel) is grpc.StatusCode.UNIMPLEMENTED

    async def test_mutual_tls_reaches_the_server(self, async_server: Any, pki: Pki, use_shared_channel: bool) -> None:
        config: ClientConfig = _config(await async_server(pki, True), pki, pki)
        assert await _async_call(config, use_shared_channel) is grpc.StatusCode.UNIMPLEMENTED

    async def test_no_identity_is_refused_by_a_client_auth_server(
        self, async_server: Any, pki: Pki, use_shared_channel: bool
    ) -> None:
        config: ClientConfig = _config(await async_server(pki, True), pki)
        assert await _async_call(config, use_shared_channel) is grpc.StatusCode.UNAVAILABLE

    async def test_an_identity_from_an_unrelated_ca_is_refused(
        self, async_server: Any, pki: Pki, foreign: Pki, use_shared_channel: bool
    ) -> None:
        config: ClientConfig = _config(await async_server(pki, True), pki, foreign)
        assert await _async_call(config, use_shared_channel) is grpc.StatusCode.UNAVAILABLE

    async def test_insecure_with_an_identity_is_refused(self, pki: Pki, use_shared_channel: bool) -> None:
        with pytest.raises(ValueError, match="use a secure channel"):
            AsyncClient(config=_config(1, pki, pki), use_secure_channel=False, use_shared_channel=use_shared_channel)


class TestClientConfig:
    @pytest.mark.parametrize("half", ["grpc_client_cert", "grpc_client_key"])
    def test_half_an_identity_is_refused_before_grpc(self, pki: Pki, half: str) -> None:
        pem: str = (pki.client_cert if half == "grpc_client_cert" else pki.client_key).decode()
        with pytest.raises(ValueError, match="set both to use mutual TLS, or neither") as refusal:
            ClientConfig(
                host=SERVER_NAME,
                port="1",
                grpc_cert=pki.ca_cert.decode(),
                grpc_client_cert=pem if half == "grpc_client_cert" else None,
                grpc_client_key=pem if half == "grpc_client_key" else None,
            )
        assert pem not in str(refusal.value) and "PRIVATE KEY" not in str(refusal.value)

    def test_repr_and_str_never_render_the_key_or_the_password(self, pki: Pki) -> None:
        config: ClientConfig = ClientConfig(
            host=SERVER_NAME,
            port="1",
            grpc_cert=pki.ca_cert.decode(),
            grpc_client_cert=pki.client_cert.decode(),
            grpc_client_key=pki.client_key.decode(),
            keycloak_url="https://keycloak.example.com/auth",
            realm="realm",
            client_id="client",
            username="user",
            password="s3cret-password",
        )
        for rendered in (repr(config), str(config)):
            assert "PRIVATE KEY" not in rendered
            assert "s3cret-password" not in rendered
            assert "grpc_client_key='***REDACTED***'" in rendered
