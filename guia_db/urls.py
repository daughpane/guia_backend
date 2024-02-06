from django.urls import path
from . import views
from django.conf import settings
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += [
  path('museum/get/all', views.getAllMuseums),
  path('admin/login', views.AdminLoginApiView.as_view()),
  path('admin/change-password', views.ChangePasswordApiView.as_view()),
]