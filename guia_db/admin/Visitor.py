from django.contrib import admin
from ..models.Visitor import Visitor

class VisitorAdmin(admin.ModelAdmin):
  list_display = ('visitor_id', 'get_museum_name', 'visitor_token', 'visited_on')
  search_fields =  list_display
  ordering = ('-visited_on',)

  def get_museum_name(self, obj):
    return obj.museum_id.museum_name
  get_museum_name.short_description = "Museum Name"

admin.site.register(Visitor, VisitorAdmin)