# No bare `export`: the release credentials reach a process only through the environment of the
# steps that use them (see `release` and WITHOUT_CREDENTIALS), never pytest, pre-commit hooks or uv.
# ---------------- BEFORE RELEASE ----------------
# 1 - Update Version Number
# 2 - Update RELEASE.md
# 3 - make update_setup
# -------------- Release Process Steps (`make ondewo_release`) --------------
# 1 - spc: version not yet on origin or PyPI, RELEASE.md documents it (read-only)
# 2 - Load the credentials from devops-accounts and DELETE that clone before anything runs
# 3 - release_preflight: credentials valid, host tools present (read-only)
# 4 - Build, pre-commit, check_build and the full test suite
# 5 - Local commit, PyPI upload, wait until PyPI serves the version
# 6 - Push, release branch, release tag, GitHub release
# 7 - release_verify: tag on origin, non-empty GitHub release body, PyPI serves the version

########################################################
# 		Variables
########################################################

# MUST BE THE SAME AS API in Mayor and Minor Version Number
# example: API 2.9.0 --> Client 2.9.X
ONDEWO_VTSI_VERSION=9.1.0
# The version as an anchored-regex fragment (dots escaped), for every heading / version match below.
ONDEWO_VTSI_VERSION_RE=$(subst .,\.,${ONDEWO_VTSI_VERSION})
PYPI_PACKAGE=ondewo-vtsi-client

# The credentials have NO defaults: GITHUB_GH_TOKEN (push access to this repository), PYPI_USERNAME and
# PYPI_PASSWORD come from the environment, normally loaded by `ondewo_release` from devops-accounts.
# A placeholder default would only move the failure from `release_preflight` to the middle of the release.

# Prefix of every release step that needs no credential: it runs with the credentials removed from its
# environment, so pytest, pre-commit hooks, uv and the proto-compiler containers never see them.
WITHOUT_CREDENTIALS=env -u GITHUB_GH_TOKEN -u GH_TOKEN -u PYPI_USERNAME -u PYPI_PASSWORD

# How long `verify_pypi` waits for PyPI to serve a freshly uploaded version.
RELEASE_VERIFY_ATTEMPTS?=20
RELEASE_VERIFY_INTERVAL_S?=30

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
# The heading is ANCHORED at both ends with the dots escaped, exactly like the generator's own
# `grep -qE "^#+ Release ONDEWO VTSI Python Client <version>$$"`: unanchored, releasing 9.1.1 would
# also open the slice on a `9.1.10` heading. `\#` because a bare `#` starts a make comment.
#
# Keep the version reference and the `=` on SEPARATE lines: older generators rewrote, wholesale, any
# line that names ONDEWO_VTSI_VERSION and also carries an equals sign.
CURRENT_RELEASE_NOTES=`cat RELEASE.md \
	| perl -ne 'print if /^\#+ Release ONDEWO VTSI Python Client ${ONDEWO_VTSI_VERSION_RE}$$/../^\*{5}/'`

GH_REPO="https://github.com/ondewo/ondewo-vtsi-client-python"
GH_REPO_NAME=ondewo/ondewo-vtsi-client-python
DEVOPS_ACCOUNT_GIT=ondewo-devops-accounts
ONDEWO_VTSI_API_GIT_BRANCH=tags/9.1.0
ONDEWO_PROTO_COMPILER_GIT_BRANCH=tags/5.15.7
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

setup_developer_environment_locally: install_precommit_hooks install_dev_environment

install_precommit_hooks: ## Installs pre-commit hooks and sets them up for the ondewo-csi-client repo
	-pip install pre-commit
	pre-commit install
	pre-commit install --hook-type commit-msg

# The release runs in a FRESH clone (ondewo-vtsi-api's `release_client`), which has no .venv. The mypy hook is
# `uv run --no-sync mypy`, so without this target uv created an EMPTY .venv on whatever interpreter it found
# (CPython 3.14 on the release host) and the hook died with `Failed to spawn: mypy`. Same sync as the CI workflow.
install_dev_environment: ## Creates/updates the project .venv from uv.lock (runtime + dev extra, Python 3.12)
	uv sync --extra dev --frozen --python 3.12

precommit_hooks_run_all_files: install_dev_environment ## Runs all pre-commit hooks on all files and not just the changed ones
	uv run --no-sync pre-commit run --all-files

# Exactly the CI workflow's checks. `release` runs this BEFORE it commits, branches, tags or publishes anything.
test: install_dev_environment ## Runs ruff, mypy and the unit suite with the coverage gate, as the CI workflow does
	uv run --no-sync ruff check .
	uv run --no-sync mypy ondewo
	uv run --no-sync pytest tests/unit -q \
		--cov=ondewo.vtsi.client.utils.keycloak \
		--cov=ondewo.vtsi.client.client_config \
		--cov=ondewo.vtsi.client.services_interface \
		--cov=ondewo.vtsi.client.async_services_interface \
		--cov-report=term-missing \
		--cov-fail-under=100

# ruff replaced flake8 (config: [tool.ruff] in pyproject.toml) and mypy reads [tool.mypy] in pyproject.toml; there
# is no .flake8 and no mypy.ini. Both run through the project .venv (uv sync --extra dev), as the CI workflow does.
ruff: ## Runs ruff lint + format check (the flake8 replacement)
	uv run --no-sync ruff check .
	uv run --no-sync ruff format --check .

flake8: ruff ## Alias of ruff, kept for muscle memory: flake8 itself is no longer installed

mypy: ## Run mypy static code checking
	@echo "---------------------------------------------"
	@echo "START: Run mypy in pre-commit hook (tests, examples) ..."
	uv run --no-sync pre-commit run mypy --all-files
	@echo "DONE: Run mypy in pre-commit hook."
	@echo "---------------------------------------------"
	@echo "START: Run mypy on the package, as the CI workflow does ..."
	uv run --no-sync mypy --config-file=pyproject.toml ondewo
	@echo "DONE: Run mypy on the package"
	@echo "---------------------------------------------"

help: ## Print usage info about help targets
	# (first comment after target starting with double hashes ##)
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

makefile_chapters: ## Shows all sections of Makefile
	@echo `cat Makefile| grep "########################################################" -A 1 | grep -v "########################################################"`

TEST:
	@echo "GH Token: \t $(if $(GITHUB_GH_TOKEN),<set>,<unset>)"
	@echo "PyPI User: \t $(if $(PYPI_USERNAME),<set>,<unset>)"
	@echo "PyPI Password: \t $(if $(PYPI_PASSWORD),<set>,<unset>)"
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
		if test $$? != 0; then  echo "No Proto-Code for $${file}"; exit 1;fi \
	done
	@rm -rf build_check.txt

########################################################
#       Repo Specific Make Targets
########################################################
#		Build

update_setup: ## Update Version in pyproject.toml
	@perl -i -pe 's/^version = "\d+\.\d+\.\d+"/version = "${ONDEWO_VTSI_VERSION}"/' pyproject.toml

build: clear_package_data prepare_submodules build_compiler generate_all_protos create_async_services update_setup ## Build source code

push_to_pypi_via_docker: build_utils_docker_image push_to_pypi_via_docker_image  ## Release automation for building and pushing to pypi via a docker image

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

# The ORDER is the release contract shared by every ondewo-vtsi-client-<lang> repository, and
# tests/unit/test_release_runs_in_a_fresh_clone.py pins it: nothing is committed, published, pushed or tagged
# before the preflight and the full test suite passed, and PyPI (the one step that cannot be undone) is
# published and verified BEFORE anything reaches origin. Plain `make`, not `$(MAKE)`, so `make -n release`
# prints the steps instead of running the sub-makes.
release: ## Automate the entire release process (see README "Release")
	@echo "Start Release"
	make release_preflight
	${WITHOUT_CREDENTIALS} make build
	${WITHOUT_CREDENTIALS} make precommit_hooks_run_all_files
	git status
	${WITHOUT_CREDENTIALS} make check_build
	${WITHOUT_CREDENTIALS} make test
	git add ondewo
	git add Makefile
	git add RELEASE.md
	git add pyproject.toml uv.lock
	git add ${ONDEWO_PROTO_COMPILER_DIR}
	git add ${ONDEWO_VTSI_API_DIR}
	git status
	git diff --cached --quiet || ${WITHOUT_CREDENTIALS} git commit --no-verify -m "PREPARING FOR RELEASE ${ONDEWO_VTSI_VERSION}"
	make push_to_pypi_via_docker
	make verify_pypi
	${WITHOUT_CREDENTIALS} git push
	${WITHOUT_CREDENTIALS} make create_release_branch
	${WITHOUT_CREDENTIALS} make create_release_tag
	make release_to_github_via_docker
	make release_verify
	@echo "Release Finished"

# Read-only: nothing is committed, pushed, tagged or uploaded. It builds the local utils image, because gh and
# twine run in it. `spc` repeats here so a direct `make release` is guarded as well as `make ondewo_release`.
release_preflight: check_host_tools spc build_utils_docker_image check_github_credentials check_pypi_credentials ## Read-only: fails before the release builds, commits or pushes anything
	@echo "release_preflight: OK for ${PYPI_PACKAGE} ${ONDEWO_VTSI_VERSION}"

# The host needs only these. gh and twine run in the pinned utils image (Dockerfile.utils); uv runs the
# build, the pre-commit hooks and the tests from uv.lock.
check_host_tools: ## Fails unless the tools the release runs on the host are installed
	@for tool in docker git make perl curl uv; do \
		command -v $$tool >/dev/null 2>&1 || { echo "release_preflight: '$$tool' is not installed on this host"; exit 1; }; \
	done
	@docker info >/dev/null 2>&1 || { echo "release_preflight: the docker daemon is not reachable"; exit 1; }

# Proves the token is valid AND may push here; `gh` reads it from GH_TOKEN, so nothing is stored in
# ~/.config/gh and the value is never on an argv.
check_github_credentials: ## Fails unless GITHUB_GH_TOKEN has push permission on this repository
	@test -n "$${GITHUB_GH_TOKEN}" || { echo "release_preflight: GITHUB_GH_TOKEN is not set"; exit 1; }
	@push=$$(GH_TOKEN="$${GITHUB_GH_TOKEN}" docker run --rm -e GH_TOKEN ${IMAGE_UTILS_NAME} \
		gh api repos/${GH_REPO_NAME} --jq .permissions.push); \
	test "$$push" = true || { echo "release_preflight: GITHUB_GH_TOKEN cannot push to ${GH_REPO_NAME} (permissions.push='$$push')"; exit 1; }
	@echo "release_preflight: GITHUB_GH_TOKEN may push to ${GH_REPO_NAME}"

# PyPI offers no read-only "whoami". The cheapest REAL probe is an upload PyPI is guaranteed to refuse to
# publish: the newest file ALREADY on PyPI, downloaded from PyPI a second earlier and sent again. PyPI checks the
# credential and the upload permission on this project FIRST and answers 403 when either fails; only then does it
# see the file exists and answer 400 "File already exists" (or 200 for a byte-identical file). So a pass proves
# the credential authenticates AND may upload to ${PYPI_PACKAGE}, and nothing new can be published.
# NOT `twine upload --skip-existing`: twine then asks the index whether the file exists and skips WITHOUT
# contacting the upload endpoint, so a bogus token passes (measured).
check_pypi_credentials: ## Fails unless PYPI_USERNAME/PYPI_PASSWORD may upload to the PyPI project
	@test -n "$${PYPI_USERNAME}" && test -n "$${PYPI_PASSWORD}" || { echo "release_preflight: PYPI_USERNAME / PYPI_PASSWORD are not set"; exit 1; }
	@docker run --rm -e PYPI_USERNAME -e PYPI_PASSWORD -e COLUMNS=1000 ${IMAGE_UTILS_NAME} make probe_pypi_upload_permission \
		|| { echo "release_preflight: PyPI refused PYPI_USERNAME / PYPI_PASSWORD for ${PYPI_PACKAGE}"; exit 1; }
	@echo "release_preflight: PyPI accepts the credentials for ${PYPI_PACKAGE}"

# Runs INSIDE the utils image (see check_pypi_credentials). COLUMNS keeps twine's message on one line.
probe_pypi_upload_permission:
	@url=$$(curl -fsS https://pypi.org/pypi/${PYPI_PACKAGE}/json \
		| python3 -c 'import json, sys; print(next(u["url"] for u in json.load(sys.stdin)["urls"] if u["packagetype"] == "sdist"))') \
		&& mkdir -p /tmp/pypi-probe \
		&& curl -fsSL -o "/tmp/pypi-probe/$${url##*/}" "$$url" \
		&& { out=$$(TWINE_USERNAME="$${PYPI_USERNAME}" TWINE_PASSWORD="$${PYPI_PASSWORD}" \
			twine upload --non-interactive --disable-progress-bar -r pypi /tmp/pypi-probe/* 2>&1); status=$$?; \
			printf '%s\n' "$$out"; \
			test $$status -eq 0 || printf '%s' "$$out" | grep -q 'File already exists'; }

check_release_notes: ## Fails unless RELEASE.md documents ONDEWO_VTSI_VERSION exactly once, with a non-empty body
	@test "$$(grep -cE '^#+ Release ONDEWO VTSI Python Client ${ONDEWO_VTSI_VERSION_RE}$$' RELEASE.md)" = 1 \
		|| { echo "RELEASE.md must carry exactly one '## Release ONDEWO VTSI Python Client ${ONDEWO_VTSI_VERSION}' heading"; exit 1; }
	@test -n "$$(printf '%s\n' "${CURRENT_RELEASE_NOTES}" | perl -ne 'print unless /^#+ Release / || /^\*{5}/' | tr -d '[:space:]')" \
		|| { echo "RELEASE.md has no release notes under its ${ONDEWO_VTSI_VERSION} heading"; exit 1; }
	@echo "RELEASE.md documents ${ONDEWO_VTSI_VERSION}"

# Read-only, after publishing; ondewo-vtsi-api's driver runs it to decide whether a client is released.
release_verify: verify_tag verify_github_release verify_pypi ## Read-only: fails unless the tag, the GitHub release notes and the PyPI version all exist
	@echo "release_verify: ${PYPI_PACKAGE} ${ONDEWO_VTSI_VERSION} is released"

verify_tag:
	@git ls-remote --exit-code origin "refs/tags/${ONDEWO_VTSI_VERSION}" >/dev/null \
		|| { echo "release_verify: tag ${ONDEWO_VTSI_VERSION} is not on origin"; exit 1; }

verify_github_release: build_utils_docker_image
	@body=$$(GH_TOKEN="$${GITHUB_GH_TOKEN}" docker run --rm -e GH_TOKEN ${IMAGE_UTILS_NAME} \
		gh release view "${ONDEWO_VTSI_VERSION}" --repo ${GH_REPO_NAME} --json body --jq .body); \
	test -n "$$(printf '%s' "$$body" | tr -d '[:space:]')" \
		|| { echo "release_verify: the GitHub release ${ONDEWO_VTSI_VERSION} is missing or has an empty body"; exit 1; }

# The PyPI JSON API lags an upload by seconds to minutes; poll instead of failing on the first miss.
verify_pypi: ## Polls the PyPI JSON API until it serves ONDEWO_VTSI_VERSION with at least one file
	@for attempt in $$(seq 1 ${RELEASE_VERIFY_ATTEMPTS}); do \
		served=$$(curl -fsS "https://pypi.org/pypi/${PYPI_PACKAGE}/${ONDEWO_VTSI_VERSION}/json" 2>/dev/null \
			| perl -MJSON::PP -0777 -ne 'my $$d = decode_json($$_); print $$d->{info}{version} if @{$$d->{urls}}'); \
		if [ "$$served" = "${ONDEWO_VTSI_VERSION}" ]; then echo "PyPI serves ${PYPI_PACKAGE} ${ONDEWO_VTSI_VERSION}"; exit 0; fi; \
		echo "PyPI does not serve ${PYPI_PACKAGE} ${ONDEWO_VTSI_VERSION} yet (attempt $$attempt/${RELEASE_VERIFY_ATTEMPTS})"; \
		sleep ${RELEASE_VERIFY_INTERVAL_S}; \
	done; \
	echo "release_verify: PyPI does not serve ${PYPI_PACKAGE} ${ONDEWO_VTSI_VERSION}"; exit 1

create_release_branch: ## Create Release Branch and push it to origin
	git checkout -b "release/${ONDEWO_VTSI_VERSION}"
	git push -u origin "release/${ONDEWO_VTSI_VERSION}"

create_release_tag: ## Create Release Tag and push it to origin
	git tag -a ${ONDEWO_VTSI_VERSION} -m "release/${ONDEWO_VTSI_VERSION}"
	git push origin ${ONDEWO_VTSI_VERSION}

# `--verify-tag` refuses to create a tag gh would otherwise invent; check_release_notes refuses an empty body
# (`gh release create -n ""` succeeds and publishes a release without notes).
build_gh_release: check_release_notes ## Generate Github Release with CLI (reads GH_TOKEN)
	gh release create --repo $(GH_REPO) "$(ONDEWO_VTSI_VERSION)" --verify-tag -n "$(CURRENT_RELEASE_NOTES)" -t "Release ${ONDEWO_VTSI_VERSION}"

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

# twine reads TWINE_USERNAME / TWINE_PASSWORD from the environment; `-u` / `-p` would put the
# credentials on its argv, which /proc/<pid>/cmdline shows to every user on the host.
upload_package:
	@TWINE_USERNAME="$${PYPI_USERNAME}" TWINE_PASSWORD="$${PYPI_PASSWORD}" twine upload --verbose -r pypi dist/*

clear_package_data: ## Clears PYPI Package
	echo "Waiting 5s so directory for removal is not busy anymore"
	sleep 5s
	-rm -rf build dist/* ondewo_vtsi_client.egg-info

push_to_pypi_via_docker_image:  ## Push source code to pypi via docker
	[ -d $(OUTPUT_DIR) ] || mkdir -p $(OUTPUT_DIR)
	@docker run --rm \
		-v ${shell pwd}/dist:/home/ondewo/dist \
		-e PYPI_USERNAME \
		-e PYPI_PASSWORD \
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
		-e PYPI_USERNAME \
		-e PYPI_PASSWORD \
		${IMAGE_UTILS_NAME} make show_pypi
	rm -rf dist

########################################################
#		GITHUB

push_to_gh: build_gh_release ## Creates the GitHub release (gh reads GH_TOKEN; nothing is stored in ~/.config/gh)
	@echo 'Released to Github'

# "$${GITHUB_GH_TOKEN}" is expanded by the shell from the environment and handed to gh as GH_TOKEN by name.
# $(GITHUB_GH_TOKEN) would be expanded by make INTO the recipe line, i.e. onto the argv of `/bin/sh -c`.
release_to_github_via_docker_image:  ## Release to Github via docker
	@GH_TOKEN="$${GITHUB_GH_TOKEN}" docker run --rm \
		-e GH_TOKEN \
		${IMAGE_UTILS_NAME} make push_to_gh

########################################################
#		DEVOPS-ACCOUNTS

# The credentials are loaded into the ENVIRONMENT of `make release` (`make release NAME=<value>` would put every
# value on make's argv, which /proc/<pid>/cmdline shows to every user on the host), and the devops-accounts clone
# is DELETED before `make release` starts - also when the clone, the load or the release fails (trap). The clone
# lives in a mktemp directory, never in this repository, so no `docker build .` context or mount can contain it.
# DEVOPS_ACCOUNT_DIR: an existing clone to use instead (ondewo-vtsi-api's driver clones once for all clients and
# deletes it itself). Plain `make release`, not `$(MAKE)`, so `make -n ondewo_release` clones nothing.
ondewo_release: spc ## Release with credentials from devops-accounts repo (DEVOPS_ACCOUNT_DIR reuses a clone)
	@rm -rf ./${DEVOPS_ACCOUNT_GIT}
	@set -e; \
	owned=""; \
	trap 'if [ -n "$$owned" ]; then rm -rf "$$owned"; fi' EXIT; \
	trap 'exit 130' INT TERM; \
	if [ -n "$${DEVOPS_ACCOUNT_DIR:-}" ] && [ -d "$${DEVOPS_ACCOUNT_DIR}" ]; then \
		accounts="$${DEVOPS_ACCOUNT_DIR}"; \
	else \
		owned="$$(mktemp -d)"; \
		accounts="$$owned/${DEVOPS_ACCOUNT_GIT}"; \
		git clone -q --depth 1 git@bitbucket.org:ondewo/${DEVOPS_ACCOUNT_GIT}.git "$$accounts"; \
	fi; \
	set -a; \
	eval "$$(grep -h -E '^(GITHUB_GH_TOKEN|PYPI_USERNAME|PYPI_PASSWORD)=' \
		"$$accounts/account_github.env" "$$accounts/account_pypi.env")"; \
	set +a; \
	if [ -n "$$owned" ]; then rm -rf "$$owned"; owned=""; fi; \
	make release

# Read-only and credential-free, so `ondewo_release` runs it before it loads any credential.
spc: check_release_notes ## Checks that release/<version>, tag <version> and the PyPI version do not exist yet
	@git ls-remote --exit-code origin "refs/heads/release/${ONDEWO_VTSI_VERSION}" >/dev/null; status=$$?; \
	case $$status in \
		2) echo "-- Test 1: Branch is fine";; \
		0) echo "-- Test 1: branch release/${ONDEWO_VTSI_VERSION} already exists on origin"; exit 1;; \
		*) echo "-- Test 1: cannot list the branches of origin (git ls-remote exit $$status)"; exit 1;; \
	esac
	@git ls-remote --exit-code origin "refs/tags/${ONDEWO_VTSI_VERSION}" >/dev/null; status=$$?; \
	case $$status in \
		2) echo "-- Test 2: Tag is fine";; \
		0) echo "-- Test 2: tag ${ONDEWO_VTSI_VERSION} already exists on origin"; exit 1;; \
		*) echo "-- Test 2: cannot list the tags of origin (git ls-remote exit $$status)"; exit 1;; \
	esac
	@code=$$(curl -s -o /dev/null -w '%{http_code}' "https://pypi.org/pypi/${PYPI_PACKAGE}/${ONDEWO_VTSI_VERSION}/json"); \
	case $$code in \
		404) echo "-- Test 3: PyPI version is fine";; \
		200) echo "-- Test 3: ${PYPI_PACKAGE} ${ONDEWO_VTSI_VERSION} is already on PyPI"; exit 1;; \
		*) echo "-- Test 3: cannot ask PyPI for ${PYPI_PACKAGE} ${ONDEWO_VTSI_VERSION} (HTTP $$code)"; exit 1;; \
	esac

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
