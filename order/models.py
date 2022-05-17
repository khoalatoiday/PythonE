
from time import time
from django.db import models
from pytz import timezone
from customer import models as CustomerModel
# Create your models here.
class Cart(models.Model):
  id= models.AutoField(primary_key=True)
  totalPrice = models.FloatField(default=0)
  customer = models.ForeignKey(CustomerModel.Customer, null=True,blank=True, on_delete=models.CASCADE)
  status = models.BooleanField(default=False)
  def __str__(self):
        return str(self.id)

class Shipment(models.Model):
  id = models.AutoField(primary_key=True)
  type = models.CharField(max_length=50, null=True, blank=True)
  extra_price = models.FloatField()
  def __str__(self):
        return str(self.id)

class Payment(models.Model):
  id= models.AutoField(primary_key=True)
  type = models.CharField(max_length=50, null=True, blank=True)
  extra_price = models.FloatField(null=True)

  def __str__(self):
        return str(self.id)

class Order(models.Model):
  id = models.AutoField(primary_key=True)
  orderDate = models.DateTimeField(auto_now_add=True)
  totalPrice = models.FloatField(null=True)
  status = models.BooleanField(default=False, null= False, blank=False)
  discount = models.IntegerField(default=0, null=True, blank=True)
  customer = models.ForeignKey(CustomerModel.Customer, null=True,blank=True, on_delete=models.CASCADE)
  cart = models.OneToOneField(Cart,null=True, on_delete=models.CASCADE)
  shipment = models.ForeignKey(Shipment, null =True, on_delete=models.CASCADE)
  payment = models.ForeignKey(Payment, null=True,on_delete=models.CASCADE)
  address = models.CharField(max_length=200,null=True)

  def __str__(self):
        return str(self.id)