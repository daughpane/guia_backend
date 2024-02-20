from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from django.core.exceptions import ObjectDoesNotExist

from ..models import Section, Museum

class GetSectionSerializer(serializers.Serializer):
  section_id = serializers.CharField(required=False)
  museum_id = serializers.CharField(required=True)

  def validate(self, data):
    section_id = data.get('section_id')
    museum_id = data.get('museum_id')

    try:
      museum = Museum.objects.get(museum_id=museum_id)
    except ObjectDoesNotExist:
      raise ObjectDoesNotExist("Museum not found.")

    if(section_id == None):
      section = Section.objects.filter(museum_id=museum.museum_id)
    else:
      section = Section.objects.filter(museum_id=museum.museum_id, section_id=section_id)

      if(len(section)==0):
        raise ObjectDoesNotExist("Section not found.")
      
    data['section'] = section
    return data

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
      model = Section
      fields = '__all__'
    