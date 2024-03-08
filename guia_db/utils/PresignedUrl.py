import boto3
import environ
import os

env = environ.Env()
environ.Env.read_env()

def get_presigned_urls(key, expires_in=86400):
  aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
  aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
  bucket_name = os.environ['AWS_STORAGE_BUCKET_NAME']

  s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
      )
  
  return s3_client.generate_presigned_url('get_object',
                Params={'Bucket': bucket_name,
                        'Key': key},
                ExpiresIn=expires_in)

