import streamlit as st

name = st.text_input("Enter Your Name :")

Father_name = st.text_input("Enter Your Father Name :")

add = st.text_area("Enter Your Address :")

classdata = st.selectbox("Enter Your Class :", (1,2,3,4,5,6,7,8,9,10,11,12))

button = st.button("Submit")

if button:
    st.markdown(f"""
    Name = {name}\n
    FatherName = {Father_name}\n
    Address = {add}\n
    Class = {classdata}\n
""")

