"""
공통 사이드바 컴포넌트
Lyra MIRACLE v1.0
"""

import streamlit as st


def render_common_sidebar(current_page="home"):
    """
    공통 사이드바 렌더링
    
    Args:
        current_page: 'home', 'guardian', 'rest', 'setting', 'about'
    """
    
    with st.sidebar:
        # 로고/타이틀
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <h2 style="
                background: linear-gradient(135deg, #667eea 0%, #4DB6AC 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin: 0;
            ">🌟 Lyra MIRACLE</h2>
            <p style="color: #999; font-size: 0.8rem; margin: 0.5rem 0 0 0;">v1.0</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # 현재 위치 표시
        page_names = {
            'home': '🏠 홈',
            'guardian': '🛡️ Guardian',
            'rest': '🌙 R.E.S.T.',
            'setting': '⚙️ 설정',
            'about': 'ℹ️ 소개'
        }
        
        if current_page in page_names:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #667eea15, #4DB6AC15);
                padding: 0.8rem;
                border-radius: 10px;
                text-align: center;
                font-weight: 600;
                color: #667eea;
                margin-bottom: 1rem;
            ">
                현재: {page_names[current_page]}
            </div>
            """, unsafe_allow_html=True)
        
        # 네비게이션 버튼
        st.markdown("### 🧭 메뉴")
        
        if current_page != 'home':
            if st.button("🏠 홈으로", use_container_width=True, type="secondary"):
                st.switch_page("app.py")
        
        if current_page != 'guardian':
            if st.button("🛡️ GINI Guardian", use_container_width=True):
                st.switch_page("pages/02_stockbot.py")
        
        if current_page != 'rest':
            if st.button("🌙 GINI R.E.S.T.", use_container_width=True):
                st.switch_page("pages/03_ai_counsel.py")
        
        st.markdown("---")
        
        # 추가 메뉴
        st.markdown("### ⚙️ 기타")
        
        if current_page != 'setting':
            if st.button("⚙️ 설정", use_container_width=True, type="secondary"):
                st.switch_page("pages/04_setting.py")
        
        if current_page != 'about':
            if st.button("ℹ️ 소개", use_container_width=True, type="secondary"):
                st.switch_page("pages/05_about.py")
        
        st.markdown("---")
        
        # 푸터
        st.markdown("""
        <div style="text-align: center; color: #999; font-size: 0.75rem; padding: 1rem 0;">
            <p>🌟 Lyra MIRACLE</p>
            <p>Built by MIRACLE</p>
        </div>
        """, unsafe_allow_html=True)


def render_guardian_sidebar():
    """Guardian 전용 사이드바 추가 정보"""
    
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 📊 내 포트폴리오")
        
        if 'portfolio' in st.session_state and st.session_state.portfolio:
            for stock in st.session_state.portfolio[:3]:  # 최대 3개만
                st.markdown(f"""
                **{stock['종목명']}**
                - {stock['수량']}주
                - {stock['매입가']:,}원
                """)
            
            if len(st.session_state.portfolio) > 3:
                st.caption(f"외 {len(st.session_state.portfolio) - 3}개 종목")
        else:
            st.info("포트폴리오 정보가 없습니다.")
        
        st.markdown("---")
        
        if st.button("🗑️ 대화 내역 지우기", use_container_width=True, type="secondary"):
            st.session_state.guardian_chat = []
            st.rerun()


def render_rest_sidebar():
    """R.E.S.T. 전용 사이드바 추가 정보"""
    
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 📊 현재 상태")
        
        # 감정 레벨
        e_score = st.session_state.get('emotion_score', 1)
        e_colors = {1: "🟢", 2: "🟡", 3: "🟠", 4: "🔴", 5: "🚨"}
        e_labels = {1: "안정", 2: "주의", 3: "위험", 4: "심각", 5: "위기"}
        
        st.metric(
            "감정 레벨",
            f"E{e_score}",
            e_labels[e_score]
        )
        
        st.markdown(f"{e_colors[e_score]} {e_labels[e_score]}")
        
        st.markdown("---")
        
        crisis_count = st.session_state.get('crisis_count', 0)
        st.metric("위기 신호", f"{crisis_count}회", "최근 7일")
        
        st.markdown("---")
        
        if st.button("🗑️ 대화 내역 지우기", use_container_width=True, type="secondary"):
            st.session_state.rest_chat = []
            st.rerun()
        
        st.markdown("---")
        
        st.markdown("""
        **⚠️ 응급 연락처**
        - 📞 1577-0199
        - 📞 1393
        - 📞 1588-9191
        """)
