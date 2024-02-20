from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.core.exceptions import ObjectDoesNotExist

from ..models import Artwork, Section, Admin, ArtworkImage


def greater_than_zero(value):
    if value <= 0:
        raise ValidationError("Value must be greater than zero.")

def validate_images_length(images):
    if len(images) != 10:
        raise ValidationError("10 artwork images are required.")

class ArtworkSerializer(serializers.Serializer):
    section_id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=True)
    artist_name = serializers.CharField(required=True)
    medium = serializers.CharField(required=True)
    date_published = serializers.CharField(required=True)
    dimen_width_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=True, validators=[greater_than_zero])
    dimen_length_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=True, validators=[greater_than_zero])
    dimen_height_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=False, validators=[greater_than_zero])
    description = serializers.CharField(required=True)
    additional_info = serializers.CharField()
    added_by = serializers.IntegerField(required=True)
    # Accepts list of images
    images = serializers.ListField(child=serializers.CharField(), validators=[validate_images_length])
    thumbnail = serializers.CharField()

    def validate(self, data):
      section_id = data.get("section_id")
      title = data.get("title")      
      artist_name = data.get("artist_name")
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
      
      if Artwork.objects.filter(title=title, artist_name=artist_name).exists():
          raise ValidationError({"duplicate_artwork": "Artwork with the same title and artist name already exists."})
      
      artwork = Artwork(
        section_id=section,
        title=title,
        artist_name=artist_name,
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

class ArtworkViewSerializer(serializers.Serializer):
  art_id = serializers.IntegerField(required=True)

  def validate(self, data):
    art_id = data.get("art_id")
    try:
      artwork = Artwork.objects.get(art_id=art_id)
      images = ArtworkImage.objects.all().filter(artwork=artwork)
      
    except ObjectDoesNotExist:
      raise ObjectDoesNotExist("Artwork does not exist.")

    data['artwork'] = artwork
    data['images'] = images
    return data


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
      model = Artwork
      fields = '__all__'

class ArtworkImageSerializer(serializers.ModelSerializer):
    class Meta:
      model = ArtworkImage
      fields = ['image_link', 'is_thumbnail']
    