"""
소개 페이지
Lyra MIRACLE v1.0
"""

import streamlit as st
import sys
sys.path.append('..')
from utils.sidebar import render_common_sidebar

st.set_page_config(
    page_title="About - Lyra MIRACLE",
    page_icon="ℹ️",
    layout="wide"
)

# 공통 사이드바
render_common_sidebar(current_page='about')

# CSS
st.markdown("""
<style>
.about-header {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #4DB6AC 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

.version-tag {
    text-align: center;
    color: #667eea;
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 2rem;
}

.team-card {
    background: white;
    padding: 1.5rem;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="about-header">ℹ️ About Lyra MIRACLE</div>', unsafe_allow_html=True)
st.markdown('<div class="version-tag">v1.0 - Built by MIRACLE (Claude)</div>', unsafe_allow_html=True)

st.markdown("---")

# 프로젝트 소개
st.subheader("🌟 Lyra MIRACLE란?")

st.markdown("""
**Lyra MIRACLE**은 AI 기반 정신건강 & 투자심리 회복 플랫폼입니다.

**탄생 배경:**
"정신건강 상담에 4만원짜리 설문지? 그냥 약만 받으려 했는데..."

이런 경험에서 시작되었습니다. 우리는 다음을 제공합니다:

- 🌙 **GINI R.E.S.T.**: 정신건강 회복 AI 상담
- 🛡️ **GINI Guardian**: 주식 과잉매매 방지 AI

**MIRACLE Edition**은 Groq API 기반 대화형 시스템으로 완전히 새롭게 구현되었습니다.
""")

st.markdown("---")

# 왜 MIRACLE인가?
st.subheader("💡 왜 Lyra MIRACLE인가요?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### ❌ 기존 방식의 문제
    
    - 📋 체크박스 설문지
    - 💰 비싼 상담비 (4만원+)
    - 🚪 접근성 낮음
    - 🤖 수동적, 기계적
    - ⏰ 예약 필요
    """)

with col2:
    st.markdown("""
    ### ✅ Lyra MIRACLE의 해결
    
    - 💬 자유로운 대화
    - 💙 무료/저렴한 이용
    - 📱 언제 어디서나
    - 🎯 능동적, 공감적
    - 🚀 즉시 이용 가능
    """)

st.markdown("---")

# 미션
st.subheader("🎯 우리의 미션")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 💙 정신건강 회복
    
    - 위기 신호 조기 감지
    - 강력한 개입 시스템
    - 24/7 AI 상담
    - 설문지가 아닌 진짜 대화
    """)

with col2:
    st.markdown("""
    ### 🛡️ 투자 심리 보호
    
    - 감정적 투자 방지
    - 위험도 실시간 분석
    - 압박 메시지 시스템
    - 포트폴리오 기반 상담
    """)

st.markdown("---")

# 팀 소개
st.subheader("👥 Team GINI")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="team-card">
    <h3>🎨 라이라 (Raira)</h3>
    <p><strong>Role:</strong> 설계 & UX</p>
    <p>사용자 경험과 시스템 설계를 담당합니다.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="team-card">
    <h3>💙 미라클 (MIRACLE)</h3>
    <p><strong>Role:</strong> 개발 & 구현</p>
    <p>AI 시스템 개발과 코드 구현을 담당합니다.</p>
    <p><em>Claude by Anthropic</em></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="team-card">
    <h3>🧠 제미나이 (Gemini)</h3>
    <p><strong>Role:</strong> 전략 & 로직</p>
    <p>개입 전략과 핵심 로직을 설계합니다.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 기술 스택
st.subheader("🛠️ 기술 스택")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Frontend
    - Streamlit
    - Python
    - HTML/CSS
    """)

with col2:
    st.markdown("""
    ### AI & Backend
    - Groq API (Llama 3.1-8b-instant)
    - GitHub
    - Streamlit Cloud
    """)

st.markdown("---")

# 연혁
st.subheader("📅 개발 연혁")

st.markdown("""
- **2024.11**: GINI Guardian v1.0 출시
- **2024.11**: GINI Guardian v4.4 완성
- **2024.12**: GINI R.E.S.T. v3.0 출시
- **2024.12**: Lyra 플랫폼 통합
- **2024.12**: Groq 대화형 전환 완료
- **2024.12**: **Lyra MIRACLE v1.0 출시** 🎉
""")

st.markdown("---")

# 연락처
st.subheader("📧 Contact")

st.info("""
**문의사항이 있으신가요?**

GitHub: [lyra_webapp](https://github.com/jameskim707/lyra_webapp)

Made with ❤️ by Team GINI
""")

st.markdown("---")

# 특별한 메시지
st.success("""
### 💙 우리의 약속

**"설문지가 아닌 진짜 대화를,**  
**4만원이 아닌 따뜻한 공감을"**

Lyra MIRACLE은 접근성과 공감을 최우선으로 합니다.
""")

# 라이센스
st.markdown("---")
st.caption("""
© 2024 Team GINI. All rights reserved.

**Lyra MIRACLE v1.0** - Built by MIRACLE (Claude)
""")
