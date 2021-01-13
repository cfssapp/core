from django.urls import path
from . import views

urlpatterns = [
	path('item/', views.ItemList.as_view(), name='listitem'),
]