from flask import Flask, jsonify, request
from ocr.ocr import ocr_image
from ocr.parser import Parser
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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