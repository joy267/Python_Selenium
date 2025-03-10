import streamlit as st
import pyrebase
import firebase_admin
from validate_email_address import validate_email

# 🔹 Initialize Firebase App (Ensure it's only initialized once)

# For Firebase JS SDK v7.20.0 and later, measurementId is optional
config = {
    'apiKey': "AIzaSyCsQVKILoHmcBSMztaptC7zQpSOSiGlc2Y",
    'authDomain': "webtestingapp-64f14.firebaseapp.com",
    'projectId': "webtestingapp-64f14",
    'databaseURL': "https://webtestingapp-64f14-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'storageBucket': "webtestingapp-64f14.firebasestorage.app",
    'messagingSenderId': "883011116295",
    'appId': "1:883011116295:web:1d22ad19fa03827390b9a2",
    'measurementId': "G-5KB2CC6TJ6",
}

# Firebase Authentication
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Database Authentication
db = firebase.database()
storage = firebase.storage()

# 🔐 Initialize authentication session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user_email" not in st.session_state:
    st.session_state.user_email = None

st.title("Welcome to :violet[Web Testing Application] 😎")


def is_valid_email(login_email):
    return validate_email(login_email)


# def authenticate_user(email, password):
#     """Authenticate user with Firebase"""
#     with st.form(key='login_form', clear_on_submit=False):
#         st.header("**:green[Login]**")
#         login_email = st.text_input("Email", key='login_email', placeholder="Enter your email address")
#         login_password = st.text_input("Password", key='login_password', placeholder="Enter your password",
#                                        type="password")
#
#         col1, col2, col3, col4, col5 = st.columns(5)
#         with col3:
#             login_button = st.form_submit_button("Login")
#     try:
#         user = auth.sign_in_with_email_and_password(login_email, login_password)
#         # Dummy password check (Firebase does not support direct password validation)
#         if email and password:
#             st.session_state.authenticated = True
#             st.session_state.user_email = email
#             return True
#     except Exception as e:
#         st.error("❌ Authentication failed: Invalid email or password.")
#         return False


# 🏠 Login Form
def login():
    with st.form(key='login_form', clear_on_submit=True):
        st.header("**:green[Login]**")
        login_email = st.text_input("Email", key='login_email', placeholder="Enter your email address")
        login_password = st.text_input("Password", key='login_password', placeholder="Enter your password", type="password")

        col1, col2, col3, col4, col5 = st.columns(5)
        with col3:
            login_button = st.form_submit_button("Login")

    try:
        if login_button:
            if login_email:
                if is_valid_email(login_email):
                    # if username:
                    #     if len(username) >= 4:
                    if login_password:
                        if len(login_password) >= 8:
                            # if confirm_password:
                            #     if password == confirm_password:
                            user = auth.sign_in_with_email_and_password(login_email, login_password)
                            if user:
                                st.session_state.authenticated = True
                                st.success("✅ Login Successfully !! 🎉🎉🎉")
                                st.balloons()
                            else:
                                st.error("�� Authentication failed: Invalid email or password.")
                                st.session_state.authenticated = False
                                st.session_state.user_email = None

                                # else:
                        #     st.error(" ⚠️ Passwords do not match")
                        # else:
                        #     st.error(" ⚠️ Confirm Password field is required.")
                        else:
                            st.error(" ❌ Password must be at least 8 characters long.")
                    else:
                        st.error(" ⚠️ Password field is required.")
                #     else:
                #         st.error(" ⚠️ Username is too short")
                # else:
                #     st.error(" ⚠️ Username field is required.")
                else:
                    st.error(" ❌ Invalid email address")
            else:
                st.error(" ⚠️ Email field is required.")

    except Exception as e:
        st.error(" ❌ ❌ Authentication failed: Invalid email or password.")


# # ✅ Handle login
# if login_button:
#     if authenticate_user(login_email, login_password):
#         st.success("✅ Login successful!")
#         st.rerun()  # Refresh the page to reflect login state
#
# # 🚀 Redirect to the menu page if authenticated
# if st.session_state.authenticated:
#     st.switch_page("pages/menu.py")  # Ensure you have `menu.py` in the `pages/` folder
