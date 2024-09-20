import streamlit as st

username = st.text_input("enter the username")
password = st.text_input("enter the password,type'password")

if st.button("login"):
    if password == "pass":
        st.success("logged in successfully")
        st.warning("logged in successfully")
        st.error("logged in successfully")
    else:
        st.error("wrong credential")