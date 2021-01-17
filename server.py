from flask import Flask, request
from bs4 import BeautifulSoup
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
