# Release History
*****************
## Release ONDEWO VTSI Client Python 2.1.0

### Improvements

* changed voip to vtsi in some variable names
* lots of example scripts
* get_minimal_client has more and better defaults

*****************
## Release ONDEWO VTSI Client Python 3.0.0

### Improvements
* added initial_intent triggering functionality
> * reformatted to align with all the other clients import styles
> * using the most up-to-date version of logging

### Breaking Changes
> * import style has changed to be compliant with the rest of the clients
> * grpc_certificate format has changed from PEM to JSON

### Migration Guide
* from ondewo.vtsi.client import Client => from ondewo.vtsi.client.client import Client
* from ondewo.vtsi.client_config import ClientConfig => from ondew.vtsi.client.client_config import ClientConfig
> * get a new grpc certificate from us in the json format

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
