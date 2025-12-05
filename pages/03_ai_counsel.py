"""
GINI R.E.S.T. v3.0 MIRACLE - 정신건강 회복 AI
by MIRACLE (Claude)
"""

import streamlit as st
import sys
sys.path.append('..')
from utils.groq_client import get_groq_client
from datetime import datetime

st.set_page_config(
    page_title="GINI R.E.S.T. MIRACLE",
    page_icon="🌙",
    layout="wide"
)

# CSS
st.markdown("""
<style>
.main-header {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(120deg, #6EE7C8, #4DB6AC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

.version-tag {
    text-align: center;
    color: #4DB6AC;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.status-safe {
    background: #d4edda;
    border-left: 4px solid #28a745;
    padding: 1rem;
    border-radius: 5px;
    margin: 1rem 0;
}

.status-warning {
    background: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 1rem;
    border-radius: 5px;
    margin: 1rem 0;
}

.status-danger {
    background: #f8d7da;
    border-left: 4px solid #dc3545;
    padding: 1rem;
    border-radius: 5px;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown('<div class="main-header">🌙 GINI R.E.S.T.</div>', unsafe_allow_html=True)
st.markdown('<div class="version-tag">v3.0 MIRACLE Edition</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; color: #666; margin-bottom: 2rem;">정신건강 회복 AI 상담 시스템</div>', unsafe_allow_html=True)

# Session State 초기화
if 'rest_chat' not in st.session_state:
    st.session_state.rest_chat = []

if 'emotion_score' not in st.session_state:
    st.session_state.emotion_score = 1  # E1~E5

if 'crisis_count' not in st.session_state:
    st.session_state.crisis_count = 0

# Groq 클라이언트
groq_client = get_groq_client()

# 인트로
st.info("""
💡 **GINI R.E.S.T. MIRACLE는:**
- 정신건강 회복을 위한 AI 상담 시스템입니다
- 감정 패턴을 분석합니다 (E1~E5)
- 위기 신호를 감지합니다
- 강력한 개입으로 도와드립니다
""")

st.markdown("---")

# 사이드바 - 상태
with st.sidebar:
    st.markdown("### 📊 현재 상태")
    
    # 감정 레벨
    e_score = st.session_state.emotion_score
    e_colors = {1: "🟢", 2: "🟡", 3: "🟠", 4: "🔴", 5: "🚨"}
    e_labels = {1: "안정", 2: "주의", 3: "위험", 4: "심각", 5: "위기"}
    
    st.metric(
        "감정 레벨",
        f"E{e_score}",
        e_labels[e_score]
    )
    
    st.markdown(f"{e_colors[e_score]} {e_labels[e_score]}")
    
    st.markdown("---")
    
    st.metric("위기 신호", f"{st.session_state.crisis_count}회", "최근 7일")
    
    st.markdown("---")
    
    if st.button("🗑️ 대화 내역 지우기", use_container_width=True):
        st.session_state.rest_chat = []
        st.rerun()
    
    st.markdown("---")
    
    st.markdown("""
    **⚠️ 응급 연락처**
    - 📞 1577-0199
    - 📞 1393
    - 📞 1588-9191
    """)

# 채팅 히스토리
for msg in st.session_state.rest_chat:
    with st.chat_message(msg['role']):
        st.write(msg['content'])
        
        # 메타 정보
        if msg['role'] == 'assistant' and 'meta' in msg:
            meta = msg['meta']
            
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"💭 감정: E{meta.get('emotion', 1)}")
            with col2:
                if meta.get('tone'):
                    st.caption(f"🎯 톤: {meta['tone']}")

# 사용자 입력
user_input = st.chat_input("💬 무엇이든 편하게 이야기해주세요...")

if user_input:
    # 사용자 메시지 추가
    st.session_state.rest_chat.append({
        'role': 'user',
        'content': user_input
    })
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # 위기 키워드 체크 (간단 버전)
    crisis_keywords = ['죽고', '자살', '끝', '포기', '의미없', '소용없']
    has_crisis = any(keyword in user_input for keyword in crisis_keywords)
    
    if has_crisis:
        st.session_state.crisis_count += 1
        st.session_state.emotion_score = 5
    
    # System Prompt
    e_score = st.session_state.emotion_score
    crisis_count = st.session_state.crisis_count
    
    # Tone 결정
    if e_score >= 5 or crisis_count >= 3:
        tone = "Crisis"
        tone_desc = "즉각적이고 단호하게. 전문가 연락처(1577-0199) 제공."
    elif e_score >= 3:
        tone = "Directive"
        tone_desc = "단호하지만 공감적으로. 명확한 행동 지시."
    elif e_score >= 2:
        tone = "Neutral"
        tone_desc = "균형잡힌 어조. 공감과 조언."
    else:
        tone = "Soft"
        tone_desc = "따뜻하고 지지적으로."
    
    system_prompt = f"""당신은 GINI R.E.S.T. 정신건강 회복 AI 상담사입니다.

**현재 상태:**
- 감정 레벨: E{e_score}
- 위기 신호: {crisis_count}회

**적용 톤:** {tone}
{tone_desc}

**원칙:**
1. 따뜻하고 공감적인 대화
2. 구체적이고 실행 가능한 조언
3. 짧고 명확한 답변 (3-5문장)
4. 위기 시 즉각 대응
"""
    
    # 메시지 구성
    messages = [{"role": "system", "content": system_prompt}]
    
    for msg in st.session_state.rest_chat[-10:]:
        messages.append({
            "role": msg['role'],
            "content": msg['content']
        })
    
    # AI 응답
    with st.chat_message("assistant"):
        with st.spinner("💭 생각 중..."):
            response, _ = groq_client.chat(messages)
            
            # 위기 시 추가 메시지
            if tone == "Crisis":
                response = f"""🚨 **위기 상태 감지**

{response}

**지금 바로 도움 받으세요:**
- 📞 정신건강 상담: 1577-0199
- 📞 자살예방: 1393
- 📞 생명의 전화: 1588-9191
"""
            
            st.write(response)
            
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"💭 감정: E{e_score}")
            with col2:
                st.caption(f"🎯 톤: {tone}")
    
    # AI 응답 추가
    st.session_state.rest_chat.append({
        'role': 'assistant',
        'content': response,
        'meta': {
            'emotion': e_score,
            'tone': tone,
            'crisis': has_crisis
        }
    })
    
    # 감정 점수 조정 (간단 버전)
    if has_crisis:
        st.session_state.emotion_score = 5
    elif '힘들' in user_input or '우울' in user_input:
        st.session_state.emotion_score = min(5, st.session_state.emotion_score + 1)
    elif '좋아' in user_input or '괜찮' in user_input:
        st.session_state.emotion_score = max(1, st.session_state.emotion_score - 1)
    
    st.rerun()

# 안내
st.markdown("---")

# 상태 표시
e_score = st.session_state.emotion_score

if e_score == 1:
    st.markdown("""
    <div class="status-safe">
    <strong>✅ 안정 상태</strong><br>
    현재 상태가 좋습니다. 계속 잘 유지하세요!
    </div>
    """, unsafe_allow_html=True)
elif e_score <= 3:
    st.markdown("""
    <div class="status-warning">
    <strong>⚠️ 주의 필요</strong><br>
    조금 주의가 필요한 상태입니다. 휴식을 취하세요.
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="status-danger">
    <strong>🚨 즉시 조치 필요</strong><br>
    전문가 상담이 필요합니다. 1577-0199로 전화하세요.
    </div>
    """, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.caption("🌙 GINI R.E.S.T. v3.0 MIRACLE Edition | Built by MIRACLE (Claude)")
