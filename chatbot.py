import openai
import streamlit as st

# Nastavení API klíče OpenAI
openai.api_key = "TVŮJ_API_KLÍČ"

# Nastavení Streamlit aplikace
st.title("Chatbot na ochranu před kyberkriminalitou")

# Uživatelský vstup
user_input = st.text_input("Zadej svůj dotaz:")

# Odeslání dotazu do OpenAI API
if st.button("Odeslat"):
    if user_input:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Správný model pro verzi 0.28
            prompt=user_input,  # Vstup od uživatele
            max_tokens=150  # Počet tokenů v odpovědi
        )
        st.write(response["choices"][0]["text"])  # Výpis odpovědi
    else:
        st.wr
