from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import FoodItemSerializer, OrderSerializer
from .models import FoodItem, Order

from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from rest_framework import filters

# Create your views here.
class FoodItemList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodItemSerializer

    def get_queryset(self):
        return FoodItem.objects.filter(cartadded=False, ordered=False).order_by('-id')

