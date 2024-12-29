from django.contrib.auth.models import User
from .models import *
from rest_framework.serializers import ModelSerializer, Serializer


class UserSerializer(ModelSerializer): 
    class Meta:  
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
class CustomerSerializer(ModelSerializer): 
    user = UserSerializer()
    class Meta: 
        model = customer
        fields = ('user', 'name', 'phoneNumber', 'address', 'created_at')
        
    def create(self, validated_data):
        userData = validated_data.pop('user')
        
        # Debugging 
        print(userData)
        
        # creating user object first for one to one relation
        userObject = User.objects.create_user(**userData)
        
        # making customer object
        CustomerObject = customer.objects.create(user = userObject, **validated_data) 
        
        return CustomerObject
        
class foodSerializer(ModelSerializer): 
    class Meta: 
        model = food
        fields = '__all__'
