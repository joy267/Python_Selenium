import streamlit as st
from streamlit_option_menu import option_menu
from console_logs import console_log
from page_speed_check import page_performance
from sign_up import sign_up
from login import log_in

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("🔒 Please log in first!")
    st.stop()

selected = option_menu(
        menu_title="Web Testing",
        options=['Console Logs', 'Page Performance'],
        icons=['circle-fill', 'circle-fill', 'circle-fill', 'circle-fill'],
        menu_icon='display',
        default_index=0,
    )

if selected == 'Console Logs':
    console_log()

elif selected == 'Page Performance':
    page_performance()

# elif drop_down == "Sign Up":
#     sign_up()

#     selected = option_menu(
#         menu_title="Web Testing",
#         options=['Console Logs', 'Page Performance', 'SignUp', 'Login'],
#         icons=['circle-fill', 'circle-fill', 'circle-fill', 'circle-fill'],
#         menu_icon='display',
#         default_index=0,
#     )
#
# if selected == 'Console Logs':
#     console_log()
#
# elif selected == 'Page Performance':
#     page_performance()
#
# elif selected == 'SignUp':
#     sign_up()
#
# elif selected == 'Login':
#     log_in()
