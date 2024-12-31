import streamlit as st
import package.law as law

st.session_state['result'] = None

def search_specific_law():
    value = st.slider("選擇一個數值", 1, 4, step=1)
    bt = st.button("開始尋找")
    if bt:
        st.session_state['result'] = law.search_specific_law(int(value))
    if st.session_state['result']:
      st.text(st.session_state['result'])
    return 

# result = search_specific_law()
def search_by_keyword():
    keyword = st.text_input("請輸入關鍵字")
    bt = st.button("開始尋找")
    if bt:
        st.session_state['result'] = law.search_by_keyword(keyword)
    if st.session_state['result']:
      st.text(st.session_state['result'])
    return

def print_all_law():
  bt = st.button("開始尋找")
  if bt:
    st.session_state['result'] = law.print_all_law()
  if st.session_state['result']:
      st.text(st.session_state['result'])
  return
# if st.session_state['result']:
#     st.text(st.session_state['result'])

