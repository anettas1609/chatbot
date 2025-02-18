import streamlit as st
import openai

# Nastavení OpenAI API klíče (nahraď svým klíčem)
openai.api_key = "TVŮJ_OPENAI_API_KLÍČ"

# Název aplikace
st.title("Chatbot pro prevenci kyberkriminality")

# Popis aplikace
st.write("Tento chatbot pomáhá chránit před phishingem a dezinformacemi. Zadej svůj dotaz!")

# Vstup od uživatele
dotaz = st.text_input("Zadej svůj dotaz:")

# Odpověď AI po stisknutí tlačítka
if st.button("Odeslat"):
    if dotaz:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # nebo použij jiný model jako gpt-4
                messages=[
                    {"role": "system", "content": "Jsem chatbot zaměřený na kybernetickou bezpečnost."},
                    {"role": "user", "content": dotaz}
                ]
            )
            odpoved = response['choices'][0]['message']['content']
            st.success(odpoved)
        except Exception as e:
            st.error(f"Chyba při komunikaci s OpenAI: {str(e)}")
    else:
        st.warning("Zadej prosím dotaz.")
