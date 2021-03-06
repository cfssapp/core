from django.urls import path
from . import views

urlpatterns = [
	path('item/', views.FoodItemList.as_view(), name='listfooditem'),
	path('item/<int:pk>/', views.FoodItemDetail.as_view(), name='detailfooditem'),
    path('item/create/', views.CreateFoodItem.as_view(), name='fooditemcreate'),
    path('item/edit/<int:pk>/', views.EditFoodItem.as_view(), name='fooditemedit'),
    path('item/delete/<int:pk>/', views.DeleteFoodItem.as_view(), name='fooditemdelete'),
    path('item/avatar/', views.CreateFoodAvatar.as_view(), name='foodavatarcreate'),

    path('csv/', views.UploadFileView.as_view(), name='fileupload'),

    path('cart/', views.FoodCartList.as_view(), name='listfoodcart'),
    path('add-to-cart/', views.AddToCartView.as_view(), name='foodaddtocart'),
    path('remove-from-cart/', views.RemoveFromCartView.as_view(), name='foodremovefromcart'),
    
    path('address/', views.AddressList.as_view(), name='listaddress'),
    path('address/create/', views.CreateAddress.as_view(), name='addresscreate'),
    path('address/edit/<int:pk>/', views.EditAddress.as_view(), name='addressedit'),

    path('order/', views.FoodOrderList.as_view(), name='listfoodorder'),
	path('add-to-order/', views.AddToOrderView.as_view(), name='foodaddtoorder'),
    path('order/delete/<int:pk>/', views.DeleteOrderView.as_view(), name='foodorderdelete'),

    # path('fake-data/', views.fake_data, name="notices_list"),
    path('fake-data3/', views.fake_data3, name="datafake3"),
    path('fake-data/', views.fake_data.as_view(), name="datafake"),
    path('fake-data/<int:pk>/', views.FakeDataDetail.as_view(), name='detaildatafake'),
]