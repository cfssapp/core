from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    path('cart/', views.CartList.as_view(), name='listcart'),
    path('cart/<int:pk>/', views.CartDetail.as_view(), name='detailcertificate'),

    path('cart/json/', views.jsonView, name='json-view'),
]