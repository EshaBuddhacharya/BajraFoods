from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *
from .models import food, customer, orderFood, order

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
    def isValid(data):
        """
            fields required: 
                discription
                foods -> 
                    [[foodName, quantity], [foodName, quantity]]
                
        """
        # checking if fields exists in data 
        required_fields = ['discription', 'foods']
        is_fields_valid = set(required_fields).issubset(set(data.keys()))

        # checking if foods is in right format
        foods = data.get('foods', None)
        is_foods_valid = False
        if foods: 
            is_foods_valid = isinstance(foods, list) and all(isinstance(value, list) and len(value) == 2 for value in foods)

        # returning validity
        return is_fields_valid and is_foods_valid
    
    if isValid(request.data):
        Customer = customer.objects.get(user = request.user)
        
        # creating order object
        Order = order.objects.create(customer = Customer, discription = request.data.get('discription', None))
        
        # creating orderFood object for each foods
        for Food in request.data.get('foods', None): 
            food_name = Food[0]
            food_quantity = Food[1]
            try:
                food_object = food.objects.get(name=food_name)
                
            except food.DoesNotExist:
                return Response({'message': f'Food {food_name} not found'}, status=status.HTTP_404_NOT_FOUND)
            
            orderFood.objects.create(order = Order, food = food_object, quantity = food_quantity)
            
            
        return Response({'message': 'Order placed successfully'}, status = status.HTTP_200_OK)
    
    return Response({'message': 'request data format not in correct format'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrders(request): 
    # getting customer object from key request.user
    Customer = customer.objects.get(user = request.user)
    
    # getting orders of customer
    Order = order.objects.prefetch_related('order_foods').filter(customer = Customer)
    
    serializer = orderSerializer(Order, many = True)
    
    return Response(serializer.data, status = status.HTTP_200_OK)