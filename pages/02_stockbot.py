"""
GINI Guardian v4.5 MIRACLE - 주식 과잉매매 방지 AI
by MIRACLE (Claude)
"""

import streamlit as st
import sys
sys.path.append('..')
from utils.groq_client import get_groq_client
from utils.sidebar import render_common_sidebar, render_guardian_sidebar

st.set_page_config(
    page_title="GINI Guardian MIRACLE",
    page_icon="🛡️",
    layout="wide"
)

# 공통 사이드바
render_common_sidebar(current_page='guardian')
render_guardian_sidebar()

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
    margin-bottom: 0.5rem;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 1.1rem;
    margin-bottom: 2rem;
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
    font-size: 0.85rem;
}

.risk-badge-medium {
    background: #ff9800;
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.85rem;
}

.risk-badge-high {
    background: #f44336;
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.85rem;
}
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown('<div class="main-header">🛡️ GINI Guardian</div>', unsafe_allow_html=True)
st.markdown('<div class="version-tag">v4.5 MIRACLE Edition</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">감정적 투자를 막아주는 AI 투자심리 상담가</div>', unsafe_allow_html=True)

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
💡 **Guardian과 함께하면:**
- 💬 자유롭게 투자 고민을 이야기하세요 (설문지 ❌)
- 🎯 감정을 분석하고 위험도를 측정합니다
- 🛡️ 과잉매매를 막아드립니다
- 📊 포트폴리오 기반 맞춤 조언을 드립니다
""")

st.markdown("---")

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
user_input = st.chat_input("💬 투자 고민을 자유롭게 이야기해주세요...")

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
        
        # 위험도 계산
        if emotion_score is None:
            emotion_score = 5.0
        
        risk_score = emotion_score * 1.2
        if risk_score > 10:
            risk_score = 10.0
        
        # AI 응답 추가
        st.session_state.guardian_chat.append({
            'role': 'assistant',
            'content': response,
            'meta': {
                'risk': risk_score,
                'emotion': emotion_score
            }
        })
    
    st.rerun()

# 안내
st.markdown("---")

if not st.session_state.guardian_chat:
    st.markdown("""
    <div style="background: #e8f5e9; padding: 1.5rem; border-radius: 15px; border-left: 4px solid #4caf50;">
    <h4 style="margin-top: 0;">💬 이렇게 시작해보세요:</h4>
    <ul>
    <li>"요즘 주식 때문에 스트레스받아요"</li>
    <li>"삼성전자가 계속 떨어지는데 어떡하죠?"</li>
    <li>"손절해야 할지 고민이에요"</li>
    <li>"자꾸 물타기하게 돼요"</li>
    </ul>
    <p style="margin-bottom: 0; color: #666;">💡 체크박스가 아닌 자유로운 대화로 시작하세요!</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="background: #fff3cd; padding: 1rem; border-radius: 10px;">
    <strong>💡 대화 팁:</strong>
    <ul style="margin-bottom: 0;">
    <li>솔직하게 감정을 표현하세요</li>
    <li>종목명을 구체적으로 말씀하세요</li>
    <li>계속 이어서 대화할 수 있어요</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.caption("🛡️ GINI Guardian v4.5 MIRACLE Edition | Built by MIRACLE (Claude)")
