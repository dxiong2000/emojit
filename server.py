from flask import Flask, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# /getEmoji?search=SearchStr
@app.route('/getEmoji')
def getEmoji():
    searchStr = request.args.get('search')
    