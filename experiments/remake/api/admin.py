from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import food, customer, order, orderFood

# Register your models here.
@admin.register(food)
class FoodModelAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price', 'discription', 'image', 'availability')
    search_fields = ('name',)
    list_filter = ('availability',)
    
@admin.register(customer)
class CustomerModelAdmin(admin.ModelAdmin): 
    list_display = ('user', 'name', 'phoneNumber', 'address')
    search_fields = ('name','email', 'phoneNumber')
    
@admin.register(order)
class OrderModelAdmin(admin.ModelAdmin): 
    list_display = ('customer', 'discription', 'orderStatus', 'total')
    search_fields = ('customer__name', 'customer__address')
    
@admin.register(orderFood)
class OrderFoodModelAdmin(admin.ModelAdmin): 
    list_display = ('order', 'food', 'quantity', 'price')
    search_fields = ('order__customer__name', 'food__name')