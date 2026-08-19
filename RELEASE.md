# Release History

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
