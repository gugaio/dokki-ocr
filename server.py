from flask import Flask, jsonify, request, redirect
from ocr.ocr import ocr_image
from ocr.parser import Parser
from flask import Flask
from flask_cors import CORS
import uuid
import os
from s3 import upload


app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    file_extension = os.path.splitext(file.filename)[1]
    filename = str(uuid.uuid4()) + file_extension

    agent = request.args.get('agent')
    sender = request.args.get('sender')

    key = agent + "/" + sender + "/" + filename
    print("key: " + key)

    if file:
        try:          
            upload(file, key) 
            return 'File uploaded successfully!!!' + file.filename
        except Exception as e:
            return str(e)

@app.route('/ocr', methods=['GET'])
def get_ocr():
    agent = request.args.get('agent')
    sender = request.args.get('sender')
    uuid = request.args.get('uuid')
    key = agent + "/" + sender + "/" + uuid  + ".jpg"
    print("key: " + key)
    data = ocr_image(key)
    return jsonify(data)

@app.route('/singlepage', methods=['GET'])
def get_singlepage():
    agent = request.args.get('agent')
    sender = request.args.get('sender')
    uuid = request.args.get('uuid')
    key = agent + "/" + sender + "/" + uuid  + ".jpg"
    print("key: " + key)
    data = ocr_image(key)
    wordParser = Parser()
    page = wordParser.all_words_single_page(data)
    return jsonify(page)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')