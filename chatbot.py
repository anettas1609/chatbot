import os

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API klíč nebyl nalezen. Přidej ho do GitHub Secrets nebo prostředí.")
