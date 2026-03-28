 from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static')
CORS(app)

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    if not GEMINI_API_KEY:
        return jsonify({'error': 'API key not configured on server'}), 500

    data = request.json
    system_prompt = data.get('systemPrompt', '')
    chat_history  = data.get('chatHistory', [])

    contents = [
        {'role': 'user',  'parts': [{'text': system_prompt + '\n\nAcknowledge briefly.'}]},
        {'role': 'model', 'parts': [{'text': 'Understood! Ready to help.'}]},
    ]
    for msg in chat_history:
        contents.append({
            'role': 'model' if msg['role'] == 'assistant' else 'user',
            'parts': [{'text': msg['content']}]
        })

    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}'
    resp = requests.post(url, json={'contents': contents})
    result = resp.json()

    if 'error' in result:
        return jsonify({'error': result['error']['message']}), 500

    reply = result['candidates'][0]['content']['parts'][0]['text']
    return jsonify({'reply': reply})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
