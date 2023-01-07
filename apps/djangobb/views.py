from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import TopicSerializer, PostSerializer
from .models import Topic, Post

from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from rest_framework import filters


# def fake_data_01(request):
# 	api_urls = {
#     "salesData": [
#         {
#             "x": "Jan",
#             "y": 1
#         },
#     ],
# }

# 	return JsonResponse(api_urls, safe=False)

# def fake_data_01(request):
# 	api_urls = [
#     {
#         "userId": 1,
#         "id": 1,
#         "title": "server: pythonanywhere",
#         "body": "This is a test."
#     },

# ]
# 	return JsonResponse(api_urls, safe=False)

def fake_data_01(request):
	api_urls = [
    {
        "success": True,
    "data": {
        "list": [
            {
                "id": 0,
                "name": "Umi",
                "nickName": "U",
                "gender": "MALE"
            },
            {
                "id": 1,
                "name": "Fish",
                "nickName": "B",
                "gender": "FEMALE"
            }
        ]
    },
    "errorCode": 0
    },

]
	return JsonResponse(api_urls, safe=False)


class TopicList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=forum']

    def get_queryset(self):
        return Topic.objects.filter(user=self.request.user).order_by('-id')


class TopicDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class CreateTopic(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def create(self, request, *args, **kwargs):
        # avatar_id = request.data.get('avatar')
        # avatar_get = FoodAvatar.objects.get(id=avatar_id)

        serializer = TopicSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        obj = serializer.save()

        # fooditem_get = FoodItem.objects.get(id=obj.id)
        # fooditem_get.avatar = avatar_get
        # fooditem_get.save()

        #test
        # fooditem_ten = FoodItem.objects.get(id=10)
        # avatar_twentytwo = FoodAvatar.objects.get(id=22)
        # fooditem_ten.avatar = avatar_twentytwo
        # fooditem_ten.save()

        articles = Topic.objects.filter(user=self.request.user).order_by('-id')
        serializer = TopicSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


class EditTopic(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    def update(self, request, *args, **kwargs):
        # avatar_id = request.data.get('avatar')
        # avatar_get = FoodAvatar.objects.get(id=avatar_id)
        # fooditem_id = request.data.get('id')

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # fooditem_get = FoodItem.objects.get(id=fooditem_id)
        # fooditem_get.avatar = avatar_get
        # fooditem_get.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        articles = Topic.objects.filter(user=self.request.user).order_by('-id')
        serializer = TopicSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


class DeleteTopic(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        articles = Topic.objects.filter(user=self.request.user).order_by('-id')
        serializer = TopicSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


class PostToTopicView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    def post(self, request, *args, **kwargs):
        topic_id = request.data.get('id')
        post_content = request.data.get('content')
        

        new_post = Post.objects.create(
            user=self.request.user,
            content=post_content,
            topic_id=topic_id
        )

        order_qs = Topic.objects.filter(id=topic_id).order_by('-id').first()

        order_qs.posts.add(new_post)

        articles = Topic.objects.get(id=topic_id)
        serializer = TopicSerializer(articles)
        return JsonResponse(serializer.data, safe=False)