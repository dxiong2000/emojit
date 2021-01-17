from flask import Flask, request
from replace import tagWords

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# /convertText
@app.route('/convertText', methods=['POST'])
def convertText():
    data = request.get_json(force=True)
    text = data['input']
    newText = tagWords(text)
    return {"data": newText}

app.run()
