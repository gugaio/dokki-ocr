FROM python:3.8-slim

RUN apt-get update \
    && apt-get install --no-install-recommends ffmpeg libsm6 libxext6 -y \
    && pip install python-doctr \
    && pip install rapidfuzz==2.15.1 \
    && pip install torch torchvision torchaudio

RUN pip install Flask
RUN pip install flask-requests
RUN pip install flask-cors
RUN pip install boto3
RUN pip install python-dotenv

COPY . .

RUN mkdir temp

EXPOSE 5000

CMD [ "python3", "server.py"]


