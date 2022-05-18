
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
    category = models.CharField(max_length=50,null=False,default="book")
    def __str__(self):
        return str(self.id)

class Laptop(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank= True)
    price = models.FloatField(null=False, blank=True)
    description = models.CharField(max_length=255, null= False, blank=True)
    image = models.ImageField(upload_to="laptop",null=True, blank=True)
    category = models.CharField(max_length=50,null=False,default="Laptop")
    def __str__(self):
        return str(self.id)

class Clothes(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank= True)
    price = models.FloatField(null=False, blank=True)
    description = models.CharField(max_length=255, null= False, blank=True)
    image = models.ImageField(upload_to="chothes",null=True, blank=True)
    category= models.CharField(max_length=50,null=False,default="clothes")
    def __str__(self):
        return str(self.id)

class OrderedBook(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=1, null= True, blank=True)
    totalPrice = models.FloatField( blank=True, default=0)
    book =models.ForeignKey(Book,null=True, default=None,  on_delete=models.CASCADE)
    Laptop =models.ForeignKey(Laptop,null=True,default=None,  on_delete=models.CASCADE)
    clothes =models.ForeignKey(Clothes,null=True,default=None,  on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,null=True,  on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    def get_total_price(self):
        if self.book:
            return self.quantity * self.book.price
        if self.Laptop:
            return self.quantity * self.Laptop.price
        if self.clothes:
            return self.quantity * self.clothes.price
    
    def get_total_discount_price(self):
        return (self.quantity * self.book.price) * self.book.discount / 100

    def get_amount_saved(self):
        return self.get_total_price() - self.get_total_discount_price()
    
    def get_final_price(self):
        if self.book.discount:
            return self.get_total_discount_price()
        return self.get_total_price()