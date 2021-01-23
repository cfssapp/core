import uuid
from django.db import models
from django.conf import settings


# Create your models here.
class FoodAvatar(models.Model):
    imagefile = models.ImageField(default='default.jpg', upload_to='upload_pics')

    def __str__(self):
        return str(self.id)
        # return str(self.file)
        # return f"https://antapi.pythonanywhere.com/media/{str(self.file)}"


class FoodItem(models.Model):
    # avatar = models.ForeignKey('FoodAvatar', on_delete=models.CASCADE, blank=True, null=True)
    avatar = models.OneToOneField(FoodAvatar, on_delete=models.CASCADE, blank=True, null=True)
    # avatar = models.CharField(max_length=100, default="not set")
    name = models.CharField(max_length=100, default="not set")
    price = models.CharField(max_length=100, default="not set")
    category = models.CharField(max_length=100, default="not set")
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
        

class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='addressorder', default=1)
    street_name = models.CharField(max_length=100, default="not set")
    state = models.CharField(max_length=100, default="not set")                          
    postal_code = models.CharField(max_length=100, default="not set")
    default = models.BooleanField(default=True)

    def __str__(self):
        return self.user.user_name