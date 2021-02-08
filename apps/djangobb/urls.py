from django.urls import path
from . import views

urlpatterns = [
    path('fake-data-01/', views.fake_data_01, name="datafake01"),

    # path('topic/', views.show_topic, name='topicshow),
    # url('^topic/(?P<topic_id>\d+)/$', forum_views.show_topic, name='topic'),

    path('topic/', views.TopicList.as_view(), name='listfooditem'),
]