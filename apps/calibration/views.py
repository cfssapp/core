from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import CertificateSerializer, CommentSerializer, CommentImageSerializer, ActivitySerializer
from .models import Certificate, Comment, CommentImage, Activity

from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from rest_framework import filters

from rest_framework.decorators import api_view

api_urls = {
    "data": [
        {
            "id": "trend-1",
            "updatedAt": "2021-08-20T11:49:35.376Z",
            "user": {
                "name": "曲丽丽",
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png"
            },
            "group": {
                "name": "高逼格设计天团",
                "link": "http://github.com/"
            },
            "project": {
                "name": "六月迭代",
                "link": "http://github.com/"
            },
            "template": "在 @{group} 新建项目 @{project}"
        },
        {
            "id": "trend-2",
            "updatedAt": "2021-08-20T11:49:35.376Z",
            "user": {
                "name": "付小小",
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/cnrhVkzwxjPwAaCfPbdc.png"
            },
            "group": {
                "name": "高逼格设计天团",
                "link": "http://github.com/"
            },
            "project": {
                "name": "六月迭代",
                "link": "http://github.com/"
            },
            "template": "在 @{group} 新建项目 @{project}"
        },
    ]
}


@api_view(['GET'])
def apiOverview(request):
	
	return Response(api_urls)


class CertificateList(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['=forum']

    def get_queryset(self):
        # return Certificate.objects.filter(user=self.request.user).order_by('-id')
        return Certificate.objects.filter().order_by('-id')


class CertificateDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]

    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    lookup_field = 'certificate_id'


class CommentToCertificateView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()

    def post(self, request, *args, **kwargs):
        topic_id = request.data.get('id')
        post_content = request.data.get('content')
        
        avatar_id = request.data.get('imagesupload_id')
        # avatar_get = CommentImage.objects.get(id=avatar_id)
        comment_user = "admin"


        new_post = Comment.objects.create(
            # user=self.request.user,
            user=comment_user,
            content=post_content,
            cert_id=topic_id,
        )

        for imageid in avatar_id:
            avatar_get = CommentImage.objects.get(id=imageid)
            new_post.image.add(avatar_get)

        order_qs = Certificate.objects.filter(id=topic_id).order_by('-id').first()
        order_qs.comments.add(new_post)

        
        # create activity
        new_activity = Activity.objects.create(
            user=self.request.user,
            group=post_content,
            project=topic_id,
            certificate=order_qs,
            template='commented on @{certificate}.'
        )


        articles = Certificate.objects.get(id=topic_id)
        serializer = CertificateSerializer(articles)
        return JsonResponse(serializer.data, safe=False)


class CreateCommentImage(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    queryset = CommentImage.objects.all()
    serializer_class = CommentImageSerializer


class ActivityList(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['=forum']

    def get_queryset(self):
        # return Certificate.objects.filter(user=self.request.user).order_by('-id')
        return Activity.objects.filter().order_by('-id')