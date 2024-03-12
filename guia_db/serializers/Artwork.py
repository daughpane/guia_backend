from rest_framework import serializers
from rest_framework.exceptions import ValidationError, PermissionDenied

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.db.models import Q

from ..models import Artwork, Section, Admin, ArtworkImage


def greater_than_zero(value):
    if value <= 0:
        raise ValidationError("Value must be greater than zero.")

def validate_images_length(images):
    if len(images) != 10:
        raise ValidationError("10 artwork images are required.")

class ArtworkCreateSerializer(serializers.Serializer):
    section_id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=True)
    artist_name = serializers.CharField(required=True)
    medium = serializers.CharField(required=True)
    date_published = serializers.CharField(required=True)
    dimen_width_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=True, validators=[greater_than_zero])
    dimen_length_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=True, validators=[greater_than_zero])
    dimen_height_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=False, validators=[greater_than_zero], allow_null=True)
    description = serializers.CharField(required=True)
    additional_info = serializers.CharField(required=False, allow_null=True, allow_blank=True)
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

      # Check if section exists
      try:
        section = Section.objects.get(section_id=section_id)

      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Section does not exist.")

      # Check if added by id is one of the admin
      try:
        added_by = Admin.objects.get(user__id=added_by)
        
      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("User does not exist.")
      
      # Check if who is logged in is who made the create request
      request_user = self.context['request'].user
      if added_by.user != request_user:
        raise PermissionDenied("Logged in admin should make the create artwork request.")

      # Check if ang iyang gi edit an section is sa museum na iyang gi work-an
      if section.museum_id != added_by.museum_id:
        raise PermissionDenied("Admin not allowed to add artwork in this section.")

      
      if Artwork.objects.filter(title=title, artist_name=artist_name, is_deleted=False, section_id=section).exists():
          raise ValidationError({"duplicate_artwork": "Artwork with the same title and artist name already exists."})

      if thumbnail not in images:
        raise ValidationError({"thumbnail": "Thumbnail should be one of the images."})
      
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
  admin_id = serializers.IntegerField(required=False)

  def validate(self, data):
    art_id = data.get("art_id")
    admin_id = data.get("admin_id")

    try:
      artwork = Artwork.objects.get(art_id=art_id, is_deleted=False)
      images = ArtworkImage.objects.all().filter(artwork=artwork, is_deleted=False)
      
    except ObjectDoesNotExist:
      raise ObjectDoesNotExist("Artwork does not exist.")
    
    if admin_id != None:
      try: 
        admin = Admin.objects.get(user__id=admin_id)
      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Admin does not exist.")

      if artwork.section_id.museum_id != admin.museum_id:
        raise PermissionDenied("Admin not allowed to acess this artwork.")

    data['artwork'] = artwork
    data['images'] = images
    return data

class ArtworkEditSerializer(serializers.Serializer):
    art_id = serializers.IntegerField(required=True)
    section_id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=True)
    artist_name = serializers.CharField(required=True)
    medium = serializers.CharField(required=True)
    date_published = serializers.CharField(required=True)
    dimen_width_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=True, validators=[greater_than_zero])
    dimen_length_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=True, validators=[greater_than_zero])
    dimen_height_cm = serializers.DecimalField(max_digits=100, decimal_places=2, required=False, validators=[greater_than_zero], allow_null=True)
    description = serializers.CharField(required=True)
    additional_info = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    updated_by = serializers.IntegerField(required=True)
    # Accepts list of images
    images = serializers.ListField(child=serializers.CharField(), validators=[validate_images_length])
    thumbnail = serializers.CharField()

    def validate(self, data):
      art_id = data.get("art_id")
      section_id = data.get("section_id")
      title = data.get("title")      
      artist_name = data.get("artist_name")
      medium = data.get("medium")
      date_published = data.get("date_published")
      description = data.get("description")
      additional_info = data.get("additional_info")
      updated_by = data.get("updated_by")
      dimen_width_cm = data.get("dimen_width_cm")
      dimen_length_cm = data.get("dimen_length_cm")
      dimen_height_cm = data.get("dimen_height_cm")
      images_url = data.get('images', [])
      thumbnail = data.get("thumbnail")
      
      try:
        section = Section.objects.get(section_id=section_id)
      
      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Section does not exist.")

      try: 
        updated_by = Admin.objects.get(user__id=updated_by)

      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("User does not exist.")

      # Check if who is logged in is who made the create request
      request_user = self.context['request'].user
      if updated_by.user != request_user:
        # raise PermissionDenied("Logged in admin should make the edit artwork request.")
        raise PermissionDenied("Unathorized Access.")

      # Check if ang iyang gi edit an section is sa museum na iyang gi work-an
      if section.museum_id != updated_by.museum_id:
        # raise PermissionDenied("Admin not allowed to edit artwork in this section.")
        raise PermissionDenied("Unauthorized Access.")

      try:
        artwork = Artwork.objects.get(art_id=art_id, is_deleted=False)
        images_list = ArtworkImage.objects.all().filter(artwork=artwork, is_deleted=False)
      
      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Artwork does not exist.")
      
      if Artwork.objects.filter(
          title__iexact=title, 
          artist_name__iexact=artist_name,
          is_deleted=False, 
          section_id__museum_id=section.museum_id).exclude(art_id=art_id).exists():
          raise ValidationError({"duplicate_artwork": "Artwork with the same title and artist name already exists."})

      if thumbnail not in images_url:
          raise ValidationError({"thumbnail": "Thumbnail should be one of the images."})

      artwork.section_id = section
      artwork.title = title
      artwork.artist_name = artist_name
      artwork.medium = medium
      artwork.date_published = date_published
      artwork.description = description
      artwork.additional_info = additional_info
      artwork.updated_by = updated_by
      artwork.updated_on = timezone.now()
      artwork.dimen_width_cm = dimen_width_cm
      artwork.dimen_length_cm = dimen_length_cm
      artwork.dimen_height_cm = dimen_height_cm
      artwork.thumbnail = thumbnail

      data['artwork'] = artwork
      data['images_url'] = images_url
      data['images_list'] = images_list
      data['thumbnail'] = thumbnail
      return data

class ArtworkDeleteSerializer(serializers.Serializer):
  art_id = serializers.IntegerField(required=True)

  def validate(self, data):
      art_id = data.get("art_id")

      try:
        artwork = Artwork.objects.get(art_id=art_id, is_deleted=False)
        images_list = ArtworkImage.objects.all().filter(artwork=artwork, is_deleted=False)

      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Artwork does not exist.")
        
      request_user = self.context['request'].user
      try:
        admin = Admin.objects.get(user=request_user)
      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Admin does not exist.")

      if artwork.section_id.museum_id != admin.museum_id:
        raise PermissionDenied("Admin not allowed to delete artwork in this section.")

      artwork.updated_on = timezone.now()
      artwork.updated_by = admin
      
      data['artwork'] = artwork
      data['images_list'] = images_list
      return data

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
      model = Artwork
      fields = '__all__'

class ArtworkImageSerializer(serializers.ModelSerializer):
    class Meta:
      model = ArtworkImage
      fields = ['image_link', 'is_thumbnail']
    
class ArtworkListViewSerializer(serializers.Serializer):
  admin_id = serializers.IntegerField(required=True)

  def validate(self, data):
    admin_id = data.get("admin_id")
    try:
      admin_id = Admin.objects.get(user__id=admin_id)
      artworks = Artwork.objects.all().filter(
        section_id__museum_id = admin_id.museum_id,
        is_deleted=False
      ).order_by("art_id")

      data["artworks"] = artworks
      return data
    except ObjectDoesNotExist:
      raise ObjectDoesNotExist("User does not exist.")