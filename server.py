from flask import Flask, request, send_from_directory
from replace import tagWords

app = Flask(__name__, static_folder='./build', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

# /convertText
@app.route('/convertText', methods=['POST'])
def convertText():
    data = request.get_json(force=True)
    text = data['input']
    newText = tagWords(text)
    return {"data": newText}

if __name__ == '__main__':
    app.run()
