import os
import openai
import streamlit as st

# Načtení API klíče z prostředí
openai_api_key = os.getenv('API_KEY')

# Kontrola, zda je API klíč k dispozici
if not openai_api_key:
    st.error("API klíč nebyl nalezen. Přidej ho do GitHub Secrets nebo prostředí.")
    st.stop()

# Nastavení API klíče pro OpenAI
openai.api_key = openai_api_key

# Funkce pro získání odpovědi z OpenAI
def get_response_from_openai(question):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150,
            temperature=0.5
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Chyba při komunikaci s OpenAI: {e}"

# Nastavení Streamlit aplikace
st.set_page_config(page_title="Chatbot - Prevence kyberkriminality", page_icon="🤖")
st.title("🤖 Chatbot pro prevenci kyberkriminality")

# Uživatelský vstup
user_question = st.text_input("Zeptej se na cokoliv ohledně phishingu nebo dezinformací:")

# Zpracování dotazu a zobrazení odpovědi
if user_question:
    with st.spinner("Zpracovávám odpověď..."):
        answer = get_response_from_openai(user_question)
        st.success(answer)

# Příklad doporučených dotazů
st.markdown("""
### Příklady dotazů:
- Jak poznám phishingový e-mail?
- Jak se bránit podvodným SMS zprávám?
- Co dělat, když kliknu na podezřelý odkaz?
- Jak se chránit před dezinformacemi na sociálních sítích?
- Jak ověřit pravost webové stránky?
- Jaké jsou nejčastější typy kyberpodvodů?
- Jak mohu bezpečně používat veřejné Wi-Fi sítě?
- Co je dvoufaktorová autentizace a proč je důležitá?
- Jak chránit svá osobní data online?
- Jak rozpoznat podvodné telefonáty?
""")
