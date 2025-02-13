from django.db import models
from django.core.exceptions import ValidationError
from ..models import Artwork

from ..utils import get_presigned_urls
class ArtworkImage(models.Model):
    artwork = models.ForeignKey(
        Artwork, 
        related_name='images', 
        on_delete=models.CASCADE)
    
    def get_upload_to(instance, filename):
        return 'art{}/{}'.format(instance.artwork.art_id, filename)
    
    image = models.ImageField(upload_to=get_upload_to, blank=True)

    image_link = models.TextField(blank=True)

    is_thumbnail = models.BooleanField(default=False)    

    is_deleted = models.BooleanField(default=False)      
    class Meta:
        verbose_name_plural = "Artwork Images"

    @property
    def _image_link(self):
        # Perform the calculation here
        return get_presigned_urls(self.image_link)
