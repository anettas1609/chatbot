from flask import Flask, request, jsonify
import openai

# Nastavení API klíče
openai.api_key = "tvůj_api_klíč"  # nebo použít Vercel secrets

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("input")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
