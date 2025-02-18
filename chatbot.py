import openai
import streamlit as st

# Načtení API klíče ze secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Funkce pro komunikaci s OpenAI API
def get_response_from_openai(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        temperature=0.7 # Teplota pro řízení kreativity (0.0 = nejvíce striktní, 1.0 = nejvíce kreativní)
    )
    return response.choices[0].message["content"].strip()

# Inicializace Streamlit aplikace
st.title("Chatbot proti dezinformacím a phishingu")

# Udržování historie zpráv v session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Zobrazení historie zpráv
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Vstup pro uživatele
user_input = st.text_input("Zadejte Váš dotaz:")

# Odeslání dotazu a získání odpovědi
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Vytvoření zpráv pro OpenAI API
    messages = [
        {"role": "system", "content": "Jsi užitečný chatbot proti dezinformacím a phishingu."},
        *st.session_state.messages
    ]

    response = get_response_from_openai(messages)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
