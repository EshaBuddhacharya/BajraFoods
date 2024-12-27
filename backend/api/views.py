from django.shortcuts import render
from .models import food
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import getFoodSerializer, CustomerSerializer

@api_view(['GET'])
def getFood(request): 
    # getting all foods data from db 
    foods = food.objects.all()
    
    # Turning python objects into json format 
    serializer = getFoodSerializer(foods, many = True)
    
    # returning data
    return Response(serializer.data)

@api_view(['POST'])
def registerCustomer(request): 
    serializer = CustomerSerializer(data=request.data)
    
    if serializer.is_valid(): 
        serializer.save()
        return Response({'message': 'Customer Registered Successfully'}, status=status.HTTP_201_CREATED)
    
    return Response({"message": "Failed to register Customer"}, status=status.HTTP_400_BAD_REQUEST)