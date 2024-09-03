from django.db import models
from django.contrib.auth.models import User


class UserInfo(User):
    deliveryAddress = models.CharField(max_length= 255, null = True, blank = True )
    profilePic = models.FileField()

class Catageory(models.Model):
    name = models.CharField(max_length= 255, null = True, blank = True )
    image = models.CharField(max_length= 255, null = True, blank = True )
    class Meta:
        verbose_name_plural = "Catageory"

class Products(models.Model):
    title = models.CharField(max_length= 255, null = True, blank = True )
    description = models.CharField(max_length= 255, null = True, blank = True )
    image = models.CharField(max_length= 255, null = True, blank = True )
    price = models.IntegerField(null = True, blank = True)
    stock = models.IntegerField(null = True, blank = True)
    catageory = models.ForeignKey(Catageory,on_delete = models.CASCADE)
    review = models.IntegerField(null = True, blank = True)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    products = models.ForeignKey(Products, on_delete = models.CASCADE, null = True, blank = True)
    total = models.IntegerField(null = True, blank = True)
    status = models.CharField(max_length= 255, null = True, blank = True )
    payment = models.CharField(max_length= 255, null = True, blank = True )

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    products = models.ForeignKey(Products, on_delete = models.CASCADE, null = True, blank = True)
    total = models.IntegerField(null = True, blank = True)