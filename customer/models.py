from ast import Add, Or
from operator import mod
from pyexpat import model
from django.db import models;
from product import models as Model
from django.contrib.auth.models import User as User
# Create your models here.

class FullName(models.Model):
    id= models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=200,null=True, blank = True)
    middleName = models.CharField(max_length=200, null=True,  blank = True)
    lastName = models.CharField(max_length=200, null=True,  blank = True)
    
    def __str__(self):
        return str(self.id)

class Address(models.Model):
    id= models.AutoField(primary_key=True)
    city = models.CharField(max_length=200,null=True, blank = True)
    street = models.CharField(max_length=200, null=True,  blank = True)
    district = models.CharField(max_length=200, null=True,  blank = True)

    def __str__(self):
        return str(self.id)



class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fullName = models.ForeignKey(FullName, null=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100, null=True, blank=True)
    phoneNumber = models.CharField(max_length=11,null=True, blank=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar",null=True)
    
    def __str__(self):
        return str(self.id)


        
    


