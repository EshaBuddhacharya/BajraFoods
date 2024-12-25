from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def placeOrder(request): 
    return Response({'message':"Order Placed Successfull"})


@api_view(['POST'])
def createCustomer(request): 
    serializer = CustomerSerializer(data = request.data)
    
    if serializer.is_valid(): 
        serializer.save()
        return Response({"message": "Data Saved Successfully"}, status = status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)