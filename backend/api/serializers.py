from .models import customer, food
from rest_framework import serializers
from django.contrib.auth.models import User

class getFoodSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = food
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ('id', 'username', 'email', 'password')
        read_only_fields = ('id',)
        write_only_fields = ('password',)
        
class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer for User model
    
    class Meta:
        model = customer
        fields = ('id', 'user', 'name', 'phoneNumber', 'address', 'created_at')
        read_only_fields = ('id', 'created_at')
    
    def create(self, validated_data):
        # Extract user data from the validated data
        user_data = validated_data.pop('user')
        
        # Create User instance first
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data.get('email', '')
        )
        
        # Create customer instance with the user
        customer_instance = customer.objects.create(
            user=user,
            **validated_data
        )
        
        return customer_instance
