from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.core.validators import RegexValidator
from .Museum import Museum
from django.contrib.auth.models import User
# Define the attributes and methods of the Admin model
class Admin(models.Model):
    # admin is a type of user.
    # user is django built-in model.
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # museum_id is a foreign key from the Museum model 
    # If the referenced museum is deleted, also delete the Admin objects that have references to it
    museum_id = models.ForeignKey(
        Museum, 
        on_delete=models.CASCADE, 
        verbose_name='museum id'
    )
