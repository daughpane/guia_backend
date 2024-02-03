from django.db import models
from .Section import Section
from .Admin import Admin

# Define the attributes and methods of the Artwork model
class Artwork(models.Model):
    # unique id for each artwork
    #art_id is a primary key that is auto incrementing
    art_id = models.BigAutoField(primary_key=True)
    # section_id is a foreign key from the Section model
    # If the referenced section is deleted, also delete the Artwork objects that have references to it
    section_id = models.ForeignKey(
        Section,
        on_delete = models.CASCADE,
        related_name = 'section_artworks',
        verbose_name = 'section_id'
    )
    # location is a foreign key from the Section model
    # this will specify which section the artwork is located
    # when the referenced Section is deleted, set location to NULL
    # allows NULL values if the location of the artwork is not yet finalized
    location = models.ForeignKey(
        Section,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'located_artworks',
        verbose_name = 'location'
    )
    # title of the artwork will be stored here as text
    title = models.TextField()
    # medium of the artwork being used is specified here 
    medium = models.TextField()
    # assign date and time when the artwork was published
    date_published = models.DateTimeField()
    # storing here the different dimensions of the artwork
    dimen_width_cm = models.DecimalField(max_digits=100, decimal_places=2)
    dimen_length_cm = models.DecimalField(max_digits=100, decimal_places=2)
    dimen_height_cm = models.DecimalField(max_digits=100, decimal_places=2)
    # this will store the description of the artwork
    description = models.TextField()
    # this is for additional information about the artwork
    additional_info = models.TextField()
    # images of the artwork will be stored here as a list from the cloud storage
    images = models.JSONField(default=list)
    # automatically set the field to the current date and time when the Artwork object is created
    added_on = models.DateTimeField(auto_now_add=True)
    # admin_id is a foreign key from the Admin model
    # when the referenced Admin is deleted, set added_by to NULL
    added_by = models.ForeignKey(
        Admin, 
        on_delete = models.SET_NULL, 
        null = True,
        verbose_name = 'added by'
    )
    # automatically update the field to the current date and time whenever the Artwork object is saved
    updated_on = models.DateTimeField(auto_now=True)
    # admin_id is a foreign key from the Admin model
    # when the referenced Admin is deleted, set updated_by to NULL
    # allows NULL values if no one has updated the artwork yet
    # related_name is used to avoid conflicts with the reverse relation
    updated_by = models.ForeignKey(
        Admin,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updated_artworks',
        verbose_name='updated by'
    )
    # is_deleted is a boolean field that indicates whether the artwork is deleted or not
    # but artwork is not deleted from the database, but is only marked as deleted
    # this is useful so we can still keep track of the artwork
    is_deleted = models.BooleanField(default=False)