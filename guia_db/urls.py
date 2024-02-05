from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
  path('api/museum/get/all', views.getAllMuseums),
]