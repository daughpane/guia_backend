from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.db import connection

class Museum(models.Model):
    # museum_id is a primary key that is auto incrementing
    museum_id = models.BigAutoField(primary_key=True)
    # museum_name is a text field that will store the name of the museum
    museum_name = models.TextField()


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
        # Check if the object is being saved for the first time (i.e., creating a new record)
        if not self.admin_id:
            # Query the database for the maximum admin_id
            max_admin_id = Admin.objects.aggregate(models.Max('admin_id'))['admin_id__max'] or 0
            # Set the new admin_id to be one greater than the current maximum
            self.admin_id = max_admin_id + 1
        # password is hashed before saving
        self.admin_password = make_password(self.admin_password)
        # call the save method of the superclass
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        # Store museum_id before deletion
        museum_id = self.museum_id_id
        max_admin_id = Admin.objects.aggregate(models.Max('admin_id'))['admin_id__max'] or 0
        # Call the delete method of the superclass
        super().delete(*args, **kwargs)
        
        # Reset the sequence manually
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT setval(pg_get_serial_sequence('guia_db_admin_admin_id_seq', 'id'), 1, false) WHERE id = {museum_id};")