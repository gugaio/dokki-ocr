from flask import Flask, jsonify, request, send_file
from ocr.ocr import ocr_image
from ocr.parser import Parser
from flask import Flask
from flask_cors import CORS
from PIL import Image
import numpy as np
from io import BytesIO
from image.resize import resize_image

app = Flask(__name__)
CORS(app)

@app.route('/singlepage', methods=['POST'])
def singlepage():  
    doc = []  
    file = request.files['image']    
    binary_data = file.read()
    image_bytes_io = BytesIO(binary_data)
    image = Image.open(image_bytes_io)    
    img_array = np.array(image)    
    doc.append(img_array)
    data = ocr_image(doc)

    wordParser = Parser()
    page = wordParser.all_words_single_page(data)
    ocrJson = jsonify(page)
    print(ocrJson)
    return ocrJson

@app.route('/resize', methods=['POST'])
def resize():
    data = request.get_json()
    id = data['id']
    resize_image(id)
    return "success"
    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')