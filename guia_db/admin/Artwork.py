from django.contrib import admin
from ..models.Artwork import Artwork

class ArtworkAdmin(admin.ModelAdmin):
  list_display = ('art_id', 'title', 'get_section_name', 'medium', 'date_published', 'added_on', 'get_added_by_name', 'updated_on', 'get_updated_by_name', 'is_deleted')
  search_fields = ('art_id', 'title', 'section_id__section_name', 'medium', 'date_published', 'added_by__admin_user', 'updated_on', 'is_deleted')
  ordering = ('art_id',)

  def get_section_name(self, obj):
    return obj.section_id.section_name
  get_section_name.short_description = "Section Name"

  def get_added_by_name(self, obj):
    if obj.added_by is None:
      return ""
    else:
      return obj.added_by.user.username
  get_added_by_name.short_description = "Added By"

  def get_updated_by_name(self, obj):
    if obj.updated_by is None:
      return ""
    else:
      return obj.updated_by.user.username
  get_updated_by_name.short_description = "Updated By"

admin.site.register(Artwork, ArtworkAdmin)
