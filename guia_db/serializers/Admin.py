from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from ..models import Admin

class AdminSerializer(serializers.Serializer):
  admin_username = serializers.CharField(required=True)
  admin_password = serializers.CharField(required=True)
  
  def validate(self, data):
    username = data.get('admin_username')
    password = data.get('admin_password')

    try:
      # Authenticate user using username and password
      user = authenticate(username = username, password = password)
      admin = Admin.objects.get(user=user)
      
    except ObjectDoesNotExist:
      raise ObjectDoesNotExist("User does not exist.")
    
    data['admin'] = admin
    return data



class ChangePasswordSerializer(serializers.Serializer):
    admin_id = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    # Add django's password validator to check password requirements
    new_password = serializers.CharField(required=True, validators=[validate_password])

    def validate(self, data):
      admin_id = data.get('admin_id')
      old_password = data.get('old_password')
      new_password = data.get('new_password')

      try:
        # Since user is a foreignKey, to access its attributes, it needs double underscore
        admin = Admin.objects.get(user__id=admin_id)
        
      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("User does not exist.")

      if not admin.user.check_password(old_password):
        raise AuthenticationFailed("Invalid login credentials.")

      if old_password==new_password:
        raise ValidationError("Password has already been used.")
          
      data['admin'] = admin
      return data



class LogoutSerializer(serializers.Serializer):
    admin_id = serializers.CharField(required=True)
    
    def validate(self, data):
      admin_id = data.get('admin_id')

      try:
        admin = Admin.objects.get(user__id=admin_id)
      except ObjectDoesNotExist:
        raise ObjectDoesNotExist("User does not exist.")


      data['admin'] = admin
      return data
  

    