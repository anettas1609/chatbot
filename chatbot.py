import os
import openai
import streamlit as st

# Načtení API klíče z prostředí
api_key = os.getenv("API_KEY")
if not api_key:
    st.error("API klíč nebyl nalezen!")
    st.stop()  # Zastaví aplikaci, pokud API klíč není načtený

openai.api_key = api_key

# Funkce pro komunikaci s chatbotem
def get_chatbot_response(user_input):
    try:
        # Vytvoření požadavku na OpenAI GPT-3.5
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Používáme model GPT-3.5 Turbo
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        # Získání odpovědi z modelu
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Chyba při komunikaci s OpenAI API: {e}"

# Nastavení aplikace pomocí Streamlit
st.title("Chatbot pomocí OpenAI")
user_input = st.text_input("Zadej svůj dotaz:")

if user_input:
    bot_response = get_chatbot_response(user_input)
    st.write("**Odpověď chatbota:**")
    st.write(bot_response)
