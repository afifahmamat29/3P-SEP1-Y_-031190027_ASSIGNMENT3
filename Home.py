import streamlit as st
from gtts import gTTS
from pypdf import PdfReader
import webbrowser

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

st.title('Text to Speech With OCR')
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Text To Speech")
   st.markdown('''<a href="http://localhost:8501/Text_App"> 
   <img src="https://raw.githubusercontent.com/afifahmamat29/WOU-SE-PROJECT/main/img/text%20to%20speech(transparent).png"  width="100%" height="100%" text-align: center;/></a>'''\
               ,unsafe_allow_html=True)
   
with col2:
   st.header("OCR Application")
   st.markdown('''<a href="http://localhost:8501/OCR_App"> 
   <img src="https://raw.githubusercontent.com/afifahmamat29/WOU-SE-PROJECT/main/img/OCR.png"  width="100%" height="100%" /></a>'''\
               ,unsafe_allow_html=True)
   s_col1, s_col2, s_col3 = st.columns(3)
   with s_col1:
      st.markdown('''<a href="http://localhost:8501/OCR_Bahasa"> 
   <img src="https://raw.githubusercontent.com/afifahmamat29/WOU-SE-PROJECT/main/img/1.png"  width="100%" height="100%" /></a>'''\
               ,unsafe_allow_html=True)
   with s_col2:
      st.markdown('''<a href="http://localhost:8501/OCR_Mandarin"> 
   <img src="https://raw.githubusercontent.com/afifahmamat29/WOU-SE-PROJECT/main/img/2.png"  width="100%" height="100%" /></a>'''\
               ,unsafe_allow_html=True)
   with s_col3:
      st.markdown('''<a href="http://localhost:8501/OCR_Tamil"> 
   <img src="https://raw.githubusercontent.com/afifahmamat29/WOU-SE-PROJECT/main/img/3.png"  width="100%" height="100%" /></a>'''\
               ,unsafe_allow_html=True)
   

with col3:
   st.header("PDF Application")
   st.markdown('''<a href="http://localhost:8501/PDF_App"> 
   <img src="https://raw.githubusercontent.com/afifahmamat29/WOU-SE-PROJECT/main/img/PDFTOSPEECH.png"  width="100%" height="100%" /></a>'''\
               ,unsafe_allow_html=True)
   


