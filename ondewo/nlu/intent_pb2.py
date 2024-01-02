# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/nlu/intent.proto
"""Generated protocol buffer code."""
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ondewo.nlu import operations_pb2 as ondewo_dot_nlu_dot_operations__pb2
from ondewo.nlu import common_pb2 as ondewo_dot_nlu_dot_common__pb2
from ondewo.nlu import context_pb2 as ondewo_dot_nlu_dot_context__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17ondewo/nlu/intent.proto\x12\nondewo.nlu\x1a\x1cgoogle/api/annotations.proto\x1a\x18ondewo/nlu/context.proto\x1a\x17ondewo/nlu/common.proto\x1a\x1bondewo/nlu/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xcf\'\n\x06Intent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x36\n\rwebhook_state\x18\x06 \x01(\x0e\x32\x1f.ondewo.nlu.Intent.WebhookState\x12\x10\n\x08priority\x18\x03 \x01(\x05\x12\x13\n\x0bis_fallback\x18\x04 \x01(\x08\x12\x13\n\x0bml_disabled\x18\x13 \x01(\x08\x12\x1b\n\x13input_context_names\x18\x07 \x03(\t\x12\x0e\n\x06\x65vents\x18\x08 \x03(\t\x12;\n\x10training_phrases\x18\t \x03(\x0b\x32!.ondewo.nlu.Intent.TrainingPhrase\x12\x0e\n\x06\x61\x63tion\x18\n \x01(\t\x12,\n\x0foutput_contexts\x18\x0b \x03(\x0b\x32\x13.ondewo.nlu.Context\x12\x16\n\x0ereset_contexts\x18\x0c \x01(\x08\x12\x30\n\nparameters\x18\r \x03(\x0b\x32\x1c.ondewo.nlu.Intent.Parameter\x12,\n\x08messages\x18\x0e \x03(\x0b\x32\x1a.ondewo.nlu.Intent.Message\x12G\n\x1a\x64\x65\x66\x61ult_response_platforms\x18\x0f \x03(\x0e\x32#.ondewo.nlu.Intent.Message.Platform\x12!\n\x19root_followup_intent_name\x18\x10 \x01(\t\x12#\n\x1bparent_followup_intent_name\x18\x11 \x01(\t\x12\x43\n\x14\x66ollowup_intent_info\x18\x12 \x03(\x0b\x32%.ondewo.nlu.Intent.FollowupIntentInfo\x12\x17\n\x0fnext_page_token\x18\x1e \x01(\t\x12\x13\n\x0b\x64omain_name\x18\x1f \x01(\t\x12\x1d\n\x15is_start_of_deviation\x18  \x01(\x08\x12\x1b\n\x13is_end_of_deviation\x18! \x01(\x08\x12\x1d\n\x15training_phrase_count\x18\" \x01(\x05\x12/\n\x06status\x18# \x01(\x0e\x32\x1f.ondewo.nlu.Intent.IntentStatus\x12.\n\nstart_date\x18$ \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_date\x18% \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04tags\x18& \x03(\t\x1a\xe2\x03\n\x0eTrainingPhrase\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x04type\x18\x02 \x01(\x0e\x32&.ondewo.nlu.Intent.TrainingPhrase.Type\x12\x0c\n\x04text\x18\x03 \x01(\t\x12:\n\x08\x65ntities\x18\x04 \x03(\x0b\x32(.ondewo.nlu.Intent.TrainingPhrase.Entity\x12\x19\n\x11times_added_count\x18\x05 \x01(\x05\x12\x15\n\rlanguage_code\x18\x06 \x01(\t\x1a\xd6\x01\n\x06\x45ntity\x12\x18\n\x10\x65ntity_type_name\x18\x01 \x01(\t\x12 \n\x18\x65ntity_type_display_name\x18\x03 \x01(\t\x12\x19\n\x11\x65ntity_value_name\x18\x04 \x01(\t\x12!\n\x19\x65ntity_value_display_name\x18\x05 \x01(\t\x12\r\n\x05start\x18\x06 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x07 \x01(\x05\x12\x16\n\x0eparameter_name\x18\x08 \x01(\t\x12\x1e\n\x16parameter_display_name\x18\t \x01(\t\"7\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x45XAMPLE\x10\x01\x12\x0c\n\x08TEMPLATE\x10\x02\x1a\xa8\x02\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x15\n\rdefault_value\x18\x04 \x01(\t\x12\x18\n\x10\x65ntity_type_name\x18\x05 \x01(\t\x12 \n\x18\x65ntity_type_display_name\x18\x06 \x01(\t\x12\x11\n\tmandatory\x18\x07 \x01(\x08\x12\x34\n\x07prompts\x18\x08 \x03(\x0b\x32#.ondewo.nlu.Intent.Parameter.Prompt\x12\x0f\n\x07is_list\x18\t \x01(\x08\x1a;\n\x06Prompt\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x1a\x87\x18\n\x07Message\x12\x0c\n\x04name\x18\x10 \x01(\t\x12\x15\n\rlanguage_code\x18\x11 \x01(\t\x12/\n\x04text\x18\x01 \x01(\x0b\x32\x1f.ondewo.nlu.Intent.Message.TextH\x00\x12\x31\n\x05image\x18\x02 \x01(\x0b\x32 .ondewo.nlu.Intent.Message.ImageH\x00\x12@\n\rquick_replies\x18\x03 \x01(\x0b\x32\'.ondewo.nlu.Intent.Message.QuickRepliesH\x00\x12/\n\x04\x63\x61rd\x18\x04 \x01(\x0b\x32\x1f.ondewo.nlu.Intent.Message.CardH\x00\x12*\n\x07payload\x18\x05 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x12\x46\n\x10simple_responses\x18\x07 \x01(\x0b\x32*.ondewo.nlu.Intent.Message.SimpleResponsesH\x00\x12:\n\nbasic_card\x18\x08 \x01(\x0b\x32$.ondewo.nlu.Intent.Message.BasicCardH\x00\x12=\n\x0bsuggestions\x18\t \x01(\x0b\x32&.ondewo.nlu.Intent.Message.SuggestionsH\x00\x12K\n\x13link_out_suggestion\x18\n \x01(\x0b\x32,.ondewo.nlu.Intent.Message.LinkOutSuggestionH\x00\x12<\n\x0blist_select\x18\x0b \x01(\x0b\x32%.ondewo.nlu.Intent.Message.ListSelectH\x00\x12\x44\n\x0f\x63\x61rousel_select\x18\x0c \x01(\x0b\x32).ondewo.nlu.Intent.Message.CarouselSelectH\x00\x12\x38\n\thtml_text\x18\r \x01(\x0b\x32#.ondewo.nlu.Intent.Message.HTMLTextH\x00\x12\x31\n\x05video\x18\x0e \x01(\x0b\x32 .ondewo.nlu.Intent.Message.VideoH\x00\x12\x31\n\x05\x61udio\x18\x0f \x01(\x0b\x32 .ondewo.nlu.Intent.Message.AudioH\x00\x12\x35\n\x08platform\x18\x06 \x01(\x0e\x32#.ondewo.nlu.Intent.Message.Platform\x12\x11\n\tis_prompt\x18\x12 \x01(\x08\x1a\x14\n\x04Text\x12\x0c\n\x04text\x18\x01 \x03(\t\x1a\x36\n\x05Image\x12\x11\n\timage_uri\x18\x01 \x01(\t\x12\x1a\n\x12\x61\x63\x63\x65ssibility_text\x18\x02 \x01(\t\x1a\x34\n\x0cQuickReplies\x12\r\n\x05title\x18\x01 \x01(\t\x12\x15\n\rquick_replies\x18\x02 \x03(\t\x1a\x9d\x01\n\x04\x43\x61rd\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x11\n\timage_uri\x18\x03 \x01(\t\x12\x37\n\x07\x62uttons\x18\x04 \x03(\x0b\x32&.ondewo.nlu.Intent.Message.Card.Button\x1a(\n\x06\x42utton\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08postback\x18\x02 \x01(\t\x1aL\n\x0eSimpleResponse\x12\x16\n\x0etext_to_speech\x18\x01 \x01(\t\x12\x0c\n\x04ssml\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_text\x18\x03 \x01(\t\x1aV\n\x0fSimpleResponses\x12\x43\n\x10simple_responses\x18\x01 \x03(\x0b\x32).ondewo.nlu.Intent.Message.SimpleResponse\x1a\xbf\x02\n\tBasicCard\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x16\n\x0e\x66ormatted_text\x18\x03 \x01(\t\x12/\n\x05image\x18\x04 \x01(\x0b\x32 .ondewo.nlu.Intent.Message.Image\x12<\n\x07\x62uttons\x18\x05 \x03(\x0b\x32+.ondewo.nlu.Intent.Message.BasicCard.Button\x1a\x89\x01\n\x06\x42utton\x12\r\n\x05title\x18\x01 \x01(\t\x12R\n\x0fopen_uri_action\x18\x02 \x01(\x0b\x32\x39.ondewo.nlu.Intent.Message.BasicCard.Button.OpenUriAction\x1a\x1c\n\rOpenUriAction\x12\x0b\n\x03uri\x18\x01 \x01(\t\x1a\x1b\n\nSuggestion\x12\r\n\x05title\x18\x01 \x01(\t\x1aI\n\x0bSuggestions\x12:\n\x0bsuggestions\x18\x01 \x03(\x0b\x32%.ondewo.nlu.Intent.Message.Suggestion\x1a:\n\x11LinkOutSuggestion\x12\x18\n\x10\x64\x65stination_name\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x1a\xed\x01\n\nListSelect\x12\r\n\x05title\x18\x01 \x01(\t\x12\x39\n\x05items\x18\x02 \x03(\x0b\x32*.ondewo.nlu.Intent.Message.ListSelect.Item\x1a\x94\x01\n\x04Item\x12\x37\n\x04info\x18\x01 \x01(\x0b\x32).ondewo.nlu.Intent.Message.SelectItemInfo\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12/\n\x05image\x18\x04 \x01(\x0b\x32 .ondewo.nlu.Intent.Message.Image\x1a\xe6\x01\n\x0e\x43\x61rouselSelect\x12=\n\x05items\x18\x01 \x03(\x0b\x32..ondewo.nlu.Intent.Message.CarouselSelect.Item\x1a\x94\x01\n\x04Item\x12\x37\n\x04info\x18\x01 \x01(\x0b\x32).ondewo.nlu.Intent.Message.SelectItemInfo\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12/\n\x05image\x18\x04 \x01(\x0b\x32 .ondewo.nlu.Intent.Message.Image\x1a\x18\n\x08HTMLText\x12\x0c\n\x04text\x18\x01 \x03(\t\x1a\x30\n\x05Video\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x1a\n\x12\x61\x63\x63\x65ssibility_text\x18\x02 \x01(\t\x1a\x30\n\x05\x41udio\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x1a\n\x12\x61\x63\x63\x65ssibility_text\x18\x02 \x01(\t\x1a/\n\x0eSelectItemInfo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08synonyms\x18\x02 \x03(\t\"\x92\x04\n\x08Platform\x12\x18\n\x14PLATFORM_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x46\x41\x43\x45\x42OOK\x10\x01\x12\t\n\x05SLACK\x10\x02\x12\x0c\n\x08TELEGRAM\x10\x03\x12\x07\n\x03KIK\x10\x04\x12\t\n\x05SKYPE\x10\x05\x12\x08\n\x04LINE\x10\x06\x12\t\n\x05VIBER\x10\x07\x12\x15\n\x11\x41\x43TIONS_ON_GOOGLE\x10\x08\x12\x11\n\rPLACEHOLDER_1\x10\t\x12\x11\n\rPLACEHOLDER_2\x10\n\x12\x11\n\rPLACEHOLDER_3\x10\x0b\x12\x11\n\rPLACEHOLDER_4\x10\x0c\x12\x11\n\rPLACEHOLDER_5\x10\r\x12\x11\n\rPLACEHOLDER_6\x10\x0e\x12\x11\n\rPLACEHOLDER_7\x10\x0f\x12\x11\n\rPLACEHOLDER_8\x10\x10\x12\x11\n\rPLACEHOLDER_9\x10\x11\x12\x12\n\x0ePLACEHOLDER_10\x10\x12\x12\x12\n\x0ePLACEHOLDER_11\x10\x13\x12\x12\n\x0ePLACEHOLDER_12\x10\x14\x12\x12\n\x0ePLACEHOLDER_13\x10\x15\x12\x12\n\x0ePLACEHOLDER_14\x10\x16\x12\x12\n\x0ePLACEHOLDER_15\x10\x17\x12\x12\n\x0ePLACEHOLDER_16\x10\x18\x12\x12\n\x0ePLACEHOLDER_17\x10\x19\x12\x12\n\x0ePLACEHOLDER_18\x10\x1a\x12\x12\n\x0ePLACEHOLDER_19\x10\x1b\x12\x12\n\x0ePLACEHOLDER_20\x10\x1c\x42\t\n\x07message\x1aW\n\x12\x46ollowupIntentInfo\x12\x1c\n\x14\x66ollowup_intent_name\x18\x01 \x01(\t\x12#\n\x1bparent_followup_intent_name\x18\x02 \x01(\t\"(\n\x0cIntentStatus\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\"t\n\x0cWebhookState\x12\x1d\n\x19WEBHOOK_STATE_UNSPECIFIED\x10\x00\x12\x19\n\x15WEBHOOK_STATE_ENABLED\x10\x01\x12*\n&WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING\x10\x02\"\xfe\x01\n\x12ListIntentsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12+\n\x0bintent_view\x18\x03 \x01(\x0e\x32\x16.ondewo.nlu.IntentView\x12\x12\n\npage_token\x18\x05 \x01(\t\x12\x36\n\x12\x66ilter_by_category\x18\x06 \x01(\x0e\x32\x1a.ondewo.nlu.IntentCategory\x12\x30\n\rsort_by_field\x18\x07 \x01(\x0b\x32\x19.ondewo.nlu.IntentSorting\x12\x16\n\x0e\x66ilter_by_tags\x18\x08 \x03(\t\"S\n\x13ListIntentsResponse\x12#\n\x07intents\x18\x01 \x03(\x0b\x32\x12.ondewo.nlu.Intent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"x\n\x10GetIntentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12+\n\x0bintent_view\x18\x03 \x01(\x0e\x32\x16.ondewo.nlu.IntentView\x12\x12\n\npage_token\x18\n \x01(\t\"\x8d\x01\n\x13\x43reateIntentRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\"\n\x06intent\x18\x02 \x01(\x0b\x32\x12.ondewo.nlu.Intent\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x12+\n\x0bintent_view\x18\x04 \x01(\x0e\x32\x16.ondewo.nlu.IntentView\"\xae\x01\n\x13UpdateIntentRequest\x12\"\n\x06intent\x18\x01 \x01(\x0b\x32\x12.ondewo.nlu.Intent\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12+\n\x0bintent_view\x18\x04 \x01(\x0e\x32\x16.ondewo.nlu.IntentView\"#\n\x13\x44\x65leteIntentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x84\x02\n\x19\x42\x61tchUpdateIntentsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x1a\n\x10intent_batch_uri\x18\x02 \x01(\tH\x00\x12\x36\n\x13intent_batch_inline\x18\x03 \x01(\x0b\x32\x17.ondewo.nlu.IntentBatchH\x00\x12\x15\n\rlanguage_code\x18\x04 \x01(\t\x12/\n\x0bupdate_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12+\n\x0bintent_view\x18\x06 \x01(\x0e\x32\x16.ondewo.nlu.IntentViewB\x0e\n\x0cintent_batch\"A\n\x1a\x42\x61tchUpdateIntentsResponse\x12#\n\x07intents\x18\x01 \x03(\x0b\x32\x12.ondewo.nlu.Intent\"P\n\x19\x42\x61tchDeleteIntentsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12#\n\x07intents\x18\x02 \x03(\x0b\x32\x12.ondewo.nlu.Intent\"2\n\x0bIntentBatch\x12#\n\x07intents\x18\x01 \x03(\x0b\x32\x12.ondewo.nlu.Intent\"\xec\x02\n\rIntentSorting\x12\x43\n\rsorting_field\x18\x01 \x01(\x0e\x32,.ondewo.nlu.IntentSorting.IntentSortingField\x12-\n\x0csorting_mode\x18\x02 \x01(\x0e\x32\x17.ondewo.nlu.SortingMode\"\xe6\x01\n\x12IntentSortingField\x12\x15\n\x11NO_INTENT_SORTING\x10\x00\x12\x17\n\x13SORT_INTENT_BY_NAME\x10\x01\x12 \n\x1cSORT_INTENT_BY_CREATION_DATE\x10\x02\x12\x1f\n\x1bSORT_INTENT_BY_LAST_UPDATED\x10\x03\x12!\n\x1dSORT_INTENT_BY_USERSAYS_COUNT\x10\x04\x12\x1d\n\x19SORT_INTENT_BY_START_DATE\x10\x05\x12\x1b\n\x17SORT_INTENT_BY_END_DATE\x10\x06\"5\n\x10IntentTagRequest\x12\x13\n\x0bintent_name\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\"+\n\x14GetIntentTagsRequest\x12\x13\n\x0bintent_name\x18\x01 \x01(\t\",\n\x15GetIntentTagsResponse\x12\x13\n\x0bintent_tags\x18\x01 \x03(\t\")\n\x17GetAllIntentTagsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\"`\n!BatchUpdateTrainingPhrasesRequest\x12;\n\x10training_phrases\x18\x01 \x03(\x0b\x32!.ondewo.nlu.Intent.TrainingPhrase\"\x81\x01\n\x14TrainingPhraseStatus\x12<\n\x0ftraining_phrase\x18\x01 \x01(\x0b\x32!.ondewo.nlu.Intent.TrainingPhraseH\x00\x12\x17\n\rerror_message\x18\x02 \x01(\tH\x00\x42\x12\n\x10phrase_or_status\"|\n\"BatchTrainingPhrasesStatusResponse\x12\x42\n\x18training_phrase_statuses\x18\x01 \x03(\x0b\x32 .ondewo.nlu.TrainingPhraseStatus\x12\x12\n\nhas_errors\x18\x02 \x01(\x08\"\x80\x02\n!BatchCreateTrainingPhrasesRequest\x12k\n\x18training_phrase_requests\x18\x01 \x03(\x0b\x32I.ondewo.nlu.BatchCreateTrainingPhrasesRequest.CreateTrainingPhraseRequest\x1an\n\x1b\x43reateTrainingPhraseRequest\x12\x13\n\x0bintent_name\x18\x01 \x01(\t\x12:\n\x0ftraining_phrase\x18\x02 \x01(\x0b\x32!.ondewo.nlu.Intent.TrainingPhrase\"/\n\x1e\x42\x61tchGetTrainingPhrasesRequest\x12\r\n\x05names\x18\x01 \x03(\t\"2\n!BatchDeleteTrainingPhrasesRequest\x12\r\n\x05names\x18\x01 \x03(\t\"\x9c\x02\n\"BatchDeleteTrainingPhrasesResponse\x12\x62\n\x0f\x64\x65lete_statuses\x18\x01 \x03(\x0b\x32I.ondewo.nlu.BatchDeleteTrainingPhrasesResponse.DeleteTrainingPhraseStatus\x12\x12\n\nhas_errors\x18\x02 \x01(\x08\x1a~\n\x1a\x44\x65leteTrainingPhraseStatus\x12\x36\n\x14successfully_deleted\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x17\n\rerror_message\x18\x02 \x01(\tH\x00\x42\x0f\n\rdelete_status\"\\\n\x1aListTrainingPhrasesRequest\x12\x13\n\x0bintent_name\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\"s\n\x1bListTrainingPhrasesResponse\x12;\n\x10training_phrases\x18\x01 \x03(\x0b\x32!.ondewo.nlu.Intent.TrainingPhrase\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa1\x02\n#BatchResponseMessagesStatusResponse\x12h\n\x19response_message_statuses\x18\x01 \x03(\x0b\x32\x45.ondewo.nlu.BatchResponseMessagesStatusResponse.ResponseMessageStatus\x12\x12\n\nhas_errors\x18\x02 \x01(\x08\x1a|\n\x15ResponseMessageStatus\x12\x36\n\x10response_message\x18\x01 \x01(\x0b\x32\x1a.ondewo.nlu.Intent.MessageH\x00\x12\x17\n\rerror_message\x18\x02 \x01(\tH\x00\x42\x12\n\x10phrase_or_status\"\xff\x01\n\"BatchCreateResponseMessagesRequest\x12n\n\x19response_message_requests\x18\x01 \x03(\x0b\x32K.ondewo.nlu.BatchCreateResponseMessagesRequest.CreateResponseMessageRequest\x1ai\n\x1c\x43reateResponseMessageRequest\x12\x13\n\x0bintent_name\x18\x01 \x01(\t\x12\x34\n\x10response_message\x18\x02 \x01(\x0b\x32\x1a.ondewo.nlu.Intent.Message\"[\n\"BatchUpdateResponseMessagesRequest\x12\x35\n\x11response_messages\x18\x01 \x03(\x0b\x32\x1a.ondewo.nlu.Intent.Message\"0\n\x1f\x42\x61tchGetResponseMessagesRequest\x12\r\n\x05names\x18\x01 \x03(\t\"3\n\"BatchDeleteResponseMessagesRequest\x12\r\n\x05names\x18\x01 \x03(\t\"\xa0\x02\n#BatchDeleteResponseMessagesResponse\x12\x64\n\x0f\x64\x65lete_statuses\x18\x01 \x03(\x0b\x32K.ondewo.nlu.BatchDeleteResponseMessagesResponse.DeleteResponseMessageStatus\x12\x12\n\nhas_errors\x18\x02 \x01(\x08\x1a\x7f\n\x1b\x44\x65leteResponseMessageStatus\x12\x36\n\x14successfully_deleted\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x17\n\rerror_message\x18\x02 \x01(\tH\x00\x42\x0f\n\rdelete_status\"]\n\x1bListResponseMessagesRequest\x12\x13\n\x0bintent_name\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\"n\n\x1cListResponseMessagesResponse\x12\x35\n\x11response_messages\x18\x01 \x03(\x0b\x32\x1a.ondewo.nlu.Intent.Message\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xfd\x01\n\x1d\x42\x61tchParametersStatusResponse\x12U\n\x12parameter_statuses\x18\x01 \x03(\x0b\x32\x39.ondewo.nlu.BatchParametersStatusResponse.ParameterStatus\x12\x12\n\nhas_errors\x18\x02 \x01(\x08\x1aq\n\x0fParameterStatus\x12\x31\n\tparameter\x18\x01 \x01(\x0b\x32\x1c.ondewo.nlu.Intent.ParameterH\x00\x12\x17\n\rerror_message\x18\x02 \x01(\tH\x00\x42\x12\n\x10phrase_or_status\"\xdb\x01\n\x1c\x42\x61tchCreateParametersRequest\x12[\n\x12parameter_requests\x18\x01 \x03(\x0b\x32?.ondewo.nlu.BatchCreateParametersRequest.CreateParameterRequest\x1a^\n\x16\x43reateParameterRequest\x12\x13\n\x0bintent_name\x18\x01 \x01(\t\x12/\n\tparameter\x18\x02 \x01(\x0b\x32\x1c.ondewo.nlu.Intent.Parameter\"P\n\x1c\x42\x61tchUpdateParametersRequest\x12\x30\n\nparameters\x18\x01 \x03(\x0b\x32\x1c.ondewo.nlu.Intent.Parameter\"*\n\x19\x42\x61tchGetParametersRequest\x12\r\n\x05names\x18\x01 \x03(\t\"-\n\x1c\x42\x61tchDeleteParametersRequest\x12\r\n\x05names\x18\x01 \x03(\t\"\x88\x02\n\x1d\x42\x61tchDeleteParametersResponse\x12X\n\x0f\x64\x65lete_statuses\x18\x01 \x03(\x0b\x32?.ondewo.nlu.BatchDeleteParametersResponse.DeleteParameterStatus\x12\x12\n\nhas_errors\x18\x02 \x01(\x08\x1ay\n\x15\x44\x65leteParameterStatus\x12\x36\n\x14successfully_deleted\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x17\n\rerror_message\x18\x02 \x01(\tH\x00\x42\x0f\n\rdelete_status\"W\n\x15ListParametersRequest\x12\x13\n\x0bintent_name\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\"c\n\x16ListParametersResponse\x12\x30\n\nparameters\x18\x01 \x03(\x0b\x32\x1c.ondewo.nlu.Intent.Parameter\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x82\x01\n1ListTrainingPhrasesofIntentsWithEnrichmentRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x12\n\nintent_ids\x18\x03 \x03(\t\x12\x12\n\npage_token\x18\x04 \x01(\t\"g\n2ListTrainingPhrasesofIntentsWithEnrichmentResponse\x12\x18\n\x10training_phrases\x18\x01 \x03(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*\x8a\x01\n\nIntentView\x12\x1b\n\x17INTENT_VIEW_UNSPECIFIED\x10\x00\x12\x14\n\x10INTENT_VIEW_FULL\x10\x01\x12\x17\n\x13INTENT_VIEW_PARTIAL\x10\x02\x12\x17\n\x13INTENT_VIEW_SHALLOW\x10\x03\x12\x17\n\x13INTENT_VIEW_MINIMUM\x10\x04*\x9e\x01\n\x0eIntentCategory\x12\x0f\n\x0b\x41LL_INTENTS\x10\x00\x12\x13\n\x0f\x44\x45\x46\x41ULT_INTENTS\x10\x01\x12\x18\n\x14USER_DEFINED_INTENTS\x10\x02\x12\x18\n\x14\x44\x41TE_EXPIRED_INTENTS\x10\x03\x12\x17\n\x13\x44\x41TE_ACTIVE_INTENTS\x10\x04\x12\x19\n\x15\x44\x41TE_UPCOMING_INTENTS\x10\x05\x32\xbe\x19\n\x07Intents\x12}\n\x0bListIntents\x12\x1e.ondewo.nlu.ListIntentsRequest\x1a\x1f.ondewo.nlu.ListIntentsResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v2/{parent=projects/*/agent}/intents\x12l\n\tGetIntent\x12\x1c.ondewo.nlu.GetIntentRequest\x1a\x12.ondewo.nlu.Intent\"-\x82\xd3\xe4\x93\x02\'\x12%/v2/{name=projects/*/agent/intents/*}\x12u\n\x0c\x43reateIntent\x12\x1f.ondewo.nlu.CreateIntentRequest\x1a\x12.ondewo.nlu.Intent\"0\x82\xd3\xe4\x93\x02*\"%/v2/{parent=projects/*/agent}/intents:\x01*\x12|\n\x0cUpdateIntent\x12\x1f.ondewo.nlu.UpdateIntentRequest\x1a\x12.ondewo.nlu.Intent\"7\x82\xd3\xe4\x93\x02\x31\x32,/v2/{intent.name=projects/*/agent/intents/*}:\x01*\x12v\n\x0c\x44\x65leteIntent\x12\x1f.ondewo.nlu.DeleteIntentRequest\x1a\x16.google.protobuf.Empty\"-\x82\xd3\xe4\x93\x02\'*%/v2/{name=projects/*/agent/intents/*}\x12\x90\x01\n\x12\x42\x61tchUpdateIntents\x12%.ondewo.nlu.BatchUpdateIntentsRequest\x1a\x15.ondewo.nlu.Operation\"<\x82\xd3\xe4\x93\x02\x36\"1/v2/{parent=projects/*/agent}/intents:batchUpdate:\x01*\x12\x90\x01\n\x12\x42\x61tchDeleteIntents\x12%.ondewo.nlu.BatchDeleteIntentsRequest\x1a\x15.ondewo.nlu.Operation\"<\x82\xd3\xe4\x93\x02\x36\"1/v2/{parent=projects/*/agent}/intents:batchDelete:\x01*\x12}\n\tTagIntent\x12\x1c.ondewo.nlu.IntentTagRequest\x1a\x16.google.protobuf.Empty\":\x82\xd3\xe4\x93\x02\x34\"//v2/{parent=projects/*/agent}/intents:tagIntent:\x01*\x12\x89\x01\n\x0f\x44\x65leteIntentTag\x12\x1c.ondewo.nlu.IntentTagRequest\x1a\x16.google.protobuf.Empty\"@\x82\xd3\xe4\x93\x02:\"5/v2/{parent=projects/*/agent}/intents:deleteIntentTag:\x01*\x12V\n\rGetIntentTags\x12 .ondewo.nlu.GetIntentTagsRequest\x1a!.ondewo.nlu.GetIntentTagsResponse\"\x00\x12\\\n\x10GetAllIntentTags\x12#.ondewo.nlu.GetAllIntentTagsRequest\x1a!.ondewo.nlu.GetIntentTagsResponse\"\x00\x12{\n\x1a\x42\x61tchCreateTrainingPhrases\x12-.ondewo.nlu.BatchCreateTrainingPhrasesRequest\x1a..ondewo.nlu.BatchTrainingPhrasesStatusResponse\x12u\n\x17\x42\x61tchGetTrainingPhrases\x12*.ondewo.nlu.BatchGetTrainingPhrasesRequest\x1a..ondewo.nlu.BatchTrainingPhrasesStatusResponse\x12{\n\x1a\x42\x61tchUpdateTrainingPhrases\x12-.ondewo.nlu.BatchUpdateTrainingPhrasesRequest\x1a..ondewo.nlu.BatchTrainingPhrasesStatusResponse\x12{\n\x1a\x42\x61tchDeleteTrainingPhrases\x12-.ondewo.nlu.BatchDeleteTrainingPhrasesRequest\x1a..ondewo.nlu.BatchDeleteTrainingPhrasesResponse\x12\x66\n\x13ListTrainingPhrases\x12&.ondewo.nlu.ListTrainingPhrasesRequest\x1a\'.ondewo.nlu.ListTrainingPhrasesResponse\x12~\n\x1b\x42\x61tchCreateResponseMessages\x12..ondewo.nlu.BatchCreateResponseMessagesRequest\x1a/.ondewo.nlu.BatchResponseMessagesStatusResponse\x12x\n\x18\x42\x61tchGetResponseMessages\x12+.ondewo.nlu.BatchGetResponseMessagesRequest\x1a/.ondewo.nlu.BatchResponseMessagesStatusResponse\x12~\n\x1b\x42\x61tchUpdateResponseMessages\x12..ondewo.nlu.BatchUpdateResponseMessagesRequest\x1a/.ondewo.nlu.BatchResponseMessagesStatusResponse\x12~\n\x1b\x42\x61tchDeleteResponseMessages\x12..ondewo.nlu.BatchDeleteResponseMessagesRequest\x1a/.ondewo.nlu.BatchDeleteResponseMessagesResponse\x12i\n\x14ListResponseMessages\x12\'.ondewo.nlu.ListResponseMessagesRequest\x1a(.ondewo.nlu.ListResponseMessagesResponse\x12l\n\x15\x42\x61tchCreateParameters\x12(.ondewo.nlu.BatchCreateParametersRequest\x1a).ondewo.nlu.BatchParametersStatusResponse\x12\x66\n\x12\x42\x61tchGetParameters\x12%.ondewo.nlu.BatchGetParametersRequest\x1a).ondewo.nlu.BatchParametersStatusResponse\x12l\n\x15\x42\x61tchUpdateParameters\x12(.ondewo.nlu.BatchUpdateParametersRequest\x1a).ondewo.nlu.BatchParametersStatusResponse\x12l\n\x15\x42\x61tchDeleteParameters\x12(.ondewo.nlu.BatchDeleteParametersRequest\x1a).ondewo.nlu.BatchDeleteParametersResponse\x12W\n\x0eListParameters\x12!.ondewo.nlu.ListParametersRequest\x1a\".ondewo.nlu.ListParametersResponse\x12\xab\x01\n*ListTrainingPhrasesofIntentsWithEnrichment\x12=.ondewo.nlu.ListTrainingPhrasesofIntentsWithEnrichmentRequest\x1a>.ondewo.nlu.ListTrainingPhrasesofIntentsWithEnrichmentResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ondewo.nlu.intent_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _INTENTS.methods_by_name['ListIntents']._options = None
    _INTENTS.methods_by_name['ListIntents']._serialized_options = b'\202\323\344\223\002\'\022%/v2/{parent=projects/*/agent}/intents'
    _INTENTS.methods_by_name['GetIntent']._options = None
    _INTENTS.methods_by_name['GetIntent']._serialized_options = b'\202\323\344\223\002\'\022%/v2/{name=projects/*/agent/intents/*}'
    _INTENTS.methods_by_name['CreateIntent']._options = None
    _INTENTS.methods_by_name['CreateIntent']._serialized_options = b'\202\323\344\223\002*\"%/v2/{parent=projects/*/agent}/intents:\001*'
    _INTENTS.methods_by_name['UpdateIntent']._options = None
    _INTENTS.methods_by_name['UpdateIntent']._serialized_options = b'\202\323\344\223\00212,/v2/{intent.name=projects/*/agent/intents/*}:\001*'
    _INTENTS.methods_by_name['DeleteIntent']._options = None
    _INTENTS.methods_by_name['DeleteIntent']._serialized_options = b'\202\323\344\223\002\'*%/v2/{name=projects/*/agent/intents/*}'
    _INTENTS.methods_by_name['BatchUpdateIntents']._options = None
    _INTENTS.methods_by_name['BatchUpdateIntents']._serialized_options = b'\202\323\344\223\0026\"1/v2/{parent=projects/*/agent}/intents:batchUpdate:\001*'
    _INTENTS.methods_by_name['BatchDeleteIntents']._options = None
    _INTENTS.methods_by_name['BatchDeleteIntents']._serialized_options = b'\202\323\344\223\0026\"1/v2/{parent=projects/*/agent}/intents:batchDelete:\001*'
    _INTENTS.methods_by_name['TagIntent']._options = None
    _INTENTS.methods_by_name['TagIntent']._serialized_options = b'\202\323\344\223\0024\"//v2/{parent=projects/*/agent}/intents:tagIntent:\001*'
    _INTENTS.methods_by_name['DeleteIntentTag']._options = None
    _INTENTS.methods_by_name['DeleteIntentTag']._serialized_options = b'\202\323\344\223\002:\"5/v2/{parent=projects/*/agent}/intents:deleteIntentTag:\001*'
    _globals['_INTENTVIEW']._serialized_start=10996
    _globals['_INTENTVIEW']._serialized_end=11134
    _globals['_INTENTCATEGORY']._serialized_start=11137
    _globals['_INTENTCATEGORY']._serialized_end=11295
    _globals['_INTENT']._serialized_start=276
    _globals['_INTENT']._serialized_end=5347
    _globals['_INTENT_TRAININGPHRASE']._serialized_start=1235
    _globals['_INTENT_TRAININGPHRASE']._serialized_end=1717
    _globals['_INTENT_TRAININGPHRASE_ENTITY']._serialized_start=1446
    _globals['_INTENT_TRAININGPHRASE_ENTITY']._serialized_end=1660
    _globals['_INTENT_TRAININGPHRASE_TYPE']._serialized_start=1662
    _globals['_INTENT_TRAININGPHRASE_TYPE']._serialized_end=1717
    _globals['_INTENT_PARAMETER']._serialized_start=1720
    _globals['_INTENT_PARAMETER']._serialized_end=2016
    _globals['_INTENT_PARAMETER_PROMPT']._serialized_start=1957
    _globals['_INTENT_PARAMETER_PROMPT']._serialized_end=2016
    _globals['_INTENT_MESSAGE']._serialized_start=2019
    _globals['_INTENT_MESSAGE']._serialized_end=5098
    _globals['_INTENT_MESSAGE_TEXT']._serialized_start=2964
    _globals['_INTENT_MESSAGE_TEXT']._serialized_end=2984
    _globals['_INTENT_MESSAGE_IMAGE']._serialized_start=2986
    _globals['_INTENT_MESSAGE_IMAGE']._serialized_end=3040
    _globals['_INTENT_MESSAGE_QUICKREPLIES']._serialized_start=3042
    _globals['_INTENT_MESSAGE_QUICKREPLIES']._serialized_end=3094
    _globals['_INTENT_MESSAGE_CARD']._serialized_start=3097
    _globals['_INTENT_MESSAGE_CARD']._serialized_end=3254
    _globals['_INTENT_MESSAGE_CARD_BUTTON']._serialized_start=3214
    _globals['_INTENT_MESSAGE_CARD_BUTTON']._serialized_end=3254
    _globals['_INTENT_MESSAGE_SIMPLERESPONSE']._serialized_start=3256
    _globals['_INTENT_MESSAGE_SIMPLERESPONSE']._serialized_end=3332
    _globals['_INTENT_MESSAGE_SIMPLERESPONSES']._serialized_start=3334
    _globals['_INTENT_MESSAGE_SIMPLERESPONSES']._serialized_end=3420
    _globals['_INTENT_MESSAGE_BASICCARD']._serialized_start=3423
    _globals['_INTENT_MESSAGE_BASICCARD']._serialized_end=3742
    _globals['_INTENT_MESSAGE_BASICCARD_BUTTON']._serialized_start=3605
    _globals['_INTENT_MESSAGE_BASICCARD_BUTTON']._serialized_end=3742
    _globals['_INTENT_MESSAGE_BASICCARD_BUTTON_OPENURIACTION']._serialized_start=3714
    _globals['_INTENT_MESSAGE_BASICCARD_BUTTON_OPENURIACTION']._serialized_end=3742
    _globals['_INTENT_MESSAGE_SUGGESTION']._serialized_start=3744
    _globals['_INTENT_MESSAGE_SUGGESTION']._serialized_end=3771
    _globals['_INTENT_MESSAGE_SUGGESTIONS']._serialized_start=3773
    _globals['_INTENT_MESSAGE_SUGGESTIONS']._serialized_end=3846
    _globals['_INTENT_MESSAGE_LINKOUTSUGGESTION']._serialized_start=3848
    _globals['_INTENT_MESSAGE_LINKOUTSUGGESTION']._serialized_end=3906
    _globals['_INTENT_MESSAGE_LISTSELECT']._serialized_start=3909
    _globals['_INTENT_MESSAGE_LISTSELECT']._serialized_end=4146
    _globals['_INTENT_MESSAGE_LISTSELECT_ITEM']._serialized_start=3998
    _globals['_INTENT_MESSAGE_LISTSELECT_ITEM']._serialized_end=4146
    _globals['_INTENT_MESSAGE_CAROUSELSELECT']._serialized_start=4149
    _globals['_INTENT_MESSAGE_CAROUSELSELECT']._serialized_end=4379
    _globals['_INTENT_MESSAGE_CAROUSELSELECT_ITEM']._serialized_start=3998
    _globals['_INTENT_MESSAGE_CAROUSELSELECT_ITEM']._serialized_end=4146
    _globals['_INTENT_MESSAGE_HTMLTEXT']._serialized_start=4381
    _globals['_INTENT_MESSAGE_HTMLTEXT']._serialized_end=4405
    _globals['_INTENT_MESSAGE_VIDEO']._serialized_start=4407
    _globals['_INTENT_MESSAGE_VIDEO']._serialized_end=4455
    _globals['_INTENT_MESSAGE_AUDIO']._serialized_start=4457
    _globals['_INTENT_MESSAGE_AUDIO']._serialized_end=4505
    _globals['_INTENT_MESSAGE_SELECTITEMINFO']._serialized_start=4507
    _globals['_INTENT_MESSAGE_SELECTITEMINFO']._serialized_end=4554
    _globals['_INTENT_MESSAGE_PLATFORM']._serialized_start=4557
    _globals['_INTENT_MESSAGE_PLATFORM']._serialized_end=5087
    _globals['_INTENT_FOLLOWUPINTENTINFO']._serialized_start=5100
    _globals['_INTENT_FOLLOWUPINTENTINFO']._serialized_end=5187
    _globals['_INTENT_INTENTSTATUS']._serialized_start=5189
    _globals['_INTENT_INTENTSTATUS']._serialized_end=5229
    _globals['_INTENT_WEBHOOKSTATE']._serialized_start=5231
    _globals['_INTENT_WEBHOOKSTATE']._serialized_end=5347
    _globals['_LISTINTENTSREQUEST']._serialized_start=5350
    _globals['_LISTINTENTSREQUEST']._serialized_end=5604
    _globals['_LISTINTENTSRESPONSE']._serialized_start=5606
    _globals['_LISTINTENTSRESPONSE']._serialized_end=5689
    _globals['_GETINTENTREQUEST']._serialized_start=5691
    _globals['_GETINTENTREQUEST']._serialized_end=5811
    _globals['_CREATEINTENTREQUEST']._serialized_start=5814
    _globals['_CREATEINTENTREQUEST']._serialized_end=5955
    _globals['_UPDATEINTENTREQUEST']._serialized_start=5958
    _globals['_UPDATEINTENTREQUEST']._serialized_end=6132
    _globals['_DELETEINTENTREQUEST']._serialized_start=6134
    _globals['_DELETEINTENTREQUEST']._serialized_end=6169
    _globals['_BATCHUPDATEINTENTSREQUEST']._serialized_start=6172
    _globals['_BATCHUPDATEINTENTSREQUEST']._serialized_end=6432
    _globals['_BATCHUPDATEINTENTSRESPONSE']._serialized_start=6434
    _globals['_BATCHUPDATEINTENTSRESPONSE']._serialized_end=6499
    _globals['_BATCHDELETEINTENTSREQUEST']._serialized_start=6501
    _globals['_BATCHDELETEINTENTSREQUEST']._serialized_end=6581
    _globals['_INTENTBATCH']._serialized_start=6583
    _globals['_INTENTBATCH']._serialized_end=6633
    _globals['_INTENTSORTING']._serialized_start=6636
    _globals['_INTENTSORTING']._serialized_end=7000
    _globals['_INTENTSORTING_INTENTSORTINGFIELD']._serialized_start=6770
    _globals['_INTENTSORTING_INTENTSORTINGFIELD']._serialized_end=7000
    _globals['_INTENTTAGREQUEST']._serialized_start=7002
    _globals['_INTENTTAGREQUEST']._serialized_end=7055
    _globals['_GETINTENTTAGSREQUEST']._serialized_start=7057
    _globals['_GETINTENTTAGSREQUEST']._serialized_end=7100
    _globals['_GETINTENTTAGSRESPONSE']._serialized_start=7102
    _globals['_GETINTENTTAGSRESPONSE']._serialized_end=7146
    _globals['_GETALLINTENTTAGSREQUEST']._serialized_start=7148
    _globals['_GETALLINTENTTAGSREQUEST']._serialized_end=7189
    _globals['_BATCHUPDATETRAININGPHRASESREQUEST']._serialized_start=7191
    _globals['_BATCHUPDATETRAININGPHRASESREQUEST']._serialized_end=7287
    _globals['_TRAININGPHRASESTATUS']._serialized_start=7290
    _globals['_TRAININGPHRASESTATUS']._serialized_end=7419
    _globals['_BATCHTRAININGPHRASESSTATUSRESPONSE']._serialized_start=7421
    _globals['_BATCHTRAININGPHRASESSTATUSRESPONSE']._serialized_end=7545
    _globals['_BATCHCREATETRAININGPHRASESREQUEST']._serialized_start=7548
    _globals['_BATCHCREATETRAININGPHRASESREQUEST']._serialized_end=7804
    _globals['_BATCHCREATETRAININGPHRASESREQUEST_CREATETRAININGPHRASEREQUEST']._serialized_start=7694
    _globals['_BATCHCREATETRAININGPHRASESREQUEST_CREATETRAININGPHRASEREQUEST']._serialized_end=7804
    _globals['_BATCHGETTRAININGPHRASESREQUEST']._serialized_start=7806
    _globals['_BATCHGETTRAININGPHRASESREQUEST']._serialized_end=7853
    _globals['_BATCHDELETETRAININGPHRASESREQUEST']._serialized_start=7855
    _globals['_BATCHDELETETRAININGPHRASESREQUEST']._serialized_end=7905
    _globals['_BATCHDELETETRAININGPHRASESRESPONSE']._serialized_start=7908
    _globals['_BATCHDELETETRAININGPHRASESRESPONSE']._serialized_end=8192
    _globals['_BATCHDELETETRAININGPHRASESRESPONSE_DELETETRAININGPHRASESTATUS']._serialized_start=8066
    _globals['_BATCHDELETETRAININGPHRASESRESPONSE_DELETETRAININGPHRASESTATUS']._serialized_end=8192
    _globals['_LISTTRAININGPHRASESREQUEST']._serialized_start=8194
    _globals['_LISTTRAININGPHRASESREQUEST']._serialized_end=8286
    _globals['_LISTTRAININGPHRASESRESPONSE']._serialized_start=8288
    _globals['_LISTTRAININGPHRASESRESPONSE']._serialized_end=8403
    _globals['_BATCHRESPONSEMESSAGESSTATUSRESPONSE']._serialized_start=8406
    _globals['_BATCHRESPONSEMESSAGESSTATUSRESPONSE']._serialized_end=8695
    _globals['_BATCHRESPONSEMESSAGESSTATUSRESPONSE_RESPONSEMESSAGESTATUS']._serialized_start=8571
    _globals['_BATCHRESPONSEMESSAGESSTATUSRESPONSE_RESPONSEMESSAGESTATUS']._serialized_end=8695
    _globals['_BATCHCREATERESPONSEMESSAGESREQUEST']._serialized_start=8698
    _globals['_BATCHCREATERESPONSEMESSAGESREQUEST']._serialized_end=8953
    _globals['_BATCHCREATERESPONSEMESSAGESREQUEST_CREATERESPONSEMESSAGEREQUEST']._serialized_start=8848
    _globals['_BATCHCREATERESPONSEMESSAGESREQUEST_CREATERESPONSEMESSAGEREQUEST']._serialized_end=8953
    _globals['_BATCHUPDATERESPONSEMESSAGESREQUEST']._serialized_start=8955
    _globals['_BATCHUPDATERESPONSEMESSAGESREQUEST']._serialized_end=9046
    _globals['_BATCHGETRESPONSEMESSAGESREQUEST']._serialized_start=9048
    _globals['_BATCHGETRESPONSEMESSAGESREQUEST']._serialized_end=9096
    _globals['_BATCHDELETERESPONSEMESSAGESREQUEST']._serialized_start=9098
    _globals['_BATCHDELETERESPONSEMESSAGESREQUEST']._serialized_end=9149
    _globals['_BATCHDELETERESPONSEMESSAGESRESPONSE']._serialized_start=9152
    _globals['_BATCHDELETERESPONSEMESSAGESRESPONSE']._serialized_end=9440
    _globals['_BATCHDELETERESPONSEMESSAGESRESPONSE_DELETERESPONSEMESSAGESTATUS']._serialized_start=9313
    _globals['_BATCHDELETERESPONSEMESSAGESRESPONSE_DELETERESPONSEMESSAGESTATUS']._serialized_end=9440
    _globals['_LISTRESPONSEMESSAGESREQUEST']._serialized_start=9442
    _globals['_LISTRESPONSEMESSAGESREQUEST']._serialized_end=9535
    _globals['_LISTRESPONSEMESSAGESRESPONSE']._serialized_start=9537
    _globals['_LISTRESPONSEMESSAGESRESPONSE']._serialized_end=9647
    _globals['_BATCHPARAMETERSSTATUSRESPONSE']._serialized_start=9650
    _globals['_BATCHPARAMETERSSTATUSRESPONSE']._serialized_end=9903
    _globals['_BATCHPARAMETERSSTATUSRESPONSE_PARAMETERSTATUS']._serialized_start=9790
    _globals['_BATCHPARAMETERSSTATUSRESPONSE_PARAMETERSTATUS']._serialized_end=9903
    _globals['_BATCHCREATEPARAMETERSREQUEST']._serialized_start=9906
    _globals['_BATCHCREATEPARAMETERSREQUEST']._serialized_end=10125
    _globals['_BATCHCREATEPARAMETERSREQUEST_CREATEPARAMETERREQUEST']._serialized_start=10031
    _globals['_BATCHCREATEPARAMETERSREQUEST_CREATEPARAMETERREQUEST']._serialized_end=10125
    _globals['_BATCHUPDATEPARAMETERSREQUEST']._serialized_start=10127
    _globals['_BATCHUPDATEPARAMETERSREQUEST']._serialized_end=10207
    _globals['_BATCHGETPARAMETERSREQUEST']._serialized_start=10209
    _globals['_BATCHGETPARAMETERSREQUEST']._serialized_end=10251
    _globals['_BATCHDELETEPARAMETERSREQUEST']._serialized_start=10253
    _globals['_BATCHDELETEPARAMETERSREQUEST']._serialized_end=10298
    _globals['_BATCHDELETEPARAMETERSRESPONSE']._serialized_start=10301
    _globals['_BATCHDELETEPARAMETERSRESPONSE']._serialized_end=10565
    _globals['_BATCHDELETEPARAMETERSRESPONSE_DELETEPARAMETERSTATUS']._serialized_start=10444
    _globals['_BATCHDELETEPARAMETERSRESPONSE_DELETEPARAMETERSTATUS']._serialized_end=10565
    _globals['_LISTPARAMETERSREQUEST']._serialized_start=10567
    _globals['_LISTPARAMETERSREQUEST']._serialized_end=10654
    _globals['_LISTPARAMETERSRESPONSE']._serialized_start=10656
    _globals['_LISTPARAMETERSRESPONSE']._serialized_end=10755
    _globals['_LISTTRAININGPHRASESOFINTENTSWITHENRICHMENTREQUEST']._serialized_start=10758
    _globals['_LISTTRAININGPHRASESOFINTENTSWITHENRICHMENTREQUEST']._serialized_end=10888
    _globals['_LISTTRAININGPHRASESOFINTENTSWITHENRICHMENTRESPONSE']._serialized_start=10890
    _globals['_LISTTRAININGPHRASESOFINTENTSWITHENRICHMENTRESPONSE']._serialized_end=10993
    _globals['_INTENTS']._serialized_start=11298
    _globals['_INTENTS']._serialized_end=14560
# @@protoc_insertion_point(module_scope)
