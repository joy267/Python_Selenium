import streamlit as st
from streamlit_option_menu import option_menu
from console_logs import console_log
from page_speed_check import page_performance
from practice_automation_code import main_app
from sign_up import sign_up
from login import login

# drop_down = st.sidebar.selectbox("Login/Sign Up", ("Login", "Sign Up"))
#
# if drop_down == "Login":
#     login()
#     if "authenticated" not in st.session_state:
#         st.session_state.authenticated = True
#         st.switch_page(main_app())

with st.sidebar:
    selected = option_menu(
        menu_title="Web Testing",
        options=['Console Logs', 'Page Performance', 'SignUp', 'Login'],
        icons=['circle-fill', 'circle-fill', 'circle-fill', 'circle-fill'],
        menu_icon='display',
        default_index=0,
    )

if selected == 'Console Logs':
    console_log()

elif selected == 'Page Performance':
    page_performance()

elif selected == 'SignUp':
    sign_up()

elif selected == 'Login':
    login()
