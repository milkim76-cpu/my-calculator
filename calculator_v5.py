# 계산기 v5 - Streamlit 웹 앱

import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="계산기", page_icon="🧮")
st.title("🧮 나의 계산기")
st.write("사칙연산을 지원하는 계산기입니다.")

# --- 계산 함수 (v4에서 그대로 가져옴) ---
def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2, None
    elif operator == "-":
        return num1 - num2, None
    elif operator == "*":
        return num1 * num2, None
    elif operator == "/":
        if num2 == 0:
            return None, "0으로 나눌 수 없어요!"
        return num1 / num2, None
    else:
        return None, "올바른 연산자가 아니에요!"


# --- UI 구성 ---
col1, col2, col3 = st.columns(3)       # ✅ 화면을 3칸으로 나누기

with col1:
    num1 = st.number_input("첫 번째 숫자", value=0.0)   # ✅ 숫자 입력 위젯

with col2:
    operator = st.selectbox("연산자", ["+", "-", "*", "/"])  # ✅ 드롭다운 선택

with col3:
    num2 = st.number_input("두 번째 숫자", value=0.0)


# --- 계산 버튼 ---
if st.button("계산하기", type="primary"):               # ✅ 버튼 클릭 시 실행
    result, error = calculate(num1, operator, num2)

    if error:
        st.error(f"❌ {error}")                         # ✅ 빨간 오류 메시지
    else:
        st.success(f"✅ {num1} {operator} {num2} = **{result}**")  # ✅ 초록 성공 메시지

        # 계산 기록 저장
        if "history" not in st.session_state:          # ✅ session_state: 새로고침해도 데이터 유지
            st.session_state.history = []

        st.session_state.history.append(f"{num1} {operator} {num2} = {result}")


# --- 계산 기록 ---
if "history" in st.session_state and st.session_state.history:
    st.divider()
    st.subheader("📋 계산 기록")

    for i, record in enumerate(reversed(st.session_state.history), start=1):
        st.text(f"{i}. {record}")                      # 최근 기록이 위에 오도록 reversed

    if st.button("기록 지우기"):
        st.session_state.history = []
        st.rerun()                                     # ✅ 화면 새로고침
