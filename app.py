"""Main application."""

import io

import streamlit as st
from PIL import Image

from s3_uploader import upload

st.set_page_config(page_icon='📷', page_title='ViZTranZ')


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
             or dragging the image.'
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
        ['Bulgarian', 'German', 'Russian'],
        ['Bulgarian']
    )

    return options


def main():
    """Handle process of using the application."""
    show_welcome()

    in_mem_file = get_upl_file()

    if in_mem_file is not None:
        st.image(in_mem_file, 'Your image')

        options = get_langs()

        if options is not None and len(options) > 0:
            st.write(f'Translate to {options}')

            if st.button('Translate!', help='Click this button to begin the \
                translation process'):
                if upload(in_mem_file):
                    st.write('Successful upload!')


if __name__ == '__main__':
    main()
