"""
홈 대시보드
Lyra MIRACLE v1.0
"""

import streamlit as st
import sys
sys.path.append('..')
from utils.sidebar import render_common_sidebar

st.set_page_config(
    page_title="홈 - Lyra MIRACLE",
    page_icon="🏠",
    layout="wide"
)

# 공통 사이드바
render_common_sidebar(current_page='home')

# CSS
st.markdown("""
<style>
.dashboard-header {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #4DB6AC 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

.welcome-text {
    text-align: center;
    color: #666;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

.quick-access-card {
    background: white;
    padding: 1.5rem;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 1rem;
    transition: transform 0.2s;
}

.quick-access-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown('<div class="dashboard-header">🏠 홈 대시보드</div>', unsafe_allow_html=True)
st.markdown('<div class="welcome-text">환영합니다! Lyra MIRACLE에서 회복의 여정을 시작하세요.</div>', unsafe_allow_html=True)

st.markdown("---")

# 빠른 접근
st.subheader("🚀 빠른 시작")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="quick-access-card">
        <h3>🛡️ GINI Guardian</h3>
        <p>주식 투자로 힘드신가요?<br>
        감정적 투자를 막아드립니다.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🛡️ Guardian 시작", use_container_width=True, type="primary"):
        st.switch_page("pages/02_stockbot.py")

with col2:
    st.markdown("""
    <div class="quick-access-card">
        <h3>🌙 GINI R.E.S.T.</h3>
        <p>마음이 힘드신가요?<br>
        정신건강 회복을 도와드립니다.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🌙 R.E.S.T. 시작", use_container_width=True, type="primary"):
        st.switch_page("pages/03_ai_counsel.py")

st.markdown("---")

# 최근 활동
st.subheader("📊 나의 활동")

col1, col2, col3 = st.columns(3)

# Guardian 활동
guardian_count = len(st.session_state.get('guardian_chat', []))
with col1:
    st.metric("Guardian 대화", f"{guardian_count}회", "최근 세션")

# R.E.S.T. 활동
rest_count = len(st.session_state.get('rest_chat', []))
with col2:
    st.metric("R.E.S.T. 대화", f"{rest_count}회", "최근 세션")

# 감정 상태
emotion = st.session_state.get('emotion_score', 1)
with col3:
    emotion_labels = {1: "😊 안정", 2: "🙂 주의", 3: "😐 위험", 4: "😟 심각", 5: "😱 위기"}
    st.metric("현재 감정", f"E{emotion}", emotion_labels.get(emotion, ""))

st.markdown("---")

# 오늘의 팁
st.subheader("💡 오늘의 조언")

import random

tips = [
    "💙 **정신건강**: 충분한 수면은 정신건강의 기본입니다. 오늘은 일찍 주무세요!",
    "🛡️ **투자심리**: 손실이 난다고 해서 바로 손절하지 마세요. 냉정하게 생각할 시간을 가지세요.",
    "💙 **정신건강**: 하루 10분 명상으로 마음을 안정시킬 수 있습니다.",
    "🛡️ **투자심리**: 감정적 판단은 금물! 투자 전 3번 생각하세요.",
    "💙 **정신건강**: 햇빛을 쐬는 것만으로도 기분이 좋아질 수 있어요.",
    "🛡️ **투자심리**: 물타기는 신중하게! 계획 없는 물타기는 위험합니다.",
]

st.info(random.choice(tips))

st.markdown("---")

# 도움말
st.subheader("❓ 도움이 필요하신가요?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **🆘 위기 상황**
    
    즉시 전문가 도움이 필요하시다면:
    - 📞 1577-0199 (정신건강상담)
    - 📞 1393 (자살예방)
    - 📞 1588-9191 (생명의전화)
    """)

with col2:
    st.markdown("""
    **📚 사용 가이드**
    
    - [⚙️ 설정 보기](pages/04_setting.py)
    - [ℹ️ 서비스 소개](pages/05_about.py)
    - [💬 자유롭게 대화하세요!](#)
    """)

st.markdown("---")

# 푸터
st.caption("🏠 Lyra MIRACLE v1.0 | Built by MIRACLE (Claude)")
