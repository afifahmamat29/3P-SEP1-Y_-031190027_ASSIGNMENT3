import streamlit as st
from gtts import gTTS
import time
import pandas as pd
import easyocr

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

if 'reader5' not in st.session_state:
    st.session_state.reader5 = easyocr.Reader(['en','ch_sim'])
    
st.title('OCR Application')

#for audio(gTTS)
lang_dict = {'Mandarin':'zh-CN','English':'en'}
lang_key= list(lang_dict.keys())

acc_dict = {'Mandarin':'ch','English (Australia)':'com.au'
,	'English (United Kingdom)':'co.uk'
,	'English (United States)':'us'
,	'English (Canada)':'ca'
,	'English (India)':'co.in'
,	'English (Ireland)':'ie'
,	'English (South Africa)':'co.za'

}
acc_key= list(acc_dict.keys())
lang_option = st.selectbox('Language',lang_key)
acc_option = st.selectbox('Accent',acc_key)

uploaded_file = st.file_uploader("Upload your picture", type=['png','jpg', 'jpeg'])
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    start_time = time.time()
    result = st.session_state.reader5.readtext(uploaded_file.getvalue())
    total_time = time.time() - start_time
    txt = "\n".join([item[1] for item in result])
    st.text(txt)
    st.caption(f'The processing of image to text took : {total_time:.3f} seconds')
    start_time = time.time()
    tts = gTTS(txt, lang=lang_dict[lang_option], tld=acc_dict[acc_option])
    tts.save('hello.mp3')
    st.audio('hello.mp3', format='audio/ogg')
    total_time = (time.time() - start_time)
    st.caption(f'The processing of text to audio took : {total_time:.3f} seconds')
    with st.expander("See Accuracy"):
        st.dataframe(pd.DataFrame(result,columns=['Pixel','Text','Accuracy'])[['Text', 'Accuracy', 'Pixel']])
