import openai
import os
import streamlit as st

# Načteme API klíč z prostředí
openai.api_key = os.getenv("API_KEY")  # Předpokládáme, že je uložený v GitHub Secrets

# Ověření, zda je API klíč správně načten
if openai.api_key is None:
    st.error("API klíč není nalezen. Zkontrolujte, že je nastavený v GitHub Secrets.")
else:
    st.success("API klíč je načtený.")

# Funkce pro chatbota s novým API
def get_chatbot_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Můžeš změnit podle potřeby na jiný model (např. gpt-4)
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

# Streamlit rozhraní pro interakci s chatbotem
st.title("Chatbot s OpenAI API")

user_input = st.text_input("Zadej svůj dotaz:")

if user_input:
    bot_response = get_chatbot_response(user_input)
    st.write(f"Chatbot odpověděl: {bot_response}")
