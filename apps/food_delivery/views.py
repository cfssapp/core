from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import FoodItemSerializer, FoodOrderSerializer, FoodAvatarSerializer, AddressSerializer
from .models import FoodItem, FoodOrder, FoodAvatar, Address
from .myclass import OrderCode

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
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

    def create(self, request, *args, **kwargs):
        avatar_id = request.data.get('avatar')
        avatar_get = FoodAvatar.objects.get(id=avatar_id)

        serializer = FoodItemSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        obj = serializer.save()

        fooditem_get = FoodItem.objects.get(id=obj.id)
        fooditem_get.avatar = avatar_get
        fooditem_get.save()

        #test
        # fooditem_ten = FoodItem.objects.get(id=10)
        # avatar_twentytwo = FoodAvatar.objects.get(id=22)
        # fooditem_ten.avatar = avatar_twentytwo
        # fooditem_ten.save()

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


class AddToCartView(APIView):
    def post(self, request, *args, **kwargs):
        fooditem_id = request.data.get('id')

        fooditem_get = FoodItem.objects.filter(id=fooditem_id)
        fooditem_get.update(cartadded=True)
        
        articles = FoodItem.objects.filter(cartadded=False, ordered=False).order_by('-id')
        serializer = FoodItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


class RemoveFromCartView(APIView):
    def post(self, request, *args, **kwargs):
        fooditem_id = request.data.get('id')

        fooditem_get = FoodItem.objects.filter(id=fooditem_id)
        fooditem_get.update(cartadded=False)
        
        articles = FoodItem.objects.filter(cartadded=True, ordered=False).order_by('-id')
        serializer = FoodItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


class AddressList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user, default=True)


class CreateAddress(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=self.request.user)
        articles = Address.objects.filter(user=self.request.user, default=True)
        serializer = AddressSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
        

class EditAddress(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        articles = Address.objects.filter(user=self.request.user, default=True)
        serializer = AddressSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


class FoodCartList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodItemSerializer

    def get_queryset(self):
        return FoodItem.objects.filter(cartadded=True, ordered=False).order_by('-id')


class FoodOrderList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodOrderSerializer

    def get_queryset(self):
        return FoodOrder.objects.filter(user=self.request.user).order_by('-id')


class AddToOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodOrderSerializer
    queryset = FoodOrder.objects.all()

    def post(self, request, *args, **kwargs):
        shipping_id = request.data.get('shipping_id')

        order_no = OrderCode()

        order = FoodOrder.objects.create(
            order_id = order_no,
            user=self.request.user,
            shipping_address=shipping_id,
        )

        articles = FoodItem.objects.filter(cartadded=True, ordered=False).order_by('-id')
        serializer = FoodItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)