from django.shortcuts import render
from .models import food
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import getFoodSerializer

@api_view(['GET'])
def getFood(request): 
    # getting all foods data from db 
    foods = food.objects.all()
    
    # Turning python objects into json format 
    serializer = getFoodSerializer(foods, many = True)
    
    # returning data
    return Response(serializer.data)