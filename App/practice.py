import os

import pandas as pd
import streamlit as st

# Title

st.title("This is my first application")

# Header

st.header("This is a header")

# Subheader

st.subheader("This is a subheader")

# Divider

st.divider()

# code

code = "hello world"
st.code(code)

# caption

st.caption("This is a caption")

# Display text

st.markdown("This is my first description")

# Italic text

st.markdown("*italic font*")

# Bold text

st.markdown("**bold text**")

# List down the text

st.markdown("* first element")

st.markdown("* second element")

# Info Text

st.info("This is a information")

# Warning Text

st.warning("This is a warning")

# Error Text

st.error("This is an error")

# Json Text

json_response = {"status": 200, "text": "Successful"}

st.write(json_response)

list_data = ["item 1", "item 2", "item 3", "item 4"]

st.write(list_data)

# Display and count the data

dataset = pd.read_csv("C:\\Users\\mrity\\Downloads\\disney_plus_titles.csv")

st.write(dataset)

value_counts = dataset["release_year"].value_counts()

st.bar_chart(value_counts)

# User Inputs

text_inputs = st.sidebar.text_input("Enter your name", "")

text_area_inputs = st.sidebar.text_area("Enter your description")

number_inputs = st.sidebar.number_input("Enter a number", min_value=0, max_value=60, value=20, step=1)

columns = st.columns((2, 1))

with columns[0]:
    if text_inputs != "":
        st.markdown(
            f"""
            * Your name is: {text_inputs}
            * Your description is: {text_area_inputs}
            * Your age is: {number_inputs}
        """
        )

# Checkbox

with columns[1]:
    checkbox = st.sidebar.checkbox("Available to work")
    st.write(f"Available to work : {checkbox}")

# Slider

with columns[1]:
    threshold = st.sidebar.slider("Pick a number", min_value=0, max_value=100, value=50, step=1)
    st.write(f"slider : {threshold}")

# Drop Down Button

with columns[1]:
    drop_down_option = st.sidebar.selectbox("Pick a element", ("element 1", "element 2", "element 3"))
    st.write(f"Selected element is :", drop_down_option)

# Redio Button

with columns[1]:
    radio_button_option = st.sidebar.radio("Pick a element", ("element 1", "element 2", "element 3"))
    st.write(f"Selected element is :", radio_button_option)

# Upload a file

with columns[1]:
    file = st.sidebar.file_uploader("Pick a file")
    st.write(file)

# Pick a date

with columns[0]:
    date = st.sidebar.date_input("Pick a date")
    st.write(f"Today is :", date)
