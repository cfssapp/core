from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    path('certificate/', views.CertificateList.as_view(), name='listcertificate'),
    path('certificate/<int:pk>/', views.CertificateDetail.as_view(), name='detailcertificate'),

    path('comment-to-certificate/', views.CommentToCertificateView.as_view(), name='commentaddtocertificate'),

    path('comment/image/', views.CreateCommentImage.as_view(), name='foodavatarcreate'),
]