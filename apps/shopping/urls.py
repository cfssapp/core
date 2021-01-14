from django.urls import path
from . import views

urlpatterns = [
	path('item/', views.ItemList.as_view(), name='listitem'),
	path('item/<int:pk>/', views.ItemDetail.as_view(), name='detailitem'),
    path('item/create/', views.CreateItem.as_view(), name='itemcreate'),
    path('item/edit/<int:pk>/', views.EditItem.as_view(), name='itemedit'),
    path('item/delete/<int:pk>/', views.DeleteItem.as_view(), name='itemdelete'),

	path('cart/', views.CartList.as_view(), name='listcart'),
	path('add-to-cart/', views.AddToCartView.as_view(), name='addtocart'),
    path('remove-from-cart/', views.RemoveFromCartView.as_view(), name='removefromcart'),

	path('order/', views.OrderList.as_view(), name='listorder'),
	path('add-to-order/', views.AddToOrderView.as_view(), name='addtoorder'),
	path('order/delete/<int:pk>/', views.DeleteItem.as_view(), name='orderdelete'),
]