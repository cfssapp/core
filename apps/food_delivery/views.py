from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import FoodItemSerializer, FoodOrderSerializer, FoodAvatarSerializer, AddressSerializer, CsvSerializer
from .models import FoodItem, FoodOrder, FoodAvatar, Address, Csv

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
        avatar_id = request.data.get('avatar')
        avatar_get = FoodAvatar.objects.get(id=avatar_id)
        fooditem_id = request.data.get('id')

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        fooditem_get = FoodItem.objects.get(id=fooditem_id)
        fooditem_get.avatar = avatar_get
        fooditem_get.save()

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
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^order_id']

    def get_queryset(self):
        return FoodOrder.objects.filter(user=self.request.user).order_by('-id')


class AddToOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodOrderSerializer
    queryset = FoodOrder.objects.all()

    def post(self, request, *args, **kwargs):
        # shipping_id = request.data.get('id')
        shipping_address = Address.objects.get(id=13)

        parts = (shipping_address.street_name, shipping_address.postal_code, shipping_address.state)
        testjoin = ', '.join(str(part) for part in parts if part is not None)

        order = FoodOrder.objects.create(
            user=self.request.user,
            # shipping_address=shipping_address.street_name,
            shipping_address=testjoin,
        )

        order_qs = FoodOrder.objects.filter(user=self.request.user).order_by('-id').first()
        order_id = order_qs.order_id

        cartadded_items = FoodItem.objects.filter(cartadded=True)
        for item in cartadded_items:
            order.items.add(item)
        cartadded_items.update(order_id=order_id)
        cartadded_items.update(ordered=True)
        cartadded_items.update(cartadded=False)
        for item in cartadded_items:
            item.save()

        articles = FoodItem.objects.filter(cartadded=True, ordered=False).order_by('-id')
        serializer = FoodItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


class DeleteOrderView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodOrderSerializer
    queryset = FoodOrder.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        order_id = instance.order_id
        self.perform_destroy(instance)

        ordered_items = FoodItem.objects.filter(order_id=order_id)
        ordered_items.update(ordered=False)
        for item in ordered_items:
            item.save()

        articles = FoodOrder.objects.filter(user=self.request.user).order_by('-id')
        serializer = FoodOrderSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


class UploadFileView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Csv.objects.all()
    serializer_class = CsvSerializer


def fake_data(request):
	api_urls = [
  {
    "visitData": [
        {
            "x": "2021-01-29",
            "y": 7
        },
        {
            "x": "2021-01-30",
            "y": 5
        },
        {
            "x": "2021-01-31",
            "y": 4
        },
        {
            "x": "2021-02-01",
            "y": 2
        },
        {
            "x": "2021-02-02",
            "y": 4
        },
        {
            "x": "2021-02-03",
            "y": 7
        },
        {
            "x": "2021-02-04",
            "y": 5
        },
        {
            "x": "2021-02-05",
            "y": 6
        },
        {
            "x": "2021-02-06",
            "y": 5
        },
        {
            "x": "2021-02-07",
            "y": 9
        },
        {
            "x": "2021-02-08",
            "y": 6
        },
        {
            "x": "2021-02-09",
            "y": 3
        },
        {
            "x": "2021-02-10",
            "y": 1
        },
        {
            "x": "2021-02-11",
            "y": 5
        },
        {
            "x": "2021-02-12",
            "y": 3
        },
        {
            "x": "2021-02-13",
            "y": 6
        },
        {
            "x": "2021-02-14",
            "y": 5
        }
    ],
    "visitData2": [
        {
            "x": "2021-01-29",
            "y": 1
        },
        {
            "x": "2021-01-30",
            "y": 6
        },
        {
            "x": "2021-01-31",
            "y": 4
        },
        {
            "x": "2021-02-01",
            "y": 8
        },
        {
            "x": "2021-02-02",
            "y": 3
        },
        {
            "x": "2021-02-03",
            "y": 7
        },
        {
            "x": "2021-02-04",
            "y": 2
        }
    ],
    "salesData": [
        {
            "x": "1月",
            "y": 1063
        },
        {
            "x": "2月",
            "y": 1127
        },
        {
            "x": "3月",
            "y": 1181
        },
        {
            "x": "4月",
            "y": 688
        },
        {
            "x": "5月",
            "y": 543
        },
        {
            "x": "6月",
            "y": 212
        },
        {
            "x": "7月",
            "y": 664
        },
        {
            "x": "8月",
            "y": 880
        },
        {
            "x": "9月",
            "y": 1051
        },
        {
            "x": "10月",
            "y": 321
        },
        {
            "x": "11月",
            "y": 1188
        },
        {
            "x": "12月",
            "y": 894
        }
    ],
    "searchData": [
        {
            "index": 1,
            "keyword": "搜索关键词-0",
            "count": 926,
            "range": 95,
            "status": 0
        },
        {
            "index": 2,
            "keyword": "搜索关键词-1",
            "count": 752,
            "range": 37,
            "status": 0
        },
        {
            "index": 3,
            "keyword": "搜索关键词-2",
            "count": 428,
            "range": 56,
            "status": 1
        },
        {
            "index": 4,
            "keyword": "搜索关键词-3",
            "count": 141,
            "range": 85,
            "status": 1
        },
        {
            "index": 5,
            "keyword": "搜索关键词-4",
            "count": 999,
            "range": 56,
            "status": 1
        },
        {
            "index": 6,
            "keyword": "搜索关键词-5",
            "count": 584,
            "range": 67,
            "status": 0
        },
        {
            "index": 7,
            "keyword": "搜索关键词-6",
            "count": 749,
            "range": 52,
            "status": 1
        },
        {
            "index": 8,
            "keyword": "搜索关键词-7",
            "count": 418,
            "range": 98,
            "status": 0
        },
        {
            "index": 9,
            "keyword": "搜索关键词-8",
            "count": 257,
            "range": 27,
            "status": 1
        },
        {
            "index": 10,
            "keyword": "搜索关键词-9",
            "count": 793,
            "range": 17,
            "status": 1
        },
        {
            "index": 11,
            "keyword": "搜索关键词-10",
            "count": 314,
            "range": 70,
            "status": 0
        },
        {
            "index": 12,
            "keyword": "搜索关键词-11",
            "count": 621,
            "range": 40,
            "status": 1
        },
        {
            "index": 13,
            "keyword": "搜索关键词-12",
            "count": 48,
            "range": 10,
            "status": 1
        },
        {
            "index": 14,
            "keyword": "搜索关键词-13",
            "count": 914,
            "range": 89,
            "status": 0
        },
        {
            "index": 15,
            "keyword": "搜索关键词-14",
            "count": 967,
            "range": 83,
            "status": 1
        },
        {
            "index": 16,
            "keyword": "搜索关键词-15",
            "count": 908,
            "range": 4,
            "status": 1
        },
        {
            "index": 17,
            "keyword": "搜索关键词-16",
            "count": 408,
            "range": 58,
            "status": 1
        },
        {
            "index": 18,
            "keyword": "搜索关键词-17",
            "count": 30,
            "range": 12,
            "status": 1
        },
        {
            "index": 19,
            "keyword": "搜索关键词-18",
            "count": 806,
            "range": 20,
            "status": 1
        },
        {
            "index": 20,
            "keyword": "搜索关键词-19",
            "count": 271,
            "range": 26,
            "status": 1
        },
        {
            "index": 21,
            "keyword": "搜索关键词-20",
            "count": 733,
            "range": 56,
            "status": 0
        },
        {
            "index": 22,
            "keyword": "搜索关键词-21",
            "count": 757,
            "range": 39,
            "status": 0
        },
        {
            "index": 23,
            "keyword": "搜索关键词-22",
            "count": 543,
            "range": 94,
            "status": 1
        },
        {
            "index": 24,
            "keyword": "搜索关键词-23",
            "count": 50,
            "range": 74,
            "status": 1
        },
        {
            "index": 25,
            "keyword": "搜索关键词-24",
            "count": 359,
            "range": 99,
            "status": 0
        },
        {
            "index": 26,
            "keyword": "搜索关键词-25",
            "count": 92,
            "range": 69,
            "status": 0
        },
        {
            "index": 27,
            "keyword": "搜索关键词-26",
            "count": 196,
            "range": 23,
            "status": 1
        },
        {
            "index": 28,
            "keyword": "搜索关键词-27",
            "count": 590,
            "range": 17,
            "status": 1
        },
        {
            "index": 29,
            "keyword": "搜索关键词-28",
            "count": 506,
            "range": 6,
            "status": 0
        },
        {
            "index": 30,
            "keyword": "搜索关键词-29",
            "count": 238,
            "range": 33,
            "status": 1
        },
        {
            "index": 31,
            "keyword": "搜索关键词-30",
            "count": 111,
            "range": 75,
            "status": 1
        },
        {
            "index": 32,
            "keyword": "搜索关键词-31",
            "count": 804,
            "range": 37,
            "status": 0
        },
        {
            "index": 33,
            "keyword": "搜索关键词-32",
            "count": 847,
            "range": 83,
            "status": 1
        },
        {
            "index": 34,
            "keyword": "搜索关键词-33",
            "count": 335,
            "range": 40,
            "status": 0
        },
        {
            "index": 35,
            "keyword": "搜索关键词-34",
            "count": 273,
            "range": 23,
            "status": 0
        },
        {
            "index": 36,
            "keyword": "搜索关键词-35",
            "count": 947,
            "range": 43,
            "status": 1
        },
        {
            "index": 37,
            "keyword": "搜索关键词-36",
            "count": 82,
            "range": 74,
            "status": 0
        },
        {
            "index": 38,
            "keyword": "搜索关键词-37",
            "count": 916,
            "range": 72,
            "status": 1
        },
        {
            "index": 39,
            "keyword": "搜索关键词-38",
            "count": 748,
            "range": 43,
            "status": 0
        },
        {
            "index": 40,
            "keyword": "搜索关键词-39",
            "count": 953,
            "range": 78,
            "status": 1
        },
        {
            "index": 41,
            "keyword": "搜索关键词-40",
            "count": 373,
            "range": 81,
            "status": 1
        },
        {
            "index": 42,
            "keyword": "搜索关键词-41",
            "count": 86,
            "range": 73,
            "status": 1
        },
        {
            "index": 43,
            "keyword": "搜索关键词-42",
            "count": 667,
            "range": 37,
            "status": 0
        },
        {
            "index": 44,
            "keyword": "搜索关键词-43",
            "count": 968,
            "range": 71,
            "status": 1
        },
        {
            "index": 45,
            "keyword": "搜索关键词-44",
            "count": 468,
            "range": 18,
            "status": 1
        },
        {
            "index": 46,
            "keyword": "搜索关键词-45",
            "count": 340,
            "range": 77,
            "status": 1
        },
        {
            "index": 47,
            "keyword": "搜索关键词-46",
            "count": 280,
            "range": 8,
            "status": 1
        },
        {
            "index": 48,
            "keyword": "搜索关键词-47",
            "count": 457,
            "range": 37,
            "status": 1
        },
        {
            "index": 49,
            "keyword": "搜索关键词-48",
            "count": 40,
            "range": 18,
            "status": 1
        },
        {
            "index": 50,
            "keyword": "搜索关键词-49",
            "count": 522,
            "range": 59,
            "status": 0
        }
    ],
    "offlineData": [
        {
            "name": "Stores 0",
            "cvr": 0.2
        },
        {
            "name": "Stores 1",
            "cvr": 0.2
        },
        {
            "name": "Stores 2",
            "cvr": 0.9
        },
        {
            "name": "Stores 3",
            "cvr": 0.2
        },
        {
            "name": "Stores 4",
            "cvr": 0.1
        },
        {
            "name": "Stores 5",
            "cvr": 0.4
        },
        {
            "name": "Stores 6",
            "cvr": 0.7
        },
        {
            "name": "Stores 7",
            "cvr": 0.6
        },
        {
            "name": "Stores 8",
            "cvr": 0.5
        },
        {
            "name": "Stores 9",
            "cvr": 0.3
        }
    ],
    "offlineChartData": [
        {
            "x": 1611879493807,
            "y1": 106,
            "y2": 10
        },
        {
            "x": 1611881293807,
            "y1": 60,
            "y2": 14
        },
        {
            "x": 1611883093807,
            "y1": 101,
            "y2": 35
        },
        {
            "x": 1611884893807,
            "y1": 55,
            "y2": 103
        },
        {
            "x": 1611886693807,
            "y1": 45,
            "y2": 20
        },
        {
            "x": 1611888493807,
            "y1": 70,
            "y2": 27
        },
        {
            "x": 1611890293807,
            "y1": 19,
            "y2": 57
        },
        {
            "x": 1611892093807,
            "y1": 19,
            "y2": 49
        },
        {
            "x": 1611893893807,
            "y1": 36,
            "y2": 59
        },
        {
            "x": 1611895693807,
            "y1": 76,
            "y2": 84
        },
        {
            "x": 1611897493807,
            "y1": 19,
            "y2": 105
        },
        {
            "x": 1611899293807,
            "y1": 82,
            "y2": 96
        },
        {
            "x": 1611901093807,
            "y1": 61,
            "y2": 31
        },
        {
            "x": 1611902893807,
            "y1": 62,
            "y2": 38
        },
        {
            "x": 1611904693807,
            "y1": 52,
            "y2": 64
        },
        {
            "x": 1611906493807,
            "y1": 96,
            "y2": 51
        },
        {
            "x": 1611908293807,
            "y1": 59,
            "y2": 49
        },
        {
            "x": 1611910093807,
            "y1": 76,
            "y2": 19
        },
        {
            "x": 1611911893807,
            "y1": 101,
            "y2": 87
        },
        {
            "x": 1611913693807,
            "y1": 82,
            "y2": 60
        }
    ],
    "salesTypeData": [
        {
            "x": "家用电器",
            "y": 4544
        },
        {
            "x": "食用酒水",
            "y": 3321
        },
        {
            "x": "个护健康",
            "y": 3113
        },
        {
            "x": "服饰箱包",
            "y": 2341
        },
        {
            "x": "母婴产品",
            "y": 1231
        },
        {
            "x": "其他",
            "y": 1231
        }
    ],
    "salesTypeDataOnline": [
        {
            "x": "家用电器",
            "y": 244
        },
        {
            "x": "食用酒水",
            "y": 321
        },
        {
            "x": "个护健康",
            "y": 311
        },
        {
            "x": "服饰箱包",
            "y": 41
        },
        {
            "x": "母婴产品",
            "y": 121
        },
        {
            "x": "其他",
            "y": 111
        }
    ],
    "salesTypeDataOffline": [
        {
            "x": "家用电器",
            "y": 99
        },
        {
            "x": "食用酒水",
            "y": 188
        },
        {
            "x": "个护健康",
            "y": 344
        },
        {
            "x": "服饰箱包",
            "y": 255
        },
        {
            "x": "其他",
            "y": 65
        }
    ],
    "radarData": [
        {
            "name": "个人",
            "label": "引用",
            "value": 10
        },
        {
            "name": "个人",
            "label": "口碑",
            "value": 8
        },
        {
            "name": "个人",
            "label": "产量",
            "value": 4
        },
        {
            "name": "个人",
            "label": "贡献",
            "value": 5
        },
        {
            "name": "个人",
            "label": "热度",
            "value": 7
        },
        {
            "name": "团队",
            "label": "引用",
            "value": 3
        },
        {
            "name": "团队",
            "label": "口碑",
            "value": 9
        },
        {
            "name": "团队",
            "label": "产量",
            "value": 6
        },
        {
            "name": "团队",
            "label": "贡献",
            "value": 3
        },
        {
            "name": "团队",
            "label": "热度",
            "value": 1
        },
        {
            "name": "部门",
            "label": "引用",
            "value": 4
        },
        {
            "name": "部门",
            "label": "口碑",
            "value": 1
        },
        {
            "name": "部门",
            "label": "产量",
            "value": 6
        },
        {
            "name": "部门",
            "label": "贡献",
            "value": 5
        },
        {
            "name": "部门",
            "label": "热度",
            "value": 7
        }
    ]
}
]
	return JsonResponse(api_urls, safe=False)