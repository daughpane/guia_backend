from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from ..models import Artwork, ArtworkImage
from ..serializers import ArtworkSerializer, ArtworkViewSerializer, ArtworkImageSerializer, ArtworkCreateSerializer, ArtworkEditSerializer, ArtworkDeleteSerializer

from ..authentication import ExpiringTokenAuthentication

from ..utils import get_presigned_urls

class ArtworkCreateView(APIView):
    serializer_class = ArtworkCreateSerializer
    permission_classes = [IsAuthenticated, HasAPIKey]
    authentication_classes = [SessionAuthentication, ExpiringTokenAuthentication]

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
            image_link = str(image),
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

class ArtworkView(APIView):
    serializer_class = ArtworkViewSerializer
    permission_classes = [IsAuthenticated, HasAPIKey]
    authentication_classes = [SessionAuthentication, ExpiringTokenAuthentication]

    def get(self, request, *args, **kwargs):
      try:
        serializer = self.serializer_class(data=request.query_params, context={'request': request})
        serializer.is_valid(raise_exception=True)

        artwork = serializer.validated_data['artwork']

        images = serializer.validated_data['images']

        images_presigned = []

        for image in images:
          images_presigned.append(image._image_link)

        artwork_data = ArtworkSerializer(artwork).data
        artwork_data["images"] = images_presigned

        return Response(
          data = {
            'artwork': artwork_data
          },
          status=status.HTTP_200_OK
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

class ArtworkEditView(APIView):
    serializer_class = ArtworkEditSerializer
    permission_classes = [IsAuthenticated, HasAPIKey]
    authentication_classes = [SessionAuthentication, ExpiringTokenAuthentication]
    
    def post(self, request, *args, **kwargs):
      try:
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        artwork = serializer.validated_data['artwork']
        artwork.save()
        
        images_list = serializer.validated_data['images_list']
        images_url = serializer.validated_data['images_url']
        thumbnail = serializer.validated_data['thumbnail']

        for index, artworkImage in enumerate(images_list):
          artworkImage.image_link = str(images_url[index])
          artworkImage.is_thumbnail = thumbnail == str(images_url[index])
          artworkImage.save()

        return Response(
          data = {
            'message': "Artwork edited successfully."
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


class ArtworkDeleteView(APIView):
  serializer_class = ArtworkDeleteSerializer
  permission_classes = [IsAuthenticated, HasAPIKey]

  def post(self, request, *args, **kwargs):
      try:
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        artwork = serializer.validated_data['artwork']
        artwork.is_deleted = True

        images_list = serializer.validated_data['images_list']

        for image in images_list:
          image.is_deleted = True
          image.save()

        artwork.save()

        return Response(
          data = {
            'message': "Artwork deleted successfully."
          },
          status=status.HTTP_200_OK
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