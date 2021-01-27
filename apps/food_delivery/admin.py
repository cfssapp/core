from django.contrib import admin
from .models import FoodItem, FoodOrder, FoodAvatar, Address, Csv

# Register your models here.
admin.site.register(FoodAvatar)
admin.site.register(FoodItem)
admin.site.register(FoodOrder)
admin.site.register(Address)
admin.site.register(Csv)