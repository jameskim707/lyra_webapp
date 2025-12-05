"""
GINI Guardian v4.5 MIRACLE - 주식 과잉매매 방지 AI
by MIRACLE (Claude)
"""

import streamlit as st
import sys
sys.path.append('..')
from utils.groq_client import get_groq_client

st.set_page_config(
    page_title="GINI Guardian MIRACLE",
    page_icon="🛡️",
    layout="wide"
)

# CSS
st.markdown("""
<style>
.main-header {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

.version-tag {
    text-align: center;
    color: #667eea;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.chat-user {
    background: #e3f2fd;
    padding: 1rem;
    border-radius: 10px;
    margin: 0.5rem 0;
}

.chat-assistant {
    background: #f3e5f5;
    padding: 1rem;
    border-radius: 10px;
    margin: 0.5rem 0;
}

.risk-badge-low {
    background: #4caf50;
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-weight: 600;
}

.risk-badge-medium {
    background: #ff9800;
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-weight: 600;
}

.risk-badge-high {
    background: #f44336;
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown('<div class="main-header">🛡️ GINI Guardian</div>', unsafe_allow_html=True)
st.markdown('<div class="version-tag">v4.5 MIRACLE Edition</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; color: #666; margin-bottom: 2rem;">주식 과잉매매 방지 AI 상담가</div>', unsafe_allow_html=True)

# Session State 초기화
if 'guardian_chat' not in st.session_state:
    st.session_state.guardian_chat = []

if 'portfolio' not in st.session_state:
    st.session_state.portfolio = [
        {'종목명': '삼성전자', '수량': 10, '매입가': 70000},
        {'종목명': 'SK하이닉스', '수량': 5, '매입가': 130000}
    ]

# Groq 클라이언트
groq_client = get_groq_client()

# 인트로
st.info("""
💡 **GINI Guardian MIRACLE는:**
- 감정적 투자를 막아주는 AI 상담가입니다
- 12가지 감정 태그를 분석합니다
- 위험도를 측정하고 경고합니다
- 계속 대화가 가능합니다
""")

st.markdown("---")

# 사이드바 - 포트폴리오
with st.sidebar:
    st.markdown("### 📊 내 포트폴리오")
    
    for stock in st.session_state.portfolio:
        st.markdown(f"""
        **{stock['종목명']}**
        - 수량: {stock['수량']}주
        - 매입가: {stock['매입가']:,}원
        """)
    
    st.markdown("---")
    
    if st.button("🗑️ 대화 내역 지우기", use_container_width=True):
        st.session_state.guardian_chat = []
        st.rerun()

# 채팅 히스토리
for msg in st.session_state.guardian_chat:
    if msg['role'] == 'user':
        st.markdown(f'<div class="chat-user">👤 **You:** {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-assistant">🛡️ **Guardian:** {msg["content"]}</div>', unsafe_allow_html=True)
        
        # 메타 정보
        if 'meta' in msg:
            meta = msg['meta']
            risk = meta.get('risk', 0)
            
            if risk < 5:
                badge = 'risk-badge-low'
                emoji = '🟢'
            elif risk < 7:
                badge = 'risk-badge-medium'
                emoji = '🟡'
            else:
                badge = 'risk-badge-high'
                emoji = '🔴'
            
            st.markdown(f'<span class="{badge}">{emoji} 위험도: {risk:.1f}/10</span>', unsafe_allow_html=True)

# 사용자 입력
user_input = st.chat_input("💬 투자 고민을 말씀해주세요...")

if user_input:
    # 사용자 메시지 추가
    st.session_state.guardian_chat.append({
        'role': 'user',
        'content': user_input
    })
    
    # System Prompt
    portfolio_info = "\n".join([f"- {s['종목명']}: {s['수량']}주" for s in st.session_state.portfolio])
    
    system_prompt = f"""당신은 GINI Guardian, 투자 심리 상담가입니다.

[현재 포트폴리오]
{portfolio_info}

**원칙:**
1. 감정적 투자를 막고 합리적 판단을 돕기
2. 위험이 보이면 강력히 경고
3. 짧고 명확한 조언 (3-5문장)
4. 감정 점수 0~10으로 평가

**응답 형식:**
[감정점수: X]
(조언)
"""
    
    # 메시지 구성
    messages = [{"role": "system", "content": system_prompt}]
    
    for msg in st.session_state.guardian_chat[-10:]:
        messages.append({
            "role": msg['role'],
            "content": msg['content']
        })
    
    # AI 응답
    with st.spinner("🤔 AI가 분석 중..."):
        response, emotion_score = groq_client.chat(messages)
        
        # 위험도 계산 (간단 버전)
        if emotion_score is None:
            emotion_score = 5.0
        
        risk_score = emotion_score * 1.2  # 0~12 범위를 0~10으로 조정
        if risk_score > 10:
            risk_score = 10.0
        
        # AI 응답 추가
        st.session_state.guardian_chat.append({
            'role': 'assistant',
            'content': response,
