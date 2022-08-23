import streamlit as st
import pandas as pd
import sqlite3

con = sqlite3.connect('db.db')
cur = con.cursor()

menu = st.sidebar.selectbox('메뉴', options=['회원목록','회원가입'])
if menu == '회원목록':

    st.subheader('회원목록')
    df= pd.read_sql("SELECT * FROM users",con)
    st.dataframe(df)

elif menu == '회원가입':

    st.subheader('회원가입')

    with st.form('my_form', clear_on_submit=True):
        st.info('다음 양식을 모두 입력 후 제출합니다.')
        uid = st.text_input('ID', max_chars=12)
        upw = st.text_input('PW', type='password')
        upw_chk = st.text_input('PW_CHECK', type='password')
        usex = st.radio('SEX', options=['남','여'], horizontal=True)

        submitted = st.form_submit_button('제출')
        if submitted:

            if upw != upw_chk:
                st.warning('다시 쳐')
                st.stop()
            st.success(f'{uid} {upw} {usex}');
            cur.execute(f"INSERT INTO users VALUES ("
                        f"'{uid}','{upw}',"
                        f"'{usex}')")
            con.commit()
