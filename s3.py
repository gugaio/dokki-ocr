import boto3
from dotenv import load_dotenv

load_dotenv()

import os

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET = 'notas-dev-s3'

s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def download(key, filetemp):
    s3_client.download_file(Bucket='notas-dev-s3', Key=key, Filename=filetemp)

def upload(file,key):
    s3_client.upload_fileobj(file, S3_BUCKET, key)
