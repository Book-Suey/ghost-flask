from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Eric's Ghost!"

@app.route('/ghost-event', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print('Data received from Webhook is: ', request.json)
        return "Webhook received!"