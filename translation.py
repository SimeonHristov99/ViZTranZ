"""Stores code used for Neural Machine Translation."""

from transformers import pipeline

tr_ru = pipeline('translation_en_to_ru', model='opus-mt-en-ru')
tr_de = pipeline('translation_en_to_de', model='opus-mt-en-de')
tr_bg = pipeline('translation_en_to_bg', model='opus-mt-en-bg')

translators = {
    'bg': tr_bg,
    'de': tr_de,
    'ru': tr_ru,
}


def translate(model, text):
    """Return the translated text."""
    return model(text)[0]['translation_text']
