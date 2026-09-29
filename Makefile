export
# ---------------- BEFORE RELEASE ----------------
# 1 - Update Version Number
# 2 - Update RELEASE.md
# 3 - make update_setup
# -------------- Release Process Steps --------------
# 1 - Get Credentials from devops-accounts repo
# 2 - Create Release Branch and push
# 3 - Create Release Tag and push
# 4 - GitHub Release
# 5 - PyPI Release

########################################################
# 		Variables
########################################################

# MUST BE THE SAME AS API in Mayor and Minor Version Number
# example: API 2.9.0 --> Client 2.9.X
ONDEWO_VTSI_VERSION=9.0.0
PYPI_USERNAME?=ENTER_HERE_YOUR_PYPI_USERNAME
PYPI_PASSWORD?=ENTER_HERE_YOUR_PYPI_PASSWORD

# You need to setup an access token at https://github.com/settings/tokens - permissions are important
GITHUB_GH_TOKEN?=ENTER_YOUR_TOKEN_HERE

# The heading wording is the one the ondewo-vtsi-api release generator WRITES, not a free choice.
# `release_client` in ondewo-vtsi-api's Makefile emits `## Release ONDEWO VTSI Python Client <version>`
# and greps RELEASE.md for exactly that form before deciding whether to insert its boilerplate entry.
# This slice pattern read `... Client Python ...` - the same three words the other way round - so it
# matched nothing, the slice was EMPTY, and `gh release create -n ""` published a release with no body
# and no error anywhere.
#
# MEASURED 2026-09-15 over all 31 published releases of this client - `gh api .../releases` body length
# against the wording of the matching RELEASE.md heading - and the correlation is exact. Old `Client
# Python` wording: 2.2.0, 2.3.0, 3.0.0, 3.1.0, 3.2.0, 3.3.0, 3.4.0, 3.5.0 and 8.3.0, nine releases,
# every one with a NON-EMPTY body of 44-668 bytes. Generator wording: twenty releases, every one with a
# body of length 0 - as are 4.0.0 and 6.3.1, which carry no RELEASE.md entry at all. So this pattern was
# CORRECT for 3.5.0 and older and went stale when the heading wording flipped at 5.0.0; 8.3.0 is the one
# entry written with the old wording AFTER that flip, which is why it is the only non-empty body from
# 4.0.0 onwards. It is not the only old-wording entry in the file.
#
# RELEASE.md carries 37 `## Release` headings today: 21 in the generator's wording, 15 in the old one,
# 1 template. README.md's release instructions use the generator's wording. The 15 old headings are
# deliberately LEFT ALONE - the generator greps only for the version being released, so rewriting
# shipped entries fixes nothing and destroys the measurement above.
#
# The PATTERN is what moves. Rewriting the CURRENT version's heading instead would make the generator's
# own guard miss, insert a second heading for the same version, and trip markdownlint MD024 - which does
# not auto-fix, so the client's pre-commit fails and the release aborts mid-publish.
#
# Terminate on the ***** separator that delimits release entries, NOT on /\*\*/ - that matched the first
# markdown **bold** span inside an entry and truncated the notes there, again with no error. All
# separators in RELEASE.md are exactly 17 asterisks, so ^\*{5} cannot match anything but a separator.
#
# Keep the version reference and the `=` on SEPARATE lines: at release time the generator rewrites,
# wholesale, any line that names ONDEWO_VTSI_VERSION and also carries an equals sign.
CURRENT_RELEASE_NOTES=`cat RELEASE.md \
	| perl -ne 'print if /Release ONDEWO VTSI Python Client ${ONDEWO_VTSI_VERSION}/../^\*{5}/'`

GH_REPO="https://github.com/ondewo/ondewo-vtsi-client-python"
DEVOPS_ACCOUNT_GIT="ondewo-devops-accounts"
DEVOPS_ACCOUNT_DIR="./${DEVOPS_ACCOUNT_GIT}"
ONDEWO_VTSI_API_GIT_BRANCH=62031d9ee13900ebfbc240f80e5fdee7a2ba3785
ONDEWO_PROTO_COMPILER_GIT_BRANCH=tags/5.15.0
ONDEWO_PROTO_COMPILER_DIR=ondewo-proto-compiler
ONDEWO_VTSI_API_DIR=ondewo-vtsi-api
GOOGLE_PROTOS_DIR=${ONDEWO_VTSI_API_DIR}/google
NLU_PROTOS_DIR=ondewo/nlu
S2T_PROTOS_DIR=ondewo/s2t
T2S_PROTOS_DIR=ondewo/t2s
SIP_PROTOS_DIR=ondewo/sip
VTSI_PROTOS_DIR=ondewo/vtsi
IMAGE_UTILS_NAME=ondewo-vtsi-client-utils-python:${ONDEWO_VTSI_VERSION}
.DEFAULT_GOAL := help

########################################################
#       ONDEWO Standard Make Targets
########################################################

setup_developer_environment_locally: install_precommit_hooks install_dependencies_locally

install_precommit_hooks: ## Installs pre-commit hooks and sets them up for the ondewo-csi-client repo
	-pip install pre-commit
	-conda -y install pre-commit
	pre-commit install
	pre-commit install --hook-type commit-msg

precommit_hooks_run_all_files: ## Runs all pre-commit hooks on all files and not just the changed ones
	pre-commit run --all-file

install_dependencies_locally: ## Install dependencies locally
	pip install -r requirements-dev.txt
	pip install -r requirements.txt

flake8: ## Runs flake8
	flake8 --config .flake8 .

mypy: ## Run mypy static code checking
	@echo "---------------------------------------------"
	@echo "START: Run mypy in pre-commit hook ..."
	pre-commit run mypy --all-files
	@echo "DONE: Run mypy in pre-commit hook."
	@echo "---------------------------------------------"
	@echo "START: Run mypy directly ..."
	mypy --config-file=mypy.ini .
	@echo "DONE: Run mypy directly"
	@echo "---------------------------------------------"

help: ## Print usage info about help targets
	# (first comment after target starting with double hashes ##)
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

makefile_chapters: ## Shows all sections of Makefile
	@echo `cat Makefile| grep "########################################################" -A 1 | grep -v "########################################################"`

TEST:
	@echo ${GITHUB_GH_TOKEN}
	@echo ${PYPI_USERNAME}
	@echo ${PYPI_PASSWORD}
	@echo "\n${CURRENT_RELEASE_NOTES}"

check_build: ## Checks if all built proto-code is there
	@rm -rf build_check.txt
	@for proto in `find ondewo-vtsi-api/ondewo -iname "*.proto*"`; \
	do \
		echo $${proto} | cut -d "/" -f 4 | cut -d "." -f 1 >> build_check.txt; \
	done
	@echo "`sort build_check.txt | uniq`" > build_check.txt
	@perl -i -pe "s/\-/\_/g" build_check.txt
	@for file in `cat build_check.txt`;\
	do \
		find ondewo -iname "*pb*" | grep -q $${file}; \
		if test $$? != 0; then  echo "No Proto-Code for $${file}" & exit 1;fi \
	done
	@rm -rf build_check.txt

########################################################
#       Repo Specific Make Targets
########################################################
#		Build

update_setup: ## Update Version in pyproject.toml
	@perl -i -pe 's/^version = "\d+\.\d+\.\d+"/version = "${ONDEWO_VTSI_VERSION}"/' pyproject.toml

build: clear_package_data prepare_submodules build_compiler generate_all_protos create_async_services update_setup ## Build source code

push_to_pypi_via_docker: push_to_pypi_via_docker_image  ## Release automation for building and pushing to pypi via a docker image

release_to_github_via_docker: build_utils_docker_image release_to_github_via_docker_image  ## Release automation for building and releasing on GitHub via a docker image

build_compiler:
	make -C ondewo-proto-compiler/python build

clean_python_api:  ## Clear generated python files
	find ./ondewo -name \*pb2.py -type f -exec rm -f {} \;
	find ./ondewo -name \*pb2_grpc.py -type f -exec rm -f {} \;
	find ./ondewo -name \*.pyi -type f -exec rm -f {} \;

generate_all_protos: generate_nlu_protos generate_s2t_protos generate_t2s_protos generate_sip_protos generate_vtsi_protos
	-make precommit_hooks_run_all_files
	make precommit_hooks_run_all_files

generate_nlu_protos:
	make -f ondewo-proto-compiler/python/Makefile run \
		PROTO_DIR=${ONDEWO_VTSI_API_DIR}/ondewo \
		EXTRA_PROTO_DIR=${GOOGLE_PROTOS_DIR} \
		TARGET_DIR='${NLU_PROTOS_DIR}' \
		OUTPUT_DIR='.'
	make -f ondewo-proto-compiler/python/Makefile run \
		PROTO_DIR=${ONDEWO_VTSI_API_DIR}/ondewo \
		EXTRA_PROTO_DIR=${GOOGLE_PROTOS_DIR} \
		TARGET_DIR='ondewo/qa' \
		OUTPUT_DIR='.'

generate_s2t_protos:
	make -f ondewo-proto-compiler/python/Makefile run \
		PROTO_DIR=${ONDEWO_VTSI_API_DIR}/ondewo \
		TARGET_DIR='${S2T_PROTOS_DIR}' \
		OUTPUT_DIR='.'

generate_t2s_protos:
	make -f ondewo-proto-compiler/python/Makefile run \
		PROTO_DIR=${ONDEWO_VTSI_API_DIR}/ondewo \
		TARGET_DIR='${T2S_PROTOS_DIR}' \
		OUTPUT_DIR='.'

generate_sip_protos:
	make -f ondewo-proto-compiler/python/Makefile run \
		PROTO_DIR=${ONDEWO_VTSI_API_DIR}/ondewo \
		TARGET_DIR='${SIP_PROTOS_DIR}' \
		OUTPUT_DIR='.'

generate_vtsi_protos:
	make -f ondewo-proto-compiler/python/Makefile run \
		PROTO_DIR=${ONDEWO_VTSI_API_DIR}/ondewo \
		EXTRA_PROTO_DIR=${GOOGLE_PROTOS_DIR} \
		TARGET_DIR='${VTSI_PROTOS_DIR}' \
		OUTPUT_DIR='.'

build_utils_docker_image:  ## Build utils docker image
	docker build -f Dockerfile.utils -t ${IMAGE_UTILS_NAME} .

setup_conda_env: ## Checks for CONDA Environment
	@echo "\n START SETTING UP CONDA ENV \n"
	@conda env list | grep -q ondewo-vtsi-client-python \
	&& make release || ( echo "\n CONDA ENV FOR REPO DOESNT EXIST \n" \
	&& make create_conda_env)

create_conda_env: ## Creates CONDA Environment
	conda create -y --name ondewo-vtsi-client-python python=3.9
	/bin/bash -c 'source `conda info --base`/bin/activate ondewo-vtsi-client-python; make setup_developer_environment_locally && echo "\n PRECOMMIT INSTALLED \n"'
	make release

HAND_WRITTEN_ASYNC_MARKER=ondewo:hand-written-async-service

create_async_services: ## Create async services for all synchronous services
	# The rewrite below turns every `self.stub.Rpc(...)` into `await self.stub.Rpc(...)`, which is
	# correct for a unary RPC (grpc.aio returns an awaitable UnaryUnaryCall) and WRONG for a
	# server-streaming one (UnaryStreamCall is an async ITERATOR and must not be awaited). A generated
	# async streaming wrapper therefore fails at runtime, silently, on the first call. An async_*.py
	# carrying ${HAND_WRITTEN_ASYNC_MARKER} is maintained by hand and is left alone.
	@find ondewo -type d -name "services" ! -path "*/.*/*" | while read -r dir; do \
	    for file in "$$dir"/*.py; do \
	        filename=$$(basename -- "$$file"); \
	        case "$$filename" in \
	            "__init__.py"|async_*) continue ;; \
	        esac; \
	        if [ -f "$$dir/async_$$filename" ] && grep -q "${HAND_WRITTEN_ASYNC_MARKER}" "$$dir/async_$$filename"; then \
	            echo "create_async_services: keeping hand-written $$dir/async_$$filename"; \
	            continue; \
	        fi; \
	        cp "$$file" "$$dir/async_$$filename"; \
	    done; \
	    for file in "$$dir"/async_*.py; do \
	        if grep -q "${HAND_WRITTEN_ASYNC_MARKER}" "$$file"; then continue; fi; \
	        perl -i -pe 'unless(/def stub/){ s/^([[:space:]]*)def /$$1async def /g; s/self\.stub/await self.stub/g; s/\(BaseServicesInterface\)/(AsyncBaseServicesInterface)/g; s/base_services_interface/async_base_services_interface/g; s/import BaseServicesInterface/import AsyncBaseServicesInterface/g; s/services_interface import ServicesInterface/async_services_interface import AsyncServicesInterface/g; s/\((?<!Async)ServicesInterface\)/(AsyncServicesInterface)/g; }' \
	            "$$file"; \
	    done; \
	done
	-make precommit_hooks_run_all_files
	make precommit_hooks_run_all_files

########################################################
#		Release

release: ## Automate the entire release process
	@echo "Start Release"
	make build
	/bin/bash -c 'source `conda info --base`/bin/activate ondewo-vtsi-client-python; make precommit_hooks_run_all_files || echo "PRECOMMIT FOUND SOMETHING"'
	git status
	make check_build
	git add ondewo
	git add Makefile
	git add RELEASE.md
	git add pyproject.toml uv.lock
	git add ${ONDEWO_PROTO_COMPILER_DIR}
	git add ${ONDEWO_VTSI_API_DIR}
	git add ondewo-vtsi-api
	git status
	-git commit --no-verify -m "PREPARING FOR RELEASE ${ONDEWO_VTSI_VERSION}"
	git push
	make create_release_branch
	make create_release_tag
	make release_to_github_via_docker
	make push_to_pypi_via_docker
	@echo "Release Finished"

create_release_branch: ## Create Release Branch and push it to origin
	git checkout -b "release/${ONDEWO_VTSI_VERSION}"
	git push -u origin "release/${ONDEWO_VTSI_VERSION}"

create_release_tag: ## Create Release Tag and push it to origin
	git tag -a ${ONDEWO_VTSI_VERSION} -m "release/${ONDEWO_VTSI_VERSION}"
	git push origin ${ONDEWO_VTSI_VERSION}

login_to_gh: ## Login to Github CLI with Access Token
	@echo $(GITHUB_GH_TOKEN) | gh auth login -p ssh --with-token

build_gh_release: ## Generate Github Release with CLI
	gh release create --repo $(GH_REPO) "$(ONDEWO_VTSI_VERSION)" -n "$(CURRENT_RELEASE_NOTES)" -t "Release ${ONDEWO_VTSI_VERSION}"

########################################################
#		Submodules

prepare_submodules: init_submodules checkout_defined_submodule_versions

init_submodules:
	git submodule update --init --recursive

checkout_defined_submodule_versions:
	@echo "START checking out submodules ..."
	git -C ${ONDEWO_VTSI_API_DIR} fetch --all
	git -C ${ONDEWO_VTSI_API_DIR} checkout ${ONDEWO_VTSI_API_GIT_BRANCH}
	git	-C ${ONDEWO_PROTO_COMPILER_DIR} fetch --all
	git -C ${ONDEWO_PROTO_COMPILER_DIR} checkout ${ONDEWO_PROTO_COMPILER_GIT_BRANCH}
	make -C ${ONDEWO_VTSI_API_DIR} build
	@echo "DONE checking out submodules"

install: init_submodules
	pip install -e .

########################################################
#		PYPI

# PEP 517 build: setup.py no longer exists (pyproject.toml declares the setuptools backend).
# uv is the frontend because Dockerfile.utils already ships uv and twine; the `build` package
# is not installed there.
build_package: ## Builds PYPI Package
	uv build --sdist --wheel --out-dir dist
	chmod a+rw dist -R

upload_package:
	@twine upload --verbose -r pypi dist/* -u${PYPI_USERNAME} -p${PYPI_PASSWORD}

clear_package_data: ## Clears PYPI Package
	echo "Waiting 5s so directory for removal is not busy anymore"
	sleep 5s
	-rm -rf build dist/* ondewo_vtsi_client.egg-info

push_to_pypi_via_docker_image:  ## Push source code to pypi via docker
	[ -d $(OUTPUT_DIR) ] || mkdir -p $(OUTPUT_DIR)
	@docker run --rm \
		-v ${shell pwd}/dist:/home/ondewo/dist \
		-e PYPI_USERNAME=${PYPI_USERNAME} \
		-e PYPI_PASSWORD=${PYPI_PASSWORD} \
		${IMAGE_UTILS_NAME} make push_to_pypi
	rm -rf dist

push_to_pypi: build_package upload_package clear_package_data ## Builds -> Uploads -> Clears PYPI Package
	@echo 'YAY - Pushed to pypi : )'

show_pypi: build_package ## Shows PYPI Package with Dockerimage
	tar xvfz dist/ondewo-vtsi-client-${ONDEWO_VTSI_VERSION}.tar.gz
	tree ondewo-vtsi-client-${ONDEWO_VTSI_VERSION}
	cat ondewo-vtsi-client-${ONDEWO_VTSI_VERSION}/ondewo_vtsi_client.egg-info/requires.txt

show_pypi_via_docker_image: build_utils_docker_image ## Push source code to pypi via docker
	[ -d $(OUTPUT_DIR) ] || mkdir -p $(OUTPUT_DIR)
	@docker run --rm \
		-v ${shell pwd}/dist:/home/ondewo/dist \
		-e PYPI_USERNAME=${PYPI_USERNAME} \
		-e PYPI_PASSWORD=${PYPI_PASSWORD} \
		${IMAGE_UTILS_NAME} make show_pypi
	rm -rf dist

########################################################
#		GITHUB

push_to_gh: login_to_gh build_gh_release ## Logs into GitHub CLI and Releases
	@echo 'Released to Github'

release_to_github_via_docker_image:  ## Release to Github via docker
	@docker run --rm \
		-e GITHUB_GH_TOKEN=${GITHUB_GH_TOKEN} \
		${IMAGE_UTILS_NAME} make push_to_gh

########################################################
#		DEVOPS-ACCOUNTS

ondewo_release: spc clone_devops_accounts run_release_with_devops ## Release with credentials from devops-accounts repo
	@rm -rf ${DEVOPS_ACCOUNT_GIT}

clone_devops_accounts: ## Clones devops-accounts repo
	if [ -d $(DEVOPS_ACCOUNT_GIT) ]; then rm -Rf $(DEVOPS_ACCOUNT_GIT); fi
	git clone git@bitbucket.org:ondewo/${DEVOPS_ACCOUNT_GIT}.git

run_release_with_devops:
	$(eval info:= $(shell cat ${DEVOPS_ACCOUNT_DIR}/account_github.env | grep GITHUB_GH & cat ${DEVOPS_ACCOUNT_DIR}/account_pypi.env | grep PYPI_USERNAME & cat ${DEVOPS_ACCOUNT_DIR}/account_pypi.env | grep PYPI_PASSWORD))
	@make release $(info)

spc: ## Checks if the Release Branch, Tag and Pypi version already exist
	$(eval filtered_branches:= $(shell git branch --all | grep "release/${ONDEWO_VTSI_VERSION}"))
	$(eval filtered_tags:= $(shell git tag --list | grep "${ONDEWO_VTSI_VERSION}"))
	$(eval setuppy_version:= $(shell cat setup.py | grep "version"))
	@if test "$(filtered_branches)" != ""; then echo "-- Test 1: Branch exists!!" & exit 1; else echo "-- Test 1: Branch is fine";fi
	@if test "$(filtered_tags)" != ""; then echo "-- Test 2: Tag exists!!" & exit 1; else echo "-- Test 2: Tag is fine";fi
	#	@if test "$(setuppy_version)" != "version='${ONDEWO_VTSI_VERSION}',"; then echo "-- Test 3: Setup.py not updated!!" & exit 1; else echo "-- Test 3: Setup.py is fine";fi

########################################################
#		DEVELOPMENT-AUTOMATION
fetch_build_commit_push_new_vtsi_api:
	-git -C ondewo-vtsi-api fetch --all
	-git -C ondewo-vtsi-api pull
	make build
	git add Makefile
	git add pyproject.toml uv.lock
	git add ondewo/nlu
	git add ondewo/qa
	git add ondewo/s2t
	git add ondewo/sip
	git add ondewo/t2s
	git add ondewo/vtsi
	git add ondewo-vtsi-api
	# message="$$(git --no-pager -C ondewo-vtsi-api log -3 --pretty=%B | tail -3 | tr -d '[:space:]')"; git commit -m "$$message"
	git commit -m "Generated new vtsi python library files"
	git push

# execute in conda environment
update_vtsi_python_client_in_vtsi_and_install_master_version: fetch_build_commit_push_new_vtsi_api
	-cd ~/ondewo/ondewo-vtsi && yes | pip uninstall ondewo-vtsi-client
	-cd ~/ondewo/ondewo-vtsi && yes | pip install git+https://github.com/ondewo/ondewo-vtsi-client-python.git@master#egg=ondewo-vtsi-client
