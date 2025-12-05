import streamlit as st
from utils.groq_client import get_groq_client

st.title("🧠 EmotionCare 3.0 (AI 심리 상담)")
st.write("당신의 감정과 고민을 들어드릴게요. 편하게 이야기해보세요.")

client = get_groq_client()

# 대화 입력창
user_input = st.text_input("지금 어떤 고민이 있으신가요?")

if st.button("상담 요청"):
    if user_input.strip() == "":
        st.warning("메시지를 입력해주세요.")
    else:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "당신은 따뜻하고 공감적인 심리상담사입니다. 한국어로 답변하세요."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=300
        )

        answer = response.choices[0].message["content"]
        st.success(answer)
