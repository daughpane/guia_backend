from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from django.core.exceptions import ObjectDoesNotExist

from ..models import Section

class GetSectionSerializer(serializers.Serializer):
  section_id = serializers.CharField(required=False)

  def validate(self, data):
    section_id = data.get('section_id')

    if(section_id == None):
      section = Section.objects.all()
    else:
      section = Section.objects.all().filter(section_id=section_id)

      if(len(section)==0):
        raise ObjectDoesNotExist("Section not found.")
      
    data['section'] = section
    return data

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
      model = Section
      fields = '__all__'
    