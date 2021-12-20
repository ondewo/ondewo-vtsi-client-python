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

install:
	git submodule update --init --recursive
	pip install -e .

# {{{ PROTOS
generate_all_protos: generate_ondewo_protos generate_google_protos
generate_google_protos:
	# generate google api files
	python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. ${GOOGLE_APIS_DIR}/google/api/annotations.proto
	python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. ${GOOGLE_APIS_DIR}/google/rpc/status.proto
	python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. ${GOOGLE_APIS_DIR}/google/type/latlng.proto
	python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. ${GOOGLE_APIS_DIR}/google/api/http.proto
	python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. ${GOOGLE_APIS_DIR}/google/longrunning/operations.proto

generate_ondewo_protos:
	for f in $$(find ${NLU_PROTOS_DIR} -name '*.proto'); do \
		python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} -I${NLU_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. $$f; \
	done

generate_specific_protos:
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
push_to_pypi: build_package upload_package clear_package_data
	echo 'pushed to pypi : )'

build_package:
	python setup.py sdist bdist_wheel

upload_package:
	twine upload -r pypi dist/*

clear_package_data:
	rm -rf build dist ondewo_vtsi_client_python.egg-info
# vim:foldmethod=marker:foldlevel=0
