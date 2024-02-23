from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from django.db.models import F
from django.contrib.postgres.aggregates import ArrayAgg
from django.core.exceptions import FieldError

from ..models import ArtworkImage, Artwork
from ..serializers import ArtGroupSerializer

class ArtworkImageGetView(APIView):
  permission_classes = [HasAPIKey]

  def get(self, request, *args, **kwargs):
    try:
      filtered_artworks = Artwork.objects.filter(is_deleted=False)
      artworkImages = ArtworkImage.objects.filter(
         artwork__in=filtered_artworks,
         is_deleted=False
      ).values('artwork__art_id').annotate(
        image_links = ArrayAgg('image_link')
      ).order_by('artwork__art_id')

      serializer = ArtGroupSerializer(artworkImages, many=True)

      return Response(
        {"artwork_images":serializer.data},
        status=status.HTTP_200_OK
      )

    except (NameError, FieldError) as e:
        return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    except ValidationError as e:
        return Response({'detail': str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

