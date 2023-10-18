from flask import Flask, jsonify, request, redirect
from ocr.ocr import ocr_image
from ocr.parser import Parser
from flask import Flask
from flask_cors import CORS
from PIL import Image
import numpy as np
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route('/singlepage', methods=['POST'])
def singlepage():  
    doc = []  
    print("check request.files")
    print(request.files)
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
    
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')