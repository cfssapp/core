from django.contrib import admin
from .models import FoodItem, FoodOrder, FoodAvatar, Address, Csv
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class FoodItemAdmin(ImportExportModelAdmin):
    resource_class = FoodItem

admin.site.register(FoodAvatar)
admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(FoodOrder)
admin.site.register(Address)
admin.site.register(Csv)
