"""Stores code used for Neural Machine Translation."""

from transformers import pipeline

tr_ru = pipeline('translation_en_to_ru', model='t5-small')
tr_de = pipeline('translation_en_to_de', model='t5-small')
tr_bg = pipeline('translation_de_to_bg', model='opus-mt-de-bg')

res_de = tr_de('Dog')
res_ru = tr_ru('Dog')
res_bg = tr_bg('Hunde')

print(f'{res_de=}')
print(f'{res_ru=}')
print(f'{res_bg=}')