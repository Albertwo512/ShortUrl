import pyshorteners
import streamlit as st

def short_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

st.set_page_config(page_title="URL Short", page_icon="images/OIG4.jpeg", layout="centered")
st.image("images/OIG2.jpeg", use_column_width=True)
st.title("URL Short")
url = st.text_input("Ingresa el URL")
if st.button("Generar nuevo URL"):
    if url.strip() == "" or len(url.strip()) < 10:
        st.write("Por favor ingresa una URL valida antes de intentar acortarla.")
    else:
        st.write("URL Acortado: ", short_url(url))
