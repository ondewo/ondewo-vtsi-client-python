<div align="center">
  <table>
    <tr>
      <td>
        <a href="https://ondewo.com/en/products/natural-language-understanding/">
            <img width="400px" src="https://raw.githubusercontent.com/ondewo/ondewo-logos/master/ondewo_we_automate_your_phone_calls.png"/>
        </a>
      </td>
    </tr>
    <tr>
        <td align="center">
          <a href="https://www.linkedin.com/company/ondewo "><img width="40px" src="https://cdn-icons-png.flaticon.com/512/3536/3536505.png"></a>
          <a href="https://www.facebook.com/ondewo"><img width="40px" src="https://cdn-icons-png.flaticon.com/512/733/733547.png"></a>
          <a href="https://twitter.com/ondewo"><img width="40px" src="https://cdn-icons-png.flaticon.com/512/733/733579.png"> </a>
          <a href="https://www.instagram.com/ondewo.ai/"><img width="40px" src="https://cdn-icons-png.flaticon.com/512/174/174855.png"></a>
        </td>
    </tr>
  </table>
  <h1>
  Ondewo VTSI Client Python Library
  </h1>
</div>

This library facilitates the interaction between a user and a CAI server. It achieves this by providing a higher-level interface mediator.

This higher-level interface mediator is structured around a series of python files generated from protobuf files. These protobuf files specify the details of the interface, and can be used to generate code in 10+ high-level languages. They are found in the [ONDEWO VTSI API](https://github.com/ondewo/ondewo-vtsi-api) along with the older Google protobufs from Dialogueflow that were used at the start. The [ONDEWO PROTO-COMPILER](https://github.com/ondewo/ondewo-proto-compiler) will generate the needed files directly in this library.

## Python Installation

You can install the library by installing it directly from the PyPi:

```bash
pip install ondewo-vtsi-client
```

Or, you could clone it and install the requirements:

```bash
git clone git@github.com:ondewo/ondewo-vtsi-client-python.git
cd ondewo-vtsi-client-python
make setup_developer_environment_locally
```

## Repository Structure

```
.
├── examples
│   ├── analysis
│   │   └── analysis.py
│   ├── caller
│   │   ├── caller_deployment_minimal.py
│   │   ├── caller_deployment_mirror_mode.py
│   │   ├── configure_context_parameters.py
│   │   ├── full_config.py
│   │   └── make_multiple_calls.py
│   └── listener
│       ├── listener_deployment.py
│       └── minimal_listener.py
├── ondewo
│   ├── nlu
│   │   ├── agent_pb2_grpc.py
│   │   ├── agent_pb2.py
│   │   ├── agent_pb2.pyi
│   │   ├── aiservices_pb2_grpc.py
│   │   ├── aiservices_pb2.py
│   │   ├── aiservices_pb2.pyi
│   │   ├── ccai_project_pb2_grpc.py
│   │   ├── ccai_project_pb2.py
│   │   ├── ccai_project_pb2.pyi
│   │   ├── common_pb2_grpc.py
│   │   ├── common_pb2.py
│   │   ├── common_pb2.pyi
│   │   ├── context_pb2_grpc.py
│   │   ├── context_pb2.py
│   │   ├── context_pb2.pyi
│   │   ├── entity_type_pb2_grpc.py
│   │   ├── entity_type_pb2.py
│   │   ├── entity_type_pb2.pyi
│   │   ├── __init__.py
│   │   ├── intent_pb2_grpc.py
│   │   ├── intent_pb2.py
│   │   ├── intent_pb2.pyi
│   │   ├── operation_metadata_pb2_grpc.py
│   │   ├── operation_metadata_pb2.py
│   │   ├── operation_metadata_pb2.pyi
│   │   ├── operations_pb2_grpc.py
│   │   ├── operations_pb2.py
│   │   ├── operations_pb2.pyi
│   │   ├── project_role_pb2_grpc.py
│   │   ├── project_role_pb2.py
│   │   ├── project_role_pb2.pyi
│   │   ├── project_statistics_pb2_grpc.py
│   │   ├── project_statistics_pb2.py
│   │   ├── project_statistics_pb2.pyi
│   │   ├── server_statistics_pb2_grpc.py
│   │   ├── server_statistics_pb2.py
│   │   ├── server_statistics_pb2.pyi
│   │   ├── session_pb2_grpc.py
│   │   ├── session_pb2.py
│   │   ├── session_pb2.pyi
│   │   ├── user_pb2_grpc.py
│   │   ├── user_pb2.py
│   │   ├── user_pb2.pyi
│   │   ├── utility_pb2_grpc.py
│   │   ├── utility_pb2.py
│   │   ├── utility_pb2.pyi
│   │   ├── webhook_pb2_grpc.py
│   │   ├── webhook_pb2.py
│   │   └── webhook_pb2.pyi
│   ├── qa
│   │   ├── __init__.py
│   │   ├── qa_pb2_grpc.py
│   │   ├── qa_pb2.py
│   │   └── qa_pb2.pyi
│   ├── s2t
│   │   ├── __init__.py
│   │   ├── speech_to_text_pb2_grpc.py
│   │   ├── speech_to_text_pb2.py
│   │   └── speech_to_text_pb2.pyi
│   ├── sip
│   │   ├── __init__.py
│   │   ├── sip_pb2_grpc.py
│   │   ├── sip_pb2.py
│   │   └── sip_pb2.pyi
│   ├── t2s
│   │   ├── __init__.py
│   │   ├── text_to_speech_pb2_grpc.py
│   │   ├── text_to_speech_pb2.py
│   │   └── text_to_speech_pb2.pyi
│   ├── vtsi
│   │   ├── client.py
│   │   ├── __init__.py
│   │   ├── vtsi_pb2_grpc.py
│   │   ├── vtsi_pb2.py
│   │   └── vtsi_pb2.pyi
│   └── __init__.py
├── ondewo-proto-compiler
├── ondewo-vtsi-api
├── CONTRIBUTING.md
├── Dockerfile.utils
├── LICENSE
├── Makefile
├── MANIFEST.in
├── pyproject.toml
├── README.md
├── RELEASE.md
├── tests
└── uv.lock
```

## Build

The `make build` command is dependent on 2 `repositories` and their speciefied `version`:

- [ondewo-vtsi-api](https://github.com/ondewo/ondewo-vtsi-api) -- `VTSI_API_GIT_BRANCH` in `Makefile`
- [ondewo-proto-compiler](https://github.com/ondewo/ondewo-proto-compiler) -- `ONDEWO_PROTO_COMPILER_GIT_BRANCH` in `Makefile`

It will generate a `_pb2.py`, `_pb2.pyi` and `_pb2_grpc.py` file for every `.proto` in the api submodule.

> :warning: All Files in the `ondewo` folder that dont have `pb2` in their name are handwritten, and therefor need to be manually adjusted to any changes in the proto-code.

## Examples

The `/examples` folder provides a possible implementation of this library. To run an example, simple execute it like any other python file. To specify the server and credentials, you need to provide the following values:

- host `// The hostname of the Server - e.g. 127.0.0.1`
- port `// Port of the Server - e.g. 6600`
- grpc_cert `// gRPC Certificate of the server (required for a secure channel)`
- keycloak_url `// Base URL of the Keycloak server (D18 auth) - e.g. https://keycloak.example.com/auth`
- realm `// Keycloak realm name (D18 auth)`
- client_id `// Id of the public Keycloak SDK client (D18 auth) - no client secret`
- username `// Username / email of the (2FA-exempt technical) user for the ROPC grant (D18 auth)`
- password `// Password of that user`

The client authenticates with the D18 Keycloak offline-token (bearer) flow: it logs in once against a
**public** Keycloak client with `grant_type=password` + `scope=offline_access`, then auto-refreshes the
short-lived access token. The legacy `http_token` (`Authorization: Basic`) is removed (D5) and is no longer
required. The service wrappers under `ondewo/vtsi/client/services/` sit on top of the generated
`_pb2_grpc.py` stubs and inject the freshly refreshed token via `self.metadata` on every call, so application
code stays clean. Without a wrapper the same call would attach the token manually:

```python
metadata = [("authorization", "Bearer <token>")]
stub.StartCaller(request, metadata=metadata)
```

### Softphone accounts

`client.services.softphones` manages SIP accounts on a project's Asterisk for humans using a softphone such
as Zoiper. The create (and rotate) response is the **only** place the SIP password and the password-protected
PKCS#12 bundle ever appear, so store them at once and never log the response; Get, List and provisioning
return public material only. See `examples/softphones/create_softphone_account.py` for the full flow.

```python
from ondewo.vtsi.softphones_pb2 import (
    SOFTPHONE_TRANSPORT_SECURITY_CLIENT_CERTIFICATE,
    CreateSoftphoneAccountRequest,
    GetSoftphoneProvisioningRequest,
    SoftphoneAccount,
)

created = client.services.softphones.create_softphone_account(
    request=CreateSoftphoneAccountRequest(
        vtsi_project_name="projects/<project_uuid>/project",
        softphone_account=SoftphoneAccount(
            sip_username="support-01",
            transport_security=SOFTPHONE_TRANSPORT_SECURITY_CLIENT_CERTIFICATE,
        ),
    ),
)
# created.credentials.sip_password / .pkcs12_bundle / .pkcs12_password are shown ONCE.
provisioning = client.services.softphones.get_softphone_provisioning(
    request=GetSoftphoneProvisioningRequest(name=created.softphone_account.name),
)
print(provisioning.zoiper_instructions)
```

### Campaigns, status streams and VtsiEvents

`client.services.campaigns` places a set of outbound calls while keeping at most `max_parallel_calls` of them
running at once, retries a failed call up to `max_attempts` times, and reports the progress (not started, in
progress, completed, failed, attempts). Calls join a campaign through
`client.services.calls.add_callers_to_campaign` / `add_scheduled_callers_to_campaign`. A VTSI server older than
these RPCs answers `UNIMPLEMENTED` and starts nothing; do not fall back to `start_callers` then, because that starts
every caller at once. `client.services.events` manages VtsiEvent subscriptions and webhooks (custom header values
are write-only and come back masked; moving a webhook to another origin requires re-sending its headers with real
values) and streams the events themselves.
`client.services.calls` streams the status of callers, listeners and scheduled callers.

```python
from ondewo.vtsi.calls_pb2 import AddCallersToCampaignRequest
from ondewo.vtsi.campaigns_pb2 import (
    CAMPAIGN_START_MODE_START,
    Campaign,
    CampaignAssignment,
    StreamCampaignStatusRequest,
)

response = client.services.calls.add_callers_to_campaign(
    request=AddCallersToCampaignRequest(
        vtsi_project_name="projects/<project_uuid>/project",
        caller_requests=[...],  # e.g. 100 StartCallerRequest
        campaign_assignment=CampaignAssignment(
            new_campaign=Campaign(max_parallel_calls=10, max_attempts=2),
            start_mode=CAMPAIGN_START_MODE_START,
        ),
    ),
)
for update in client.services.campaigns.stream_campaign_status(
    request=StreamCampaignStatusRequest(
        vtsi_project_name="projects/<project_uuid>/project",
        campaign_names=[response.campaign.name],
    ),
):
    print(update)
```

With the `AsyncClient` a stream is iterated, not awaited: `async for update in
client.services.campaigns.stream_campaign_status(request=...)`.

### Retrying a batch start safely: `idempotency_key`

`StartCallersRequest`, `StartListenersRequest`, `StartScheduledCallersRequest`, `AddCallersToCampaignRequest` and
`AddScheduledCallersToCampaignRequest` take an optional `idempotency_key` (at most 255 printable ASCII characters,
no whitespace; empty means no deduplication). A retry carrying the same key returns the response of the first
successful attempt, on whichever replica it reaches, instead of starting the calls a second time. The key is scoped
to the VTSI project and the RPC and kept for 24 hours by default. Reusing a key with a different request is refused
with `INVALID_ARGUMENT`; a retry while the first attempt is still running is answered `ABORTED` (retry later); a
failed first attempt stores nothing. A replayed response carries no `common_services_config`. To make a single
caller or listener idempotent, send it as a batch of one.

### One shared gRPC channel (opt-in)

By default every service (`projects`, `calls`, `logs`) opens its own gRPC channel, i.e. over TLS its own connection
and handshake. Pass `use_shared_channel=True` to let all services share one channel, built with
[`build_shared_channel`](https://github.com/ondewo/ondewo-client-utils-python) (each method keeps the retry policy it
would have had on its own channel); `disconnect()` closes it once, and a later `connect()` shares again:

```python
from ondewo.vtsi.client.client import Client

client = Client(config=config, use_secure_channel=True, use_shared_channel=True)
```

`AsyncClient` takes the same keyword; construct it inside the running event loop that uses it.

## Automatic Release Process

The entire process is automated to make development easier. The actual steps are simple:

TODO after Pull Request was merged in:

- Checkout master:

  ```shell
  git checkout master
  ```

- Pull the new stuff:

  ```shell
  git pull
  ```

- (If not already, run the `setup_developer_environment_locally` command):

  ```shell
  make setup_developer_environment_locally
  ```

- Update the `ONDEWO_VTSI_VERSION` in the `Makefile`
- Add the new Release Notes in `RELEASE.md` in the format:

  ```
  ## Release ONDEWO VTSI Python Client X.X.X       <---- Beginning of Notes

     ...<NOTES>...

  *****************                      <---- End of Notes
  ```

- Release:

  ```shell
  make ondewo_release
  ```

---

`make ondewo_release` runs these steps, in this order, and stops at the first one that fails. The order is pinned by
`tests/unit/test_release_runs_in_a_fresh_clone.py` and is the same in every `ondewo-vtsi-client-<language>`
repository, so `ondewo-vtsi-api`'s release driver treats them alike.

1. `spc` (read-only, no credentials): the branch `release/<version>` and the tag `<version>` are not on origin
   (`git ls-remote --exit-code`, exact refs), PyPI does not serve `ondewo-vtsi-client <version>` yet, and `RELEASE.md`
   carries exactly one `## Release ONDEWO VTSI Python Client <version>` heading (matched anchored, dots escaped) with
   a non-empty body.
2. Load `GITHUB_GH_TOKEN`, `PYPI_USERNAME` and `PYPI_PASSWORD` from `ondewo-devops-accounts`, then **delete that
   clone** before anything else runs, and also when the clone or the release fails. The clone lives in a `mktemp`
   directory, never in this repository. When `DEVOPS_ACCOUNT_DIR` points at an existing clone (the driver clones once
   for all clients), it is used and not cloned again.
3. `release_preflight` (read-only): the host tools exist, `spc` again, and both credentials are VALID:
   - GitHub: `gh api repos/ondewo/ondewo-vtsi-client-python --jq .permissions.push` prints `true`.
   - PyPI has no read-only identity call, so the probe re-uploads the newest file that is already on PyPI. PyPI checks
     the credential and the upload permission on this project first (`403` when either fails) and only then refuses
     the existing file (`400 File already exists`). A pass therefore proves the credential may upload to
     `ondewo-vtsi-client`, and it cannot publish anything new.
4. `build` (regenerates the code from `ondewo-vtsi-api`), the pre-commit hooks, `check_build` and `make test` (ruff,
   mypy and the unit suite with the coverage gate). These steps run with the credentials removed from their
   environment.
5. Commit locally (only when something changed), upload to PyPI, and wait until the PyPI JSON API serves the version.
   PyPI comes first because it is the one step that cannot be undone.
6. Push, create and push `release/<version>` and the tag `<version>`, create the GitHub release from the `RELEASE.md`
   section (an empty body is refused).
7. `release_verify` (read-only, also run by the driver afterwards): the tag is on origin, the GitHub release has a
   non-empty body, and PyPI serves the version (polled 20 x 30 s).

Host requirements: `docker`, `git`, `make`, `perl`, `curl` and `uv`. `gh`, `twine` and the package build run in the
pinned `Dockerfile.utils` image (exact uv, twine and gh versions, base images by digest), and gh reads the token from
`GH_TOKEN` per call, so nothing is stored in `~/.config/gh`. No credential is ever put on a command line.
