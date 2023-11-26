import boto3
from io import BytesIO
from PIL import Image
import dotenv
import os

dotenv.load_dotenv() 

# AWS credentials and S3 bucket details
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
bucket_name = os.environ.get("BUCKET_NAME")

def make_square(im, target_size=1000, fill_color=(0, 0, 0)):
    x, y = im.size
    size = max(x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    if size != target_size:
        new_im = new_im.resize((target_size, target_size))
    return new_im

def resize_image(s3Key):
  source_image_key = s3Key
  destination_image_key = s3Key

  # Initialize the S3 client
  s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

  # Get the original image from S3
  response = s3.get_object(Bucket=bucket_name, Key=source_image_key)
  content_type = response['ContentType']
  original_image_data = response['Body'].read()

  # Resize the image to a square of 1000x1000 pixels
  original_image = Image.open(BytesIO(original_image_data))
  original_image = make_square(original_image)
  output_buffer = BytesIO()
  original_image.save(output_buffer, format='JPEG')
  resized_image_data = output_buffer.getvalue()

  # Update the resized image in S3
  s3.put_object(Bucket=bucket_name, Key=destination_image_key, Body=resized_image_data, ContentType=content_type)
