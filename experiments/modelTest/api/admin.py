from django.contrib import admin
from .models import book, member, BorrowBook

# Register your models here.
@admin.register(book)
class booksModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'stockQuantity', 'availability')
    search_fields = ('name', 'author')
    
@admin.register(member)
class memberModelAdmin(admin.ModelAdmin): 
    list_display = ('name', 'address', 'phoneNumber', 'email')
    
@admin.register(BorrowBook)
class BorrowBookModelAdmin(admin.ModelAdmin): 
    list_display = ('member', 'book', 'borrow_date', 'returnStatus')
    list_editable = ('returnStatus',)
    list_filter = ('returnStatus',) 
    search_fields = ('member__name', 'book__name', 'borrow_date')