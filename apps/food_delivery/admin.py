from django.contrib import admin
from .models import FoodItem, FoodOrder, FoodAvatar

# Register your models here.
admin.site.register(FoodAvatar)
admin.site.register(FoodItem)
admin.site.register(FoodOrder)