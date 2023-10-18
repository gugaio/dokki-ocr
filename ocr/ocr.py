from doctr.models import ocr_predictor

model = ocr_predictor(pretrained=True)

def ocr_image(doc):
    result = model(doc) 
    return result.export()