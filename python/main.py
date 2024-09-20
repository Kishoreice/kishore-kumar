import streamlit as st
class buttons:
    def __init__(self ,'num'):
        if st.button(f"button number is {num}"):
            st.write(num*num)
            self.calc(num)
    def calc(self, num):
        if num % 2 == 0:
            st.balloons()
        else:
            st.snow()
for i in range(10):
    buttons()