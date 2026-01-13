import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SERVER_URL = "https://ai.hackclub.com/proxy/v1"
MODEL = "google/gemini-3-flash-preview"  # Use your preferred model

app = Flask(__name__)

@app.route('/generate-idea', methods=['POST'])
def generate_idea():
    data = request.get_json()
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a creative assistant that generates unique and fun coding project ideas for users of all skill levels."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    try:
        response = requests.post(f"{SERVER_URL}/chat/completions", headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        idea = response.json()['choices'][0]['message']['content']
        return jsonify({'result': idea})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
