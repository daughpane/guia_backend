from django.contrib import admin
from ..models.ArtworkVisits import ArtworkVisits

class ArtworkVisitsAdmin(admin.ModelAdmin):
  list_display = ('visit_id', 'visitor_id', 'get_visitor_museum_name','get_art_title', 'get_art_museum_name', 'art_visited_on', 'visit_type')
  search_fields = ('visit_id', 'visitor_id', 'art_id__art_title', 'art_visited_on', 'visit_type')
  ordering = ('visit_id',)

  def get_art_title(self, obj):
    return obj.art_id.title
  get_art_title.short_description = "Art Visited"

  def get_visitor_museum_name(self, obj):
    return obj.visitor_id.museum_id.museum_name
  get_visitor_museum_name.short_description = "Visitor Museum"

  def get_art_museum_name(self, obj):
    return obj.art_id.section_id.museum_id.museum_name
  get_art_museum_name.short_description = "Artwork Museum"

admin.site.register(ArtworkVisits, ArtworkVisitsAdmin)