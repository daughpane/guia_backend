from django.urls import path
from . import views
from django.conf import settings
from rest_framework import routers



router = routers.DefaultRouter()

urlpatterns = router.urls


urlpatterns += [
  ###### MUSEUM PATHS 
  path('museum/get', views.MuseumApiView.as_view()),

  ###### SECTION PATHS
  path('section/get', views.SectionApiView.as_view()),

  ###### ADMIN
  path('admin/login', views.AdminLoginApiView.as_view()),
  path('admin/change-password', views.ChangePasswordApiView.as_view()),
  path('admin/logout', views.AdminLogoutApiView.as_view()),

  ###### ARTWORK
  path('artwork/create', views.ArtworkCreateView.as_view()),
  path('artwork/edit', views.ArtworkEditView.as_view()),
  path('artwork/delete', views.ArtworkDeleteView.as_view()),
  path('artwork/get', views.ArtworkView.as_view()),
  path('artwork/get/all', views.ArtworkListView.as_view()),

  ##### ARTWORK IMAGES
  path('artwork-images/get/all', views.ArtworkImageGetView.as_view()),

  ###### VISITOR
  path('visitor/generate-token', views.LogVisitorApiView.as_view()),

  ###### AMAZON
  path('amazon/get-credentials', views.S3CredentialsAPIView.as_view()),

  ##### DASHBOARD
  path('dashboard/get', views.DashboardStatsView.as_view()),

]
