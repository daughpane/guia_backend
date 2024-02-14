from django.db import models
from django.core.exceptions import ValidationError
from ..models import Artwork

class ArtworkImage(models.Model):
    artwork = models.ForeignKey(
        Artwork, 
        related_name='images', 
        on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='artwork_images/'
    )

    def clean(self):
        # Ensure that curators upload exactly 10 images for each artwork
        if self.artwork.images.count() != 10:
            raise ValidationError("Please add exactly 10 images for this artwork.")
        
    class Meta:
        verbose_name_plural = "Artwork Images"