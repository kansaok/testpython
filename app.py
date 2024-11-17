import streamlit as st

# Judul aplikasi
st.title("Simple Streamlit App")

# Input text
name = st.text_input("Enter your name:")

# Slider
age = st.slider("Select your age:", 0, 100, 25)

# Tombol
if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old!")