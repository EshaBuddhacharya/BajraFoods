from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(AbstractUser): 
    phoneNumber = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    
    def __str__(self): 
        return self.username