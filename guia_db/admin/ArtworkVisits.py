from django.contrib import admin
from ..models.ArtworkVisits import ArtworkVisits

class ArtworkVisitsAdmin(admin.ModelAdmin):
  list_display = ('visit_id', 'visitor_id', 'get_art_title', 'art_visited_on', 'visit_type')
  search_fields = ('visit_id', 'visitor_id', 'art_id__art_title', 'art_visited_on', 'visit_type')
  ordering = ('visit_id',)

  def get_art_title(self, obj):
    return obj.art_id.title
  get_art_title.short_description = "Art Visited"

admin.site.register(ArtworkVisits, ArtworkVisitsAdmin)