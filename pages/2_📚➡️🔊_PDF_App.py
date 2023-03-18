import streamlit as st
from gtts import gTTS
from pypdf import PdfReader
import time

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title('PDF To Text App')

lang_dict = {'English':'en','French':'fr','Malay':'ms','Mandarin':'zh-CN','Tamil':'ta' }
lang_key= list(lang_dict.keys())

acc_dict = {'English (Australia)':'com.au','English (United Kingdom)':'co.uk','English (United States)':'us',\
        'English (Canada)':'ca','English (India)':'co.in','English (Ireland)':'ie','English (South Africa)':'co.za','Malay':'ms',\
        'French (Canada)':'ca','French (France)':'fr',	'Mandarin':'ch','Tamil':'co.in'}

acc_key= list(acc_dict.keys())
lang_option = st.selectbox('Language',lang_key)
acc_option = st.selectbox('Accent',acc_key)

uploaded_file = st.file_uploader("Choose a file", type="pdf")
if uploaded_file is not None:
    start_time = time.time()
    reader = PdfReader(uploaded_file)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    total_time = (time.time() - start_time)
    st.caption(f'The processing of PDF to text took : {total_time:.3f} seconds')
    st.text(text)
    start_time = time.time()
    tts = gTTS(text, lang=lang_dict[lang_option], tld=acc_dict[acc_option])
    tts.save('hello.mp3')
    st.audio('hello.mp3', format='audio/ogg')
    total_time = (time.time() - start_time)
    st.caption(f'The processing of text to audio took : {total_time:.3f} seconds')
