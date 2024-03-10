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
from ..serializers import GetDashboardSerializer, ArtworkSerializer, ArtworkImageSerializer, SectionSerializer

from ..authentication import ExpiringTokenAuthentication

from ..utils import get_presigned_urls

class DashboardStatsView(APIView):
  serializer_class = GetDashboardSerializer
  permission_classes = [IsAuthenticated, HasAPIKey]
  authentication_classes = [ExpiringTokenAuthentication]

  def get(self, request, *args, **kwargs):
    try:
      serializer = self.serializer_class(data=request.query_params, context={'request': request})
      serializer.is_valid(raise_exception=True)
      artworks_count = serializer.validated_data['artworks_count']
      popular_artworks = serializer.validated_data['popular_artworks']
      visitors_count = serializer.validated_data['visitors_count']
      popular_sections = serializer.validated_data['popular_sections']

      popular_artworks_data = ArtworkSerializer(popular_artworks, many=True).data

      popular_sections_data = SectionSerializer(popular_sections, many=True).data

      for art in popular_artworks_data:
        images = ArtworkImage.objects.all().filter(artwork__art_id=art["art_id"], is_deleted=False, is_thumbnail=True)
        if len(images) > 0:
          art["image_thumbnail"] = images[0]._image_link

      return Response(
          data = {
            'artworks_count': artworks_count, 
            'visitors_count': visitors_count,
            'popular_artworks': popular_artworks_data,
            'popular_sections':popular_sections_data
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