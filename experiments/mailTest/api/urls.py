from django.urls import path
from .views import *

urlpatterns = [
    path('sendMail/', sendMail, name = "sendMail")
]
