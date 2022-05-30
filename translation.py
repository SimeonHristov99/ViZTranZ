"""Stores code used for Neural Machine Translation."""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "mt5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def run_model(input_string, **generator_args):
    input_ids = tokenizer.encode(input_string, return_tensors="pt")
    res = model.generate(input_ids, **generator_args)
    return tokenizer.batch_decode(res, skip_special_tokens=True)

print(run_model('This is a string'))

# from transformers import pipeline

# tr_de = pipeline('translation_en_to_de', model='mt5-small')
# tr_ru = pipeline('translation_en_to_ru', model='mt5-small')
# tr_bg = pipeline('translation_en_to_bg', model='mt5-small')

# res_de = tr_de('Dog')
# res_ru = tr_ru('Dog')
# res_bg = tr_bg('Dog')

# print(f'{res_de=}')
# print(f'{res_ru=}')
# print(f'{res_bg=}')