from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Drinks','Drinks'),
        ('Chinese','Chinese'),
        ('Indian','Indian'),
    )
    name = models.CharField(max_length=20,null=False,blank=False)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
