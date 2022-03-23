from email.policy import default
from statistics import mode
from django.db import models

# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=255, null= False)
    image = models.ImageField(upload_to="images",null=False, default=None)

    def __str__(self):
        return f"{self.id}, {self.name}, {self.price}, {self.description} "

