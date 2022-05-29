"""Main application."""

import streamlit as st

import constants
from helpers import build_chart, get_langs, get_upl_file, toggle_results
from s3_manager import get_results, upload

################################################################################
# Title
################################################################################

st.set_page_config(
    layout='wide',
    page_icon='📷',
    page_title='ViZTranZ'
)

st.title(f'📷 ➡ 📖')
st.title('ViZTranZ')
st.header('A Visual Translation Service in Two Simple Steps!')


################################################################################
# Sidebar
################################################################################

option = st.sidebar.selectbox(
    'Which mode would you like to use?',
    ('Offline', 'AWS'),
    on_change=toggle_results
)
constants.mode = option
st.sidebar.write(f'Currently in mode `{option}`')


################################################################################
# Main menu
################################################################################

in_mem_file = get_upl_file()

if in_mem_file is not None:
    st.image(in_mem_file, 'Your image')

    langs = get_langs()

    if langs is not None and len(langs) > 0 \
        and st.button(
            'Translate!',
            help='Click this button to begin the translation process'
    ):
        if constants.mode == 'AWS' and constants.results is None:
            print(' ... uploading new image ... ')
            file_name = upload(in_mem_file)
            constants.results = get_results(file_name)
        elif constants.mode == 'Offline':
            constants.results = constants.get_sample_results()

        build_chart(langs)
