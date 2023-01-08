from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apiOverview, name="api-overview"),
    path('', views.CartViewset, name='json-view'),

    path('cart/', views.CartList.as_view(), name='listcart'),
    path('cart/<int:pk>/', views.CartDetail.as_view(), name='detailcertificate'),

    
]