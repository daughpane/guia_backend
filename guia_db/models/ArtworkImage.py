from django.db import models
from django.core.exceptions import ValidationError
from ..models import Artwork

class ArtworkImage(models.Model):
    artwork = models.ForeignKey(
        Artwork, 
        related_name='images', 
        on_delete=models.CASCADE)
    
    def get_upload_to(instance, filename):
        return 'art{}/{}'.format(instance.artwork.art_id, filename)
    
    image = models.ImageField(upload_to=get_upload_to)

    # def clean(self):
    #     # Ensure that curators upload exactly 10 images for each artwork
    #     if self.artwork.images.count() != 10:
    #         raise ValidationError("Please add exactly 10 images for this artwork.")
        
    class Meta:
        verbose_name_plural = "Artwork Images"
