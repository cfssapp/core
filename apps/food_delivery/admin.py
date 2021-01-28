from django.contrib import admin
from .models import FoodItem, FoodOrder, FoodAvatar, Address, Csv

from import_export import resources
from import_export.admin import ImportExportModelAdmin



class FoodItemResource(resources.ModelResource):

    class Meta:
        model = FoodItem
        ordering = ['-id']
    
    # def get_queryset(self):
    #     return self._meta.model.objects.order_by('-id') 


class FoodItemAdmin(ImportExportModelAdmin):
    resource_class = FoodItemResource

admin.site.register(FoodAvatar)
admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(FoodOrder)
admin.site.register(Address)
admin.site.register(Csv)
