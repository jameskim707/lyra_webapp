import streamlit as st
from utils.groq_client import get_groq_client

def run_stockbot():
    st.title("📉 Investment Guardian (주식 과잉 방지 챗봇)")
    st.write("투자 과열을 방지하기 위해 당신의 감정 상태를 점검합니다.")

    user_input = st.text_input("현재 투자 상황이나 감정을 설명해주세요.")

    if st.button("진단하기"):
        if not user_input:
            st.warning("먼저 내용을 입력해주세요.")
            return

        client = get_groq_client()
        response = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[
                {"role": "system", "content": "당신은 투자 중독 방지 전문가입니다."},
                {"role": "user", "content": user_input},
            ],
        )

        st.subheader("🧠 진단 결과")
        st.write(response.choices[0].message["content"])

