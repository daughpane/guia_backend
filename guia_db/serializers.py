from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from django.core.exceptions import ObjectDoesNotExist

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
    print("herfe")
    data['admin'] = admin
    print("heheh")
    return data

        
    


  

class MuseumSerializer(serializers.ModelSerializer):
  class Meta:
    model=Museum
    fields=('museum_id','museum_name')

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = '__all__'