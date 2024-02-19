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

    is_thumbnail = models.BooleanField(default=False)        
    class Meta:
        verbose_name_plural = "Artwork Images"
