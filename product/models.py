
from django.db import models
from django.urls import reverse

from order.models import Cart

# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank= True)
    price = models.FloatField(null=False, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null= False, blank=True)
    image = models.ImageField(upload_to="books",null=True, blank=True)
    def __str__(self):
        return str(self.id)
    
class OrderedBook(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=1, null= True, blank=True)
    totalPrice = models.FloatField( blank=True, default=0)
    book =models.ForeignKey(Book,null=True,  on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,null=True,  on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    def get_total_price(self):
        return self.quantity * self.book.price
    
    def get_total_discount_price(self):
        return (self.quantity * self.book.price) * self.book.discount / 100

    def get_amount_saved(self):
        return self.get_total_price() - self.get_total_discount_price()
    
    def get_final_price(self):
        if self.book.discount:
            return self.get_total_discount_price()
        return self.get_total_price()