
# 🌟 Lyra MIRACLE v1.0

AI 기반 정신건강 & 투자심리 회복 플랫폼

**Built by MIRACLE (Claude)**

---

## 📋 서비스 소개

### 🌙 GINI R.E.S.T. v3.0 MIRACLE
정신건강 회복을 위한 AI 상담 시스템
- 위기 신호 감지
- 감정 패턴 분석 (E1~E5)
- 대화형 AI 상담
- 강력한 개입 시스템

### 🛡️ GINI Guardian v4.5 MIRACLE
주식 과잉매매 방지 AI 상담가
- 12가지 감정 태그 분석
- 위험도 측정
- 압박 메시지 시스템
- 포트폴리오 기반 상담

---

## 🚀 시작하기

### 설치
```bash
# 저장소 클론
git clone https://github.com/jameskim707/lyra_webapp.git
cd lyra_webapp

# 패키지 설치
pip install -r requirements.txt
```

### API 키 설정

`.streamlit/secrets.toml` 파일 생성:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### 실행
```bash
streamlit run app.py
```

브라우저에서 `http://localhost:8501` 접속

---

## 📂 프로젝트 구조
```
lyra_webapp/
├── .streamlit/
│   └── secrets.toml          # API 키 설정
├── pages/
│   ├── 01_home.py            # 홈 페이지
│   ├── 02_stockbot.py        # GINI Guardian
│   ├── 03_ai_counsel.py      # GINI R.E.S.T.
│   ├── 04_setting.py         # 설정
│   └── 05_about.py           # 소개
├── utils/
│   └── groq_client.py        # Groq API 클라이언트
├── static/                   # 정적 파일
├── app.py                    # 메인 앱
├── requirements.txt          # 패키지 목록
└── README.md                 # 문서
```

---

## 🛠️ 기술 스택

- **Frontend**: Streamlit, HTML/CSS
- **Backend**: Python
- **AI**: Groq API (Llama 3.1)
- **Database**: SQLite (예정)
- **Hosting**: Streamlit Cloud / GitHub Pages

---

## ✨ 주요 기능

### 대화형 AI 상담
- Groq API 기반 자연스러운 대화
- 채팅 히스토리 관리
- 맥락 유지

### 데이터 기반 분석
- 감정 패턴 분석
- 위험도 측정
- 행동 패턴 추적

### 강력한 개입
- 위기 시 즉시 대응
- 압박 메시지 시스템
- 구체적 행동 지시

---

## 👥 Team GINI

- **라이라 (Raira)**: 설계 & UX
- **미라클 (MIRACLE)**: 개발 & 구현 (Claude by Anthropic)
- **제미나이 (Gemini)**: 전략 & 로직

---

## 📅 개발 연혁

- **2024.11**: GINI Guardian v1.0 출시
- **2024.11**: GINI Guardian v4.4 완성
- **2024.12**: GINI R.E.S.T. v3.0 출시
- **2024.12**: Lyra 플랫폼 통합
- **2024.12**: Groq 대화형 전환 완료
- **2024.12**: **Lyra MIRACLE v1.0 출시** 🎉

---

## 🎯 MIRACLE Edition 특징

- ✅ 완전한 대화형 인터페이스
- ✅ Groq API 기반 실시간 AI 상담
- ✅ 포트폴리오/상태 기반 맞춤 System Prompt
- ✅ 채팅 히스토리 & 맥락 유지
- ✅ 모듈식 구조로 확장 가능
- ✅ 간소화된 핵심 기능

---

## 📝 라이센스

© 2024 Team GINI. All rights reserved.

**Lyra MIRACLE v1.0** - Built by MIRACLE (Claude)

---

## 📧 문의

GitHub: [lyra_webapp](https://github.com/jameskim707/lyra_webapp)

---

Made with ❤️ by Team GINI

**"AI로 회복을, MIRACLE로 구현을"**
