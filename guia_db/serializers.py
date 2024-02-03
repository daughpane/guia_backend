from rest_framework import serializers
from .models import Museum

class MuseumSerializer(serializers.ModelSerializer):
  class Meta:
    model=Museum
    fields=('museum_id','museum_name')