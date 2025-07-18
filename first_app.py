import streamlit as st
st.title("Hello This is Kapil Maheshwari!")
message = st.text_input("Enter your message:")
if message:
    st.info("You said: {message}")
