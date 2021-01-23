from django.urls import path
from . import views

urlpatterns = [
	path('item/', views.FoodItemList.as_view(), name='listfooditem'),
	path('item/<int:pk>/', views.FoodItemDetail.as_view(), name='detailfooditem'),
    path('item/create/', views.CreateFoodItem.as_view(), name='fooditemcreate'),
    path('item/edit/<int:pk>/', views.EditFoodItem.as_view(), name='fooditemedit'),
    path('item/delete/<int:pk>/', views.DeleteFoodItem.as_view(), name='fooditemdelete'),
    path('item/avatar/', views.CreateFoodAvatar.as_view(), name='foodavatarcreate'),

    path('cart/', views.FoodCartList.as_view(), name='listfoodcart'),
    path('add-to-cart/', views.AddToCartView.as_view(), name='foodaddtocart'),
    path('remove-from-cart/', views.RemoveFromCartView.as_view(), name='foodremovefromcart'),
    path('address/', views.AddressList.as_view(), name='listaddress'),
]