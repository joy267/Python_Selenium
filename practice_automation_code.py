import streamlit as st
from Page_Objects.test_page_object import Tracking

test = Tracking()

st.title("Functional Testing")

st.divider()

with st.form("my_form", clear_on_submit=False):
    webdriver = st.selectbox("Choose a WebDriver", ("Chrome WebDriver", "Edge WebDriver", "Firefox WebDriver"))

    if webdriver == "Chrome WebDriver":
        test.open_chrome_webdriver()
    if webdriver == "Edge WebDriver":
        test.open_edge_webdriver()
    if webdriver == "Firefox WebDriver":
        test.open_firefox_webdriver()

    url = st.text_input("**Enter the test url **:", "")

    col1, col2, col3, col4 = st.columns([1, 2, 3, 1])
    with col4:
        run = st.form_submit_button("Run")
