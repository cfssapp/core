from django.urls import path
from . import views

urlpatterns = [
    path('fake-data-01/', views.fake_data_01, name="datafake01"),
]