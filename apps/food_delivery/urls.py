from django.urls import path
from . import views

urlpatterns = [
	path('item/', views.FoodItemList.as_view(), name='listfooditem'),
	
]