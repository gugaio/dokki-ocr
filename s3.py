import boto3
from dotenv import load_dotenv

load_dotenv()

import os

AWS_ACCESS_KEY_ID = os.getenv("AKIA5V4H4C5INBPTMLDW")
AWS_SECRET_ACCESS_KEY = os.getenv("Ko3CQMxJDKNLHt7Jl8")

s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

#uploads/dokki/client/66cc52e8-42af-4d22-bf38-4d0beefff6cc.jpg

def download(key, filetemp):
    s3_client.download_file(Bucket='notas-dev-s3', Key=key, Filename=filetemp)
