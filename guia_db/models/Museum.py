from django.db import models

# Define the attributes and methods of the Museum model
class Museum(models.Model):
    # museum_id is a primary key that is auto incrementing
    museum_id = models.BigAutoField(primary_key=True)
    # museum_name is a text field that will store the name of the museum
    museum_name = models.TextField()