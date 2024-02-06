from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from datetime import timedelta

from rest_framework.exceptions import AuthenticationFailed, ValidationError

from json.decoder import JSONDecodeError
from ..models import Admin
from ..serializers import *

class AdminLoginApiView(ObtainAuthToken):
  serializer_class = AdminSerializer
  
  
  @permission_classes([AllowAny])
  def post(self, request, *args, **kwargs):
    try:
      # Parse JSON data from the request
      data = JSONParser().parse(request)
      
      # Use the AdminSerializer for validation and authentication
      serializer = self.serializer_class(data=data, context={'request': request})
      
      try:
          serializer.is_valid()
          admin = serializer.validated_data['admin']
          token, created = Token.objects.get_or_create(user=admin.user)
          
          if not created and hasattr(token, 'created'):
            token.created = token.created.replace(tzinfo=None)
            token.expires = token.created + timedelta(hours=5)
            token.save()

          response_data = {
            'admin_id': admin.admin_id, 
            'museum_id': admin.museum_id.museum_id,
            'token': token.key 
            }
          return Response(
            data = response_data,
            status=status.HTTP_200_OK
          )

      except AuthenticationFailed as e:
        return Response(data={
          'error': 'Invalid credentials.',
          'dev_message': 'Invalid credentials.'
          }, status=status.HTTP_401_UNAUTHORIZED)

      except ObjectDoesNotExist as e:
        return Response(data={
          'error': 'Invalid credentials.',
          'dev_message': 'Account does not exist.'
          }, status=status.HTTP_401_UNAUTHORIZED)

      except ValidationError as e:
        return Response(
          data={
            'error': 'Username and password are required.'
          }, status=status.HTTP_400_BAD_REQUEST)
    
    except JSONDecodeError:
        return JsonResponse(
          {"result": "error", "message": "JSON decoding error."},
          status=status.HTTP_408_REQUEST_TIMEOUT)