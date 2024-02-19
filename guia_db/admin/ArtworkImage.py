from django.contrib import admin
from ..models import Artwork
from ..models.ArtworkImage import ArtworkImage

class ArtworkImageAdmin(admin.ModelAdmin):
    list_display = ('get_art_id', 'image', 'is_thumbnail')
    search_fields = ('artwork__artwork_title', 'image')
    ordering = ('artwork__art_id',)

    def get_art_id(self, obj):
        return obj.artwork.art_id
    get_art_id.short_description = 'Art ID'

admin.site.register(ArtworkImage, ArtworkImageAdmin)