from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import ItemSerializer, OrderSerializer
from .models import Item, Order

from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
class ItemList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ItemSerializer

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(item_owner=user, cartadded=False, ordered=False).order_by('-id')

