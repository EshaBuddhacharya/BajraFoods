from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class customer(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phoneNumber = models.IntegerField()
    address = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
class food(models.Model): 
    name = models.CharField(max_length=30, unique=True)
    price = models.PositiveIntegerField()
    discription = models.CharField(max_length=500, blank=True, null=True)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='foodImg/')
    
    def __str__(self): 
        return self.name
    
class order(models.Model): 
    ORDER_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('PREPARING', 'Preparing'),
        ('READY', 'Ready for Pickup/Delivery'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    discription = models.CharField(max_length=500, blank=True, null=True)
    orderStatus = models.CharField(choices=ORDER_STATUS_CHOICES, default = 'PENDING', max_length=30)
    orderDate = models.DateTimeField(auto_now_add=True)
    
    @property
    def total(self): 
        return sum(order_food.price for order_food in self.order_foods.all())
    
    def __str__(self): 
        return self.customer.name
    
class orderFood(models.Model): 
    order = models.ForeignKey(order, on_delete=models.CASCADE, related_name='order_foods')
    food = models.ForeignKey(food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(1000)
        ]
    )
    
    @property
    def price(self): 
        return (self.food.price * self.quantity)
    
    def __str__(self): 
        return self.order.customer.name
    