from django.urls import path
from . import views

urlpatterns = [
    path("getFood/", views.getFood, name = 'getFood')
]