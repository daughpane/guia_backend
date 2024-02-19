from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from ..models import Artwork, ArtworkImage
from ..serializers import ArtworkSerializer

class ArtworkCreateView(APIView):
    serializer_class = ArtworkSerializer
    permission_classes = [HasAPIKey]

    def post(self, request, *args, **kwargs):
      try:
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        artwork = serializer.validated_data['artwork']
        artwork.save()

        images = serializer.validated_data['images']
        thumbnail = serializer.validated_data['thumbnail']
        for image in images:
          artworkImage = ArtworkImage(
            artwork = artwork,
            image = image,
            is_thumbnail = thumbnail==str(image)
          )
          artworkImage.save()


        return Response(
          data = {
            'artwork_id': artwork.art_id
          },
          status=status.HTTP_201_CREATED
        )

      except ObjectDoesNotExist as e:
        return Response(
          data={
          'detail': e.args[0],
          'dev_message': ''
          }, 
          status=status.HTTP_400_BAD_REQUEST)

      except ValidationError as e:
        return Response(
          data={
            'detail': e.detail
          }, status=status.HTTP_400_BAD_REQUEST)

class ArtworkListView(APIView):
    serializer_class = ArtworkSerializer
    permission_classes = [HasAPIKey]

    def get(self, request, *args, **kwargs):
        artworks = Artwork.objects.all()
        serializer = self.serializer_class(artworks, many=True)
        
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK
        )