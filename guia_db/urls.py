from django.urls import path
from . import views
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
  path('api/museum/get/all', views.getAllMuseums),
  path('api/admin/login', views.AdminLoginApiView.as_view()),
]