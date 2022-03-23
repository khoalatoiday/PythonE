from django.db import models;
from product import models as Model

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=200,null=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    book = models.ForeignKey(Model.Book, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class Paying(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    type = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
