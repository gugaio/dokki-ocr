from doctr.io import DocumentFile
from doctr.models import ocr_predictor
from aws.s3 import download
import os


S3_BUCKET_NAME = 'notas-dev-s3'


model = ocr_predictor(pretrained=True)

def check_filetemp_exists(path):
    return os.path.exists(path)

def ocr_image(key):
    filetemp = 'temp/' + os.path.basename(key)
    if not check_filetemp_exists(filetemp):
        download(key, filetemp)
    doc = DocumentFile.from_images(filetemp)
    result = model(doc) 
    return result.export()

if __name__ == '__main__':
    sample_key = 'agent=dokki&sender=guga&filename=5894449e-95f5-44a3-8ad9-f7d0c7ed6242.jpg'
    print(ocr_image(sample_key))