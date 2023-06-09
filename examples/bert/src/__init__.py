# Copyright 2022 MosaicML Examples authors
# SPDX-License-Identifier: Apache-2.0

import torch

# yapf: disable
from examples.bert.src.bert_layers import (BertEmbeddings, BertEncoder,
                                           BertForMaskedLM,
                                           BertForSequenceClassification,
                                           BertGatedLinearUnitMLP, BertLayer,
                                           BertLMPredictionHead, BertModel,
                                           BertOnlyMLMHead, BertOnlyNSPHead,
                                           BertPooler,
                                           BertPredictionHeadTransform,
                                           BertSelfOutput, BertUnpadAttention,
                                           BertUnpadSelfAttention)
# yapf: enable
from examples.bert.src.bert_padding import (IndexFirstAxis, IndexPutFirstAxis,
                                            index_first_axis,
                                            index_put_first_axis, pad_input,
                                            unpad_input, unpad_input_only)
from examples.bert.src.configuration_bert import BertConfig

if torch.cuda.is_available():
    from examples.bert.src.flash_attn_triton import \
        flash_attn_func as flash_attn_func_bert # type: ignore
    from examples.bert.src.flash_attn_triton import \
        flash_attn_qkvpacked_func as flash_attn_qkvpacked_func_bert # type: ignore

from examples.bert.src.hf_bert import (create_hf_bert_classification,
                                       create_hf_bert_mlm)
from examples.bert.src.mosaic_bert import (create_mosaic_bert_classification,
                                           create_mosaic_bert_mlm)

__all__ = [
    'BertConfig',
    'BertEmbeddings',
    'BertEncoder',
    'BertForMaskedLM',
    'BertForSequenceClassification',
    'BertGatedLinearUnitMLP',
    'BertLayer',
    'BertLMPredictionHead',
    'BertModel',
    'BertOnlyMLMHead',
    'BertOnlyNSPHead',
    'BertPooler',
    'BertPredictionHeadTransform',
    'BertSelfOutput',
    'BertUnpadAttention',
    'BertUnpadSelfAttention',
    'IndexFirstAxis',
    'IndexPutFirstAxis',
    'index_first_axis',
    'index_put_first_axis',
    'pad_input',
    'unpad_input',
    'unpad_input_only',
    'create_hf_bert_classification',
    'create_hf_bert_mlm',
    'create_mosaic_bert_classification',
    'create_mosaic_bert_mlm',

    # These are commented out because they only exist if CUDA is available
    # 'flash_attn_func_bert',
    # 'flash_attn_qkvpacked_func_bert'
]
