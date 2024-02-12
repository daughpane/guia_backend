from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from django.core.exceptions import ObjectDoesNotExist

from ..models import Museum

class GetMuseumSerializer(serializers.Serializer):
  museum_id = serializers.CharField(required=False)

  def validate(self, data):
    museum_id = data.get('museum_id')

    if(museum_id == None):
      museum = Museum.objects.all()
    else:
      museum = Museum.objects.all().filter(museum_id=museum_id)

      if(len(museum)==0):
        raise ObjectDoesNotExist("Museum not found.")
      
    data['museum'] = museum
    return data

class MuseumSerializer(serializers.ModelSerializer):
    class Meta:
      model = Museum
      fields = '__all__'
    