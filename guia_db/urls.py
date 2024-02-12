from django.urls import path
from . import views
from django.conf import settings
from rest_framework import routers



router = routers.DefaultRouter()

urlpatterns = router.urls


urlpatterns += [
  ###### MUSEUM PATHS 
  path('museum/get', views.MuseumApiView.as_view()),

  ###### ADMIN
  path('admin/login', views.AdminLoginApiView.as_view()),
  path('admin/change-password', views.ChangePasswordApiView.as_view()),
  path('admin/logout', views.AdminLogoutApiView.as_view()),

  ###### ARTWORK
  path('artwork/create', views.ArtworkCreateView.as_view()),
  path('artwork/get/all', views.ArtworkListView.as_view()),

  ###### VISITOR
  path('visitor/generate-token', views.LogVisitorApiView.as_view()),

]