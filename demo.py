from doctr.io import DocumentFile
from doctr.models import ocr_predictor
from PIL import Image
import numpy as np
from io import BytesIO
import torch

model = ocr_predictor(pretrained=True)
image = Image.open("nota.png").convert('RGB')
img_array = np.array(image)
print(img_array.shape)
img_array = img_array[...,:3]

# PDF
doc = DocumentFile.from_images("nota.png")
print(doc[0].shape)
# Analyze
result = model([img_array])
# Export
print(result.export())
