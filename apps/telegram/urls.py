from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    path('sn/', views.TelegramSNList.as_view(), name='listsn01'),


]