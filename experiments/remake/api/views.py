from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import CustomerSerializer, foodSerializer
from .models import food

# Create your views here.
@api_view(['POST'])
def RegisterCustomer(request): 
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Customer Registered Successfully'}, status = status.HTTP_200_OK)
    return Response({'errors':  serializer.errors}, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getFoods(request): 
    foods = food.objects.all()
    serializer = foodSerializer(foods, many = True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def placeOrder(request): 
    return Response({'message': 'orderPlaces successfully'})