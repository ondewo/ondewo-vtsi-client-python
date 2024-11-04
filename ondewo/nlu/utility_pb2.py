# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ondewo/nlu/utility.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from ondewo.nlu import entity_type_pb2 as ondewo_dot_nlu_dot_entity__type__pb2
from ondewo.nlu import intent_pb2 as ondewo_dot_nlu_dot_intent__pb2
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
    'ondewo/nlu/utility.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18ondewo/nlu/utility.proto\x12\nondewo.nlu\x1a\x17ondewo/nlu/intent.proto\x1a\x1condewo/nlu/entity_type.proto\"%\n\x14ValidateRegexRequest\x12\r\n\x05regex\x18\x01 \x01(\t\"/\n\x15ValidateRegexResponse\x12\x16\n\x0e\x65rror_messages\x18\x01 \x03(\t\"R\n\x1cValidateEmbeddedRegexRequest\x12\x32\n\x0b\x65ntity_type\x18\x01 \x01(\x0b\x32\x1d.ondewo.nlu.EntityType.Entity\"7\n\x1dValidateEmbeddedRegexResponse\x12\x16\n\x0e\x65rror_messages\x18\x01 \x03(\t\"\xc4\x02\n\x16\x43leanAllIntentsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x1a\n\x12special_characters\x18\x03 \x01(\t\x12\x1c\n\x14substring_white_list\x18\x04 \x03(\t\x12\x0f\n\x07\x64ry_run\x18\x05 \x01(\x08\x12Q\n\x1ftraining_phrase_cleaner_options\x18\x06 \x01(\x0b\x32(.ondewo.nlu.TrainingPhraseCleanerOptions\x12J\n\x1breannotate_entities_options\x18\x07 \x01(\x0e\x32%.ondewo.nlu.ReannotateEntitiesOptions\x12\x19\n\x11number_of_workers\x18\x08 \x01(\x05\"|\n\x17\x43leanAllIntentsResponse\x12+\n\x0f\x63leaned_intents\x18\x01 \x03(\x0b\x32\x12.ondewo.nlu.Intent\x12\x34\n\x12intent_update_list\x18\x02 \x03(\x0b\x32\x18.ondewo.nlu.IntentUpdate\"\xba\x02\n\x12\x43leanIntentRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x13\n\x0bintent_name\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x12\x1a\n\x12special_characters\x18\x04 \x01(\t\x12\x1c\n\x14substring_white_list\x18\x05 \x03(\t\x12\x0f\n\x07\x64ry_run\x18\x06 \x01(\x08\x12Q\n\x1ftraining_phrase_cleaner_options\x18\x07 \x01(\x0b\x32(.ondewo.nlu.TrainingPhraseCleanerOptions\x12J\n\x1breannotate_entities_options\x18\x08 \x01(\x0e\x32%.ondewo.nlu.ReannotateEntitiesOptions\"r\n\x13\x43leanIntentResponse\x12*\n\x0e\x63leaned_intent\x18\x01 \x01(\x0b\x32\x12.ondewo.nlu.Intent\x12/\n\rintent_update\x18\x02 \x01(\x0b\x32\x18.ondewo.nlu.IntentUpdate\"\x9a\x01\n\x1cTrainingPhraseCleanerOptions\x12#\n\x1b\x64\x65lete_repeated_whitespaces\x18\x01 \x01(\x08\x12)\n!delete_leading_special_characters\x18\x02 \x01(\x08\x12*\n\"delete_trailing_special_characters\x18\x03 \x01(\x08\"(\n\x0cStringUpdate\x12\x0b\n\x03new\x18\x01 \x01(\t\x12\x0b\n\x03old\x18\x02 \x01(\t\"\xe0\x02\n\x0cIntentUpdate\x12\x1b\n\x13intent_display_name\x18\x01 \x01(\t\x12R\n\x1btraining_phrase_update_list\x18\x02 \x03(\x0b\x32-.ondewo.nlu.IntentUpdate.TrainingPhraseUpdate\x12\x1a\n\x12\x64\x65leted_parameters\x18\x03 \x03(\t\x1a\xc2\x01\n\x14TrainingPhraseUpdate\x12\x38\n\x16training_phrase_update\x18\x01 \x01(\x0b\x32\x18.ondewo.nlu.StringUpdate\x12\x30\n\x0e\x65ntity_updates\x18\x02 \x03(\x0b\x32\x18.ondewo.nlu.StringUpdate\x12\x1c\n\x14\x65ntities_reannotated\x18\x03 \x03(\t\x12 \n\x18\x63ontains_update_variable\x18\x04 \x01(\x08\"\xf4\x01\n\x10\x45ntityTypeUpdate\x12\x18\n\x10\x65ntity_type_name\x18\x01 \x01(\t\x12\x45\n\x12values_update_list\x18\x02 \x03(\x0b\x32).ondewo.nlu.EntityTypeUpdate.EntityUpdate\x1a\x7f\n\x0c\x45ntityUpdate\x12\x35\n\x13\x65ntity_value_update\x18\x01 \x01(\x0b\x32\x18.ondewo.nlu.StringUpdate\x12\x38\n\x16\x65ntity_synonym_updates\x18\x02 \x03(\x0b\x32\x18.ondewo.nlu.StringUpdate\"\xf2\x01\n\x1a\x43leanAllEntityTypesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x1a\n\x12special_characters\x18\x03 \x01(\t\x12\x1c\n\x14substring_white_list\x18\x04 \x03(\t\x12\x1f\n\x17max_entity_count_update\x18\x05 \x01(\x05\x12&\n\x1e\x66orbidden_entity_type_patterns\x18\x06 \x03(\t\x12\x0f\n\x07\x64ry_run\x18\x07 \x01(\x08\x12\x19\n\x11number_of_workers\x18\x08 \x01(\x05\"\x81\x02\n\x1b\x43leanAllEntityTypesResponse\x12\x34\n\x14\x63leaned_entity_types\x18\x01 \x03(\x0b\x32\x16.ondewo.nlu.EntityType\x12\x34\n\x14\x64\x65leted_entity_types\x18\x02 \x03(\x0b\x32\x16.ondewo.nlu.EntityType\x12\x39\n\x13\x65ntity_type_updates\x18\x03 \x03(\x0b\x32\x1c.ondewo.nlu.EntityTypeUpdate\x12;\n\x15\x65ntity_type_deletions\x18\x04 \x03(\x0b\x32\x1c.ondewo.nlu.EntityTypeUpdate\"\xc5\x01\n\x16\x43leanEntityTypeRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x18\n\x10\x65ntity_type_name\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x12\x1a\n\x12special_characters\x18\x04 \x01(\t\x12\x1c\n\x14substring_white_list\x18\x05 \x03(\t\x12\x1f\n\x17max_entity_count_update\x18\x06 \x01(\x05\x12\x0f\n\x07\x64ry_run\x18\x07 \x01(\x08\"\x88\x01\n\x17\x43leanEntityTypeResponse\x12\x33\n\x13\x63leaned_entity_type\x18\x01 \x01(\x0b\x32\x16.ondewo.nlu.EntityType\x12\x38\n\x12\x65ntity_type_update\x18\x02 \x01(\x0b\x32\x1c.ondewo.nlu.EntityTypeUpdate\"\xd1\x03\n\x19\x41\x64\x64TrainingPhrasesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12[\n\x14training_phrase_list\x18\x03 \x03(\x0b\x32=.ondewo.nlu.AddTrainingPhrasesRequest.TrainingPhraseForIntent\x12\x18\n\x10\x65xtract_entities\x18\x04 \x01(\x08\x12\x1a\n\x12special_characters\x18\x05 \x01(\t\x12Q\n\x1ftraining_phrase_cleaner_options\x18\x06 \x01(\x0b\x32(.ondewo.nlu.TrainingPhraseCleanerOptions\x12\x19\n\x11number_of_workers\x18\x07 \x01(\x05\x1a\x8b\x01\n\x17TrainingPhraseForIntent\x12\x17\n\x0ftraining_phrase\x18\x01 \x01(\t\x12\x1b\n\x13intent_display_name\x18\x02 \x01(\t\x12:\n\x08\x65ntities\x18\x03 \x03(\x0b\x32(.ondewo.nlu.Intent.TrainingPhrase.Entity\"4\n\x1a\x41\x64\x64TrainingPhrasesResponse\x12\x16\n\x0e\x65rror_messages\x18\x01 \x03(\t\"\x83\x02\n AddTrainingPhrasesFromCSVRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x14\n\x0c\x63sv_contents\x18\x03 \x01(\x0c\x12\x18\n\x10\x65xtract_entities\x18\x04 \x01(\x08\x12\x1a\n\x12special_characters\x18\x05 \x01(\t\x12Q\n\x1ftraining_phrase_cleaner_options\x18\x06 \x01(\x0b\x32(.ondewo.nlu.TrainingPhraseCleanerOptions\x12\x19\n\x11number_of_workers\x18\x07 \x01(\x05*\xab\x01\n\x19ReannotateEntitiesOptions\x12\x14\n\x10REANNOTATE_NEVER\x10\x00\x12\x15\n\x11REANNOTATE_ALWAYS\x10\x01\x12\x17\n\x13REANNOTATE_IF_EMPTY\x10\x02\x12\x1d\n\x19REANNOTATE_AFTER_DELETION\x10\x03\x12)\n%REANNOTATE_IF_EMPTY_OR_AFTER_DELETION\x10\x04\x32\x97\x06\n\tUtilities\x12T\n\rValidateRegex\x12 .ondewo.nlu.ValidateRegexRequest\x1a!.ondewo.nlu.ValidateRegexResponse\x12l\n\x15ValidateEmbeddedRegex\x12(.ondewo.nlu.ValidateEmbeddedRegexRequest\x1a).ondewo.nlu.ValidateEmbeddedRegexResponse\x12Z\n\x0f\x43leanAllIntents\x12\".ondewo.nlu.CleanAllIntentsRequest\x1a#.ondewo.nlu.CleanAllIntentsResponse\x12N\n\x0b\x43leanIntent\x12\x1e.ondewo.nlu.CleanIntentRequest\x1a\x1f.ondewo.nlu.CleanIntentResponse\x12\x66\n\x13\x43leanAllEntityTypes\x12&.ondewo.nlu.CleanAllEntityTypesRequest\x1a\'.ondewo.nlu.CleanAllEntityTypesResponse\x12Z\n\x0f\x43leanEntityType\x12\".ondewo.nlu.CleanEntityTypeRequest\x1a#.ondewo.nlu.CleanEntityTypeResponse\x12\x63\n\x12\x41\x64\x64TrainingPhrases\x12%.ondewo.nlu.AddTrainingPhrasesRequest\x1a&.ondewo.nlu.AddTrainingPhrasesResponse\x12q\n\x19\x41\x64\x64TrainingPhrasesFromCSV\x12,.ondewo.nlu.AddTrainingPhrasesFromCSVRequest\x1a&.ondewo.nlu.AddTrainingPhrasesResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ondewo.nlu.utility_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_REANNOTATEENTITIESOPTIONS']._serialized_start = 3640
    _globals['_REANNOTATEENTITIESOPTIONS']._serialized_end = 3811
    _globals['_VALIDATEREGEXREQUEST']._serialized_start = 95
    _globals['_VALIDATEREGEXREQUEST']._serialized_end = 132
    _globals['_VALIDATEREGEXRESPONSE']._serialized_start = 134
    _globals['_VALIDATEREGEXRESPONSE']._serialized_end = 181
    _globals['_VALIDATEEMBEDDEDREGEXREQUEST']._serialized_start = 183
    _globals['_VALIDATEEMBEDDEDREGEXREQUEST']._serialized_end = 265
    _globals['_VALIDATEEMBEDDEDREGEXRESPONSE']._serialized_start = 267
    _globals['_VALIDATEEMBEDDEDREGEXRESPONSE']._serialized_end = 322
    _globals['_CLEANALLINTENTSREQUEST']._serialized_start = 325
    _globals['_CLEANALLINTENTSREQUEST']._serialized_end = 649
    _globals['_CLEANALLINTENTSRESPONSE']._serialized_start = 651
    _globals['_CLEANALLINTENTSRESPONSE']._serialized_end = 775
    _globals['_CLEANINTENTREQUEST']._serialized_start = 778
    _globals['_CLEANINTENTREQUEST']._serialized_end = 1092
    _globals['_CLEANINTENTRESPONSE']._serialized_start = 1094
    _globals['_CLEANINTENTRESPONSE']._serialized_end = 1208
    _globals['_TRAININGPHRASECLEANEROPTIONS']._serialized_start = 1211
    _globals['_TRAININGPHRASECLEANEROPTIONS']._serialized_end = 1365
    _globals['_STRINGUPDATE']._serialized_start = 1367
    _globals['_STRINGUPDATE']._serialized_end = 1407
    _globals['_INTENTUPDATE']._serialized_start = 1410
    _globals['_INTENTUPDATE']._serialized_end = 1762
    _globals['_INTENTUPDATE_TRAININGPHRASEUPDATE']._serialized_start = 1568
    _globals['_INTENTUPDATE_TRAININGPHRASEUPDATE']._serialized_end = 1762
    _globals['_ENTITYTYPEUPDATE']._serialized_start = 1765
    _globals['_ENTITYTYPEUPDATE']._serialized_end = 2009
    _globals['_ENTITYTYPEUPDATE_ENTITYUPDATE']._serialized_start = 1882
    _globals['_ENTITYTYPEUPDATE_ENTITYUPDATE']._serialized_end = 2009
    _globals['_CLEANALLENTITYTYPESREQUEST']._serialized_start = 2012
    _globals['_CLEANALLENTITYTYPESREQUEST']._serialized_end = 2254
    _globals['_CLEANALLENTITYTYPESRESPONSE']._serialized_start = 2257
    _globals['_CLEANALLENTITYTYPESRESPONSE']._serialized_end = 2514
    _globals['_CLEANENTITYTYPEREQUEST']._serialized_start = 2517
    _globals['_CLEANENTITYTYPEREQUEST']._serialized_end = 2714
    _globals['_CLEANENTITYTYPERESPONSE']._serialized_start = 2717
    _globals['_CLEANENTITYTYPERESPONSE']._serialized_end = 2853
    _globals['_ADDTRAININGPHRASESREQUEST']._serialized_start = 2856
    _globals['_ADDTRAININGPHRASESREQUEST']._serialized_end = 3321
    _globals['_ADDTRAININGPHRASESREQUEST_TRAININGPHRASEFORINTENT']._serialized_start = 3182
    _globals['_ADDTRAININGPHRASESREQUEST_TRAININGPHRASEFORINTENT']._serialized_end = 3321
    _globals['_ADDTRAININGPHRASESRESPONSE']._serialized_start = 3323
    _globals['_ADDTRAININGPHRASESRESPONSE']._serialized_end = 3375
    _globals['_ADDTRAININGPHRASESFROMCSVREQUEST']._serialized_start = 3378
    _globals['_ADDTRAININGPHRASESFROMCSVREQUEST']._serialized_end = 3637
    _globals['_UTILITIES']._serialized_start = 3814
    _globals['_UTILITIES']._serialized_end = 4605
# @@protoc_insertion_point(module_scope)
