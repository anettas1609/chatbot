import os

# Získání API klíče z prostředí
api_key = os.getenv('API_KEY')

# Zkontroluj, zda je klíč načten
if api_key:
    print("API key was successfully loaded from GitHub Secrets.")
else:
    print("API key was not found.")
