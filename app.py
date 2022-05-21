import streamlit as st

st.set_page_config(page_icon='📷', page_title='ViZTranZ')


def show_welcome():
    st.title(f'📷 ➡ 📖')
    st.title('ViZTranZ')
    st.header('A Visual Translation Service')


def get_upl_file():
    st.subheader('Step 1: Upload an image')

    result = st.file_uploader(
        '',
        help='Upload one picture by clicking the "Browse files" button\
             or dragging the image.'
    )

    if result is not None:
        bytes_data = result.getvalue()
        return bytes_data


def get_langs():
    st.subheader('Step 2: Choose language to translate to')

    options = st.multiselect(
        'Pick languages in which to translate',
        ['Bulgarian', 'German', 'Russian'],
        ['Bulgarian']
    )

    return options


def main():
    show_welcome()

    im = get_upl_file()

    if im is not None:
        st.image(im, 'Your image')

        options = get_langs()

        if options is not None and len(options) > 0:
            st.write(f'Translate to {options}')


if __name__ == '__main__':
    main()
