from django.contrib import admin
from ..models.Admin import Admin

class AdminAdmin(admin.ModelAdmin):
  # Notice that there is `get_museum_name` is not an attribute of admin, but is a function we created below.
  # We will use a function so we can access the name of the museum_id that is a foreign key in our model.
  list_display = ('admin_id', 'admin_username', 'get_museum_name')

  # Similarly, since museum_id is just a foreign key, we need to something first so we can search on the name of the museum.
  # To do this, append `__[attribute name]` to the foreign_key attribute name. (In case you are confused, it is a double underscore.)
  search_fields =  ('admin_id', 'admin_username', 'museum_id__museum_name')
  ordering = ('admin_id',)

  def get_museum_name(self, obj):
    return obj.museum_id.museum_name
  get_museum_name.short_description = "Museum Name"  

admin.site.register(Admin, AdminAdmin)
