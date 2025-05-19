import streamlit as st

correct_mc = "2"
correct_sa = "파이썬"

st.title("간단한 퀴즈")

st.header("1. 객관식 퀴즈")
st.write("다음 중 프로그래밍 언어가 아닌 것은?\n1) 파이썬  2) 토마토  3) 자바")
mc_answer = st.selectbox("정답을 선택하세요", ["1", "2", "3"], index=0)

st.header("2. 주관식 퀴즈")
st.write("다음 빈칸을 채우세요:\n실리카겔 멤버는 ____명이다.")
sa_answer = st.text_input("정답을 입력하세요")

if st.button("제출"):
    correct_count = 0
    st.subheader("결과 확인")

    if mc_answer == correct_mc:
        st.success("1번 정답: 맞았습니다!")
        correct_count += 1
    else:
        st.error(f"1번 정답: 틀렸습니다. 정답은 {correct_mc}번입니다.")

    if sa_answer.strip().lower() == correct_sa.lower():
        st.success("2번 정답: 맞았습니다!")
        correct_count += 1
    else:
        st.error(f"2번 정답: 틀렸습니다. 정답은 '{correct_sa}'입니다.")

    st.write(f"총 {correct_count}/2개 정답했습니다.")
