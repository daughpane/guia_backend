from django.db import models
from .Museum import Museum

# Define the attributes and methods of the Section model
class Section(models.Model):
    # unique id for each section of the museum
    # admin_id is a primary key that is auto-incrementing
    section_id = models.BigAutoField(primary_key=True)
    # this is the name of the museum section
    section_name = models.TextField()
    # museum_id is a foreign key from the Museum model 
    # If the referenced museum is deleted, also delete the Admin objects that have references to it
    museum_id = models.ForeignKey(
        Museum,
        on_delete = models.CASCADE,
        verbose_name = 'museum_id'
    )