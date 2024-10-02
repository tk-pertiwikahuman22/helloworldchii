import streamlit as st

st.title( "Hello World")
name = st.text_input( "Name:")

st.write('Hello', name)