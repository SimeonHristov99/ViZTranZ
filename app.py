"""Main application."""

import io

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

import constants
from s3_manager import get_results, upload

st.set_page_config(page_icon='📷', page_title='ViZTranZ')


def toggle_results():
    """Delete stored results to signal new image upload."""
    constants.results = None


def show_welcome():
    """Display the welcome message and description of application."""
    st.title(f'📷 ➡ 📖')
    st.title('ViZTranZ')
    st.header('A Visual Translation Service')


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
        st.write('ERROR: No `results` for image found!')
        return

    if len(langs) < 1:
        st.write('Please select at least one language it which to translate!')
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


def main():
    """Handle process of using the application."""
    show_welcome()

    in_mem_file = get_upl_file()

    if in_mem_file is not None:
        st.image(in_mem_file, 'Your image')

        langs = get_langs()

        if langs is not None and len(langs) > 0:
            if st.button('Translate!', help='Click this button to begin the \
                translation process'):
                if constants.results is None:
                    print(' ... uploading new image ... ')
                    # constants.results = constants.get_res()
                    file_name = upload(in_mem_file)
                    constants.results = get_results(file_name)

                build_chart(langs)


if __name__ == '__main__':
    main()
