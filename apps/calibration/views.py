from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import CertificateSerializer, CommentSerializer
from .models import Certificate, Comment

from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from rest_framework import filters

api_urls = {
    "data": [
        {
            "id": "xxx1",
            "title": "Alipay",
            "logo": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
            "description": "那是一种内在的东西，他们到达不了，也无法触及的",
            "updatedAt": "2021-08-20T11:32:01.107Z",
            "member": "科学搬砖组",
            "href": "",
            "memberLink": ""
        },
        {
            "id": "xxx2",
            "title": "Angular",
            "logo": "https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png",
            "description": "希望是一个好东西，也许是最好的，好东西是不会消亡的",
            "updatedAt": "2017-07-24T00:00:00.000Z",
            "member": "全组都是吴彦祖",
            "href": "",
            "memberLink": ""
        }
    ]
}

# BK Testing
# @api_view(['GET'])
# def apiOverview(request):
	
# 	return Response(api_urls)


class CertificateList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['=forum']

    def get_queryset(self):
        # return Certificate.objects.filter(user=self.request.user).order_by('-id')
        return Certificate.objects.filter().order_by('-id')


class CertificateDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CommentToCertificateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()

    def post(self, request, *args, **kwargs):
        topic_id = request.data.get('id')
        post_content = request.data.get('content')
        

        new_post = Comment.objects.create(
            user=self.request.user,
            content=post_content,
            cert_id=topic_id
        )

        order_qs = Certificate.objects.filter(id=topic_id).order_by('-id').first()

        order_qs.posts.add(new_post)

        articles = Certificate.objects.get(id=topic_id)
        serializer = CertificateSerializer(articles)
        return JsonResponse(serializer.data, safe=False)