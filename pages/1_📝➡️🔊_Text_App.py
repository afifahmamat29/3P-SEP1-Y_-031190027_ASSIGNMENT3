import streamlit as st
from gtts import gTTS

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

st.title('Text To Speech')

lang_dict = {'English':'en','French':'fr','Malay':'ms','Mandarin':'zh-CN','Tamil':'ta' }
lang_key= list(lang_dict.keys())

acc_dict = {'English (Australia)':'com.au','English (United Kingdom)':'co.uk','English (United States)':'us',\
        'English (Canada)':'ca','English (India)':'co.in','English (Ireland)':'ie','English (South Africa)':'co.za','Malay':'ms',\
        'French (Canada)':'ca','French (France)':'fr',	'Mandarin':'ch','Tamil':'co.in'}

acc_key= list(acc_dict.keys())
lang_option = st.selectbox('Language',lang_key)
acc_option = st.selectbox('Accent',acc_key)

txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair,
    ''')

if st.button('Play'):
    tts = gTTS(txt, lang=lang_dict[lang_option], tld=acc_dict[acc_option])
    tts.save('hello.mp3')
    st.audio('hello.mp3', format='audio/ogg')
    st.write(txt)
    
