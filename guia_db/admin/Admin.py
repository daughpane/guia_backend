from django.contrib import admin
from ..models.Admin import Admin

class AdminAdmin(admin.ModelAdmin):
  # Notice that there is `get_museum_name` is not an attribute of admin, but is a function we created below.
  # We will use a function so we can access the name of the museum_id that is a foreign key in our model.
  list_display = ('get_admin_id', 'get_username', 'get_museum_name')

  # Similarly, since museum_id is just a foreign key, we need to something first so we can search on the name of the museum.
  # To do this, append `__[attribute name]` to the foreign_key attribute name. (In case you are confused, it is a double underscore.)
  search_fields =  ('user__id', 'user__username', 'museum_id__museum_name')
  ordering = ('admin_id',)

  def get_museum_name(self, obj):
    return obj.museum_id.museum_name
  get_museum_name.short_description = "Museum Name"  

  def get_username(self, obj):
    return obj.user.username
  get_username.short_description = "Username"  

  def get_admin_id(self, obj):
    return obj.user.id
  get_admin_id.short_description = "Admin ID"  

admin.site.register(Admin, AdminAdmin)
