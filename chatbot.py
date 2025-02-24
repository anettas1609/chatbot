import streamlit as st
import os

api_key = os.getenv("API_KEY")
st.write("API_KEY načten:", bool(api_key))
