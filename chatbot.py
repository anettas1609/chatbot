import openai  
import os  

# Načtení API klíče (doporučuji ho uložit do .env souboru)  
openai.api_key = "TVŮJ_API_KLÍČ"  

def chatbot(question):  
    response = openai.ChatCompletion.create(  
        model="gpt-4",  
        messages=[  
            {"role": "system", "content": "Jsi bezpečnostní asistent. Pomáháš rozpoznávat phishing a dezinformace."},  
            {"role": "user", "content": question}  
        ]  
    )  
    return response["choices"][0]["message"]["content"]  

# Test chatbota  
while True:  
    user_input = input("Zadej dotaz (nebo 'konec' pro ukončení): ")  
    if user_input.lower() == "konec":  
        break  
    print("Chatbot:", chatbot(user_input))  
