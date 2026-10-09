# Release History

*****************

## Release ONDEWO VTSI Client Python 8.7.1

### Improvements

* `Client` and `AsyncClient` take an opt-in keyword `use_shared_channel=True`: all services then share ONE gRPC channel built with `ondewo-client-utils`' `build_shared_channel` (one connection and one TLS handshake instead of one per service; measured in the library, 16 services over TLS: 44 ms per-service vs 6.5 ms shared). The default is unchanged. The service interfaces accept the keyword-only `grpc_channel=`.
* Built with [ondewo-proto-compiler 5.15.3](https://github.com/ondewo/ondewo-proto-compiler/releases/tag/5.15.3)
  (was 5.14.0), still against [ondewo-vtsi-api 8.7.0](https://github.com/ondewo/ondewo-vtsi-api/releases/tag/8.7.0);
  the VTSI service surface is unchanged.

### Bug Fixes

* `ClientConfig` no longer prints the mutual-TLS private key `grpc_client_key` (added by `ondewo-client-utils` 4.1.0). `BaseClientConfig` declares it `repr=False`, but this class overrides `__repr__` and ignored that flag, so `repr()` / `str()` rendered the PEM in clear text. It is now redacted as `***REDACTED***`, as is every other field declared `repr=False`. The `ondewo-client-utils` floor is raised to `>=4.1.1`.
* Dependency: `ondewo-client-utils>=4.1.1` on Python >=3.12 (4.1.1 requires 3.12); older interpreters keep
  `ondewo-client-utils>=3.2.0`, whose config has no client key to leak.
* `Client` / `AsyncClient` `_initialize_services` takes a `BaseClientConfig` and narrows it with an `isinstance`
  guard: a config that is not a vtsi `ClientConfig` now raises `ValueError` instead of failing later (same as
  ondewo-nlu-client).

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

## Shipped in 8.3.0 to 8.7.0 (listed here as "Unreleased" until 8.7.1)

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
