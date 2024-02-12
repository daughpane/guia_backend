from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from django.core.exceptions import ObjectDoesNotExist

from ..models import Visitor, Museum

class VisitorSerializer(serializers.Serializer):
  museum_id = serializers.CharField(required=True)

  def validate(self, data):
    museum_id = data.get("museum_id")
    try:
      # Check if ang museum ID kay id jud sa usa ka museum
      museum = Museum.objects.get(museum_id=museum_id)
    except ObjectDoesNotExist:
      raise ObjectDoesNotExist("Museum does not exist.")

    data['museum'] = museum
    return data
