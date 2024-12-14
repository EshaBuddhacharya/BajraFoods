from django.db import models

# Create your models here.
class book(models.Model): 
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    stockQuantity = models.IntegerField()
    
    @property
    def availability(self): 
        return self.stockQuantity > 0
    
    def __str__(self): 
        return self.name
    
    
    
class member(models.Model): 
    name = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    
        
    def __str__(self): 
        return self.name
    
class BorrowBook(models.Model): 
    member = models.ForeignKey(member, on_delete=models.CASCADE)
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    returnStatus = models.BooleanField(default = False)
    
    class Meta: 
        unique_together = ('member', 'book')
    