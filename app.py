from flask import Flask, request, jsonify
import google.generativeai as genai
import os

# Initialize Flask app
app = Flask(__name__)

# Configure Gemini API key (set your API key as an environment variable)
GOOGLE_API_KEY = "AIzaSyD4aq8i3-_9J0RQ8td4nS4-AmC3vOQ4qZE"
genai.configure(api_key=GOOGLE_API_KEY)

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json

    # Get query, prompt, and context from the request
    query = data.get("query", "")
    prompt = data.get("prompt", "")
    context = data.get("context", "")

    # Combine them into a final prompt
    final_prompt = f"{context}\n\n{prompt}\n\nQuestion: {query}"

    try:
        # Generate response from Gemini
        response = model.generate_content(final_prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
