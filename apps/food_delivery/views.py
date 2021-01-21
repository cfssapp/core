from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import FoodItemSerializer, FoodOrderSerializer, FoodAvatarSerializer
from .models import FoodItem, FoodOrder, FoodAvatar

from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from rest_framework import filters

# Create your views here.
class FoodItemList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=category']

    def get_queryset(self):
        return FoodItem.objects.filter(cartadded=False, ordered=False).order_by('-id')

class FoodItemDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer


class CreateFoodItem(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # parser_classes = [MultiPartParser, FormParser]
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

    def create(self, request, *args, **kwargs):
        # avatar_id = request.data.get('avatar', None)
        avatar_id = 21
        
        avatar_qs = FoodAvatar.objects.filter(id=avatar_id)
        fooditem_qs = FoodItem.objects.filter().order_by('-id').first()
        fooditem_qs.update(avatar=avatar_qs)
        fooditem_qs.update(cartadded=True)
        

        serializer = FoodItemSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        articles = FoodItem.objects.filter(cartadded=False, ordered=False).order_by('-id')
        serializer = FoodItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
        

class EditFoodItem(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        articles = FoodItem.objects.filter(cartadded=False, ordered=False).order_by('-id')
        serializer = FoodItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

class DeleteFoodItem(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        articles = FoodItem.objects.filter(cartadded=False, ordered=False).order_by('-id')
        serializer = FoodItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

class CreateFoodAvatar(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    queryset = FoodAvatar.objects.all()
    serializer_class = FoodAvatarSerializer

    