import streamlit as st

correct_mc = "토마토"
correct_sa = "4"

st.title("간단한 퀴즈")

st.header("1. 객관식 퀴즈")
st.write("다음 중 프로그래밍 언어가 아닌 것은?\n")
mc_options = ["파이썬", "토마토", "자바", "C++"]
mc_answer = st.radio("정답을 선택하세요", mc_options, key="mc")

if st.button("1번 채점", key="mc_submit"):
    if mc_answer == correct_mc:
        st.success("맞았습니다!")
    else:
        st.error(f"틀렸습니다. 정답은 '{correct_mc}'입니다.")

st.header("2. 주관식 퀴즈")
st.write("다음 빈칸을 채우세요:\n실리카겔 멤버는 ____명이다.")
sa_answer = st.text_input("정답을 입력하세요", key="sa")

if st.button("2번 채점", key="sa_submit"):
    if sa_answer.strip().lower() == correct_sa.lower():
        st.success("맞았습니다!")
    else:
        st.error(f"틀렸습니다. 정답은 '{correct_sa}'입니다.")
