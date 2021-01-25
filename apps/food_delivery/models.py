from django.db import models
from django.conf import settings

from django.db.models.signals import pre_save
from .myclass import unique_order_no_generator

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
    order_id = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name


class FoodOrder(models.Model):
    order_id = models.CharField(max_length=100, default="not set")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orderfood', default=1)
    items = models.ManyToManyField(FoodItem)
    shipping_address = models.CharField(max_length=100, default="not set")
    courier = models.CharField(max_length=100, default="not set")
    
    def __str__(self):
        return str(self.order_id)

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    instance.order_id = unique_order_no_generator(instance)
        
pre_save.connect(pre_save_create_order_id, sender=FoodOrder)


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='addressorder', default=1)
    street_name = models.CharField(max_length=100, default="not set")
    state = models.CharField(max_length=100, default="not set")                          
    postal_code = models.CharField(max_length=100, default="not set")
    default = models.BooleanField(default=True)

    def __str__(self):
        return self.user.user_name