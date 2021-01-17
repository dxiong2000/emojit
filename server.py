from flask import Flask, request
from replace import tagWords

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# /convertText
@app.route('/convertText', methods=['POST'])
def convertText():
    newText = tagWords(text)
    
app.run()
