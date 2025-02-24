import os
import streamlit as st

# Načti API klíč
api_key = os.getenv('API_KEY')

# Zkontroluj, jestli je API klíč správně načtený
if not api_key:
    st.error("API klíč nebyl nalezen. Přidej ho do GitHub Secrets nebo prostředí.")
else:
    st.success("API klíč je správně načten.")
