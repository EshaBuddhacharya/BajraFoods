from django.contrib import admin
from .models import * 

# Register your models here.
@admin.register(Parent)
class ParentModelAdmin(admin.ModelAdmin): 
    list_display = ('name',)
    
    
@admin.register(Child)
class ParentModelAdmin(admin.ModelAdmin): 
    list_display = ('name', 'parent')