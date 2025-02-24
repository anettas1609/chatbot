import os
import openai
import streamlit as st

# Načtení API klíče z GitHub Secrets
api_key = os.getenv('API_KEY')

# Kontrola, zda je API klíč k dispozici
if not api_key:
    st.error("API klíč nebyl nalezen. Přidej ho do GitHub Secrets nebo prostředí.")
else:
    st.success(f"API klíč načten: {api_key[:10]}...")  # Zobrazí první 10 znaků klíče pro kontrolu

    # Nastavení OpenAI API klíče
    openai.api_key = api_key

    # Příklad jednoduché interakce s OpenAI API
    prompt = st.text_input("Zadej text pro Chatbot:")
    if prompt:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Můžeš použít jiný model dle potřeby
                prompt=prompt,
                max_tokens=150
            )
            st.write(response.choices[0].text.strip())
        except Exception as e:
            st.error(f"Došlo k chybě při komunikaci s OpenAI: {e}")
