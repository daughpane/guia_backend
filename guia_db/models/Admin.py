from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from .Museum import Museum

# Define the attributes and methods of the Admin model
class Admin(models.Model):
    # admin_id is a primary key that is auto-incrementing
    admin_id = models.BigAutoField(primary_key=True)
    # admin_username is defined here where RegexValidator ensures that only accepted usernames will be used
    admin_username = models.TextField(validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_-]*$',
            message='Username can only letters, digits, hyphen, and underscore',
            code='invalid_username'
        )
    ])
    # admin_password is a char that store hashed passwords 
    admin_password = models.CharField()
    # museum_id is a foreign key from the Museum model 
    # If the referenced museum is deleted, also delete the Admin objects that have references to it
    museum_id = models.ForeignKey(
        Museum, 
        on_delete=models.CASCADE, 
        verbose_name='museum id'
    )

    # Override the save method
    def save(self, *args, **kwargs):
        # password is hashed before saving
        self.admin_password = make_password(self.admin_password)
        # call the save method of the superclass
        super().save(*args, **kwargs)