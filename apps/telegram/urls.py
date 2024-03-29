from django.urls import path
from . import views

urlpatterns = [

    # path('sn/', views.TelegramSNList.as_view(), name='listsn01'),
    path('sn/', views.PostToUserList.as_view(), name='listsn01'),
    path('sn/<slug:sn>/', views.TelegramSNDetail.as_view(), name='TelegramSNDetail01'),
    path('post-to-sn-detail/', views.PostToSNDetail.as_view(), name='posttouser01'),

    path('user/', views.TelegramUserList.as_view(), name='listuser01'),
    path('user/<slug:telegram_id>/', views.TelegramUserDetail.as_view(), name='detailtelegramuser01'),
    path('post-to-user/', views.PostToUser.as_view(), name='posttouser01'),


]