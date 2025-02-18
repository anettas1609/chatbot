import openai

# Nastavení API klíče
openai.api_key = 'tvůj_api_klíč'  # Nahraď tento text svým skutečným API klíčem

# Funkce pro komunikaci s OpenAI
def get_response_from_openai(query):
    try:
        # Tato metoda je pro starší verzi openai==0.28
        response = openai.Completion.create(
            engine="davinci",  # "davinci" nebo "curie", "babbage" pro starší verzi
            prompt=query,
            max_tokens=150
        )
        return response.choices[0].text.strip()  # Vrací první odpověď
    except Exception as e:
        return f"Chyba při komunikaci s OpenAI: {str(e)}"  # Ošetření chyby genericky

# Testovací dotaz
query = "Jak se bránit podvodným e-mailům?"
response = get_response_from_openai(query)
print(response)
