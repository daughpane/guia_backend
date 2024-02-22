from rest_framework import serializers
from ..models import ArtworkImage, Artwork
from .Artwork import ArtworkSerializer

class ArtGroupSerializer(serializers.Serializer):
    art_id = serializers.IntegerField(source='artwork__art_id')
    image_links = serializers.ListField(child=serializers.CharField())