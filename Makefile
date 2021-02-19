ONDEWO_APIS_DIR=ondewo-nlu-api
GOOGLE_APIS_DIR=ondewo-nlu-api/googleapis
CUSTOM_APIS_DIR=ondewo-vtsi-api/
GOOGLE_PROTOS_DIR=ondewo-nlu-api/googleapis/google/
ONDEWO_PROTOS_DIR=ondewo-nlu-api/ondewo/
CUSTOM_PROTOS_DIR=ondewo-vtsi-api/

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
	for f in $$(find ${ONDEWO_PROTOS_DIR} -name '*.proto'); do \
		python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} -I${ONDEWO_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. $$f; \
	done

generate_specific_protos:
	for f in $$(find ${ONDEWO_PROTOS_DIR}nlu -name '*.proto'); do \
		python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} -I${ONDEWO_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. $$f; \
	done
	for f in $$(find ${CUSTOM_PROTOS_DIR} -name '*.proto'); do \
		python -m grpc_tools.protoc -I${GOOGLE_APIS_DIR} -I${ONDEWO_APIS_DIR} -I${CUSTOM_APIS_DIR} --python_out=. --mypy_out=. --grpc_python_out=. $$f; \
	done
# }}}
# vim:foldmethod=marker:foldlevel=0
