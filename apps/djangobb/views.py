from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import TopicSerializer
from .models import Topic

from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from rest_framework import filters


def fake_data_01(request):
	api_urls = {
    "salesData": [
        {
            "x": "Jan",
            "y": 1
        },
    ],
}

	return JsonResponse(api_urls, safe=False)


class TopicList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=forum']

    def get_queryset(self):
        return Topic.objects.filter(user=self.request.user).order_by('-id')