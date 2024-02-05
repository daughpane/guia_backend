from django.contrib import admin
from ..models.Visitor import Visitor

class VisitorAdmin(admin.ModelAdmin):
  list_display = ('visitor_id', 'visitor_token', 'visited_on')
  search_fields =  list_display
  ordering = ('-visited_on',)

admin.site.register(Visitor, VisitorAdmin)