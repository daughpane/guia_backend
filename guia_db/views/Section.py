from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework import status

from ..models import Section
from ..serializers import *

class SectionApiView(APIView):
  permission_classes = [HasAPIKey]
  serializer_class = GetSectionSerializer

  def get(self, request, *args, **kwargs):
    try:
      # request.query_params kay get request man
      serializer = self.serializer_class(
        data=request.query_params, 
        context={'request': request})
      serializer.is_valid(raise_exception=True)

      section = serializer.validated_data['section']

      # SectionSerializer makes the list to JSON file
      return Response(
        {'section': SectionSerializer(section, many=True).data},
        status=status.HTTP_200_OK
      )

    except ObjectDoesNotExist as e:
      return Response(data={
        'detail': e.args[0],
        'dev_message': 'Section does not exist.'
        }, status=status.HTTP_404_NOT_FOUND)

    except ValidationError as e:
      return Response(
        data={
          'detail': e.detail
        }, status=status.HTTP_400_BAD_REQUEST)
    