# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ondewo/s2t/speech-to-text.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
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
    'ondewo/s2t/speech-to-text.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fondewo/s2t/speech-to-text.proto\x12\nondewo.s2t\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xeb\x05\n\x17TranscribeRequestConfig\x12\x17\n\x0fs2t_pipeline_id\x18\x01 \x01(\t\x12&\n\x08\x64\x65\x63oding\x18\x02 \x01(\x0e\x32\x14.ondewo.s2t.Decoding\x12\x1d\n\x13language_model_name\x18\x03 \x01(\tH\x00\x12<\n\x0fpost_processing\x18\x04 \x01(\x0b\x32!.ondewo.s2t.PostProcessingOptionsH\x01\x12\x44\n\x13utterance_detection\x18\x05 \x01(\x0b\x32%.ondewo.s2t.UtteranceDetectionOptionsH\x02\x12(\n\x08pyannote\x18\x06 \x01(\x0b\x32\x14.ondewo.s2t.PyannoteH\x03\x12@\n\x0ereturn_options\x18\x08 \x01(\x0b\x32&.ondewo.s2t.TranscriptionReturnOptionsH\x04\x12\x15\n\x08language\x18\t \x01(\tH\x05\x88\x01\x01\x12\x11\n\x04task\x18\n \x01(\tH\x06\x88\x01\x01\x12\x38\n\x12s2t_service_config\x18\x0b \x01(\x0b\x32\x17.google.protobuf.StructH\x07\x88\x01\x01\x12J\n\x19s2t_cloud_provider_config\x18\x0c \x01(\x0b\x32\".ondewo.s2t.S2tCloudProviderConfigH\x08\x88\x01\x01\x42\x1b\n\x19oneof_language_model_nameB\x17\n\x15oneof_post_processingB\x1b\n\x19oneof_utterance_detectionB\x1a\n\x18voice_activity_detectionB\x16\n\x14oneof_return_optionsB\x0b\n\t_languageB\x07\n\x05_taskB\x15\n\x13_s2t_service_configB\x1c\n\x1a_s2t_cloud_provider_config\"\x9f\x04\n\x16S2tCloudProviderConfig\x12W\n s2t_cloud_provider_config_amazon\x18\x01 \x01(\x0b\x32(.ondewo.s2t.S2tCloudProviderConfigAmazonH\x00\x88\x01\x01\x12[\n\"s2t_cloud_provider_config_deepgram\x18\x02 \x01(\x0b\x32*.ondewo.s2t.S2tCloudProviderConfigDeepgramH\x01\x88\x01\x01\x12W\n s2t_cloud_provider_config_google\x18\x03 \x01(\x0b\x32(.ondewo.s2t.S2tCloudProviderConfigGoogleH\x02\x88\x01\x01\x12]\n#s2t_cloud_provider_config_microsoft\x18\x04 \x01(\x0b\x32+.ondewo.s2t.S2tCloudProviderConfigMicrosoftH\x03\x88\x01\x01\x42#\n!_s2t_cloud_provider_config_amazonB%\n#_s2t_cloud_provider_config_deepgramB#\n!_s2t_cloud_provider_config_googleB&\n$_s2t_cloud_provider_config_microsoft\"\xac\x02\n\x1cS2tCloudProviderConfigAmazon\x12\x31\n$enable_partial_results_stabilization\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12&\n\x19partial_results_stability\x18\x02 \x01(\tH\x01\x88\x01\x01\x12 \n\x13language_model_name\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1c\n\x0fvocabulary_name\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\'\n%_enable_partial_results_stabilizationB\x1c\n\x1a_partial_results_stabilityB\x16\n\x14_language_model_nameB\x12\n\x10_vocabulary_name\"\xe8\x01\n\x1eS2tCloudProviderConfigDeepgram\x12\x16\n\tpunctuate\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x19\n\x0csmart_format\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x15\n\x08numerals\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x19\n\x0cmeasurements\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x16\n\tdictation\x18\x05 \x01(\x08H\x04\x88\x01\x01\x42\x0c\n\n_punctuateB\x0f\n\r_smart_formatB\x0b\n\t_numeralsB\x0f\n\r_measurementsB\x0c\n\n_dictation\"\xe6\x02\n\x1cS2tCloudProviderConfigGoogle\x12)\n\x1c\x65nable_automatic_punctuation\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12%\n\x18\x65nable_word_time_offsets\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12#\n\x16\x65nable_word_confidence\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12%\n\x18transcript_normalization\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x1d\n\x10max_alternatives\x18\x05 \x01(\x05H\x04\x88\x01\x01\x42\x1f\n\x1d_enable_automatic_punctuationB\x1b\n\x19_enable_word_time_offsetsB\x19\n\x17_enable_word_confidenceB\x1b\n\x19_transcript_normalizationB\x13\n\x11_max_alternatives\"\xb1\x01\n\x1fS2tCloudProviderConfigMicrosoft\x12\'\n\x1ause_fast_transcription_api\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\'\n\x1ause_detailed_output_format\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\x1d\n\x1b_use_fast_transcription_apiB\x1d\n\x1b_use_detailed_output_format\"\xaf\x02\n\x1aTranscriptionReturnOptions\x12\x1e\n\x16return_start_of_speech\x18\x01 \x01(\x08\x12\x14\n\x0creturn_audio\x18\x02 \x01(\x08\x12\x1f\n\x17return_confidence_score\x18\x03 \x01(\x08\x12)\n!return_alternative_transcriptions\x18\x04 \x01(\x08\x12,\n$return_alternative_transcriptions_nr\x18\x05 \x01(\x05\x12 \n\x18return_alternative_words\x18\x06 \x01(\x08\x12#\n\x1breturn_alternative_words_nr\x18\x07 \x01(\x05\x12\x1a\n\x12return_word_timing\x18\x08 \x01(\x08\"u\n\x19UtteranceDetectionOptions\x12\x1e\n\x14transcribe_not_final\x18\x01 \x01(\x08H\x00\x12\x1a\n\x12next_chunk_timeout\x18\x02 \x01(\x02\x42\x1c\n\x1aoneof_transcribe_not_final\"s\n\x15PostProcessingOptions\x12\x1b\n\x13spelling_correction\x18\x01 \x01(\x08\x12\x11\n\tnormalize\x18\x02 \x01(\x08\x12*\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x1a.ondewo.s2t.PostProcessing\"\xa3\x01\n\rTranscription\x12\x15\n\rtranscription\x18\x01 \x01(\t\x12\x18\n\x10\x63onfidence_score\x18\x02 \x01(\x02\x12%\n\x05words\x18\x03 \x03(\x0b\x32\x16.ondewo.s2t.WordDetail\x12:\n\x0c\x61lternatives\x18\x04 \x03(\x0b\x32$.ondewo.s2t.TranscriptionAlternative\"i\n\x18TranscriptionAlternative\x12\x12\n\ntranscript\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12%\n\x05words\x18\x03 \x03(\x0b\x32\x16.ondewo.s2t.WordDetail\"\x8c\x01\n\nWordDetail\x12\x12\n\nstart_time\x18\x01 \x01(\x02\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x02\x12\x0c\n\x04word\x18\x03 \x01(\t\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x12\x36\n\x11word_alternatives\x18\x05 \x03(\x0b\x32\x1b.ondewo.s2t.WordAlternative\"3\n\x0fWordAlternative\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\"\x8e\x01\n\x17TranscribeStreamRequest\x12\x13\n\x0b\x61udio_chunk\x18\x01 \x01(\x0c\x12\x15\n\rend_of_stream\x18\x02 \x01(\x08\x12\x33\n\x06\x63onfig\x18\x03 \x01(\x0b\x32#.ondewo.s2t.TranscribeRequestConfig\x12\x12\n\nmute_audio\x18\x04 \x01(\x08\"\x83\x02\n\x18TranscribeStreamResponse\x12\x31\n\x0etranscriptions\x18\x01 \x03(\x0b\x32\x19.ondewo.s2t.Transcription\x12\x0c\n\x04time\x18\x02 \x01(\x02\x12\r\n\x05\x66inal\x18\x03 \x01(\x08\x12\x14\n\x0creturn_audio\x18\x04 \x01(\x08\x12\r\n\x05\x61udio\x18\x05 \x01(\x0c\x12\x17\n\x0futterance_start\x18\x06 \x01(\x08\x12\x12\n\naudio_uuid\x18\x07 \x01(\t\x12\x35\n\x06\x63onfig\x18\x08 \x01(\x0b\x32#.ondewo.s2t.TranscribeRequestConfigH\x00\x42\x0e\n\x0coneof_config\"`\n\x15TranscribeFileRequest\x12\x12\n\naudio_file\x18\x01 \x01(\x0c\x12\x33\n\x06\x63onfig\x18\x02 \x01(\x0b\x32#.ondewo.s2t.TranscribeRequestConfig\"m\n\x16TranscribeFileResponse\x12\x31\n\x0etranscriptions\x18\x01 \x03(\x0b\x32\x19.ondewo.s2t.Transcription\x12\x0c\n\x04time\x18\x02 \x01(\x02\x12\x12\n\naudio_uuid\x18\x03 \x01(\t\"\x1b\n\rS2tPipelineId\x12\n\n\x02id\x18\x01 \x01(\t\"o\n\x17ListS2tPipelinesRequest\x12\x11\n\tlanguages\x18\x01 \x03(\t\x12\x17\n\x0fpipeline_owners\x18\x02 \x03(\t\x12\x0f\n\x07\x64omains\x18\x03 \x03(\t\x12\x17\n\x0fregistered_only\x18\x04 \x01(\x08\"S\n\x18ListS2tPipelinesResponse\x12\x37\n\x10pipeline_configs\x18\x01 \x03(\x0b\x32\x1d.ondewo.s2t.Speech2TextConfig\"C\n\x17ListS2tLanguagesRequest\x12\x0f\n\x07\x64omains\x18\x01 \x03(\t\x12\x17\n\x0fpipeline_owners\x18\x02 \x03(\t\"-\n\x18ListS2tLanguagesResponse\x12\x11\n\tlanguages\x18\x01 \x03(\t\"C\n\x15ListS2tDomainsRequest\x12\x11\n\tlanguages\x18\x01 \x03(\t\x12\x17\n\x0fpipeline_owners\x18\x02 \x03(\t\")\n\x16ListS2tDomainsResponse\x12\x0f\n\x07\x64omains\x18\x01 \x03(\t\",\n\x19S2TGetServiceInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\"\xe5\x02\n\x11Speech2TextConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12/\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32\x1a.ondewo.s2t.S2TDescription\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\x12+\n\tinference\x18\x04 \x01(\x0b\x32\x18.ondewo.s2t.S2TInference\x12\x35\n\x10streaming_server\x18\x05 \x01(\x0b\x32\x1b.ondewo.s2t.StreamingServer\x12\x44\n\x18voice_activity_detection\x18\x06 \x01(\x0b\x32\".ondewo.s2t.VoiceActivityDetection\x12\x33\n\x0fpost_processing\x18\x07 \x01(\x0b\x32\x1a.ondewo.s2t.PostProcessing\x12$\n\x07logging\x18\x08 \x01(\x0b\x32\x13.ondewo.s2t.Logging\"\\\n\x0eS2TDescription\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x16\n\x0epipeline_owner\x18\x02 \x01(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\x10\n\x08\x63omments\x18\x04 \x01(\t\"\xb1\x01\n\x0cS2TInference\x12\x33\n\x0f\x61\x63oustic_models\x18\x01 \x01(\x0b\x32\x1a.ondewo.s2t.AcousticModels\x12\x33\n\x0flanguage_models\x18\x02 \x01(\x0b\x32\x1a.ondewo.s2t.LanguageModels\x12\x37\n\x11inference_backend\x18\x03 \x01(\x0e\x32\x1c.ondewo.s2t.InferenceBackend\"\xee\x03\n\x0e\x41\x63ousticModels\x12\x0c\n\x04type\x18\x01 \x01(\t\x12$\n\x07wav2vec\x18\x02 \x01(\x0b\x32\x13.ondewo.s2t.Wav2Vec\x12\x31\n\x0ewav2vec_triton\x18\x03 \x01(\x0b\x32\x19.ondewo.s2t.Wav2VecTriton\x12$\n\x07whisper\x18\x04 \x01(\x0b\x32\x13.ondewo.s2t.Whisper\x12\x31\n\x0ewhisper_triton\x18\x05 \x01(\x0b\x32\x19.ondewo.s2t.WhisperTriton\x12\x43\n\x18s2t_cloud_service_amazon\x18\x06 \x01(\x0b\x32!.ondewo.s2t.S2tCloudServiceAmazon\x12G\n\x1as2t_cloud_service_deepgram\x18\x07 \x01(\x0b\x32#.ondewo.s2t.S2tCloudServiceDeepgram\x12\x43\n\x18s2t_cloud_service_google\x18\x08 \x01(\x0b\x32!.ondewo.s2t.S2tCloudServiceGoogle\x12I\n\x1bs2t_cloud_service_microsoft\x18\t \x01(\x0b\x32$.ondewo.s2t.S2tCloudServiceMicrosoft\"\xcd\x01\n\x15S2tCloudServiceAmazon\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x1b\n\x13streaming_available\x18\x02 \x01(\x08\x12,\n$enable_partial_results_stabilization\x18\x03 \x01(\x08\x12!\n\x19partial_results_stability\x18\x04 \x01(\t\x12\x1b\n\x13language_model_name\x18\x05 \x01(\t\x12\x17\n\x0fvocabulary_name\x18\x06 \x01(\t\"\xa3\x01\n\x17S2tCloudServiceDeepgram\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x11\n\tpunctuate\x18\x03 \x01(\x08\x12\x14\n\x0csmart_format\x18\x04 \x01(\x08\x12\x10\n\x08numerals\x18\x05 \x01(\x08\x12\x14\n\x0cmeasurements\x18\x06 \x01(\x08\x12\x11\n\tdictation\x18\x07 \x01(\x08\"\xe1\x01\n\x15S2tCloudServiceGoogle\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12$\n\x1c\x65nable_automatic_punctuation\x18\x03 \x01(\x08\x12 \n\x18\x65nable_word_time_offsets\x18\x04 \x01(\x08\x12\x1e\n\x16\x65nable_word_confidence\x18\x05 \x01(\x08\x12 \n\x18transcript_normalization\x18\x06 \x01(\x08\x12\x18\n\x10max_alternatives\x18\x07 \x01(\x05\"t\n\x18S2tCloudServiceMicrosoft\x12\x10\n\x08language\x18\x01 \x01(\t\x12\"\n\x1ause_fast_transcription_api\x18\x02 \x01(\x08\x12\"\n\x1ause_detailed_output_format\x18\x03 \x01(\x08\"N\n\x07Whisper\x12\x12\n\nmodel_path\x18\x01 \x01(\t\x12\x0f\n\x07use_gpu\x18\x02 \x01(\x08\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x0c\n\x04task\x18\x04 \x01(\t\"\xd6\x01\n\rWhisperTriton\x12\x16\n\x0eprocessor_path\x18\x01 \x01(\t\x12\x19\n\x11triton_model_name\x18\x02 \x01(\t\x12\x1c\n\x14triton_model_version\x18\x03 \x01(\t\x12\x1c\n\x14\x63heck_status_timeout\x18\x04 \x01(\x03\x12\x10\n\x08language\x18\x05 \x01(\t\x12\x0c\n\x04task\x18\x06 \x01(\t\x12\x1a\n\x12triton_server_host\x18\x07 \x01(\t\x12\x1a\n\x12triton_server_port\x18\x08 \x01(\x03\".\n\x07Wav2Vec\x12\x12\n\nmodel_path\x18\x01 \x01(\t\x12\x0f\n\x07use_gpu\x18\x02 \x01(\x08\"\xb6\x01\n\rWav2VecTriton\x12\x16\n\x0eprocessor_path\x18\x01 \x01(\t\x12\x19\n\x11triton_model_name\x18\x02 \x01(\t\x12\x1c\n\x14triton_model_version\x18\x03 \x01(\t\x12\x1c\n\x14\x63heck_status_timeout\x18\x04 \x01(\x03\x12\x1a\n\x12triton_server_host\x18\x05 \x01(\t\x12\x1a\n\x12triton_server_port\x18\x06 \x01(\x03\"%\n\x07PtFiles\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04step\x18\x02 \x01(\t\"\x18\n\x08\x43kptFile\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x88\x01\n\x0eLanguageModels\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x11\n\tbeam_size\x18\x02 \x01(\x03\x12\x12\n\ndefault_lm\x18\x03 \x01(\t\x12 \n\x18\x62\x65\x61m_search_scorer_alpha\x18\x04 \x01(\x02\x12\x1f\n\x17\x62\x65\x61m_search_scorer_beta\x18\x05 \x01(\x02\"\x91\x01\n\x0fStreamingServer\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x03\x12\x14\n\x0coutput_style\x18\x03 \x01(\t\x12L\n\x1cstreaming_speech_recognition\x18\x04 \x01(\x0b\x32&.ondewo.s2t.StreamingSpeechRecognition\"\xa4\x01\n\x1aStreamingSpeechRecognition\x12\x1c\n\x14transcribe_not_final\x18\x01 \x01(\x08\x12\x17\n\x0f\x64\x65\x63oding_method\x18\x02 \x01(\t\x12\x15\n\rsampling_rate\x18\x03 \x01(\x03\x12\x1c\n\x14min_audio_chunk_size\x18\x04 \x01(\x03\x12\x1a\n\x12next_chunk_timeout\x18\x05 \x01(\x02\"g\n\x16VoiceActivityDetection\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\t\x12\x15\n\rsampling_rate\x18\x02 \x01(\x03\x12&\n\x08pyannote\x18\x03 \x01(\x0b\x32\x14.ondewo.s2t.Pyannote\"\xa1\x01\n\x08Pyannote\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x16\n\x0emin_audio_size\x18\x02 \x01(\x03\x12\x18\n\x10min_duration_off\x18\x03 \x01(\x02\x12\x17\n\x0fmin_duration_on\x18\x04 \x01(\x02\x12\x1a\n\x12triton_server_host\x18\x05 \x01(\t\x12\x1a\n\x12triton_server_port\x18\x06 \x01(\x03\"W\n\x0ePostProcessing\x12\x10\n\x08pipeline\x18\x01 \x03(\t\x12\x33\n\x0fpost_processors\x18\x02 \x01(\x0b\x32\x1a.ondewo.s2t.PostProcessors\"n\n\x0ePostProcessors\x12\'\n\tsym_spell\x18\x01 \x01(\x0b\x32\x14.ondewo.s2t.SymSpell\x12\x33\n\rnormalization\x18\x02 \x01(\x0b\x32\x1c.ondewo.s2t.S2TNormalization\"Z\n\x08SymSpell\x12\x11\n\tdict_path\x18\x01 \x01(\t\x12$\n\x1cmax_dictionary_edit_distance\x18\x02 \x01(\x03\x12\x15\n\rprefix_length\x18\x03 \x01(\x03\"6\n\x10S2TNormalization\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x10\n\x08pipeline\x18\x02 \x03(\t\"%\n\x07Logging\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"+\n\x1cListS2tLanguageModelsRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\"C\n\x17LanguageModelPipelineId\x12\x13\n\x0bpipeline_id\x18\x01 \x01(\t\x12\x13\n\x0bmodel_names\x18\x02 \x03(\t\"]\n\x1dListS2tLanguageModelsResponse\x12<\n\x0flm_pipeline_ids\x18\x01 \x03(\x0b\x32#.ondewo.s2t.LanguageModelPipelineId\"=\n\x1e\x43reateUserLanguageModelRequest\x12\x1b\n\x13language_model_name\x18\x01 \x01(\t\"=\n\x1e\x44\x65leteUserLanguageModelRequest\x12\x1b\n\x13language_model_name\x18\x01 \x01(\t\"U\n!AddDataToUserLanguageModelRequest\x12\x1b\n\x13language_model_name\x18\x01 \x01(\t\x12\x13\n\x0bzipped_data\x18\x02 \x01(\x0c\"K\n\x1dTrainUserLanguageModelRequest\x12\x1b\n\x13language_model_name\x18\x01 \x01(\t\x12\r\n\x05order\x18\x02 \x01(\x03*M\n\x08\x44\x65\x63oding\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\n\n\x06GREEDY\x10\x01\x12\x17\n\x13\x42\x45\x41M_SEARCH_WITH_LM\x10\x02\x12\x0f\n\x0b\x42\x45\x41M_SEARCH\x10\x03*\xa1\x02\n\x10InferenceBackend\x12\x1d\n\x19INFERENCE_BACKEND_UNKNOWN\x10\x00\x12\x1d\n\x19INFERENCE_BACKEND_PYTORCH\x10\x01\x12\x1a\n\x16INFERENCE_BACKEND_FLAX\x10\x02\x12*\n&INFERENCE_BACKEND_CLOUD_SERVICE_AMAZON\x10\x03\x12,\n(INFERENCE_BACKEND_CLOUD_SERVICE_DEEPGRAM\x10\x04\x12*\n&INFERENCE_BACKEND_CLOUD_SERVICE_GOOGLE\x10\x05\x12-\n)INFERENCE_BACKEND_CLOUD_SERVICE_MICROSOFT\x10\x06\x32\xec\n\n\x0bSpeech2Text\x12Y\n\x0eTranscribeFile\x12!.ondewo.s2t.TranscribeFileRequest\x1a\".ondewo.s2t.TranscribeFileResponse\"\x00\x12\x63\n\x10TranscribeStream\x12#.ondewo.s2t.TranscribeStreamRequest\x1a$.ondewo.s2t.TranscribeStreamResponse\"\x00(\x01\x30\x01\x12L\n\x0eGetS2tPipeline\x12\x19.ondewo.s2t.S2tPipelineId\x1a\x1d.ondewo.s2t.Speech2TextConfig\"\x00\x12O\n\x11\x43reateS2tPipeline\x12\x1d.ondewo.s2t.Speech2TextConfig\x1a\x19.ondewo.s2t.S2tPipelineId\"\x00\x12H\n\x11\x44\x65leteS2tPipeline\x12\x19.ondewo.s2t.S2tPipelineId\x1a\x16.google.protobuf.Empty\"\x00\x12L\n\x11UpdateS2tPipeline\x12\x1d.ondewo.s2t.Speech2TextConfig\x1a\x16.google.protobuf.Empty\"\x00\x12_\n\x10ListS2tPipelines\x12#.ondewo.s2t.ListS2tPipelinesRequest\x1a$.ondewo.s2t.ListS2tPipelinesResponse\"\x00\x12_\n\x10ListS2tLanguages\x12#.ondewo.s2t.ListS2tLanguagesRequest\x1a$.ondewo.s2t.ListS2tLanguagesResponse\"\x00\x12Y\n\x0eListS2tDomains\x12!.ondewo.s2t.ListS2tDomainsRequest\x1a\".ondewo.s2t.ListS2tDomainsResponse\"\x00\x12Q\n\x0eGetServiceInfo\x12\x16.google.protobuf.Empty\x1a%.ondewo.s2t.S2TGetServiceInfoResponse\"\x00\x12n\n\x15ListS2tLanguageModels\x12(.ondewo.s2t.ListS2tLanguageModelsRequest\x1a).ondewo.s2t.ListS2tLanguageModelsResponse\"\x00\x12_\n\x17\x43reateUserLanguageModel\x12*.ondewo.s2t.CreateUserLanguageModelRequest\x1a\x16.google.protobuf.Empty\"\x00\x12_\n\x17\x44\x65leteUserLanguageModel\x12*.ondewo.s2t.DeleteUserLanguageModelRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x65\n\x1a\x41\x64\x64\x44\x61taToUserLanguageModel\x12-.ondewo.s2t.AddDataToUserLanguageModelRequest\x1a\x16.google.protobuf.Empty\"\x00\x12]\n\x16TrainUserLanguageModel\x12).ondewo.s2t.TrainUserLanguageModelRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ondewo.s2t.speech_to_text_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_DECODING']._serialized_start = 8665
    _globals['_DECODING']._serialized_end = 8742
    _globals['_INFERENCEBACKEND']._serialized_start = 8745
    _globals['_INFERENCEBACKEND']._serialized_end = 9034
    _globals['_TRANSCRIBEREQUESTCONFIG']._serialized_start = 107
    _globals['_TRANSCRIBEREQUESTCONFIG']._serialized_end = 854
    _globals['_S2TCLOUDPROVIDERCONFIG']._serialized_start = 857
    _globals['_S2TCLOUDPROVIDERCONFIG']._serialized_end = 1400
    _globals['_S2TCLOUDPROVIDERCONFIGAMAZON']._serialized_start = 1403
    _globals['_S2TCLOUDPROVIDERCONFIGAMAZON']._serialized_end = 1703
    _globals['_S2TCLOUDPROVIDERCONFIGDEEPGRAM']._serialized_start = 1706
    _globals['_S2TCLOUDPROVIDERCONFIGDEEPGRAM']._serialized_end = 1938
    _globals['_S2TCLOUDPROVIDERCONFIGGOOGLE']._serialized_start = 1941
    _globals['_S2TCLOUDPROVIDERCONFIGGOOGLE']._serialized_end = 2299
    _globals['_S2TCLOUDPROVIDERCONFIGMICROSOFT']._serialized_start = 2302
    _globals['_S2TCLOUDPROVIDERCONFIGMICROSOFT']._serialized_end = 2479
    _globals['_TRANSCRIPTIONRETURNOPTIONS']._serialized_start = 2482
    _globals['_TRANSCRIPTIONRETURNOPTIONS']._serialized_end = 2785
    _globals['_UTTERANCEDETECTIONOPTIONS']._serialized_start = 2787
    _globals['_UTTERANCEDETECTIONOPTIONS']._serialized_end = 2904
    _globals['_POSTPROCESSINGOPTIONS']._serialized_start = 2906
    _globals['_POSTPROCESSINGOPTIONS']._serialized_end = 3021
    _globals['_TRANSCRIPTION']._serialized_start = 3024
    _globals['_TRANSCRIPTION']._serialized_end = 3187
    _globals['_TRANSCRIPTIONALTERNATIVE']._serialized_start = 3189
    _globals['_TRANSCRIPTIONALTERNATIVE']._serialized_end = 3294
    _globals['_WORDDETAIL']._serialized_start = 3297
    _globals['_WORDDETAIL']._serialized_end = 3437
    _globals['_WORDALTERNATIVE']._serialized_start = 3439
    _globals['_WORDALTERNATIVE']._serialized_end = 3490
    _globals['_TRANSCRIBESTREAMREQUEST']._serialized_start = 3493
    _globals['_TRANSCRIBESTREAMREQUEST']._serialized_end = 3635
    _globals['_TRANSCRIBESTREAMRESPONSE']._serialized_start = 3638
    _globals['_TRANSCRIBESTREAMRESPONSE']._serialized_end = 3897
    _globals['_TRANSCRIBEFILEREQUEST']._serialized_start = 3899
    _globals['_TRANSCRIBEFILEREQUEST']._serialized_end = 3995
    _globals['_TRANSCRIBEFILERESPONSE']._serialized_start = 3997
    _globals['_TRANSCRIBEFILERESPONSE']._serialized_end = 4106
    _globals['_S2TPIPELINEID']._serialized_start = 4108
    _globals['_S2TPIPELINEID']._serialized_end = 4135
    _globals['_LISTS2TPIPELINESREQUEST']._serialized_start = 4137
    _globals['_LISTS2TPIPELINESREQUEST']._serialized_end = 4248
    _globals['_LISTS2TPIPELINESRESPONSE']._serialized_start = 4250
    _globals['_LISTS2TPIPELINESRESPONSE']._serialized_end = 4333
    _globals['_LISTS2TLANGUAGESREQUEST']._serialized_start = 4335
    _globals['_LISTS2TLANGUAGESREQUEST']._serialized_end = 4402
    _globals['_LISTS2TLANGUAGESRESPONSE']._serialized_start = 4404
    _globals['_LISTS2TLANGUAGESRESPONSE']._serialized_end = 4449
    _globals['_LISTS2TDOMAINSREQUEST']._serialized_start = 4451
    _globals['_LISTS2TDOMAINSREQUEST']._serialized_end = 4518
    _globals['_LISTS2TDOMAINSRESPONSE']._serialized_start = 4520
    _globals['_LISTS2TDOMAINSRESPONSE']._serialized_end = 4561
    _globals['_S2TGETSERVICEINFORESPONSE']._serialized_start = 4563
    _globals['_S2TGETSERVICEINFORESPONSE']._serialized_end = 4607
    _globals['_SPEECH2TEXTCONFIG']._serialized_start = 4610
    _globals['_SPEECH2TEXTCONFIG']._serialized_end = 4967
    _globals['_S2TDESCRIPTION']._serialized_start = 4969
    _globals['_S2TDESCRIPTION']._serialized_end = 5061
    _globals['_S2TINFERENCE']._serialized_start = 5064
    _globals['_S2TINFERENCE']._serialized_end = 5241
    _globals['_ACOUSTICMODELS']._serialized_start = 5244
    _globals['_ACOUSTICMODELS']._serialized_end = 5738
    _globals['_S2TCLOUDSERVICEAMAZON']._serialized_start = 5741
    _globals['_S2TCLOUDSERVICEAMAZON']._serialized_end = 5946
    _globals['_S2TCLOUDSERVICEDEEPGRAM']._serialized_start = 5949
    _globals['_S2TCLOUDSERVICEDEEPGRAM']._serialized_end = 6112
    _globals['_S2TCLOUDSERVICEGOOGLE']._serialized_start = 6115
    _globals['_S2TCLOUDSERVICEGOOGLE']._serialized_end = 6340
    _globals['_S2TCLOUDSERVICEMICROSOFT']._serialized_start = 6342
    _globals['_S2TCLOUDSERVICEMICROSOFT']._serialized_end = 6458
    _globals['_WHISPER']._serialized_start = 6460
    _globals['_WHISPER']._serialized_end = 6538
    _globals['_WHISPERTRITON']._serialized_start = 6541
    _globals['_WHISPERTRITON']._serialized_end = 6755
    _globals['_WAV2VEC']._serialized_start = 6757
    _globals['_WAV2VEC']._serialized_end = 6803
    _globals['_WAV2VECTRITON']._serialized_start = 6806
    _globals['_WAV2VECTRITON']._serialized_end = 6988
    _globals['_PTFILES']._serialized_start = 6990
    _globals['_PTFILES']._serialized_end = 7027
    _globals['_CKPTFILE']._serialized_start = 7029
    _globals['_CKPTFILE']._serialized_end = 7053
    _globals['_LANGUAGEMODELS']._serialized_start = 7056
    _globals['_LANGUAGEMODELS']._serialized_end = 7192
    _globals['_STREAMINGSERVER']._serialized_start = 7195
    _globals['_STREAMINGSERVER']._serialized_end = 7340
    _globals['_STREAMINGSPEECHRECOGNITION']._serialized_start = 7343
    _globals['_STREAMINGSPEECHRECOGNITION']._serialized_end = 7507
    _globals['_VOICEACTIVITYDETECTION']._serialized_start = 7509
    _globals['_VOICEACTIVITYDETECTION']._serialized_end = 7612
    _globals['_PYANNOTE']._serialized_start = 7615
    _globals['_PYANNOTE']._serialized_end = 7776
    _globals['_POSTPROCESSING']._serialized_start = 7778
    _globals['_POSTPROCESSING']._serialized_end = 7865
    _globals['_POSTPROCESSORS']._serialized_start = 7867
    _globals['_POSTPROCESSORS']._serialized_end = 7977
    _globals['_SYMSPELL']._serialized_start = 7979
    _globals['_SYMSPELL']._serialized_end = 8069
    _globals['_S2TNORMALIZATION']._serialized_start = 8071
    _globals['_S2TNORMALIZATION']._serialized_end = 8125
    _globals['_LOGGING']._serialized_start = 8127
    _globals['_LOGGING']._serialized_end = 8164
    _globals['_LISTS2TLANGUAGEMODELSREQUEST']._serialized_start = 8166
    _globals['_LISTS2TLANGUAGEMODELSREQUEST']._serialized_end = 8209
    _globals['_LANGUAGEMODELPIPELINEID']._serialized_start = 8211
    _globals['_LANGUAGEMODELPIPELINEID']._serialized_end = 8278
    _globals['_LISTS2TLANGUAGEMODELSRESPONSE']._serialized_start = 8280
    _globals['_LISTS2TLANGUAGEMODELSRESPONSE']._serialized_end = 8373
    _globals['_CREATEUSERLANGUAGEMODELREQUEST']._serialized_start = 8375
    _globals['_CREATEUSERLANGUAGEMODELREQUEST']._serialized_end = 8436
    _globals['_DELETEUSERLANGUAGEMODELREQUEST']._serialized_start = 8438
    _globals['_DELETEUSERLANGUAGEMODELREQUEST']._serialized_end = 8499
    _globals['_ADDDATATOUSERLANGUAGEMODELREQUEST']._serialized_start = 8501
    _globals['_ADDDATATOUSERLANGUAGEMODELREQUEST']._serialized_end = 8586
    _globals['_TRAINUSERLANGUAGEMODELREQUEST']._serialized_start = 8588
    _globals['_TRAINUSERLANGUAGEMODELREQUEST']._serialized_end = 8663
    _globals['_SPEECH2TEXT']._serialized_start = 9037
    _globals['_SPEECH2TEXT']._serialized_end = 10425
# @@protoc_insertion_point(module_scope)
