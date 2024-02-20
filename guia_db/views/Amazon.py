# In views.py of your Django app

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.permissions import HasAPIKey

import boto3
import environ
import os

env = environ.Env()
environ.Env.read_env()

class S3CredentialsAPIView(APIView):
    permission_classes = [HasAPIKey]

    def post(self, request):
        # Replace these variables with your own AWS credentials and bucket name
        aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
        aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
        bucket_name = os.environ['AWS_STORAGE_BUCKET_NAME']

        try:
          s3_client = boto3.client(
              's3',
              aws_access_key_id=aws_access_key_id,
              aws_secret_access_key=aws_secret_access_key
          )
          
          image_name = request.data.get("image_name")
          
          #Generate the presigned URL
          image_ext = image_name.split('.')[-1]

          if image_ext != "jpeg" and image_ext != "jpg":
            return Response(
              data={
              'detail': "Only JPEG files are allowed.",
              'dev_message': ''
              }, 
              status=status.HTTP_403_FORBIDDEN
          )

          response = s3_client.generate_presigned_post(
              Bucket = bucket_name,
              Key = f"artworks/{image_name}",
              ExpiresIn = 600,
              Fields={"Content-Type": "image/jpeg"},
              Conditions = [ {"Content-Type": "image/jpeg"} ]
          )

          return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            # Handle error
            error_message = f"Error occurred: {str(e)}"
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
