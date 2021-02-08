from django.urls import path
from . import views

urlpatterns = [
    path('fake-data-01/', views.fake_data_01, name="datafake01"),

    path('topic/', views.TopicList.as_view(), name='listtopic'),
    path('topic/<int:pk>/', views.FoodItemDetail.as_view(), name='detailtopic'),
    path('topic/create/', views.CreateFoodItem.as_view(), name='topiccreate'),

]