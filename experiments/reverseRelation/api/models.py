from django.db import models

# Create your models here.
class Parent(models.Model): 
    name = models.CharField(max_length=30)
    
class Child(models.Model): 
    name = models.CharField(max_length=30)
    parent = models.ForeignKey(Parent, related_name='child', on_delete=models.CASCADE)