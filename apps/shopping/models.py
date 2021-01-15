import uuid
from django.db import models
from django.conf import settings


# Create your models here.
class Item(models.Model):
    tracking_no = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    item_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owneritem', default=1)
    ordered = models.BooleanField(default=False)
    cartadded = models.BooleanField(default=False)
    # order_id = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.tracking_no


class Order(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order', default=1)
    items = models.ManyToManyField(Item)
    shipping_address = models.CharField(max_length=100, default="not set")
    courier = models.CharField(max_length=100, default="not set")
    
    def __str__(self):
        return str(self.unique_id)
        

