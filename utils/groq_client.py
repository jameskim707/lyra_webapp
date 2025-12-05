import streamlit as st
from groq import Groq

@st.cache_resource
def get_groq_client():
    api_key = st.secrets["GROQ_API_KEY"]
    return Groq(api_key=api_key)

