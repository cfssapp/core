import uuid
from django.db import models
from django.conf import settings


# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    cartadded = models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class FoodOrder(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orderfood', default=1)
    items = models.ManyToManyField(FoodItem)
    shipping_address = models.CharField(max_length=100, default="not set")
    courier = models.CharField(max_length=100, default="not set")
    
    def __str__(self):
        return str(self.courier)
        

