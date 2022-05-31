"""Stores helper functions."""

import io

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

from viztranz import constants
from viztranz.s3_manager import get_results, upload
from viztranz.translation import translate, translators


def toggle_results():
    """Delete stored results to signal new image upload."""
    constants.results = None


def get_upl_file():
    """Show menu to upload image and return uploaded image."""
    st.subheader('Step 1: Upload an image')

    result = st.file_uploader(
        '',
        help='Upload one picture by clicking the "Browse files" button\
             or dragging the image.',
        on_change=toggle_results
    )

    if result is not None:
        pil_image = Image.open(result)

        # saving file to an in-memory file
        in_mem_file = io.BytesIO()
        pil_image.save(in_mem_file, format=pil_image.format)
        in_mem_file.seek(0)

        return in_mem_file


def get_langs():
    """Show menu for choosing a language and return selection."""
    st.subheader('Step 2: Choose language(s) to translate to')

    options = st.multiselect(
        'Pick language(s) in which to translate',
        constants.SUPPORTED_LANGS,
        ['Bulgarian'],
    )

    return options


def build_chart(langs):
    """Create and display the bar chart with the confidence of the translations."""
    if constants.results is None:
        st.error('No translations for image found!')
        return

    if len(langs) < 1:
        st.info('Please select at least one language it which to translate!')
        return

    res_df = pd.DataFrame(constants.results, index=[
                          'Confidence'] + constants.SUPPORTED_LANGS).T
    res_df['Confidence'] = res_df['Confidence'].astype(float)

    for lang in langs:
        st.subheader(f'Results for {lang}')

        df = pd \
            .concat([res_df[lang], res_df['Confidence']], axis=1) \
            .nlargest(10, 'Confidence')

        df[lang] = df.index + ' => ' + df[lang]

        fig = px.bar(
            df.iloc[::-1],
            x='Confidence',
            y=lang,
            orientation='h',
            height=800,
        )

        fig.update_layout(
            font=dict(
                size=16,
            )
        )

        st.plotly_chart(fig, use_container_width=True)


def add_translations():
    """Create a dataframe from the results of the object detection."""
    classes = list(map(
        lambda x: x.decode('utf-8'),
        constants.results['detection_class_entities']
    ))

    constants.results = dict(
        zip(classes, constants.results['detection_scores'])
    )

    constants.results = {
        cls: [conf] + [translate(translator, cls)[:15]
                       for translator in translators.values()]
        for (cls, conf) in constants.results.items()
    }
