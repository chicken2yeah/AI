
import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Streamlit 애플리케이션 제목
st.title('ChatGPT와 대화하기')

# 사용자 입력 받기
user_input = st.text_input('질문을 입력하세요:')

# 버튼을 눌러서 응답 받기
if st.button('전송'):
    if user_input:
        # OpenAI API를 사용하여 응답 생성
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=150
        )

        # 응답 출력
        st.write('ChatGPT의 응답:')
        st.write(response.choices[0].text.strip())
    else:
        st.write('질문을 입력해주세요.')
