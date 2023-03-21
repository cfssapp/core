from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview01"),

    path('sn/', views.TelegramSNList.as_view(), name='listsn01'),

    path('user/', views.TelegramUserList.as_view(), name='listuser01'),
    path('user/<slug:telegram_id>/', views.TelegramUserDetail.as_view(), name='detailtelegramuser01'),


]