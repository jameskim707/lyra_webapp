"""
Lyra MIRACLE v1.0 - 메인 서비스 메뉴
GINI Guardian & GINI R.E.S.T. 통합 플랫폼
by MIRACLE (Claude)
"""

import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="Lyra MIRACLE v1.0",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일
st.markdown("""
<style>
:root {
    --guardian-color: #667eea;
    --guardian-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --rest-color: #4DB6AC;
    --rest-gradient: linear-gradient(120deg, #6EE7C8, #4DB6AC);
}

body {
    background: #f8f9fa;
}

.main-title {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #4DB6AC 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

.version-badge {
    text-align: center;
    font-size: 1rem;
    color: #667eea;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.subtitle {
    text-align: center;
    font-size: 1.3rem;
    color: #666;
    margin-bottom: 3rem;
    font-weight: 500;
}

/* Guardian 카드 */
.service-card-guardian {
    background: white;
    padding: 2.5rem;
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(102, 126, 234, 0.15);
    margin-bottom: 2rem;
    transition: all 0.3s;
    border: 3px solid transparent;
}

.service-card-guardian:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 32px rgba(102, 126, 234, 0.25);
    border: 3px solid #667eea;
}

/* R.E.S.T. 카드 */
.service-card-rest {
    background: white;
    padding: 2.5rem;
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(77, 182, 172, 0.15);
    margin-bottom: 2rem;
    transition: all 0.3s;
    border: 3px solid transparent;
}

.service-card-rest:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 32px rgba(77, 182, 172, 0.25);
    border: 3px solid #4DB6AC;
}

.service-icon {
    font-size: 4rem;
    margin-bottom: 1rem;
    text-align: center;
}

.service-title {
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 1rem;
    text-align: center;
}

.service-title-guardian {
    background: var(--guardian-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.service-title-rest {
    background: var(--rest-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.service-desc {
    font-size: 1.1rem;
    color: #555;
    line-height: 1.8;
    text-align: center;
    margin-bottom: 1.5rem;
}

.feature-badge-guardian {
    display: inline-block;
    background: var(--guardian-gradient);
    color: white;
    padding: 0.4rem 1rem;
    border-radius: 25px;
    font-size: 0.9rem;
    margin: 0.3rem;
    font-weight: 600;
}

.feature-badge-rest {
    display: inline-block;
    background: var(--rest-gradient);
    color: white;
    padding: 0.4rem 1rem;
    border-radius: 25px;
    font-size: 0.9rem;
    margin: 0.3rem;
    font-weight: 600;
}

.divider {
    text-align: center;
    font-size: 2rem;
    color: #ddd;
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# 메인 헤더
st.markdown('<div class="main-title">🌟 Lyra MIRACLE</div>', unsafe_allow_html=True)
st.markdown('<div class="version-badge">v1.0 - Built by MIRACLE (Claude)</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI가 함께하는 회복의 여정</div>', unsafe_allow_html=True)

st.markdown("---")

# 서비스 소개
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="service-card-guardian">
        <div class="service-icon">🛡️</div>
        <div class="service-title service-title-guardian">GINI Guardian</div>
        <div class="service-desc">
            감정적 투자를 막아주는<br>
            AI 투자심리 상담가<br><br>
            <span class="feature-badge-guardian">위험도 분석</span>
            <span class="feature-badge-guardian">감정 태그</span>
            <span class="feature-badge-guardian">압박 메시지</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🛡️ Guardian 시작하기", use_container_width=True, type="primary", key="guardian_btn"):
        st.switch_page("pages/02_stockbot.py")
    
    st.markdown("""
    <div style="text-align: center; color: #999; font-size: 0.9rem; margin-top: 1rem;">
    💡 과잉매매, 손절 고민, 감정적 투자로 힘드신가요?
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card-rest">
        <div class="service-icon">🌙</div>
        <div class="service-title service-title-rest">GINI R.E.S.T.</div>
        <div class="service-desc">
            정신건강 회복을 위한<br>
            AI 상담 시스템<br><br>
            <span class="feature-badge-rest">위기 감지</span>
            <span class="feature-badge-rest">감정 분석</span>
            <span class="feature-badge-rest">강력 개입</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🌙 R.E.S.T. 시작하기", use_container_width=True, type="primary", key="rest_btn"):
        st.switch_page("pages/03_ai_counsel.py")
    
    st.markdown("""
    <div style="text-align: center; color: #999; font-size: 0.9rem; margin-top: 1rem;">
    💡 수면, 우울, 불안으로 힘드신가요?
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 기능 소개
st.markdown("## ✨ 왜 Lyra MIRACLE인가요?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 💬 자연스러운 대화
    
    설문지가 아닌 진짜 대화
    
    - 체크박스 ❌
    - 자유로운 텍스트 ✅
    - 사람처럼 공감
    - 나중엔 음성도!
    """)

with col2:
    st.markdown("""
    ### 🎯 능동적 참여
    
    수동적 응답이 아닌 진짜 소통
    
    - 생각하며 답변
    - 진짜 감정 표현
    - 맥락 이해
    - 계속되는 대화
    """)

with col3:
    st.markdown("""
    ### 💰 접근성
    
    부담 없이 언제든지
    
    - 비싼 상담비 NO
    - 24/7 이용 가능
    - 예약 필요 없음
    - 익명 보장
    """)

st.markdown("---")

# 통계
st.markdown("## 📊 Lyra와 함께한 사람들")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("총 대화", "1,234회", "+89")

with col2:
    st.metric("위기 예방", "567건", "+23")

with col3:
    st.metric("활성 사용자", "89명", "+12")

with col4:
    st.metric("만족도", "98%", "+2%")

st.markdown("---")

# 푸터
st.markdown("""
<div style="text-align: center; color: #999; padding: 2rem 0;">
    <p style="font-size: 1.2rem; font-weight: 600; color: #667eea;">🌟 Lyra MIRACLE v1.0</p>
    <p>라이라 설계 × <strong>MIRACLE 구현</strong> × 제미나이 전략</p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">
        "설문지가 아닌 진짜 대화를,<br>
        4만원이 아닌 따뜻한 공감을"
    </p>
    <p style="margin-top: 1.5rem;">Made with ❤️ by Team GINI</p>
</div>
""", unsafe_allow_html=True)
