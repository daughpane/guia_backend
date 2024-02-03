from django.contrib import admin
from .models.Admin import Admin
from .models.Museum import Museum
from .models.Visitor import Visitor
from .models.Section import Section
from .models.Artwork import Artwork

# This file is for registering your models to django-admin.
# It is important to register your models here so it will be visible in the django-admin

# For a more detailed documentation, you may checkout django's official documentation on django-admin: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/ 

# The default django-admin will just show the list of model objects created (example: Admin object(1), Admin object(2)), not showing its attributes. This is not helpful for us. So, we will modify the interface of the admin.

# To modify interface of django-admin, create a class implementing the admin.ModelAdmin as shown below.
class MuseumAdmin(admin.ModelAdmin):
  # add here the attributes of the model that you want to be seen in the interface. Depending on the model, you may not want all attributes to be seen, especially when there are too many attributes in a model
  list_display = ('museum_id', 'museum_name')  

  # Django-admin also supports search. Add here the attributes where you want to be searchable.
  search_fields = ('museum_id', 'museum_name')  

  # You can also modify the ordering. 
  # In this example, the museum_id will be the basis of ordering, which will be in the ascending order.
  # To make it descending, just add `-` before the attribute name.
  # There is comma after museum_id because it only accepts tupple, which should have atleast two. Adding comma is a way to bypass the tupple requirement although its only one attribute added.
  ordering = ('museum_id',)

# Register your model here. 
# Parameter 1: The Model you want to register
# Parameter 2 (Optional): The custom admin model.
admin.site.register(Museum, MuseumAdmin)



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

class VisitorAdmin(admin.ModelAdmin):
  list_display = ('visitor_id', 'visitor_token', 'visited_on')
  search_fields =  list_display
  ordering = ('-visited_on',)

admin.site.register(Visitor, VisitorAdmin)

class SectionAdmin(admin.ModelAdmin):
  list_display = ('section_id', 'section_name', 'get_museum_name')
  search_fields = ('section_id', 'section_name', 'museum_id__museum_name')
  ordering = ('section_id',)

  def get_museum_name(self, obj):
    return obj.museum_id.museum_name
  get_museum_name.short_description = "Museum Name"  

admin.site.register(Section, SectionAdmin)

class ArtworkAdmin(admin.ModelAdmin):
  list_display = ('art_id', 'title', 'get_section_name', 'medium', 'date_published', 'added_on', 'get_added_by_name', 'updated_on', 'get_updated_by_name', 'is_deleted')
  search_fields = ('art_id', 'title', 'section_id__section_name', 'medium', 'date_published', 'admin_id__admin_username', 'updated_on', 'is_deleted')
  ordering = ('art_id',)

  def get_section_name(self, obj):
    return obj.section_id.section_name
  get_section_name.short_description = "Section Name"

  def get_added_by_name(self, obj):
    return obj.added_by.admin_username
  get_added_by_name.short_description = "Added By"

  def get_updated_by_name(self, obj):
    return obj.updated_by.admin_username
  get_updated_by_name.short_description = "Updated By"

admin.site.register(Artwork, ArtworkAdmin)