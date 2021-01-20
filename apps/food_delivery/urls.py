from django.urls import path
from . import views

urlpatterns = [
	path('item/', views.FoodItemList.as_view(), name='listfooditem'),
	path('item/<int:pk>/', views.FoodItemDetail.as_view(), name='detailfooditem'),
    path('item/create/', views.CreateFoodItem.as_view(), name='fooditemcreate'),
    path('item/edit/<int:pk>/', views.EditFoodItem.as_view(), name='fooditemedit'),
    path('item/delete/<int:pk>/', views.DeleteFoodItem.as_view(), name='fooditemdelete'),
]