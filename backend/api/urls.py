from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('registerCustomer/', RegisterCustomer, name = 'registerCustomer'),
    path('getFoods/', getFoods, name='getFoods'),
    path('placeOrder/', placeOrder, name = 'placeOrder'),
    path('getOrders/', getOrders, name = 'getOrders'),
]