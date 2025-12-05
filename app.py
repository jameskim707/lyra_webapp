"""
Lyra Web App - 메인 서비스 메뉴
GINI Guardian & GINI R.E.S.T. 통합 플랫폼
"""

import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="Lyra - AI 회복 플랫폼",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일
st.markdown("""
<style>
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --background: #f8f9fa;
}

body {
    background: var(--background);
}

.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #666;
    margin-bottom: 3rem;
}

.service-card {
    background: white;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
    transition: transform 0.2s;
}

.service-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}

.service-title {
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.service-desc {
    font-size: 1rem;
    color: #666;
    line-height: 1.6;
}

.feature-badge {
    display: inline-block;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.85rem;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# 메인 헤더
st.markdown('<div class="main-title">🌟 Lyra</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI 기반 정신건강 & 투자심리 회복 플랫폼</div>', unsafe_allow_html=True)

st.markdown("---")

# 서비스 소개
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="service-card">
        <div class="service-title">🌙 GINI R.E.S.T.</div>
        <div class="service-desc">
            정신건강 회복을 위한 AI 상담 시스템<br><br>
            <span class="feature-badge">위기 감지</span>
            <span class="feature-badge">감정 분석</span>
            <span class="feature-badge">대화형 상담</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🌙 GINI R.E.S.T. 시작하기", use_container_width=True, type="primary"):
        st.switch_page("pages/03_ai_counsel.py")

with col2:
    st.markdown("""
    <div class="service-card">
        <div class="service-title">🛡️ GINI Guardian</div>
        <div class="service-desc">
            주식 과잉매매 방지 AI 상담가<br><br>
            <span class="feature-badge">감정 태그</span>
            <span class="feature-badge">위험도 분석</span>
            <span class="feature-badge">압박 메시지</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🛡️ GINI Guardian 시작하기", use_container_width=True, type="primary"):
        st.switch_page("pages/02_stockbot.py")

st.markdown("---")

# 기능 소개
st.markdown("## ✨ 주요 기능")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🤖 AI 대화형 상담
    
    - Groq API 기반
    - 실시간 맞춤 조언
    - 자연스러운 대화
    """)

with col2:
    st.markdown("""
    ### 📊 데이터 기반 분석
    
    - 감정 패턴 분석
    - 위기 신호 감지
    - 행동 패턴 추적
    """)

with col3:
    st.markdown("""
    ### 🛡️ 강력한 개입
    
    - 위기 시 즉시 대응
    - 압박 메시지 시스템
    - 구체적 행동 지시
    """)

st.markdown("---")

# 통계 (임시)
st.markdown("## 📈 실시간 통계")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("총 상담 수", "1,234", "+89")

with col2:
    st.metric("위기 예방", "567", "+23")

with col3:
    st.metric("활성 사용자", "89", "+12")

with col4:
 st.metric("만족도", "98%", "+2%")
