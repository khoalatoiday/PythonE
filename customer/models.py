from operator import mod
from pyexpat import model
from django.db import models;
from product import models as Model
from django.contrib.auth.models import User as User
# Create your models here.

class FullName(models.Model):
    id= models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=200,null=True)
    middleName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)

class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fullName = models.OneToOneField(FullName, null=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100, null=True)
    phoneNumber = models.CharField(max_length=11,null=True)

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
