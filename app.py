from flask import Flask, request
from os import environ
import requests
from os import environ
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Eric's Ghost!"

@app.route('/ghost-event', methods=['POST'])
def webhook():
    if request.method == 'POST':
        received = request.json
        event_url = received.get('api_url')

        API_KEY = environ.get('PRIVATE_API_KEY')

        headers = {
            'Authorization': f"Bearer {API_KEY}",
        }
        
        response = requests.get(event_url, headers=headers).json()

        return response