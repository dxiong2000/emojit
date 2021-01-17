from flask import Flask, request
from scrape import getEmojiList

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# /convertText
@app.route('/convertText', methods=['POST'])
def convertText():
    # emojiList = getEmojiList(searchStr)
    
app.run()
