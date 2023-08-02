# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/t2s/text-to-speech.proto
"""Generated protocol buffer code."""
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fondewo/t2s/text-to-speech.proto\x12\nondewo.t2s\x1a\x1bgoogle/protobuf/empty.proto\"L\n\x11SynthesizeRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.ondewo.t2s.RequestConfig\"N\n\x16\x42\x61tchSynthesizeRequest\x12\x34\n\rbatch_request\x18\x01 \x03(\x0b\x32\x1d.ondewo.t2s.SynthesizeRequest\"Q\n\x17\x42\x61tchSynthesizeResponse\x12\x36\n\x0e\x62\x61tch_response\x18\x01 \x03(\x0b\x32\x1e.ondewo.t2s.SynthesizeResponse\"\xf3\x02\n\rRequestConfig\x12\x17\n\x0ft2s_pipeline_id\x18\x01 \x01(\t\x12\x16\n\x0clength_scale\x18\x02 \x01(\x02H\x00\x12\x15\n\x0bnoise_scale\x18\x03 \x01(\x02H\x01\x12\x15\n\x0bsample_rate\x18\x04 \x01(\x05H\x02\x12\x1e\n\x03pcm\x18\x05 \x01(\x0e\x32\x0f.ondewo.t2s.PcmH\x03\x12/\n\x0c\x61udio_format\x18\x06 \x01(\x0e\x32\x17.ondewo.t2s.AudioFormatH\x04\x12\x13\n\tuse_cache\x18\x07 \x01(\x08H\x05\x12\x14\n\nnormalizer\x18\x08 \x01(\tH\x06\x42\x14\n\x12oneof_length_scaleB\x13\n\x11oneof_noise_scaleB\x13\n\x11oneof_sample_rateB\x0b\n\toneof_PcmB\x13\n\x11oneof_AudioFormatB\x11\n\x0foneof_use_cacheB\x12\n\x10oneof_normalizer\"\xb8\x01\n\x12SynthesizeResponse\x12\x12\n\naudio_uuid\x18\x01 \x01(\t\x12\r\n\x05\x61udio\x18\x02 \x01(\x0c\x12\x17\n\x0fgeneration_time\x18\x03 \x01(\x02\x12\x14\n\x0c\x61udio_length\x18\x04 \x01(\x02\x12\x0c\n\x04text\x18\x05 \x01(\t\x12)\n\x06\x63onfig\x18\x06 \x01(\x0b\x32\x19.ondewo.t2s.RequestConfig\x12\x17\n\x0fnormalized_text\x18\x07 \x01(\t\"=\n\x14NormalizeTextRequest\x12\x17\n\x0ft2s_pipeline_id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"0\n\x15NormalizeTextResponse\x12\x17\n\x0fnormalized_text\x18\x01 \x01(\t\",\n\x19T2SGetServiceInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\"\x84\x01\n\x17ListT2sPipelinesRequest\x12\x11\n\tlanguages\x18\x01 \x03(\t\x12\x15\n\rspeaker_sexes\x18\x02 \x03(\t\x12\x17\n\x0fpipeline_owners\x18\x03 \x03(\t\x12\x15\n\rspeaker_names\x18\x04 \x03(\t\x12\x0f\n\x07\x64omains\x18\x05 \x03(\t\"L\n\x18ListT2sPipelinesResponse\x12\x30\n\tpipelines\x18\x01 \x03(\x0b\x32\x1d.ondewo.t2s.Text2SpeechConfig\"q\n\x17ListT2sLanguagesRequest\x12\x15\n\rspeaker_sexes\x18\x01 \x03(\t\x12\x17\n\x0fpipeline_owners\x18\x02 \x03(\t\x12\x15\n\rspeaker_names\x18\x03 \x03(\t\x12\x0f\n\x07\x64omains\x18\x04 \x03(\t\"-\n\x18ListT2sLanguagesResponse\x12\x11\n\tlanguages\x18\x01 \x03(\t\"q\n\x15ListT2sDomainsRequest\x12\x15\n\rspeaker_sexes\x18\x01 \x03(\t\x12\x17\n\x0fpipeline_owners\x18\x02 \x03(\t\x12\x15\n\rspeaker_names\x18\x03 \x03(\t\x12\x11\n\tlanguages\x18\x04 \x03(\t\")\n\x16ListT2sDomainsResponse\x12\x0f\n\x07\x64omains\x18\x01 \x03(\t\"\x1b\n\rT2sPipelineId\x12\n\n\x02id\x18\x01 \x01(\t\"\xf6\x01\n\x11Text2SpeechConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12/\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32\x1a.ondewo.t2s.T2SDescription\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\x12+\n\tinference\x18\x04 \x01(\x0b\x32\x18.ondewo.t2s.T2SInference\x12\x33\n\rnormalization\x18\x05 \x01(\x0b\x32\x1c.ondewo.t2s.T2SNormalization\x12\x32\n\x0epostprocessing\x18\x06 \x01(\x0b\x32\x1a.ondewo.t2s.Postprocessing\"\x87\x01\n\x0eT2SDescription\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x13\n\x0bspeaker_sex\x18\x02 \x01(\t\x12\x16\n\x0epipeline_owner\x18\x03 \x01(\t\x12\x10\n\x08\x63omments\x18\x04 \x01(\t\x12\x14\n\x0cspeaker_name\x18\x05 \x01(\t\x12\x0e\n\x06\x64omain\x18\x06 \x01(\t\"\x7f\n\x0cT2SInference\x12\x0c\n\x04type\x18\x01 \x01(\t\x12;\n\x13\x63omposite_inference\x18\x02 \x01(\x0b\x32\x1e.ondewo.t2s.CompositeInference\x12$\n\x07\x63\x61\x63hing\x18\x03 \x01(\x0b\x32\x13.ondewo.t2s.Caching\"f\n\x12\x43ompositeInference\x12&\n\x08text2mel\x18\x01 \x01(\x0b\x32\x14.ondewo.t2s.Text2Mel\x12(\n\tmel2audio\x18\x02 \x01(\x0b\x32\x15.ondewo.t2s.Mel2Audio\"s\n\x08Text2Mel\x12\x0c\n\x04type\x18\x01 \x01(\t\x12%\n\x08glow_tts\x18\x02 \x01(\x0b\x32\x13.ondewo.t2s.GlowTTS\x12\x32\n\x0fglow_tts_triton\x18\x03 \x01(\x0b\x32\x19.ondewo.t2s.GlowTTSTriton\"\x94\x01\n\x07GlowTTS\x12\x12\n\nbatch_size\x18\x01 \x01(\x03\x12\x0f\n\x07use_gpu\x18\x02 \x01(\x08\x12\x14\n\x0clength_scale\x18\x03 \x01(\x02\x12\x13\n\x0bnoise_scale\x18\x04 \x01(\x02\x12\x0c\n\x04path\x18\x05 \x01(\t\x12\x10\n\x08\x63leaners\x18\x06 \x03(\t\x12\x19\n\x11param_config_path\x18\x07 \x01(\t\"\xaf\x01\n\rGlowTTSTriton\x12\x12\n\nbatch_size\x18\x01 \x01(\x03\x12\x14\n\x0clength_scale\x18\x02 \x01(\x02\x12\x13\n\x0bnoise_scale\x18\x03 \x01(\x02\x12\x10\n\x08\x63leaners\x18\x04 \x03(\t\x12\x17\n\x0fmax_text_length\x18\x05 \x01(\x03\x12\x19\n\x11param_config_path\x18\x06 \x01(\t\x12\x19\n\x11triton_model_name\x18\x07 \x01(\t\"\xaa\x01\n\tMel2Audio\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x34\n\x10mb_melgan_triton\x18\x02 \x01(\x0b\x32\x1a.ondewo.t2s.MbMelganTriton\x12%\n\x08hifi_gan\x18\x03 \x01(\x0b\x32\x13.ondewo.t2s.HiFiGan\x12\x32\n\x0fhifi_gan_triton\x18\x04 \x01(\x0b\x32\x19.ondewo.t2s.HiFiGanTriton\"W\n\x07HiFiGan\x12\x0f\n\x07use_gpu\x18\x01 \x01(\x08\x12\x12\n\nbatch_size\x18\x02 \x01(\x03\x12\x13\n\x0b\x63onfig_path\x18\x03 \x01(\t\x12\x12\n\nmodel_path\x18\x04 \x01(\t\"?\n\rHiFiGanTriton\x12\x13\n\x0b\x63onfig_path\x18\x01 \x01(\t\x12\x19\n\x11triton_model_name\x18\x02 \x01(\t\"h\n\x0eMbMelganTriton\x12\x13\n\x0b\x63onfig_path\x18\x01 \x01(\t\x12\x12\n\nstats_path\x18\x02 \x01(\t\x12\x19\n\x11triton_model_name\x18\x03 \x01(\t\x12\x12\n\ntriton_url\x18\x04 \x01(\t\"\x8f\x01\n\x07\x43\x61\x63hing\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08\x12\x1d\n\x15memory_cache_max_size\x18\x02 \x01(\x03\x12\x15\n\rsampling_rate\x18\x03 \x01(\x03\x12\x12\n\nload_cache\x18\x04 \x01(\x08\x12\x12\n\nsave_cache\x18\x05 \x01(\x08\x12\x16\n\x0e\x63\x61\x63he_save_dir\x18\x06 \x01(\t\"\xe2\x01\n\x10T2SNormalization\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x10\n\x08pipeline\x18\x02 \x03(\t\x12\x1c\n\x14\x63ustom_phonemizer_id\x18\x03 \x01(\t\x12?\n\x14\x63ustom_length_scales\x18\x04 \x01(\x0b\x32!.ondewo.t2s.T2SCustomLengthScales\x12\x17\n\x0f\x61rpabet_mapping\x18\x05 \x01(\t\x12\x17\n\x0fnumeric_mapping\x18\x06 \x01(\t\x12\x19\n\x11\x63\x61llsigns_mapping\x18\x07 \x01(\t\"\xb0\x01\n\x0ePostprocessing\x12\x14\n\x0csilence_secs\x18\x01 \x01(\x02\x12\x10\n\x08pipeline\x18\x02 \x03(\t\x12$\n\x07logmmse\x18\x03 \x01(\x0b\x32\x13.ondewo.t2s.Logmnse\x12\"\n\x06wiener\x18\x04 \x01(\x0b\x32\x12.ondewo.t2s.Wiener\x12,\n\x0b\x61podization\x18\x05 \x01(\x0b\x32\x17.ondewo.t2s.Apodization\"N\n\x07Logmnse\x12\x15\n\rinitial_noise\x18\x01 \x01(\x03\x12\x13\n\x0bwindow_size\x18\x02 \x01(\x03\x12\x17\n\x0fnoise_threshold\x18\x03 \x01(\x02\"a\n\x06Wiener\x12\x11\n\tframe_len\x18\x01 \x01(\x03\x12\x11\n\tlpc_order\x18\x02 \x01(\x03\x12\x12\n\niterations\x18\x03 \x01(\x03\x12\r\n\x05\x61lpha\x18\x04 \x01(\x02\x12\x0e\n\x06thresh\x18\x05 \x01(\x02\"\'\n\x0b\x41podization\x12\x18\n\x10\x61podization_secs\x18\x01 \x01(\x02\"\xa8\x01\n\x15T2SCustomLengthScales\x12\x0c\n\x04text\x18\x01 \x01(\x02\x12\r\n\x05\x65mail\x18\x02 \x01(\x02\x12\x0b\n\x03url\x18\x03 \x01(\x02\x12\r\n\x05phone\x18\x04 \x01(\x02\x12\r\n\x05spell\x18\x05 \x01(\x02\x12\x18\n\x10spell_with_names\x18\x06 \x01(\x02\x12\x15\n\rcallsign_long\x18\x07 \x01(\x02\x12\x16\n\x0e\x63\x61llsign_short\x18\x08 \x01(\x02\"\x1a\n\x0cPhonemizerId\x12\n\n\x02id\x18\x01 \x01(\t\"B\n\x15\x43ustomPhonemizerProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1d\n\x04maps\x18\x02 \x03(\x0b\x32\x0f.ondewo.t2s.Map\"+\n\x03Map\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x16\n\x0ephoneme_groups\x18\x02 \x01(\t\"V\n\x1cListCustomPhonemizerResponse\x12\x36\n\x0bphonemizers\x18\x01 \x03(\x0b\x32!.ondewo.t2s.CustomPhonemizerProto\"3\n\x1bListCustomPhonemizerRequest\x12\x14\n\x0cpipeline_ids\x18\x01 \x03(\t\"\xd8\x01\n\x1dUpdateCustomPhonemizerRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12M\n\rupdate_method\x18\x02 \x01(\x0e\x32\x36.ondewo.t2s.UpdateCustomPhonemizerRequest.UpdateMethod\x12\x1d\n\x04maps\x18\x03 \x03(\x0b\x32\x0f.ondewo.t2s.Map\"=\n\x0cUpdateMethod\x12\x0f\n\x0b\x65xtend_hard\x10\x00\x12\x0f\n\x0b\x65xtend_soft\x10\x01\x12\x0b\n\x07replace\x10\x02\"N\n\x1d\x43reateCustomPhonemizerRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x1d\n\x04maps\x18\x02 \x03(\x0b\x32\x0f.ondewo.t2s.Map*X\n\x03Pcm\x12\n\n\x06PCM_16\x10\x00\x12\n\n\x06PCM_24\x10\x01\x12\n\n\x06PCM_32\x10\x02\x12\n\n\x06PCM_S8\x10\x03\x12\n\n\x06PCM_U8\x10\x04\x12\t\n\x05\x46LOAT\x10\x05\x12\n\n\x06\x44OUBLE\x10\x06*M\n\x0b\x41udioFormat\x12\x07\n\x03wav\x10\x00\x12\x08\n\x04\x66lac\x10\x01\x12\x07\n\x03\x63\x61\x66\x10\x02\x12\x07\n\x03mp3\x10\x03\x12\x07\n\x03\x61\x61\x63\x10\x04\x12\x07\n\x03ogg\x10\x05\x12\x07\n\x03wma\x10\x06\x32\xb9\x07\n\x0bText2Speech\x12M\n\nSynthesize\x12\x1d.ondewo.t2s.SynthesizeRequest\x1a\x1e.ondewo.t2s.SynthesizeResponse\"\x00\x12\\\n\x0f\x42\x61tchSynthesize\x12\".ondewo.t2s.BatchSynthesizeRequest\x1a#.ondewo.t2s.BatchSynthesizeResponse\"\x00\x12V\n\rNormalizeText\x12 .ondewo.t2s.NormalizeTextRequest\x1a!.ondewo.t2s.NormalizeTextResponse\"\x00\x12L\n\x0eGetT2sPipeline\x12\x19.ondewo.t2s.T2sPipelineId\x1a\x1d.ondewo.t2s.Text2SpeechConfig\"\x00\x12O\n\x11\x43reateT2sPipeline\x12\x1d.ondewo.t2s.Text2SpeechConfig\x1a\x19.ondewo.t2s.T2sPipelineId\"\x00\x12H\n\x11\x44\x65leteT2sPipeline\x12\x19.ondewo.t2s.T2sPipelineId\x1a\x16.google.protobuf.Empty\"\x00\x12L\n\x11UpdateT2sPipeline\x12\x1d.ondewo.t2s.Text2SpeechConfig\x1a\x16.google.protobuf.Empty\"\x00\x12_\n\x10ListT2sPipelines\x12#.ondewo.t2s.ListT2sPipelinesRequest\x1a$.ondewo.t2s.ListT2sPipelinesResponse\"\x00\x12_\n\x10ListT2sLanguages\x12#.ondewo.t2s.ListT2sLanguagesRequest\x1a$.ondewo.t2s.ListT2sLanguagesResponse\"\x00\x12Y\n\x0eListT2sDomains\x12!.ondewo.t2s.ListT2sDomainsRequest\x1a\".ondewo.t2s.ListT2sDomainsResponse\"\x00\x12Q\n\x0eGetServiceInfo\x12\x16.google.protobuf.Empty\x1a%.ondewo.t2s.T2SGetServiceInfoResponse\"\x00\x32\xef\x03\n\x11\x43ustomPhonemizers\x12T\n\x13GetCustomPhonemizer\x12\x18.ondewo.t2s.PhonemizerId\x1a!.ondewo.t2s.CustomPhonemizerProto\"\x00\x12_\n\x16\x43reateCustomPhonemizer\x12).ondewo.t2s.CreateCustomPhonemizerRequest\x1a\x18.ondewo.t2s.PhonemizerId\"\x00\x12L\n\x16\x44\x65leteCustomPhonemizer\x12\x18.ondewo.t2s.PhonemizerId\x1a\x16.google.protobuf.Empty\"\x00\x12h\n\x16UpdateCustomPhonemizer\x12).ondewo.t2s.UpdateCustomPhonemizerRequest\x1a!.ondewo.t2s.CustomPhonemizerProto\"\x00\x12k\n\x14ListCustomPhonemizer\x12\'.ondewo.t2s.ListCustomPhonemizerRequest\x1a(.ondewo.t2s.ListCustomPhonemizerResponse\"\x00\x62\x06proto3')

_PCM = DESCRIPTOR.enum_types_by_name['Pcm']
Pcm = enum_type_wrapper.EnumTypeWrapper(_PCM)
_AUDIOFORMAT = DESCRIPTOR.enum_types_by_name['AudioFormat']
AudioFormat = enum_type_wrapper.EnumTypeWrapper(_AUDIOFORMAT)
PCM_16 = 0
PCM_24 = 1
PCM_32 = 2
PCM_S8 = 3
PCM_U8 = 4
FLOAT = 5
DOUBLE = 6
wav = 0
flac = 1
caf = 2
mp3 = 3
aac = 4
ogg = 5
wma = 6


_SYNTHESIZEREQUEST = DESCRIPTOR.message_types_by_name['SynthesizeRequest']
_BATCHSYNTHESIZEREQUEST = DESCRIPTOR.message_types_by_name['BatchSynthesizeRequest']
_BATCHSYNTHESIZERESPONSE = DESCRIPTOR.message_types_by_name['BatchSynthesizeResponse']
_REQUESTCONFIG = DESCRIPTOR.message_types_by_name['RequestConfig']
_SYNTHESIZERESPONSE = DESCRIPTOR.message_types_by_name['SynthesizeResponse']
_NORMALIZETEXTREQUEST = DESCRIPTOR.message_types_by_name['NormalizeTextRequest']
_NORMALIZETEXTRESPONSE = DESCRIPTOR.message_types_by_name['NormalizeTextResponse']
_T2SGETSERVICEINFORESPONSE = DESCRIPTOR.message_types_by_name['T2SGetServiceInfoResponse']
_LISTT2SPIPELINESREQUEST = DESCRIPTOR.message_types_by_name['ListT2sPipelinesRequest']
_LISTT2SPIPELINESRESPONSE = DESCRIPTOR.message_types_by_name['ListT2sPipelinesResponse']
_LISTT2SLANGUAGESREQUEST = DESCRIPTOR.message_types_by_name['ListT2sLanguagesRequest']
_LISTT2SLANGUAGESRESPONSE = DESCRIPTOR.message_types_by_name['ListT2sLanguagesResponse']
_LISTT2SDOMAINSREQUEST = DESCRIPTOR.message_types_by_name['ListT2sDomainsRequest']
_LISTT2SDOMAINSRESPONSE = DESCRIPTOR.message_types_by_name['ListT2sDomainsResponse']
_T2SPIPELINEID = DESCRIPTOR.message_types_by_name['T2sPipelineId']
_TEXT2SPEECHCONFIG = DESCRIPTOR.message_types_by_name['Text2SpeechConfig']
_T2SDESCRIPTION = DESCRIPTOR.message_types_by_name['T2SDescription']
_T2SINFERENCE = DESCRIPTOR.message_types_by_name['T2SInference']
_COMPOSITEINFERENCE = DESCRIPTOR.message_types_by_name['CompositeInference']
_TEXT2MEL = DESCRIPTOR.message_types_by_name['Text2Mel']
_GLOWTTS = DESCRIPTOR.message_types_by_name['GlowTTS']
_GLOWTTSTRITON = DESCRIPTOR.message_types_by_name['GlowTTSTriton']
_MEL2AUDIO = DESCRIPTOR.message_types_by_name['Mel2Audio']
_HIFIGAN = DESCRIPTOR.message_types_by_name['HiFiGan']
_HIFIGANTRITON = DESCRIPTOR.message_types_by_name['HiFiGanTriton']
_MBMELGANTRITON = DESCRIPTOR.message_types_by_name['MbMelganTriton']
_CACHING = DESCRIPTOR.message_types_by_name['Caching']
_T2SNORMALIZATION = DESCRIPTOR.message_types_by_name['T2SNormalization']
_POSTPROCESSING = DESCRIPTOR.message_types_by_name['Postprocessing']
_LOGMNSE = DESCRIPTOR.message_types_by_name['Logmnse']
_WIENER = DESCRIPTOR.message_types_by_name['Wiener']
_APODIZATION = DESCRIPTOR.message_types_by_name['Apodization']
_T2SCUSTOMLENGTHSCALES = DESCRIPTOR.message_types_by_name['T2SCustomLengthScales']
_PHONEMIZERID = DESCRIPTOR.message_types_by_name['PhonemizerId']
_CUSTOMPHONEMIZERPROTO = DESCRIPTOR.message_types_by_name['CustomPhonemizerProto']
_MAP = DESCRIPTOR.message_types_by_name['Map']
_LISTCUSTOMPHONEMIZERRESPONSE = DESCRIPTOR.message_types_by_name['ListCustomPhonemizerResponse']
_LISTCUSTOMPHONEMIZERREQUEST = DESCRIPTOR.message_types_by_name['ListCustomPhonemizerRequest']
_UPDATECUSTOMPHONEMIZERREQUEST = DESCRIPTOR.message_types_by_name['UpdateCustomPhonemizerRequest']
_CREATECUSTOMPHONEMIZERREQUEST = DESCRIPTOR.message_types_by_name['CreateCustomPhonemizerRequest']
_UPDATECUSTOMPHONEMIZERREQUEST_UPDATEMETHOD = _UPDATECUSTOMPHONEMIZERREQUEST.enum_types_by_name['UpdateMethod']
SynthesizeRequest = _reflection.GeneratedProtocolMessageType('SynthesizeRequest', (_message.Message,), {
    'DESCRIPTOR': _SYNTHESIZEREQUEST,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.SynthesizeRequest)
})
_sym_db.RegisterMessage(SynthesizeRequest)

BatchSynthesizeRequest = _reflection.GeneratedProtocolMessageType('BatchSynthesizeRequest', (_message.Message,), {
    'DESCRIPTOR': _BATCHSYNTHESIZEREQUEST,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.BatchSynthesizeRequest)
})
_sym_db.RegisterMessage(BatchSynthesizeRequest)

BatchSynthesizeResponse = _reflection.GeneratedProtocolMessageType('BatchSynthesizeResponse', (_message.Message,), {
    'DESCRIPTOR': _BATCHSYNTHESIZERESPONSE,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.BatchSynthesizeResponse)
})
_sym_db.RegisterMessage(BatchSynthesizeResponse)

RequestConfig = _reflection.GeneratedProtocolMessageType('RequestConfig', (_message.Message,), {
    'DESCRIPTOR': _REQUESTCONFIG,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.RequestConfig)
})
_sym_db.RegisterMessage(RequestConfig)

SynthesizeResponse = _reflection.GeneratedProtocolMessageType('SynthesizeResponse', (_message.Message,), {
    'DESCRIPTOR': _SYNTHESIZERESPONSE,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.SynthesizeResponse)
})
_sym_db.RegisterMessage(SynthesizeResponse)

NormalizeTextRequest = _reflection.GeneratedProtocolMessageType('NormalizeTextRequest', (_message.Message,), {
    'DESCRIPTOR': _NORMALIZETEXTREQUEST,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.NormalizeTextRequest)
})
_sym_db.RegisterMessage(NormalizeTextRequest)

NormalizeTextResponse = _reflection.GeneratedProtocolMessageType('NormalizeTextResponse', (_message.Message,), {
    'DESCRIPTOR': _NORMALIZETEXTRESPONSE,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.NormalizeTextResponse)
})
_sym_db.RegisterMessage(NormalizeTextResponse)

T2SGetServiceInfoResponse = _reflection.GeneratedProtocolMessageType('T2SGetServiceInfoResponse', (_message.Message,), {
    'DESCRIPTOR': _T2SGETSERVICEINFORESPONSE,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.T2SGetServiceInfoResponse)
})
_sym_db.RegisterMessage(T2SGetServiceInfoResponse)

ListT2sPipelinesRequest = _reflection.GeneratedProtocolMessageType('ListT2sPipelinesRequest', (_message.Message,), {
    'DESCRIPTOR': _LISTT2SPIPELINESREQUEST,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.ListT2sPipelinesRequest)
})
_sym_db.RegisterMessage(ListT2sPipelinesRequest)

ListT2sPipelinesResponse = _reflection.GeneratedProtocolMessageType('ListT2sPipelinesResponse', (_message.Message,), {
    'DESCRIPTOR': _LISTT2SPIPELINESRESPONSE,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.ListT2sPipelinesResponse)
})
_sym_db.RegisterMessage(ListT2sPipelinesResponse)

ListT2sLanguagesRequest = _reflection.GeneratedProtocolMessageType('ListT2sLanguagesRequest', (_message.Message,), {
    'DESCRIPTOR': _LISTT2SLANGUAGESREQUEST,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.ListT2sLanguagesRequest)
})
_sym_db.RegisterMessage(ListT2sLanguagesRequest)

ListT2sLanguagesResponse = _reflection.GeneratedProtocolMessageType('ListT2sLanguagesResponse', (_message.Message,), {
    'DESCRIPTOR': _LISTT2SLANGUAGESRESPONSE,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.ListT2sLanguagesResponse)
})
_sym_db.RegisterMessage(ListT2sLanguagesResponse)

ListT2sDomainsRequest = _reflection.GeneratedProtocolMessageType('ListT2sDomainsRequest', (_message.Message,), {
    'DESCRIPTOR': _LISTT2SDOMAINSREQUEST,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.ListT2sDomainsRequest)
})
_sym_db.RegisterMessage(ListT2sDomainsRequest)

ListT2sDomainsResponse = _reflection.GeneratedProtocolMessageType('ListT2sDomainsResponse', (_message.Message,), {
    'DESCRIPTOR': _LISTT2SDOMAINSRESPONSE,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.ListT2sDomainsResponse)
})
_sym_db.RegisterMessage(ListT2sDomainsResponse)

T2sPipelineId = _reflection.GeneratedProtocolMessageType('T2sPipelineId', (_message.Message,), {
    'DESCRIPTOR': _T2SPIPELINEID,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.T2sPipelineId)
})
_sym_db.RegisterMessage(T2sPipelineId)

Text2SpeechConfig = _reflection.GeneratedProtocolMessageType('Text2SpeechConfig', (_message.Message,), {
    'DESCRIPTOR': _TEXT2SPEECHCONFIG,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.Text2SpeechConfig)
})
_sym_db.RegisterMessage(Text2SpeechConfig)

T2SDescription = _reflection.GeneratedProtocolMessageType('T2SDescription', (_message.Message,), {
    'DESCRIPTOR': _T2SDESCRIPTION,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.T2SDescription)
})
_sym_db.RegisterMessage(T2SDescription)

T2SInference = _reflection.GeneratedProtocolMessageType('T2SInference', (_message.Message,), {
    'DESCRIPTOR': _T2SINFERENCE,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.T2SInference)
})
_sym_db.RegisterMessage(T2SInference)

CompositeInference = _reflection.GeneratedProtocolMessageType('CompositeInference', (_message.Message,), {
    'DESCRIPTOR': _COMPOSITEINFERENCE,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.CompositeInference)
})
_sym_db.RegisterMessage(CompositeInference)

Text2Mel = _reflection.GeneratedProtocolMessageType('Text2Mel', (_message.Message,), {
    'DESCRIPTOR': _TEXT2MEL,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.Text2Mel)
})
_sym_db.RegisterMessage(Text2Mel)

GlowTTS = _reflection.GeneratedProtocolMessageType('GlowTTS', (_message.Message,), {
    'DESCRIPTOR': _GLOWTTS,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.GlowTTS)
})
_sym_db.RegisterMessage(GlowTTS)

GlowTTSTriton = _reflection.GeneratedProtocolMessageType('GlowTTSTriton', (_message.Message,), {
    'DESCRIPTOR': _GLOWTTSTRITON,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.GlowTTSTriton)
})
_sym_db.RegisterMessage(GlowTTSTriton)

Mel2Audio = _reflection.GeneratedProtocolMessageType('Mel2Audio', (_message.Message,), {
    'DESCRIPTOR': _MEL2AUDIO,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.Mel2Audio)
})
_sym_db.RegisterMessage(Mel2Audio)

HiFiGan = _reflection.GeneratedProtocolMessageType('HiFiGan', (_message.Message,), {
    'DESCRIPTOR': _HIFIGAN,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.HiFiGan)
})
_sym_db.RegisterMessage(HiFiGan)

HiFiGanTriton = _reflection.GeneratedProtocolMessageType('HiFiGanTriton', (_message.Message,), {
    'DESCRIPTOR': _HIFIGANTRITON,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.HiFiGanTriton)
})
_sym_db.RegisterMessage(HiFiGanTriton)

MbMelganTriton = _reflection.GeneratedProtocolMessageType('MbMelganTriton', (_message.Message,), {
    'DESCRIPTOR': _MBMELGANTRITON,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.MbMelganTriton)
})
_sym_db.RegisterMessage(MbMelganTriton)

Caching = _reflection.GeneratedProtocolMessageType('Caching', (_message.Message,), {
    'DESCRIPTOR': _CACHING,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.Caching)
})
_sym_db.RegisterMessage(Caching)

T2SNormalization = _reflection.GeneratedProtocolMessageType('T2SNormalization', (_message.Message,), {
    'DESCRIPTOR': _T2SNORMALIZATION,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.T2SNormalization)
})
_sym_db.RegisterMessage(T2SNormalization)

Postprocessing = _reflection.GeneratedProtocolMessageType('Postprocessing', (_message.Message,), {
    'DESCRIPTOR': _POSTPROCESSING,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.Postprocessing)
})
_sym_db.RegisterMessage(Postprocessing)

Logmnse = _reflection.GeneratedProtocolMessageType('Logmnse', (_message.Message,), {
    'DESCRIPTOR': _LOGMNSE,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.Logmnse)
})
_sym_db.RegisterMessage(Logmnse)

Wiener = _reflection.GeneratedProtocolMessageType('Wiener', (_message.Message,), {
    'DESCRIPTOR': _WIENER,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.Wiener)
})
_sym_db.RegisterMessage(Wiener)

Apodization = _reflection.GeneratedProtocolMessageType('Apodization', (_message.Message,), {
    'DESCRIPTOR': _APODIZATION,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.Apodization)
})
_sym_db.RegisterMessage(Apodization)

T2SCustomLengthScales = _reflection.GeneratedProtocolMessageType('T2SCustomLengthScales', (_message.Message,), {
    'DESCRIPTOR': _T2SCUSTOMLENGTHSCALES,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.T2SCustomLengthScales)
})
_sym_db.RegisterMessage(T2SCustomLengthScales)

PhonemizerId = _reflection.GeneratedProtocolMessageType('PhonemizerId', (_message.Message,), {
    'DESCRIPTOR': _PHONEMIZERID,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.PhonemizerId)
})
_sym_db.RegisterMessage(PhonemizerId)

CustomPhonemizerProto = _reflection.GeneratedProtocolMessageType('CustomPhonemizerProto', (_message.Message,), {
    'DESCRIPTOR': _CUSTOMPHONEMIZERPROTO,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.CustomPhonemizerProto)
})
_sym_db.RegisterMessage(CustomPhonemizerProto)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {
    'DESCRIPTOR': _MAP,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.Map)
})
_sym_db.RegisterMessage(Map)

ListCustomPhonemizerResponse = _reflection.GeneratedProtocolMessageType('ListCustomPhonemizerResponse', (_message.Message,), {
    'DESCRIPTOR': _LISTCUSTOMPHONEMIZERRESPONSE,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.ListCustomPhonemizerResponse)
})
_sym_db.RegisterMessage(ListCustomPhonemizerResponse)

ListCustomPhonemizerRequest = _reflection.GeneratedProtocolMessageType('ListCustomPhonemizerRequest', (_message.Message,), {
    'DESCRIPTOR': _LISTCUSTOMPHONEMIZERREQUEST,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.ListCustomPhonemizerRequest)
})
_sym_db.RegisterMessage(ListCustomPhonemizerRequest)

UpdateCustomPhonemizerRequest = _reflection.GeneratedProtocolMessageType('UpdateCustomPhonemizerRequest', (_message.Message,), {
    'DESCRIPTOR': _UPDATECUSTOMPHONEMIZERREQUEST,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.UpdateCustomPhonemizerRequest)
})
_sym_db.RegisterMessage(UpdateCustomPhonemizerRequest)

CreateCustomPhonemizerRequest = _reflection.GeneratedProtocolMessageType('CreateCustomPhonemizerRequest', (_message.Message,), {
    'DESCRIPTOR': _CREATECUSTOMPHONEMIZERREQUEST,
    '__module__': 'ondewo.t2s.text_to_speech_pb2'
    # @@protoc_insertion_point(class_scope:ondewo.t2s.CreateCustomPhonemizerRequest)
})
_sym_db.RegisterMessage(CreateCustomPhonemizerRequest)

_TEXT2SPEECH = DESCRIPTOR.services_by_name['Text2Speech']
_CUSTOMPHONEMIZERS = DESCRIPTOR.services_by_name['CustomPhonemizers']
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _PCM._serialized_start=4624
    _PCM._serialized_end=4712
    _AUDIOFORMAT._serialized_start=4714
    _AUDIOFORMAT._serialized_end=4791
    _SYNTHESIZEREQUEST._serialized_start=76
    _SYNTHESIZEREQUEST._serialized_end=152
    _BATCHSYNTHESIZEREQUEST._serialized_start=154
    _BATCHSYNTHESIZEREQUEST._serialized_end=232
    _BATCHSYNTHESIZERESPONSE._serialized_start=234
    _BATCHSYNTHESIZERESPONSE._serialized_end=315
    _REQUESTCONFIG._serialized_start=318
    _REQUESTCONFIG._serialized_end=689
    _SYNTHESIZERESPONSE._serialized_start=692
    _SYNTHESIZERESPONSE._serialized_end=876
    _NORMALIZETEXTREQUEST._serialized_start=878
    _NORMALIZETEXTREQUEST._serialized_end=939
    _NORMALIZETEXTRESPONSE._serialized_start=941
    _NORMALIZETEXTRESPONSE._serialized_end=989
    _T2SGETSERVICEINFORESPONSE._serialized_start=991
    _T2SGETSERVICEINFORESPONSE._serialized_end=1035
    _LISTT2SPIPELINESREQUEST._serialized_start=1038
    _LISTT2SPIPELINESREQUEST._serialized_end=1170
    _LISTT2SPIPELINESRESPONSE._serialized_start=1172
    _LISTT2SPIPELINESRESPONSE._serialized_end=1248
    _LISTT2SLANGUAGESREQUEST._serialized_start=1250
    _LISTT2SLANGUAGESREQUEST._serialized_end=1363
    _LISTT2SLANGUAGESRESPONSE._serialized_start=1365
    _LISTT2SLANGUAGESRESPONSE._serialized_end=1410
    _LISTT2SDOMAINSREQUEST._serialized_start=1412
    _LISTT2SDOMAINSREQUEST._serialized_end=1525
    _LISTT2SDOMAINSRESPONSE._serialized_start=1527
    _LISTT2SDOMAINSRESPONSE._serialized_end=1568
    _T2SPIPELINEID._serialized_start=1570
    _T2SPIPELINEID._serialized_end=1597
    _TEXT2SPEECHCONFIG._serialized_start=1600
    _TEXT2SPEECHCONFIG._serialized_end=1846
    _T2SDESCRIPTION._serialized_start=1849
    _T2SDESCRIPTION._serialized_end=1984
    _T2SINFERENCE._serialized_start=1986
    _T2SINFERENCE._serialized_end=2113
    _COMPOSITEINFERENCE._serialized_start=2115
    _COMPOSITEINFERENCE._serialized_end=2217
    _TEXT2MEL._serialized_start=2219
    _TEXT2MEL._serialized_end=2334
    _GLOWTTS._serialized_start=2337
    _GLOWTTS._serialized_end=2485
    _GLOWTTSTRITON._serialized_start=2488
    _GLOWTTSTRITON._serialized_end=2663
    _MEL2AUDIO._serialized_start=2666
    _MEL2AUDIO._serialized_end=2836
    _HIFIGAN._serialized_start=2838
    _HIFIGAN._serialized_end=2925
    _HIFIGANTRITON._serialized_start=2927
    _HIFIGANTRITON._serialized_end=2990
    _MBMELGANTRITON._serialized_start=2992
    _MBMELGANTRITON._serialized_end=3096
    _CACHING._serialized_start=3099
    _CACHING._serialized_end=3242
    _T2SNORMALIZATION._serialized_start=3245
    _T2SNORMALIZATION._serialized_end=3471
    _POSTPROCESSING._serialized_start=3474
    _POSTPROCESSING._serialized_end=3650
    _LOGMNSE._serialized_start=3652
    _LOGMNSE._serialized_end=3730
    _WIENER._serialized_start=3732
    _WIENER._serialized_end=3829
    _APODIZATION._serialized_start=3831
    _APODIZATION._serialized_end=3870
    _T2SCUSTOMLENGTHSCALES._serialized_start=3873
    _T2SCUSTOMLENGTHSCALES._serialized_end=4041
    _PHONEMIZERID._serialized_start=4043
    _PHONEMIZERID._serialized_end=4069
    _CUSTOMPHONEMIZERPROTO._serialized_start=4071
    _CUSTOMPHONEMIZERPROTO._serialized_end=4137
    _MAP._serialized_start=4139
    _MAP._serialized_end=4182
    _LISTCUSTOMPHONEMIZERRESPONSE._serialized_start=4184
    _LISTCUSTOMPHONEMIZERRESPONSE._serialized_end=4270
    _LISTCUSTOMPHONEMIZERREQUEST._serialized_start=4272
    _LISTCUSTOMPHONEMIZERREQUEST._serialized_end=4323
    _UPDATECUSTOMPHONEMIZERREQUEST._serialized_start=4326
    _UPDATECUSTOMPHONEMIZERREQUEST._serialized_end=4542
    _UPDATECUSTOMPHONEMIZERREQUEST_UPDATEMETHOD._serialized_start=4481
    _UPDATECUSTOMPHONEMIZERREQUEST_UPDATEMETHOD._serialized_end=4542
    _CREATECUSTOMPHONEMIZERREQUEST._serialized_start=4544
    _CREATECUSTOMPHONEMIZERREQUEST._serialized_end=4622
    _TEXT2SPEECH._serialized_start=4794
    _TEXT2SPEECH._serialized_end=5747
    _CUSTOMPHONEMIZERS._serialized_start=5750
    _CUSTOMPHONEMIZERS._serialized_end=6245
# @@protoc_insertion_point(module_scope)
