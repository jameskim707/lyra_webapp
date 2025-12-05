"""
Groq API 클라이언트
GINI Guardian & GINI R.E.S.T. 공통 사용
"""

import streamlit as st
from groq import Groq
import re


class GroqClient:
    """Groq API 클라이언트"""
    
    def __init__(self):
        """초기화"""
        self.api_key = st.secrets.get("GROQ_API_KEY", "")
        
        if not self.api_key:
            st.error("⚠️ Groq API 키가 설정되지 않았습니다.")
            self.client = None
        else:
            self.client = Groq(api_key=self.api_key)
    
    def chat(self, messages, model="llama-3.1-8b-instant", temperature=0.7, max_tokens=500):
        """대화형 API 호출"""
        
        if not self.client:
            return "⚠️ API 클라이언트가 초기화되지 않았습니다.", None
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            content = response.choices[0].message.content
            
            # 감정 점수 추출 (있을 경우)
            emotion_match = re.search(r'\[감정점수[:\s]*(\d+(?:\.\d+)?)\]', content)
            emotion_score = float(emotion_match.group(1)) if emotion_match else None
            
            # 감정 점수 제거
            clean_content = re.sub(r'\[감정점수[:\s]*\d+(?:\.\d+)?\]', '', content).strip()
            
            return clean_content, emotion_score
            
        except Exception as e:
            return f"⚠️ API 오류: {str(e)}", None
    
    def single_query(self, prompt, model="llama-3.1-8b-instant", temperature=0.7, max_tokens=500):
        """단일 질문 API 호출"""
        
        messages = [{"role": "user", "content": prompt}]
        return self.chat(messages, model, temperature, max_tokens)


# 전역 클라이언트 인스턴스
@st.cache_resource
def get_groq_client():
    """Groq 클라이언트 싱글톤"""
    return GroqClient()
