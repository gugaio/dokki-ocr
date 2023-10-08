from flask import Flask, jsonify, request, redirect
from ocr.ocr import ocr_image
from ocr.parser import Parser
from flask import Flask
from flask_cors import CORS
import uuid
import os
from aws.s3 import upload, uploadDict


app = Flask(__name__)
CORS(app)

@app.route('/ocr', methods=['GET'])
def get_ocr():
    agent = request.args.get('agent')
    sender = request.args.get('sender')
    uuid = request.args.get('uuid')
    extension = 'jpg'
    key = f"{agent}/{sender}/{uuid}.{extension}"

    data = ocr_image(key)
    return jsonify(data)

@app.route('/singlepage', methods=['GET'])
def get_singlepage():
    agent = request.args.get('agent')
    sender = request.args.get('sender')
    uuid = request.args.get('uuid')
    extension = 'jpg'
    key = f"{agent}/{sender}/{uuid}.{extension}"

    
    data = ocr_image(key)
    wordParser = Parser()
    page = wordParser.all_words_single_page(data)
    uploadDict(page, f"{agent}/{sender}/{uuid}__ocr.json")
    ocrJson = jsonify(page)
    return ocrJson

@app.route('/labels', methods=['POST'])
def labels():
    agent = request.args.get('agent')
    sender = request.args.get('sender')
    uuid = request.args.get('uuid')

    key = agent + "/" + sender + "/" + uuid + "__labels.json"

     # Get the JSON payload
    payload = request.get_json()
    uploadDict(payload, key) 

    print(payload)
    return "OK"

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

    if file:
        try:          
            upload(file, key) 
            return 'File uploaded successfully!!!' + file.filename
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')