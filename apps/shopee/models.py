from django.db import models
from django.conf import settings

from django.utils import timezone
from datetime import datetime

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=100, default="not set")
    product_name = models.CharField(max_length=255, default="not set")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    addcart_id = models.CharField(max_length=100, blank=True, null=True)

    # image = models.OneToOneField(CommentImage, on_delete=models.CASCADE, blank=True, null=True)



    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    cart_id = models.CharField(max_length=100, default="not set")
    customer = models.CharField(max_length=100, default="not set")

    list = models.ManyToManyField(Product, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.cart_id