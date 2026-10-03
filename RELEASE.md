# Release History

*****************

## Release ONDEWO VTSI Python Client 9.0.0

### Breaking changes

* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) Regenerated against
  [ondewo-vtsi-api 9.0.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/9.0.0), which renames
  `AsteriskConfigsFiles.sip_conf_file_string` to `pjsip_conf_file_string`. The `chan_sip` channel driver the old
  name referred to was removed in Asterisk 21, and the configuration file an Asterisk 22 server reads is
  `pjsip.conf`, so the field carried a name that described a file no supported Asterisk parses. **Field number 1
  and type `string` do not change and no `json_name` override is added**, so the change is binary wire-compatible
  in both directions and source-breaking only. In this client the name moves in three places in
  `ondewo/vtsi/projects_pb2.pyi` -- the attribute, the `AsteriskConfigsFiles` constructor keyword and the
  `ClearField` literal -- and in the serialized descriptor in `ondewo/vtsi/projects_pb2.py`. Rename the attribute
  and the keyword argument; nothing about the encoded bytes moves. The three sibling fields keep their names:
  `extensions.conf`, `queues.conf` and `modules.conf` exist unchanged under `res_pjsip` and only their CONTENT
  changes. The field deliberately does NOT gain the `optional` keyword -- on the create path `""` and unset are
  the same instruction, so presence would add a third state no server reads.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) **The JSON key moves with it.** With no
  `json_name` override, `protoc` derives the key from the field name, so `MessageToJson` and `ParseDict` go from
  `sipConfFileString` to `pjsipConfFileString`. Any hand-written JSON mapping must move in the same step.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) Eleven singular scalars in
  `ondewo/vtsi/calls.proto` gained the `optional` keyword, so that "the caller said nothing" stops being
  indistinguishable from "the caller said the default":
  `InterruptionHandlingConfig.transcribe_on_disabled_interruptions`,
  `TurnDetectionConfig.turn_detection_system_prompt`, `TurnDetectionConfig.turn_detection_user_prompt`,
  `AudioObjectStorageConfig.activate_audio_object_storage`,
  `AudioObjectStorageServicesActivationConfig.activate_s2t` and `.activate_t2s`,
  `MessageBrokerConfig.activate_message_broker`, and `MessageBrokerServicesActivationConfig.activate_s2t`,
  `.activate_nlu`, `.activate_t2s` and `.activate_sip`. Each keeps its field number and wire type; `optional`
  only adds explicit presence, which compiles to a synthetic one-member oneof that exists in the descriptor and
  not on the wire.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) What that presence change means for Python
  callers, measured against the 8.7.0 stubs in this package. `HasField` on those eleven names currently RAISES
  (`ValueError: Field ondewo.vtsi.MessageBrokerConfig.activate_message_broker does not have presence.`) and
  `FieldDescriptor.has_presence` is `False` for all eleven; from 9.0.0 both answer normally. And an explicitly
  assigned default now reaches the wire: `MessageBrokerConfig(activate_message_broker=False)` serialises to
  `b''` on the 8.7.0 stubs and to `b'\x08\x00'` on the 9.0.0 ones. Regenerate before relying on an explicit
  `False` arriving as an explicit `False` -- an un-regenerated client sends nothing, and a 9.0.0 server cannot
  tell that apart from unset. When you need to detect the difference in code, read
  `FieldDescriptor.has_presence`; a `HasField` probe raises on exactly the messages it is meant to classify.

### New features

* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) `AsteriskConfigsVariables` gained two fields on
  the next free numbers, 7 and 8, making the SIP trunk's transport a per-project choice instead of a property of
  the image:
  * `SipTrunkTransport sip_trunk_transport = 7` -- `SIP_TRUNK_TRANSPORT_UNSPECIFIED` (0),
    `SIP_TRUNK_TRANSPORT_TLS` (1), `SIP_TRUNK_TRANSPORT_UDP` (2), `SIP_TRUNK_TRANSPORT_TCP` (3). Unset ==
    `UNSPECIFIED` == `TLS`, so **the zero value is the encrypted one** and a caller that says nothing gets an
    encrypted trunk. It takes no `optional` keyword: an enum whose zero IS a documented `*_UNSPECIFIED` sentinel
    already carries the third state.
  * `optional string sip_trunk_source_cidr = 8` -- the source address or CIDR the carrier sends from, e.g.
    `203.0.113.7/32`. REQUIRED when the transport is `UDP` or `TCP`, where the trunk is matched by source address
    rather than authenticated by a certificate, and ignored otherwise. A hostname is refused with
    `INVALID_ARGUMENT`. This one DOES take `optional`, so an explicit empty CIDR stays distinguishable from
    nothing sent and an `update_mask` can CLEAR it rather than assign `""`.

  Both are additive: an 8.x peer decoding a 9.0.0 message skips them as unknown fields.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) The comment on `ScheduledCaller.call_name` lost
  the words "asterisk sip", matching its `Caller` and `Listener` siblings. Listed only because it is
  source-visible: it moves no descriptor byte.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) New `Softphones` service (unreleased, in
  development): the generated `ondewo/vtsi/softphones_pb2.py`, `.pyi` and `softphones_pb2_grpc.py`, plus the
  wrappers `ondewo.vtsi.client.services.softphones.Softphones` and its async twin, exposed as
  `client.services.softphones` on both `Client` and `AsyncClient`. Ten RPCs manage softphone accounts
  (create/get/update/delete/list with field masks, a structured filter, paging and sorting), rotate their
  credentials, list/get/revoke their client certificates and return Zoiper provisioning. The SIP password
  and the PKCS#12 bundle are returned ONLY by `create_softphone_account` and
  `rotate_softphone_credentials`; never log those responses. `SoftphoneAccount.enabled` carries explicit
  presence: ask `HasField("enabled")`, since an unset value means `true` on create. New example
  `examples/softphones/create_softphone_account.py`.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) Answering machine detection (AMD): regenerated
  against ondewo-vtsi-api `7a3011d`, which adds `VoiceInteractionConfig.answering_machine_detection_config = 4`
  (`AnsweringMachineDetectionConfig`, enums `AmdAction` and `AmdSensitivity`, fourteen `optional` fields and two
  phrase lists) and `Call.redial_recommended = 19` / `Call.redial_reason = 20`. The AMD fields have explicit
  presence: ask `HasField`, because an unset field means the CSI container default. The vendored `ondewo/sip`
  stubs move from sip-api 5.4.0 to sip-api `2fff350` (status 22 `OUTGOING_CALL_ANSWERING_MACHINE`,
  `AnsweringMachineDetectionResult`, `SipStatus.amd_result`, `SipEndCallRequest.end_reason` / `amd_result`) and are
  byte-identical to those of `ondewo-sip-client` 5.5.0 generated from the same commit; install the two together, or
  the last installed copy of `ondewo/sip` wins. Pinned by `tests/unit/vtsi/test_answering_machine_detection_config.py`.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) AMD voice message: regenerated against
  ondewo-vtsi-api `82f84ad`. `AmdAction` gains `LEAVE_VOICE_MESSAGE = 3`; `AnsweringMachineDetectionConfig` gains
  `voice_message_intent = 17`, `voice_message_max_beep_wait_ms = 18`, `voice_message_timeout_ms = 19`,
  `keyword_detection_active = 20` and `cadence_detection_active = 21` (all `optional`); `Call` gains
  `answering_machine_detection_end_description = 21`. The vendored `ondewo/sip` stubs move to sip-api `33d0367`:
  status 22 is RENAMED `OUTGOING_CALL_ANSWERING_MACHINE_DETECTED` and is no longer terminal (an AMD-ended call ends
  as `OUTGOING_CALL_FINISHED` with an AMD description), `ActionTaken.LEFT_VOICE_MESSAGE = 4`,
  `EndCallReason.ANSWERING_MACHINE_VOICE_MESSAGE_LEFT = 2` and the RPC `SipReportAnsweringMachineDetected`. They are
  byte-identical to those of `ondewo-sip-client` `ba915e2`.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) Carrier TLS verification: regenerated against
  ondewo-vtsi-api `f6547bf`, which adds `AsteriskConfigsVariables.sip_trunk_ca_certificates_pem = 9` (the PEM
  bundle of the CA certificate(s) the carrier's TLS certificate chains to) and
  `AsteriskConfigsVariables.sip_trunk_verify_server = 10` (default false). The server verifies the carrier's
  certificate only when both are given. Both carry explicit presence: ask `HasField`. Pinned by
  `tests/unit/vtsi/test_sip_trunk_tls_verification.py`.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) Campaigns, status streams and VtsiEvents:
  regenerated against ondewo-vtsi-api `cac5f44`. New service `Campaigns` (`ondewo/vtsi/campaigns_pb2*`, exposed as
  `client.services.campaigns`): create, get, update, delete and list campaigns, their statistics and campaign
  calls (with SIP status, description and attempts), start, stop, hard stop and resume, and the server-stream
  `StreamCampaignStatus`. A campaign caps the calls running at once with `max_parallel_calls` and retries a failed
  call up to `max_attempts` times. New service `Events` (`ondewo/vtsi/events_pb2*`, exposed as
  `client.services.events`): the `VtsiEvent` enum, CRUD for event subscriptions and webhooks (custom header values
  are write-only and returned masked), `TestWebhook` and the server-stream `SubscribeVtsiEvents`. `Calls` gains
  the unary RPCs `AddCallersToCampaign` / `AddScheduledCallersToCampaign`
  (`client.services.calls.add_callers_to_campaign` / `add_scheduled_callers_to_campaign`), which add callers to a
  campaign instead of starting them, `ScheduledCaller.campaign_name`, and the server-streams
  `StreamCallerStatus`, `StreamListenerStatus` and `StreamScheduledCallerStatus` (`client.services.calls.stream_*`).
  The async wrappers of all three services are hand-written (`ondewo:hand-written-async-service`), because a
  server-streaming RPC returns an async iterator that must not be awaited; use `async for`. Pinned by
  `tests/unit/vtsi/test_campaigns_and_events.py`.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) **Campaign enrollment is its own RPC so that a
  rolling update fails closed.** Development builds of 9.0.0 carried it as a `campaign_assignment` field on
  `StartCallersRequest` / `StartScheduledCallersRequest`; a VTSI replica older than 9.0.0 does not know that field,
  ignores it and starts every caller at once. A replica that predates `AddCallersToCampaign` answers
  `UNIMPLEMENTED` and starts nothing. Do not fall back to `StartCallers` on `UNIMPLEMENTED`; retry later. The old
  field numbers (request 3, responses 3-5 / 3-4) are `reserved`, and a server refuses a request that still carries
  one with `INVALID_ARGUMENT`.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) `AsteriskConfigsVariables.softphone_permit_cidrs
  = 11`: the source allow-list of a project's softphone accounts on both TLS ports, as full CIDRs. Empty uses the
  server's `ONDEWO_VTSI_ASTERISK_SOFTPHONE_PERMIT_CIDRS` (by default the private networks), which is also a
  ceiling every entry must lie inside.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) Documentation carried by the regenerated stubs:
  `UpdateWebhook` states that moving a webhook to another origin (scheme, host or port) while custom headers are
  stored requires re-sending `custom_headers` with their real values (or an empty map), and
  `BaseServiceConfig.grpc_cert` states that the S2T, NLU and T2S certificates of a call are required unless the
  server runs with `ONDEWO_VTSI_ALLOW_INSECURE_UPSTREAM=True`.
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) Request idempotency keys: regenerated against
  ondewo-vtsi-api `8ae9487`. `StartCallersRequest` (field 4), `StartListenersRequest` (3),
  `StartScheduledCallersRequest` (4), `AddCallersToCampaignRequest` (4) and `AddScheduledCallersToCampaignRequest`
  (4) gain an optional `string idempotency_key`: at most 255 printable ASCII characters, no whitespace; empty means
  no deduplication. A retry with the same key returns the response of the first successful attempt, on whichever
  replica it reaches, instead of starting the calls again. The key is scoped to the VTSI project and the RPC and
  retained for 24 hours by default. The same key with a different request is refused with `INVALID_ARGUMENT`; a
  retry while the first attempt is still running is answered `ABORTED` (retry later); a failed first attempt
  stores nothing. A replayed response carries no `common_services_config`. The single-resource RPCs take no key:
  send a batch of one. Pinned by `tests/unit/vtsi/test_request_idempotency_key.py`.

### Bug Fixes

* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) `make mypy` and `make flake8` run the gates that
  exist. `make mypy` ran `mypy --config-file=mypy.ini .` against a `mypy.ini` this repository does not have, and
  `make flake8` called a `flake8` that is installed nowhere (ruff replaced it). `make mypy` now runs mypy with the
  pre-commit hook's configuration (`pyproject.toml`), and `make flake8` is an alias of the new `make ruff`
  (`ruff check` + `ruff format --check`).
* [[OND233-367]](https://ondewo.atlassian.net/browse/OND233-367) The GitHub release body is no longer empty. The
  `Makefile` sliced `RELEASE.md` for a heading reading `Release ONDEWO VTSI Client Python <version>` while this
  file, `README.md` and the ondewo-vtsi-api release generator all write `Release ONDEWO VTSI Python Client
  <version>` -- the same three words the other way round -- so the slice matched nothing and
  `gh release create -n ""` published a release with no notes and no error. Every release from 6.9.0 to 8.7.0
  except 8.3.0 shipped with a body of length 0. `tests/unit/test_release_notes_slice.py` now re-derives the
  pattern from the `Makefile` and fails when the current version's slice is empty, unterminated or heading-only.

*****************

## Release ONDEWO VTSI Python Client 8.7.0

### Improvements

* Built against [ondewo-vtsi-api 8.7.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/8.7.0),
  which re-vendors [ondewo-nlu-api 7.1.0](https://github.com/ondewo/ondewo-nlu-api/releases/tag/7.1.0)
  (was 7.0.0) and [ondewo-s2t-api 7.5.0](https://github.com/ondewo/ondewo-s2t-api/releases/tag/7.5.0)
  (was 7.4.0). `ondewo/vtsi/**` is unchanged in that API release, so the VTSI service surface is
  identical and this client stays wire-compatible with 8.6.0.
* **This release exists for the vendored surface, not for the VTSI one.** This package ships
  `ondewo/vtsi` *plus* vendored copies of `ondewo/nlu` and `ondewo/{s2t,t2s,sip,qa}`, and those land on
  the same module paths as `ondewo-nlu-client` and `ondewo-s2t-client` in one site-packages. Measured
  against the 8.6.0 wheel: its `ondewo/nlu` tree differed from `ondewo-nlu-client` 7.1.2 in exactly
  `rag_pb2.py` / `.pyi`, and its `ondewo/s2t` tree from `ondewo-s2t-client` 7.5.0 in exactly
  `speech_to_text_pb2.py` / `.pyi`. A consumer pinning 8.6.0 next to those clients therefore resolved
  the skew by install order rather than by an error, which is the failure mode this lockstep bump
  exists to prevent.
* What the vendored surface gains: `speech-to-text.proto` adds the `VadMethod` and `TsdMethod` enums
  and the `Silero` and `WespeakerTsd` messages; `rag.proto` adds `RagCrawlerIncrementalConfig`.
  `RagCrawlerFilters` re-declares four fields as `[deprecated = true]` -- every field number, name and
  type preserved, so nothing on the wire changes.

*****************

## Release ONDEWO VTSI Python Client 8.6.0

### Improvements

* Tracking API Version [8.6.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/8.6.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 8.5.0

### Improvements

* Tracking API Version [8.5.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/8.5.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 8.4.0

### Improvements

* Tracking API Version [8.4.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/8.4.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Client Python 8.3.0

### Bug Fixes

* [[OND221-2830]](https://ondewo.atlassian.net/browse/OND221-2830) Regenerated with [ondewo-proto-compiler 5.13.0](https://github.com/ondewo/ondewo-proto-compiler/releases/tag/5.13.0), tracking ondewo-vtsi-api 8.3.0 in line with the angular, js, nodejs and typescript clients of this release.
* [[OND221-2830]](https://ondewo.atlassian.net/browse/OND221-2830) Tooling: `conventional-pre-commit` now runs before `giticket` at the commit-msg stage - with giticket first, its `[OND221-2830] fix: ...` rewrite was no longer valid Conventional Commits and every commit on a ticket branch failed.

*****************

## Unreleased

### Improvements

* Regenerated against [ondewo-vtsi-api](https://github.com/ondewo/ondewo-vtsi-api) with the new optional field
  `AsteriskConfigs.asterisk_version`, which carries the docker image tag of the ONDEWO Asterisk image a VTSI project
  should start (e.g. `alpine-3.18-18.20.2`). The Asterisk version is therefore a per-project setting rather than a
  server-wide one.
* The field has **explicit presence**: leave it unset and the server keeps its configured default
  (`ONDEWO_VTSI_ASTERISK_IMAGE_TAG`); send an empty string and the server rejects the request. Ask
  `asterisk_configs.HasField("asterisk_version")` — reading the attribute returns `''` in both cases and cannot tell
  them apart.

### Bug Fixes

* `ClientConfig` no longer prints its credentials. `@dataclass` generates a `__repr__` that renders every field, so `log.debug(f"...{config}")` — or any traceback carrying locals — wrote the Keycloak password and the gRPC certificate to the logs in clear text. `repr()` and `str()` now render `password` and `grpc_cert` as `***REDACTED***`. An unset or empty value still renders as `None` / `''`: the marker reads as "set and sensitive", which misleads when the real fault is that nobody set it.
* **Behaviour change** for anyone who parsed the repr: read the attribute (`config.password`, `config.grpc_cert`) instead. Only the rendered text changed — the fields themselves, equality and `dataclasses.asdict()` are untouched.

*****************

## Release ONDEWO VTSI Python Client 8.2.0

### Improvements

* Tracking API Version [8.2.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/8.2.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 8.1.0

### Improvements

* Tracking API Version [8.1.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/8.1.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 8.0.0

### Improvements

* Tracking API Version [8.0.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/8.0.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 7.0.1

### Improvements

* Added functionality to pass grpc options to grpc clients based on [ONDEWO CLIENT UTILS PYTHON 2.0.0](https://github.com/ondewo/ondewo-client-utils-python/releases/tag/2.0.0)

*****************

## Release ONDEWO VTSI Python Client 7.0.0

### Improvements

* Tracking API Version [7.0.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/7.0.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 6.9.0

### Improvements

* Tracking API Version [6.9.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/6.9.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 6.8.0

### Improvements

* Tracking API Version [6.8.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/6.8.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 6.7.0

### Improvements

* Tracking API Version [6.7.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/6.7.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 6.6.0

### Improvements

* Tracking API Version [6.6.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/6.6.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 6.5.0

### Improvements

* Tracking API Version [6.5.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/6.5.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 6.4.0

### Improvements

* Tracking API Version [6.4.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/6.4.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 6.3.0

### Improvements

* Tracking API Version [6.3.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/6.3.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 6.2.0

### Improvements

* Tracking API Version [6.2.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/6.2.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 6.1.0

### Improvements

* Tracking API Version [6.1.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/6.1.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 6.0.0

### Improvements

* Tracking API Version [6.0.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/6.0.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Python Client 5.0.0

### Improvements

* Tracking API Version [5.0.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/5.0.0) ( [Documentation](https://ondewo.github.io/ondewo-vtsi-api/) )

*****************

## Release ONDEWO VTSI Client Python 3.5.0

### Improvements

* New client for VTSI API 3.0.0

*****************

## Release ONDEWO VTSI Client Python 3.4.0

### Improvements

* New client updates for retrieving minio data

*****************

## Release ONDEWO VTSI Client Python 3.3.0

### Improvements

* New client updates for s2t t2s nlu and sip

*****************

## Release ONDEWO VTSI Client Python 3.2.0

### Improvements

* New API changes
* CSI configs added so you can configure services like Rabbitmq

*****************

## Release ONDEWO VTSI Client Python 3.1.0

### Improvements

* New API changes
* CSI configs added so you can configure services like MINIO

*****************

## Release ONDEWO VTSI Client Python 3.0.0

### Improvements

* New API changes
* Adaptation to new changes of s2t and t2s
* client adaptation to changes

*****************

## Release ONDEWO VTSI Client Python 2.3.0

### Improvements

* different contexts can be used for each call in make multiple calls endpoint
* grpc_cert fields added to stt, tts and nlu configs

### Bug Fixes

* added nlu-client and sip-client as dependencies

*****************

## Release ONDEWO VTSI Client Python 2.2.0

### Improvements

* endpoint added to make multiple calls
* new multiple calls example added
* deleted manifest related code

*****************

## Release ONDEWO VTSI Client Python 2.1.1

### Improvements

* pushed to pypi

*****************

## Release ONDEWO VTSI Client Python 2.1.0

### Improvements

* changed voip to vtsi in some variable names
* lots of example scripts
* get_minimal_client has more and better defaults
* added 'initial_intent' config var
* removed many defunct proto endpoints

*****************

## Release ONDEWO VTSI Client Python 2.0.1

### Improvements

* made py2 importable

### Bug Fixes

* fixed grpc cert import bug

*****************

## Release ONDEWO VTSI Client Python 2.0.0

### Improvements

* added secure grpc authentication
* added an example listener deployment
* simplified call initiation (no difference between listners and callers)

### Bug Fixes

* fixed pip install namespace bug

*****************

## Release ONDEWO VTSI Client Python 1.2.1

### Improvements

* Added logo

*****************

## Release ONDEWO VTSI Client Python 1.2.0

### Improvements

* Cleaned the code
* Refactored the layout to be more in line with other clients
* Added LICESES etc for github
* Moved to Github

### Known issues not covered in this release

* CI/CD Integration is missing
* Code Quality checks
* Extend the README.md with an examples usage

*****************

## Release ONDEWO RELEASE Template

### New Features

### Improvements

### Bug fixes

### Breaking Changes

### Known issues not covered in this release

### Migration Guide

*****************
