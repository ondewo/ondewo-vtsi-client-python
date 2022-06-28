ONDEWO_NLU_API_GIT_BRANCH=release/2.8.0
ONDEWO_S2T_API_GIT_BRANCH=3.1.1
ONDEWO_T2S_API_GIT_BRANCH=4.0.3
ONDEWO_SIP_API_GIT_BRANCH=release/1.2.0
ONDEWO_VTSI_API_GIT_BRANCH=new_vtsi_api
ONDEWO_PROTO_COMPILER_GIT_BRANCH=tags/2.0.0

# Submodule paths
ONDEWO_NLU_API_DIR=ondewo-nlu-api
ONDEWO_PROTO_COMPILER_DIR=ondewo-proto-compiler
ONDEWO_S2T_API_DIR=ondewo-s2t-api
ONDEWO_T2S_API_DIR=ondewo-t2s-api
ONDEWO_SIP_API_DIR=ondewo-sip-api
ONDEWO_VTSI_API_DIR=ondewo-vtsi-api


# Specify protos directories
GOOGLE_API_DIR=${ONDEWO_NLU_API_DIR}/googleapis
NLU_PROTOS_DIR=${ONDEWO_NLU_API_DIR}/ondewo/
GOOGLE_PROTOS_DIR=${GOOGLE_API_DIR}/google/
S2T_PROTOS_DIR=${ONDEWO_S2T_API_DIR}/ondewo/
T2S_PROTOS_DIR=${ONDEWO_T2S_API_DIR}/ondewo/
SIP_PROTOS_DIR=${ONDEWO_SIP_API_DIR}/ondewo/
VTSI_PROTOS_DIR=${ONDEWO_VTSI_API_DIR}/ondewo/

build: clear_package_data prepate_submodules build_compiler generate_all_protos

prepate_submodules: init_submodules checkout_defined_submodule_versions

init_submodules:
	git submodule update --init --recursive

install: init_submodules
	pip install -e .

checkout_defined_submodule_versions:
	@echo "START checking out submodules ..."
	git -C ${ONDEWO_NLU_API_DIR} fetch --all
	git -C ${ONDEWO_NLU_API_DIR} checkout ${ONDEWO_NLU_API_GIT_BRANCH}
	git -C ${ONDEWO_PROTO_COMPILER_DIR} fetch --all
	git -C ${ONDEWO_PROTO_COMPILER_DIR} checkout ${ONDEWO_PROTO_COMPILER_GIT_BRANCH}
	git -C ${ONDEWO_S2T_API_DIR} fetch --all
	git -C ${ONDEWO_S2T_API_DIR} checkout ${ONDEWO_S2T_API_GIT_BRANCH}
	git -C ${ONDEWO_T2S_API_DIR} fetch --all
	git -C ${ONDEWO_T2S_API_DIR} checkout ${ONDEWO_T2S_API_GIT_BRANCH}
	git -C ${ONDEWO_SIP_API_DIR} fetch --all
	git -C ${ONDEWO_SIP_API_DIR} checkout ${ONDEWO_SIP_API_GIT_BRANCH}
	git -C ${ONDEWO_VTSI_API_DIR} fetch --all
	git -C ${ONDEWO_VTSI_API_DIR} checkout ${ONDEWO_VTSI_API_GIT_BRANCH}
	@echo "DONE checking out submodules"

build_compiler:
	make -C ondewo-proto-compiler/python build

# {{{ PROTOS
generate_all_protos: generate_nlu_protos generate_s2t_protos generate_t2s_protos generate_sip_protos generate_vtsi_protos

generate_nlu_protos:
	make -f ondewo-proto-compiler/python/Makefile run \
		PROTO_DIR=${NLU_PROTOS_DIR} \
		EXTRA_PROTO_DIR=${GOOGLE_PROTOS_DIR} \
		TARGET_DIR='ondewo' \
		OUTPUT_DIR='.'

generate_s2t_protos:
	make -f ondewo-proto-compiler/python/Makefile run \
		PROTO_DIR=${S2T_PROTOS_DIR} \
		TARGET_DIR='ondewo' \
		OUTPUT_DIR='.'

generate_t2s_protos:
	make -f ondewo-proto-compiler/python/Makefile run \
		PROTO_DIR=${T2S_PROTOS_DIR} \
		TARGET_DIR='ondewo' \
		OUTPUT_DIR='.'

generate_sip_protos:
	make -f ondewo-proto-compiler/python/Makefile run \
		PROTO_DIR=${SIP_PROTOS_DIR} \
		TARGET_DIR='ondewo' \
		OUTPUT_DIR='.'

generate_vtsi_protos:
	make -f ondewo-proto-compiler/python/Makefile run \
		PROTO_DIR=${VTSI_PROTOS_DIR} \
		EXTRA_PROTO_DIR=${GOOGLE_PROTOS_DIR} \
		TARGET_DIR='ondewo' \
		OUTPUT_DIR='.'
# }}}

#VTSI proto Preparation{{{

copy_proto_files_all_submodules: copy_proto_files_for_google_api copy_proto_files_for_ondewo_nlu_api copy_proto_files_for_ondewo_s2t_api copy_proto_files_for_ondewo_t2s_api copy_proto_files_for_ondewo_sip_api

copy_proto_files_for_google_api:
	@echo "START copying googleapis protos from submodules to build folder ..."
	-mkdir -p ${ONDEWO_VTSI_API_DIR}/google/api
	-mkdir -p ${ONDEWO_VTSI_API_DIR}/google/longrunning
	-mkdir -p ${ONDEWO_VTSI_API_DIR}/google/rpc
	-mkdir -p ${ONDEWO_VTSI_API_DIR}/google/type
	cp ${GOOGLE_PROTOS_DIR}/api/annotations.proto ${ONDEWO_VTSI_API_DIR}/google/api/
	cp ${GOOGLE_PROTOS_DIR}/api/http.proto ${ONDEWO_VTSI_API_DIR}/google/api/
	cp ${GOOGLE_PROTOS_DIR}/type/latlng.proto ${ONDEWO_VTSI_API_DIR}/google/type/
	cp ${GOOGLE_PROTOS_DIR}/rpc/status.proto ${ONDEWO_VTSI_API_DIR}/google/rpc/
	cp ${GOOGLE_PROTOS_DIR}/longrunning/operations.proto ${ONDEWO_VTSI_API_DIR}/google/longrunning/
	@echo "DONE copying googleapis protos from submodules to build folder."

copy_proto_files_for_ondewo_nlu_api:
	@echo "START copying ondewo-nlu protos from submodules to build folder ..."
	-mkdir -p ${ONDEWO_VTSI_API_DIR}/ondewo/nlu/
	cp ${NLU_PROTOS_DIR}/nlu/context.proto ${ONDEWO_VTSI_API_DIR}/ondewo/nlu/
	@echo "DONE copying ondewo-nlu protos from submodules to build folder."

copy_proto_files_for_ondewo_s2t_api:
	@echo "START copying ondewo-s2t protos from submodules to build folder ..."
	-mkdir -p ${ONDEWO_VTSI_API_DIR}/ondewo/s2t/
	cp ${S2T_PROTOS_DIR}/s2t/speech-to-text.proto ${ONDEWO_VTSI_API_DIR}/ondewo/s2t/
	@echo "DONE copying ondewo-s2t protos from submodules to build folder."

copy_proto_files_for_ondewo_t2s_api:
	@echo "START copying ondewo-t2s protos from submodules to build folder ..."
	-mkdir -p ${ONDEWO_VTSI_API_DIR}/ondewo/t2s/
	cp ${T2S_PROTOS_DIR}/t2s/text-to-speech.proto ${ONDEWO_VTSI_API_DIR}/ondewo/t2s/
	@echo "DONE copying ondewo-t2s protos from submodules to build folder."

copy_proto_files_for_ondewo_sip_api:
	@echo "START copying ondewo-sip protos from submodules to build folder ..."
	-mkdir -p ${ONDEWO_VTSI_API_DIR}/ondewo/sip/
	cp ${SIP_PROTOS_DIR}/sip/sip.proto ${ONDEWO_VTSI_API_DIR}/ondewo/sip/
	@echo "DONE copying ondewo-sip protos from submodules to build folder."
#}}}

push_to_pypi: build_package upload_package clear_package_data
	echo 'pushed to pypi : )'

build_package:
	python setup.py sdist bdist_wheel

upload_package:
	twine upload -r pypi dist/*

clear_package_data:
	rm -rf build dist ondewo_vtsi_client_python.egg-info
