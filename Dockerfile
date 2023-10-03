FROM python:3.8-slim

RUN apt-get update \
    && apt-get install --no-install-recommends ffmpeg libsm6 libxext6 -y \
    && pip install boto3 \
    && pip install python-doctr \
    && pip install rapidfuzz==2.15.1 \
    && pip install torch torchvision torchaudio

RUN pip install Flask
RUN pip install flask-requests
RUN pip install flask-cors

RUN mkdir temp

COPY ./ocr.py .
COPY ./s3.py .
COPY ./server.py .

EXPOSE 5000

CMD [ "python3", "server.py"]


