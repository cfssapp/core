from django.contrib import admin
from .models import FoodItem, FoodOrder

# Register your models here.
admin.site.register(FoodItem)
admin.site.register(FoodOrder)