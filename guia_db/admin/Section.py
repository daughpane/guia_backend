from django.contrib import admin
from ..models.Section import Section

class SectionAdmin(admin.ModelAdmin):
  list_display = ('section_id', 'section_name', 'get_museum_name')
  search_fields = ('section_id', 'section_name', 'museum_id__museum_name')
  ordering = ('section_id',)

  def get_museum_name(self, obj):
    return obj.museum_id.museum_name
  get_museum_name.short_description = "Museum Name"  

admin.site.register(Section, SectionAdmin)