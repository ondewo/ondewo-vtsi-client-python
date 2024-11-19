# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ondewo/nlu/ccai_project.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from ondewo.nlu import common_pb2 as ondewo_dot_nlu_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'ondewo/nlu/ccai_project.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dondewo/nlu/ccai_project.proto\x12\nondewo.nlu\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17ondewo/nlu/common.proto\"\xc3\x03\n\x0b\x43\x63\x61iProject\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x12\n\nowner_name\x18\x03 \x01(\t\x12G\n\x11\x63\x63\x61i_services_map\x18\x04 \x03(\x0b\x32,.ondewo.nlu.CcaiProject.CcaiServicesMapEntry\x12:\n\x13\x63\x63\x61i_project_status\x18\x05 \x01(\x0e\x32\x1d.ondewo.nlu.CcaiProjectStatus\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bmodified_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x08 \x01(\t\x12\x13\n\x0bmodified_by\x18\t \x01(\t\x12\x18\n\x10nlu_project_name\x18\n \x01(\t\x1aS\n\x14\x43\x63\x61iServicesMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.ondewo.nlu.CcaiServiceList:\x02\x38\x01\"A\n\x0f\x43\x63\x61iServiceList\x12.\n\rccai_services\x18\x01 \x03(\x0b\x32\x17.ondewo.nlu.CcaiService\"\x9b\x06\n\x0b\x43\x63\x61iService\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x12\x11\n\tgrpc_host\x18\x04 \x01(\t\x12\x11\n\tgrpc_port\x18\x05 \x01(\x05\x12\x14\n\x0cwebgrpc_host\x18\x06 \x01(\t\x12\x14\n\x0cwebgrpc_port\x18\x07 \x01(\x05\x12\x11\n\tgrpc_cert\x18\x08 \x01(\t\x12\x0c\n\x04host\x18\t \x01(\t\x12\x0c\n\x04port\x18\n \x01(\x05\x12\r\n\x05port2\x18\x0b \x01(\x05\x12\x1d\n\x15http_basic_auth_token\x18\x0c \x01(\t\x12\x14\n\x0c\x61\x63\x63ount_name\x18\r \x01(\t\x12\x18\n\x10\x61\x63\x63ount_password\x18\x0e \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x0f \x01(\t\x12\x36\n\x11\x63\x63\x61i_service_type\x18\x10 \x01(\x0e\x32\x1b.ondewo.nlu.CcaiServiceType\x12\x19\n\x11\x63\x63\x61i_project_name\x18\x11 \x01(\t\x12\x34\n\x13\x63\x63\x61i_service_config\x18\x12 \x01(\x0b\x32\x17.google.protobuf.Struct\x12.\n\ncreated_at\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bmodified_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x15 \x01(\t\x12\x13\n\x0bmodified_by\x18\x16 \x01(\t\x12-\n\x07headers\x18\x17 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x88\x01\x01\x12\x43\n\x15\x63\x63\x61i_service_provider\x18\x18 \x01(\x0e\x32\x1f.ondewo.nlu.CcaiServiceProviderH\x01\x88\x01\x01\x12\x1e\n\x11service_hierarchy\x18\x19 \x01(\tH\x02\x88\x01\x01\x42\n\n\x08_headersB\x18\n\x16_ccai_service_providerB\x14\n\x12_service_hierarchy\"c\n\x18\x43reateCcaiProjectRequest\x12-\n\x0c\x63\x63\x61i_project\x18\x01 \x01(\x0b\x32\x17.ondewo.nlu.CcaiProject\x12\x18\n\x10nlu_project_name\x18\x04 \x01(\t\"a\n\x19\x43reateCcaiProjectResponse\x12-\n\x0c\x63\x63\x61i_project\x18\x01 \x01(\x0b\x32\x17.ondewo.nlu.CcaiProject\x12\x15\n\rerror_message\x18\x02 \x01(\t\"\xeb\x01\n\x15GetCcaiProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12;\n\x11\x63\x63\x61i_project_view\x18\x02 \x01(\x0e\x32\x1b.ondewo.nlu.CcaiProjectViewH\x00\x88\x01\x01\x12?\n\x13\x63\x63\x61i_service_filter\x18\x03 \x01(\x0b\x32\x1d.ondewo.nlu.CcaiServiceFilterH\x01\x88\x01\x01\x12\x18\n\x10nlu_project_name\x18\x04 \x01(\tB\x14\n\x12_ccai_project_viewB\x16\n\x14_ccai_service_filter\"?\n\x15GetCcaiServiceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10nlu_project_name\x18\x04 \x01(\t\"\xc8\x02\n\x17ListCcaiProjectsRequest\x12\x36\n\x11\x63\x63\x61i_project_view\x18\x01 \x01(\x0e\x32\x1b.ondewo.nlu.CcaiProjectView\x12?\n\x13\x63\x63\x61i_service_filter\x18\x02 \x01(\x0b\x32\x1d.ondewo.nlu.CcaiServiceFilterH\x00\x88\x01\x01\x12\x41\n\x14\x63\x63\x61i_project_sorting\x18\x03 \x01(\x0b\x32\x1e.ondewo.nlu.CcaiProjectSortingH\x01\x88\x01\x01\x12\x17\n\npage_token\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x10nlu_project_name\x18\x05 \x01(\tB\x16\n\x14_ccai_service_filterB\x17\n\x15_ccai_project_sortingB\r\n\x0b_page_token\"c\n\x18ListCcaiProjectsResponse\x12.\n\rccai_projects\x18\x01 \x03(\x0b\x32\x17.ondewo.nlu.CcaiProject\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x8e\x03\n\x12\x43\x63\x61iProjectSorting\x12R\n\rsorting_field\x18\x01 \x01(\x0e\x32\x36.ondewo.nlu.CcaiProjectSorting.CcaiProjectSortingFieldH\x00\x88\x01\x01\x12\x32\n\x0csorting_mode\x18\x02 \x01(\x0e\x32\x17.ondewo.nlu.SortingModeH\x01\x88\x01\x01\"\xcc\x01\n\x17\x43\x63\x61iProjectSortingField\x12\x1b\n\x17NO_CCAI_PROJECT_SORTING\x10\x00\x12\x1d\n\x19SORT_CCAI_PROJECT_BY_NAME\x10\x01\x12%\n!SORT_CCAI_PROJECT_BY_DISPLAY_NAME\x10\x02\x12&\n\"SORT_CCAI_PROJECT_BY_CREATION_DATE\x10\x03\x12&\n\"SORT_CCAI_PROJECT_BY_LAST_MODIFIED\x10\x04\x42\x10\n\x0e_sorting_fieldB\x0f\n\r_sorting_mode\"d\n\x11\x43\x63\x61iServiceFilter\x12\x16\n\x0elanguage_codes\x18\x01 \x03(\t\x12\x37\n\x12\x63\x63\x61i_service_types\x18\x02 \x03(\x0e\x32\x1b.ondewo.nlu.CcaiServiceType\"\x82\x02\n\x18UpdateCcaiProjectRequest\x12-\n\x0c\x63\x63\x61i_project\x18\x01 \x01(\x0b\x32\x17.ondewo.nlu.CcaiProject\x12?\n\x13\x63\x63\x61i_service_filter\x18\x02 \x01(\x0b\x32\x1d.ondewo.nlu.CcaiServiceFilterH\x00\x88\x01\x01\x12\x34\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskH\x01\x88\x01\x01\x12\x18\n\x10nlu_project_name\x18\x04 \x01(\tB\x16\n\x14_ccai_service_filterB\x0e\n\x0c_update_mask\"@\n\x19UpdateCcaiProjectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\"B\n\x18\x44\x65leteCcaiProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10nlu_project_name\x18\x04 \x01(\t\"Z\n\x19\x44\x65leteCcaiProjectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x18\n\x10nlu_project_name\x18\x04 \x01(\t*\xab\x02\n\x11\x43\x63\x61iProjectStatus\x12#\n\x1f\x43\x43\x41I_PROJECT_STATUS_UNSPECIFIED\x10\x00\x12\"\n\x1e\x43\x43\x41I_PROJECT_STATUS_UNDEPLOYED\x10\x01\x12 \n\x1c\x43\x43\x41I_PROJECT_STATUS_UPDATING\x10\x02\x12!\n\x1d\x43\x43\x41I_PROJECT_STATUS_DEPLOYING\x10\x03\x12 \n\x1c\x43\x43\x41I_PROJECT_STATUS_DEPLOYED\x10\x04\x12#\n\x1f\x43\x43\x41I_PROJECT_STATUS_UNDEPLOYING\x10\x05\x12 \n\x1c\x43\x43\x41I_PROJECT_STATUS_DELETING\x10\x06\x12\x1f\n\x1b\x43\x43\x41I_PROJECT_STATUS_DELETED\x10\x07*\xba\x05\n\x0f\x43\x63\x61iServiceType\x12!\n\x1d\x43\x43\x41I_SERVICE_TYPE_UNSPECIFIED\x10\x00\x12 \n\x1c\x43\x43\x41I_SERVICE_TYPE_ONDEWO_AIM\x10\x01\x12 \n\x1c\x43\x43\x41I_SERVICE_TYPE_ONDEWO_BPI\x10\x02\x12 \n\x1c\x43\x43\x41I_SERVICE_TYPE_ONDEWO_CSI\x10\x03\x12 \n\x1c\x43\x43\x41I_SERVICE_TYPE_ONDEWO_NLU\x10\x04\x12 \n\x1c\x43\x43\x41I_SERVICE_TYPE_ONDEWO_S2T\x10\x05\x12 \n\x1c\x43\x43\x41I_SERVICE_TYPE_ONDEWO_SIP\x10\x06\x12 \n\x1c\x43\x43\x41I_SERVICE_TYPE_ONDEWO_T2S\x10\x07\x12!\n\x1d\x43\x43\x41I_SERVICE_TYPE_ONDEWO_VTSI\x10\x08\x12*\n&CCAI_SERVICE_TYPE_ONDEWO_VTSI_RABBITMQ\x10\t\x12#\n\x1f\x43\x43\x41I_SERVICE_TYPE_ONDEWO_NLU_QA\x10\n\x12(\n$CCAI_SERVICE_TYPE_ONDEWO_NLU_WEBHOOK\x10\x0b\x12#\n\x1f\x43\x43\x41I_SERVICE_TYPE_ONDEWO_SURVEY\x10\x0c\x12$\n CCAI_SERVICE_TYPE_ONDEWO_NLU_LLM\x10\r\x12*\n&CCAI_SERVICE_TYPE_ONDEWO_NLU_WEBSEARCH\x10\x0e\x12(\n$CCAI_SERVICE_TYPE_ONDEWO_AIM_WEBCHAT\x10\x0f\x12)\n%CCAI_SERVICE_TYPE_ONDEWO_AIM_WEBPHONE\x10\x10\x12,\n(CCAI_SERVICE_TYPE_ONDEWO_NLU_VECTORSTORE\x10\x11*\xb7\x06\n\x13\x43\x63\x61iServiceProvider\x12\x1c\n\x18NO_CCAI_SERVICE_PROVIDER\x10\x00\x12 \n\x1c\x43\x43\x41I_SERVICE_PROVIDER_ONDEWO\x10\x01\x12\'\n#CCAI_SERVICE_PROVIDER_GOOGLE_GEMINI\x10\x02\x12\x30\n,CCAI_SERVICE_PROVIDER_MICROSOFT_AZURE_OPENAI\x10\x03\x12+\n\'CCAI_SERVICE_PROVIDER_MICROSOFT_AUTOGEN\x10\x04\x12 \n\x1c\x43\x43\x41I_SERVICE_PROVIDER_OLLAMA\x10\x05\x12 \n\x1c\x43\x43\x41I_SERVICE_PROVIDER_OPENAI\x10\x06\x12#\n\x1f\x43\x43\x41I_SERVICE_PROVIDER_ANTHROPIC\x10\x07\x12%\n!CCAI_SERVICE_PROVIDER_HUGGINGFACE\x10\x08\x12\x1d\n\x19\x43\x43\x41I_SERVICE_PROVIDER_IBM\x10\t\x12\"\n\x1e\x43\x43\x41I_SERVICE_PROVIDER_HAYSTACK\x10\n\x12#\n\x1f\x43\x43\x41I_SERVICE_PROVIDER_LANGCHAIN\x10\x0b\x12 \n\x1c\x43\x43\x41I_SERVICE_PROVIDER_AMAZON\x10\x0c\x12!\n\x1d\x43\x43\x41I_SERVICE_PROVIDER_MISTRAL\x10\r\x12$\n CCAI_SERVICE_PROVIDER_DUCKDUCKGO\x10\x0e\x12$\n CCAI_SERVICE_PROVIDER_GOOGLE_PSE\x10\x0f\x12\x1e\n\x1a\x43\x43\x41I_SERVICE_PROVIDER_JINA\x10\x10\x12 \n\x1c\x43\x43\x41I_SERVICE_PROVIDER_TAVILY\x10\x11\x12\'\n#CCAI_SERVICE_PROVIDER_ELASTICSEARCH\x10\x12\x12 \n\x1c\x43\x43\x41I_SERVICE_PROVIDER_MILVUS\x10\x13\x12 \n\x1c\x43\x43\x41I_SERVICE_PROVIDER_QDRANT\x10\x14\x12 \n\x1c\x43\x43\x41I_SERVICE_PROVIDER_CHROMA\x10\x15*\x8e\x01\n\x0f\x43\x63\x61iProjectView\x12!\n\x1d\x43\x43\x41I_PROJECT_VIEW_UNSPECIFIED\x10\x00\x12\x1a\n\x16\x43\x43\x41I_PROJECT_VIEW_FULL\x10\x01\x12\x1d\n\x19\x43\x43\x41I_PROJECT_VIEW_SHALLOW\x10\x02\x12\x1d\n\x19\x43\x43\x41I_PROJECT_VIEW_MINIMUM\x10\x03\x32\xaf\x04\n\x0c\x43\x63\x61iProjects\x12L\n\x0eGetCcaiProject\x12!.ondewo.nlu.GetCcaiProjectRequest\x1a\x17.ondewo.nlu.CcaiProject\x12`\n\x11\x43reateCcaiProject\x12$.ondewo.nlu.CreateCcaiProjectRequest\x1a%.ondewo.nlu.CreateCcaiProjectResponse\x12`\n\x11\x44\x65leteCcaiProject\x12$.ondewo.nlu.DeleteCcaiProjectRequest\x1a%.ondewo.nlu.DeleteCcaiProjectResponse\x12]\n\x10ListCcaiProjects\x12#.ondewo.nlu.ListCcaiProjectsRequest\x1a$.ondewo.nlu.ListCcaiProjectsResponse\x12`\n\x11UpdateCcaiProject\x12$.ondewo.nlu.UpdateCcaiProjectRequest\x1a%.ondewo.nlu.UpdateCcaiProjectResponse\x12L\n\x0eGetCcaiService\x12!.ondewo.nlu.GetCcaiServiceRequest\x1a\x17.ondewo.nlu.CcaiServiceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ondewo.nlu.ccai_project_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CCAIPROJECT_CCAISERVICESMAPENTRY']._loaded_options = None
    _globals['_CCAIPROJECT_CCAISERVICESMAPENTRY']._serialized_options = b'8\001'
    _globals['_CCAIPROJECTSTATUS']._serialized_start = 3412
    _globals['_CCAIPROJECTSTATUS']._serialized_end = 3711
    _globals['_CCAISERVICETYPE']._serialized_start = 3714
    _globals['_CCAISERVICETYPE']._serialized_end = 4412
    _globals['_CCAISERVICEPROVIDER']._serialized_start = 4415
    _globals['_CCAISERVICEPROVIDER']._serialized_end = 5238
    _globals['_CCAIPROJECTVIEW']._serialized_start = 5241
    _globals['_CCAIPROJECTVIEW']._serialized_end = 5383
    _globals['_CCAIPROJECT']._serialized_start = 168
    _globals['_CCAIPROJECT']._serialized_end = 619
    _globals['_CCAIPROJECT_CCAISERVICESMAPENTRY']._serialized_start = 536
    _globals['_CCAIPROJECT_CCAISERVICESMAPENTRY']._serialized_end = 619
    _globals['_CCAISERVICELIST']._serialized_start = 621
    _globals['_CCAISERVICELIST']._serialized_end = 686
    _globals['_CCAISERVICE']._serialized_start = 689
    _globals['_CCAISERVICE']._serialized_end = 1484
    _globals['_CREATECCAIPROJECTREQUEST']._serialized_start = 1486
    _globals['_CREATECCAIPROJECTREQUEST']._serialized_end = 1585
    _globals['_CREATECCAIPROJECTRESPONSE']._serialized_start = 1587
    _globals['_CREATECCAIPROJECTRESPONSE']._serialized_end = 1684
    _globals['_GETCCAIPROJECTREQUEST']._serialized_start = 1687
    _globals['_GETCCAIPROJECTREQUEST']._serialized_end = 1922
    _globals['_GETCCAISERVICEREQUEST']._serialized_start = 1924
    _globals['_GETCCAISERVICEREQUEST']._serialized_end = 1987
    _globals['_LISTCCAIPROJECTSREQUEST']._serialized_start = 1990
    _globals['_LISTCCAIPROJECTSREQUEST']._serialized_end = 2318
    _globals['_LISTCCAIPROJECTSRESPONSE']._serialized_start = 2320
    _globals['_LISTCCAIPROJECTSRESPONSE']._serialized_end = 2419
    _globals['_CCAIPROJECTSORTING']._serialized_start = 2422
    _globals['_CCAIPROJECTSORTING']._serialized_end = 2820
    _globals['_CCAIPROJECTSORTING_CCAIPROJECTSORTINGFIELD']._serialized_start = 2581
    _globals['_CCAIPROJECTSORTING_CCAIPROJECTSORTINGFIELD']._serialized_end = 2785
    _globals['_CCAISERVICEFILTER']._serialized_start = 2822
    _globals['_CCAISERVICEFILTER']._serialized_end = 2922
    _globals['_UPDATECCAIPROJECTREQUEST']._serialized_start = 2925
    _globals['_UPDATECCAIPROJECTREQUEST']._serialized_end = 3183
    _globals['_UPDATECCAIPROJECTRESPONSE']._serialized_start = 3185
    _globals['_UPDATECCAIPROJECTRESPONSE']._serialized_end = 3249
    _globals['_DELETECCAIPROJECTREQUEST']._serialized_start = 3251
    _globals['_DELETECCAIPROJECTREQUEST']._serialized_end = 3317
    _globals['_DELETECCAIPROJECTRESPONSE']._serialized_start = 3319
    _globals['_DELETECCAIPROJECTRESPONSE']._serialized_end = 3409
    _globals['_CCAIPROJECTS']._serialized_start = 5386
    _globals['_CCAIPROJECTS']._serialized_end = 5945
# @@protoc_insertion_point(module_scope)
