from django.db import models

# Create your models here.
class Customer(models.Model): 
    name = models.CharField(("Name"), max_length=50)
    