import streamlit as st
# import package.law as law
import package.tool as tool

if 'result' not in st.session_state:
    st.session_state['result'] = None 

st.title("憲法蒐尋器")

method = st.selectbox("請選擇搜尋方式", ["查詢特定條文", "搜尋關鍵字", "顯示所有條文"])

if method == "查詢特定條文":
    tool.search_specific_law()

elif method == "搜尋關鍵字":
    tool.search_by_keyword()

elif method == "顯示所有條文":
    tool.print_all_law()

