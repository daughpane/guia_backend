from django.db import models
from django.contrib import admin
import uuid

from .Museum import Museum

# Define the attributes and methods of the Visitor model
class Visitor(models.Model):
    # unique id for each visitors
    # visitor_id is a primary key that is auto-incrementing
    visitor_id = models.BigAutoField(primary_key=True)
    # visitor_token is a text field that will store a generated token where token is not editable 
    visitor_token = models.TextField(editable=False)
    # automatically setting the datetime when visitor object is created
    visited_on = models.DateTimeField(auto_now_add=True)
    # museum which the visitor visited
    museum_id = models.ForeignKey(
        Museum,
        on_delete = models.CASCADE,
        verbose_name = 'museum_id',
        default=1
    )

    # Override the save method
    def save(self, *args, **kwargs):
        # if visitor_token is not set, generate a unique token before saving
        if not self.visitor_token:
            self.visitor_token = str(uuid.uuid4())
        # call the save method of the superclass
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.visitor_id)