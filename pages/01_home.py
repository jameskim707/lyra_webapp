"""
홈 페이지
Lyra MIRACLE v1.0
"""

import streamlit as st

st.set_page_config(
    page_title="Lyra MIRACLE - 홈",
    page_icon="🏠",
    layout="wide"
)

# 메인으로 리디렉션
st.switch_page("app.py")
