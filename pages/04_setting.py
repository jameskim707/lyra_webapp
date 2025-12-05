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
        if st.button("정말 삭제하시겠습니까?", type="secondary"):
            st.success("✅ 데이터가 삭제되었습니다.")

# 계정 설정
st.markdown("---")
st.subheader("👤 계정")

st.text_input("사용자 이름", value="사용자", disabled=True)
st.text_input("이메일", value="user@example.com", disabled=True)

st.caption("계정 관리 기능은 준비 중입니다.")

# 버전 정보
st.markdown("---")
st.subheader("ℹ️ 버전 정보")

st.markdown("""
- **Lyra MIRACLE**: v1.0
- **GINI R.E.S.T.**: v3.0 MIRACLE
- **GINI Guardian**: v4.5 MIRACLE
- **Build**: 2024.12
- **Built by**: MIRACLE (Claude)
""")

# 푸터
st.markdown("---")
st.caption("⚙️ Lyra MIRACLE v1.0 | Built by MIRACLE (Claude)")
