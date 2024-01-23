from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class CostumUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length = 40)
    first_name = models.CharField(max_length = 40 )
    last_name = models.CharField(max_length = 40 )
    password = models.CharField(max_length = 250 )
    password2 = models.CharField(max_length = 250 )
    pass


class Category(models.Model):
     Title = models.CharField(max_length=100)


class Product(models.Model):
      Title = models.CharField(max_length=100)
      description = models.CharField(max_length=255)
      price = models.DecimalField(max_digits=10, decimal_places=2)
      category = models.ForeignKey(Category,on_delete = models.CASCADE)

class ProductImages(models.Model):
     image = models.ImageField(upload_to="files/")
     product = models.ForeignKey(Product, related_name='image',on_delete=models.CASCADE)