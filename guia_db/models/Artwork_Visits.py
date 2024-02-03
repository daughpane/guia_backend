from django.db import models
from .Visitor import Visitor
from .Artwork import Artwork
from django.utils.translation import gettext_lazy as _

# This class defines the choices for a visitor can make to an artwork
# A visit can either be a scan or manual
class VisitType(models.TextChoices):
        SCAN = 'scan', _('Scan')
        MANUAL = 'manual', _('Manual')

# Define the attributes and methods of the Artwork_Visits model
class Artwork_Visits(models.Model):
    # visit_id is a primary key that is auto incrementing
    visit_id = models.BigAutoField(primary_key=True)
    # visitor_id is a foreign key from the Visitor model
    # If the referenced visitor is deleted, also delete the Artwork_Visits objects that have references to it
    visitor_id = models.ForeignKey(
        Visitor,
        on_delete = models.CASCADE,
        verbose_name = 'visitor_id'
    )
    # art_id is a foreign key from the Artwork model
    # If the referenced artwork is deleted, also delete the Artwork_Visits objects that have references to it
    art_id = models.ForeignKey(
        Artwork,
        on_delete = models.CASCADE,
        verbose_name = 'art_id'
    )
    # automatically setting the datetime when artwork visits object is created
    art_visited_on = models.DateTimeField(auto_now_add=True)
    # using the VisitType class to define the enumerated visit types
    # visit can either be scan or manual, with manual as its default value
    visit_type = models.CharField(
        max_length=6,
        choices=VisitType.choices,
        default=VisitType.MANUAL,
    )

    class Meta:
        verbose_name_plural = "Artwork Visits"