from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Museum
from ..serializers import *

# Create your views here.
@api_view(['GET'])
def getAllMuseums(request):
  app = Museum.objects.all()
  serializer = MuseumSerializer(app, many=True)
  return Response(serializer.data)

# class MuseumListAPIView(APIView):
#   def get(self, request, *args, **kwargs):
#       museums = Museum.objects.all()
#       serializer = MuseumSerializer(museums, many=True)
#       return Response(serializer.data)