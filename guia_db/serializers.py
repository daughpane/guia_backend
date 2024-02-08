from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Admin
from .models import *

class AdminSerializer(serializers.Serializer):
  admin_username = serializers.CharField(required=True)
  admin_password = serializers.CharField(required=True)
  
  def validate(self, data):
    username = data.get('admin_username')
    password = data.get('admin_password')

    try:
      user = authenticate(username = username, password = password)
      admin = Admin.objects.get(user=user)
      
    except ObjectDoesNotExist:
      raise ObjectDoesNotExist("Admin username does not exist.")
    
    data['admin'] = admin
    return data



class ChangePasswordSerializer(serializers.Serializer):
    admin_id = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
      admin_id = data.get('admin_id')
      old_password = data.get('old_password')
      new_password = data.get('new_password')
      
      try:
        admin = Admin.objects.get(user__id=admin_id)
        
      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Admin username does not exist.")


      if not admin.user.check_password(old_password):
        raise AuthenticationFailed("Invalid old password.")

      if old_password==new_password:
        raise ValidationError("Password already used.")
          
      data['admin'] = admin
      return data




  

class MuseumSerializer(serializers.ModelSerializer):
  class Meta:
    model=Museum
    fields=('museum_id','museum_name')

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = '__all__'