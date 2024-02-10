from django.shortcuts import render
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from datetime import timedelta
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.exceptions import AuthenticationFailed, ValidationError
import traceback

from ..authentication import token_expire_handler, expires_in, ExpiringTokenAuthentication

from json.decoder import JSONDecodeError
from ..models import Admin
from ..serializers import *


class AdminLoginApiView(ObtainAuthToken):
  serializer_class = AdminSerializer
  permission_classes = [HasAPIKey]
  def post(self, request, *args, **kwargs):
    try:
      # Parse JSON data from the request
      data = JSONParser().parse(request)
      
      # Use the AdminSerializer for validation and authentication
      serializer = self.serializer_class(data=data, context={'request': request})
      
      try:
          serializer.is_valid(raise_exception=True)
          admin = serializer.validated_data['admin']
          
          token, created = Token.objects.get_or_create(user=admin.user)
          is_expired, token = token_expire_handler(token)   
          token.save()

          response_data = {
            'admin_id': admin.user.id, 
            'museum_id': admin.museum_id.museum_id,
            'token': token.key, 
            'token_expires': token.created+expires_in(token),
            'token_created': token.created
            }

          return Response(
            data = response_data,
            status=status.HTTP_200_OK
          )

      except ObjectDoesNotExist as e:
        return Response(data={
          'error': 'Invalid credentials.',
          'dev_message': 'Wrong username or password.'
          }, status=status.HTTP_401_UNAUTHORIZED)

      except ValidationError as e:
        return Response(
          data={
            'error': e.detail,
            'dev_message':'Missing parameters.'
          }, status=status.HTTP_400_BAD_REQUEST)
    
    except JSONDecodeError:
        return JsonResponse(
          {"error": "Internal error.", "dev_message": "JSON decoding error."},
          status=status.HTTP_408_REQUEST_TIMEOUT)



class ChangePasswordApiView(APIView):
    permission_classes = [IsAuthenticated, HasAPIKey]
    authentication_classes = [SessionAuthentication, ExpiringTokenAuthentication]
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):    

      try:
        # Use the AdminSerializer for validation and authentication
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        admin = serializer.validated_data['admin']
        new_password = serializer.validated_data['new_password']

        admin.user.set_password(new_password)
        admin.user.save()

        return Response(
          {'message': 'Password changed successfully.'},
          status=status.HTTP_200_OK
      )

      except AuthenticationFailed as e:
        return Response(data={
          'error': e.detail,
          'dev_message': 'Invalid credentials.'
          }, status=status.HTTP_401_UNAUTHORIZED)

      except ObjectDoesNotExist as e:
        return Response(data={
          'error': e.args[0],
          'dev_message': 'Account does not exist.'
          }, status=status.HTTP_401_UNAUTHORIZED)

      except ValidationError as e:
        return Response(
          data={
            'error': e.detail
          }, status=status.HTTP_400_BAD_REQUEST)

class AdminLogoutApiView(APIView):
  permission_classes = [IsAuthenticated, HasAPIKey]
  serializer_class = LogoutSerializer

  def post(self, request, *args, **kwargs):  
    try:
      # Use the AdminSerializer for validation and authentication
      serializer = self.serializer_class(data=request.data, context={'request': request})
      serializer.is_valid(raise_exception=True)

      admin = serializer.validated_data['admin']  
      token = Token.objects.get(user=admin.user)
      token.delete()

      return Response(
          {'message': 'Logout successful.'},
          status=status.HTTP_200_OK)

    except ObjectDoesNotExist as e:
      return Response(data={
        'error': e.args[0],
        'dev_message': 'Account does not exist.'
        }, status=status.HTTP_401_UNAUTHORIZED)

    except ValidationError as e:
      return Response(
        data={
          'error': e.detail
        }, status=status.HTTP_400_BAD_REQUEST)


