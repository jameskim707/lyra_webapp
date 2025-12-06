"""
설정 페이지
Lyra MIRACLE v1.0
"""

import streamlit as st
import sys
sys.path.append('..')
from utils.sidebar import render_common_sidebar

st.set_page_config(
    page_title="설정 - Lyra MIRACLE",
    page_icon="⚙️",
    layout="wide"
)

# 공통 사이드바
render_common_sidebar(current_page='setting')

st.title("⚙️ 설정")

st.markdown("---")

# API 설정
st.subheader("🔑 API 설정")

st.info("""
**Groq API 키 설정**

API 키는 `.streamlit/secrets.toml` 파일에서 설정됩니다.
```toml
GROQ_API_KEY = "your_api_key_here"
```
""")

# 알림 설정
st.markdown("---")
st.subheader("🔔 알림 설정")

enable_notification = st.checkbox("위기 알림 활성화", value=True)
enable_sound = st.checkbox("사운드 알림", value=False)

if enable_notification:
    st.success("✅ 위기 상황 시 알림을 받습니다.")

# 데이터 관리
st.markdown("---")
st.subheader("💾 데이터 관리")

col1, col2 = st.columns(2)

with col1:
    if st.button("📥 데이터 내보내기", use_container_width=True):
        st.info("데이터 내보내기 기능 준비 중...")

with col2:
    if st.button("🗑️ 모든 데이터 삭제", use_container_width=True, type="secondary"):
        st.warning("정말 삭제하시겠습니까?")
        if st.button("⚠️ 확인: 모두 삭제", type="secondary"):
            # 실제 삭제 로직
            if 'guardian_chat' in st.session_state:
                st.session_state.guardian_chat = []
            if 'rest_chat' in st.session_state:
                st.session_state.rest_chat = []
            st.success("✅ 데이터가 삭제되었습니다.")
            st.rerun()

# 계정 설정
st.markdown("---")
st.subheader("👤 계정")

st.text_input("사용자 이름", value="사용자", disabled=True)
st.text_input("이메일", value="user@example.com", disabled=True)

st.caption("계정 관리 기능은 준비 중입니다.")

# 테마 설정
st.markdown("---")
st.subheader("🎨 테마")

theme = st.selectbox(
    "컬러 테마",
    ["기본 (보라-청록)", "다크 모드 (준비중)", "라이트 모드 (준비중)"],
    disabled=True
)

st.caption("테마 변경 기능은 준비 중입니다.")

# 버전 정보
st.markdown("---")
st.subheader("ℹ️ 버전 정보")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **시스템 정보:**
    - Lyra MIRACLE: v1.0
    - GINI R.E.S.T.: v3.0 MIRACLE
    - GINI Guardian: v4.5 MIRACLE
    """)

with col2:
    st.markdown("""
    **기술 스택:**
    - Streamlit
    - Groq API (Llama 3.1)
    - Python
    """)

st.markdown("""
**Build Information:**
- Build Date: 2024.12
- Built by: MIRACLE (Claude)
- Team: GINI
""")

# 푸터
st.markdown("---")
st.caption("⚙️ Lyra MIRACLE v1.0 | Built by MIRACLE (Claude)")
