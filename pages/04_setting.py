"""
설정 페이지
Lyra MIRACLE v1.0
"""

import streamlit as st

st.set_page_config(
    page_title="설정 - Lyra MIRACLE",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ 설정")

st.markdown("---")

# API 설정
st.subheader("🔑 API 설정")

st.info("""
**Groq API 키 설정**

API 키는 `.streamlit/secrets.toml` 파일에서 설정됩니다.
```toml
