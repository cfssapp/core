from django.contrib import admin
from .models import FoodItem, FoodOrder, FoodAvatar, Address, Csv, SalesData, FakeData2

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class FoodItemResource(resources.ModelResource):

    class Meta:
        model = FoodItem


class FoodItemAdmin(ImportExportModelAdmin):
    resource_class = FoodItemResource


class SalesDataResource(resources.ModelResource):

    class Meta:
        model = SalesData


class SalesDataAdmin(ImportExportModelAdmin):
    resource_class = SalesDataResource

admin.site.register(FoodAvatar)
admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(FoodOrder)
admin.site.register(Address)
admin.site.register(Csv)

admin.site.register(SalesData, SalesDataAdmin)
admin.site.register(FakeData2)