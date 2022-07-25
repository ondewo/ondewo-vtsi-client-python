include ./envs/versions.env
export
export GH_TOKEN=
# Fully automated build and deploy process for ondewo-vtsi-client-python
# Release Process Steps:
# 1 - Create Release Branch and push
# 2 - Create Release Tag and push
# 3 - GitHub Release
# 4 - PyPI Release

NLU_APIS_DIR=ondewo-nlu-api
GOOGLE_APIS_DIR=ondewo-nlu-api/googleapis
VTSI_APIS_DIR=ondewo-vtsi-api/
SIP_APIS_DIR=ondewo-sip-api/
S2T_APIS_DIR=ondewo-s2t-api/
T2S_APIS_DIR=ondewo-t2s-api/
GOOGLE_PROTOS_DIR=ondewo-nlu-api/googleapis/google/
NLU_PROTOS_DIR=ondewo-nlu-api/ondewo/
VTSI_PROTOS_DIR=ondewo-vtsi-api/
SIP_PROTOS_DIR=ondewo-sip-api/
S2T_PROTOS_DIR=ondewo-s2t-api/
T2S_PROTOS_DIR=ondewo-t2s-api/

TESTFILE := ondewo
CODE_CHECK_IMAGE := code_check_image_${TESTFILE}
IMAGE_NAME := dockerregistry.ondewo.com:5000/ondewo-vtsi-client-python

CURRENT_RELEASE_NOTES=`cat RELEASE.md \
	| sed -n '/Release ONDEWO VTSI Client Python ${ONDEWO_VTSI_VERSION}/,/\*\*/p'`

GH_REPO="https://github.com/ondewo/ondewo-vtsi-client-python"

IMAGE_UTILS_NAME=ondewo-vtsi-client-utils-python:${ONDEWO_VTSI_VERSION}

.DEFAULT_GOAL := help


# First comment after target starting with double ## specifies usage
help:  ## Print usage info about help targets
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' Makefile | awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'


# BEFORE "release"
update_setup: ## Update VTSI Version in setup.py
	@sed -i "s/version='[0-9]*.[0-9]*.[0-9]*'/version='${ONDEWO_VTSI_VERSION}'/g" setup.py
	@sed -i "s/version=\"[0-9]*.[0-9]*.[0-9]*\"/version='${ONDEWO_VTSI_VERSION}'/g" setup.py

release: ## Automate the entire release process
	@echo "Release Automation started"
	create_release_branch
	create_release_tag
	build_and_release_to_github_via_docker
	build_and_push_to_pypi_via_docker
	@echo "Release Finished"

create_release_branch: ## Create Release Branch and push it to origin
	git checkout -b "release/${ONDEWO_VTSI_VERSION}"
	git push -u origin "release/${ONDEWO_VTSI_VERSION}"

create_release_tag: ## Create Release Tag and push it to origin
	git tag -a ${ONDEWO_VTSI_VERSION} -m "release/${ONDEWO_VTSI_VERSION}"
	git push origin ${ONDEWO_VTSI_VERSION}

login_to_gh: ## Login to Github CLI with Access Token
	echo $(GITHUB_GH_TOKEN) | gh auth login -p ssh --with-token

build_gh_release: ## Generate Github Release with CLI
	gh release create --repo $(GH_REPO) "$(ONDEWO_VTSI_VERSION)" -n "$(CURRENT_RELEASE_NOTES)" -t "Release ${ONDEWO_VTSI_VERSION}"

build_and_push_to_pypi_via_docker:  push_to_pypi_via_docker_image  ## Release automation for building and pushing to pypi via a docker image

build_and_release_to_github_via_docker: build build_utils_docker_image release_to_github_via_docker_image  ## Release automation for building and releasing on GitHub via a docker image

build: clear_package_data init_submodules checkout_defined_submodule_versions generate_ondewo_protos update_setup ## Build source code

install:
	git submodule update --init --recursive
	pip install -e .
	pip install -r requirements.txt

clean_python_api:  ## Clear generated python files
	find ./ondewo -name \*pb2.py -type f -exec rm -f {} \;
	find ./ondewo -name \*pb2_grpc.py -type f -exec rm -f {} \;
	find ./ondewo -name \*.pyi -type f -exec rm -f {} \;
	rm -rf google

# {{{ PROTOS
generate_all_protos: generate_ondewo_protos generate_google_protos generate_specific_protos ## Generate all Protos

generate_google_protos: ## Generate Google API Protos
	python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. ${GOOGLE_APIS_DIR}/google/api/annotations.proto
	python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. ${GOOGLE_APIS_DIR}/google/rpc/status.proto
	python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. ${GOOGLE_APIS_DIR}/google/type/latlng.proto
	python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. ${GOOGLE_APIS_DIR}/google/api/http.proto
	python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. ${GOOGLE_APIS_DIR}/google/longrunning/operations.proto

generate_ondewo_protos: ## Generate Ondewo Protos
	for f in $$(find ${NLU_PROTOS_DIR} -name '*.proto'); do \
		python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} -I${NLU_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. $$f; \
	done

generate_specific_protos: ## Generate NLU-SIP-S2T-T2S-VTSI Protos
	for f in $$(find ${NLU_PROTOS_DIR}nlu -name '*.proto'); do \
		python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} -I${NLU_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. $$f; \
	done
	for f in $$(find ${SIP_PROTOS_DIR} -name '*.proto'); do \
		python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} -I${NLU_APIS_DIR} -I${SIP_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. $$f; \
	done
	for f in $$(find ${S2T_PROTOS_DIR} -name '*.proto'); do \
		python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} -I${NLU_APIS_DIR} -I${S2T_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. $$f; \
	done
	for f in $$(find ${T2S_PROTOS_DIR} -name '*.proto'); do \
		python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} -I${NLU_APIS_DIR} -I${T2S_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. $$f; \
	done
	for f in $$(find ${VTSI_PROTOS_DIR} -name '*.proto'); do \
		python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} -I${NLU_APIS_DIR} -I${VTSI_APIS_DIR} -I${SIP_APIS_DIR} -I${T2S_APIS_DIR} -I${S2T_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. $$f; \
	done

# }}}

init_submodules:  ## Initialize submodules
	@echo "START initializing submodules ..."
	git submodule update --init --recursive
	@echo "DONE initializing submodules"

checkout_defined_submodule_versions:  ## Update submodule versions
	@echo "START checking out submodules ..."
	git -C ${ONDEWO_NLU_API_DIR} fetch --all
	git -C ${ONDEWO_NLU_API_DIR} checkout ${ONDEWO_NLU_API_GIT_BRANCH}
	git -C ${SIP_APIS_DIR} fetch --all
	git -C ${SIP_APIS_DIR} checkout ${ONDEWO_SIP_API_GIT_BRANCH}
	git -C ${S2T_APIS_DIR} fetch --all
	git -C ${S2T_APIS_DIR} checkout ${ONDEWO_S2T_API_GIT_BRANCH}
	git -C ${T2S_APIS_DIR} fetch --all
	git -C ${T2S_APIS_DIR} checkout ${ONDEWO_T2S_API_GIT_BRANCH}
	git -C ${VTSI_APIS_DIR} fetch --all
	git -C ${VTSI_APIS_DIR} checkout ${ONDEWO_VTSI_API_GIT_BRANCH}
	@echo "DONE checking out submodules"

build_utils_docker_image:  ## Build utils docker image
	docker build -f Dockerfile.utils -t ${IMAGE_UTILS_NAME} .

push_to_pypi_via_docker_image:  ## Push source code to pypi via docker
	[ -d $(OUTPUT_DIR) ] || mkdir -p $(OUTPUT_DIR)
	docker run --rm \
		-v ${shell pwd}/dist:/home/ondewo/dist \
		-e PYPI_USERNAME=${PYPI_USERNAME} \
		-e PYPI_PASSWORD=${PYPI_PASSWORD} \
		${IMAGE_UTILS_NAME} make push_to_pypi
	rm -rf dist

push_to_pypi: build_package upload_package clear_package_data
	@echo 'YAY - Pushed to pypi : )'

push_to_gh: login_to_gh build_gh_release
	@echo 'Released to Github'

release_to_github_via_docker_image:  ## Release to Github via docker
	docker run --rm \
		${IMAGE_UTILS_NAME} make push_to_gh

build_package:
	python setup.py sdist bdist_wheel
	chmod a+rw dist -R

upload_package:
	twine upload --verbose -r pypi dist/* -u${PYPI_USERNAME} -p${PYPI_PASSWORD}

clear_package_data:
	rm -rf build dist/* ondewo_vtsi_client.egg-info

ondewo_release: spc clone_devops_accounts run_release_with_devops ## Release with credentials from devops-accounts repo
	@rm -rf ${DEVOPS_ACCOUNT_GIT}

clone_devops_accounts: ## Clones devops-accounts repo
	if [ -d $(DEVOPS_ACCOUNT_GIT) ]; then rm -Rf $(DEVOPS_ACCOUNT_GIT); fi
	git clone git@bitbucket.org:ondewo/${DEVOPS_ACCOUNT_GIT}.git

DEVOPS_ACCOUNT_GIT="ondewo-devops-accounts"
DEVOPS_ACCOUNT_DIR="./${DEVOPS_ACCOUNT_GIT}"

TEST:
	@echo ${GITHUB_GH_TOKEN}
	@echo ${PYPI_USERNAME}
	@echo ${PYPI_PASSWORD}
	@echo ${CURRENT_RELEASE_NOTES}

run_release_with_devops:
	$(eval info:= $(shell cat ${DEVOPS_ACCOUNT_DIR}/account_github.env | grep GITHUB_GH & cat ${DEVOPS_ACCOUNT_DIR}/account_pypi.env | grep PYPI_USERNAME & cat ${DEVOPS_ACCOUNT_DIR}/account_pypi.env | grep PYPI_PASSWORD))
	make release $(info)

spc: ## Checks if the Release Branch, Tag and Pypi version already exist
	$(eval filtered_branches:= $(shell git branch --all | grep "release/${ONDEWO_VTSI_VERSION}"))
	$(eval filtered_tags:= $(shell git tag --list | grep "${ONDEWO_VTSI_VERSION}"))
	$(eval setuppy_version:= $(shell cat setup.py | grep "version"))
	@if test "$(filtered_branches)" != ""; then echo "-- Test 1: Branch exists!!" & exit 1; else echo "-- Test 1: Branch is fine";fi
	@if test "$(filtered_tags)" != ""; then echo "-- Test 2: Tag exists!!" & exit 1; else echo "-- Test 2: Tag is fine";fi
	@if test "$(setuppy_version)" != "version='${ONDEWO_VTSI_VERSION}',"; then echo "-- Test 3: Setup.py not updated!!" & exit 1; else echo "-- Test 3: Setup.py is fine";fi

