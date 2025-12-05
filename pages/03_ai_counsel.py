import streamlit as st
from utils.groq_client import get_groq_client

st.title("💛 EmotionCare 3.0 — AI 심리 상담")
st.write("지금 마음 상태를 편안하게 도와드릴게요.")

user_input = st.text_area("지금 어떤 점이 가장 힘드세요?", height=150)

if st.button("상담 요청하기"):
    if not user_input:
        st.warning("내용을 입력해주세요.")
    else:
        client = get_groq_client()
        response = client.chat.completions.create(
           model="llama3-8b-8192",

            messages=[
                {"role": "system", "content": "너는 따뜻한 AI 심리상담사다."},
                {"role": "user", "content": user_input},
            ],
        )

        st.subheader("🧠 AI 상담 답변")
        st.write(response.choices[0].message["content"])
