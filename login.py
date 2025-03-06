import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("C:\\Projects\\Python_Selenium\\webtestingapp-64f14-939a27fc3f91.json")
# firebase_admin.initialize_app(cred)


st.title("Welcome to :violet[Web Testing Application]:sunglasses:")


# def login():

with st.form(key='login', clear_on_submit=False):
    st.header("**:green[Login]**")
    login_email = st.text_input("Email", key='login_email', placeholder="Enter your email address")
    login_password = st.text_input("Password", key='login_password', placeholder="Enter your password")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.form_submit_button("Login")