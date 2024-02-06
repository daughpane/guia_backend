from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from .models import Admin
from .models import *

class AdminSerializer(serializers.ModelSerializer):

  class Meta:
    model=Admin
    fields=['admin_username', 'admin_password']
  
  def validate(self, data):
    username = data.get('admin_username')
    password = data.get('admin_password')
    if not username or not password:
      raise ValidationError("Username and password are required.")

    try:
      admin = Admin.objects.get(admin_username=username)
      
    except ObjectDoesNotExist:
      raise ObjectDoesNotExist("Admin username does not exist.")
    
    if not admin.checkPassword(input_password=password):
      raise AuthenticationFailed("Incorrect password.")
    
    data['admin'] = admin
    return data



class ChangePasswordSerializer(serializers.Serializer):
    admin_id = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
      admin_id = data.get('admin_id')
      old_password = data.get('old_password')
      
      try:
        admin = Admin.objects.get(admin_id=admin_id)
        
      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Admin username does not exist.")

      if not admin.checkPassword(old_password):
          raise AuthenticationFailed("Invalid old password.")
          
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