from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from . import views

urlpatterns = [
    path("getFood/", views.getFood, name = 'getFood'),
    path("token/", TokenObtainPairView.as_view(), name='token'),
    path("token/refresh/", TokenRefreshView.as_view(), name='refresh'),
    
]