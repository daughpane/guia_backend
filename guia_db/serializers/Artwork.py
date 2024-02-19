from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.core.exceptions import ObjectDoesNotExist

from ..models import Artwork, Section, Admin


def greater_than_zero(value):
    if value <= 0:
        raise ValidationError("Value must be greater than zero.")

def validate_images_length(images):
    if len(images) != 10:
        raise ValidationError("10 artwork images are required.")

class ArtworkSerializer(serializers.Serializer):
    section_id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=True)
    medium = serializers.CharField(required=True)
    date_published = serializers.CharField(required=True)
    dimen_width_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=True, validators=[greater_than_zero])
    dimen_length_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=True, validators=[greater_than_zero])
    dimen_height_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=False, validators=[greater_than_zero])
    description = serializers.CharField(required=True)
    additional_info = serializers.CharField()
    added_by = serializers.IntegerField(required=True)
    # Accepts list of images
    images = serializers.ListField(child=serializers.ImageField(), validators=[validate_images_length])
    thumbnail = serializers.CharField()

    def validate(self, data):
      section_id = data.get("section_id")
      title = data.get("title")
      medium = data.get("medium")
      date_published = data.get("date_published")
      description = data.get("description")
      additional_info = data.get("additional_info")
      added_by = data.get("added_by")
      dimen_width_cm = data.get("dimen_width_cm")
      dimen_length_cm = data.get("dimen_length_cm")
      dimen_height_cm = data.get("dimen_height_cm")
      images = data.get('images', [])
      thumbnail = data.get("thumbnail")

      try:
        section = Section.objects.get(section_id=section_id)

      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Section does not exist.")

      try:
        added_by = Admin.objects.get(user__id=added_by)

      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Admin does not exist.")
      
      
      artwork = Artwork(
        section_id=section,
        title=title,
        medium=medium,
        date_published=date_published,
        dimen_width_cm=dimen_width_cm,
        dimen_length_cm=dimen_length_cm,
        dimen_height_cm=dimen_height_cm,
        description=description,
        additional_info=additional_info,
        added_by=added_by
      )

      data['artwork'] = artwork
      data['images'] = images
      data['thumbnail'] = thumbnail
      return data
