from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import CartSerializer, ProductSerializer
from .models import Cart, Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

import json


# api_urls = {
#     "success": True,
#     "data": {
#         "list": [
#     {
#         "id": 5,
#         "avatar": {
#             "id": 43,
#             "imagefile": "https://antapi.pythonanywhere.com/media/upload_pics/2509_SDg7PyR.png"
#         },
#         "name": "100 Plus",
#         "price": "RM4.53",
#         "category": "Beverages",
#         "cartadded": False,
#         "ordered": False,
#         "order_id": ""
#     },
#     {
#         "id": 3,
#         "avatar": {
#             "id": 41,
#             "imagefile": "https://antapi.pythonanywhere.com/media/upload_pics/1003_4Htt9rm.png"
#         },
#         "name": "Double Cheeseburger",
#         "price": "RM10.37",
#         "category": "Burgers",
#         "cartadded": False,
#         "ordered": False,
#         "order_id": ""
#     },
#     {
#         "id": 2,
#         "avatar": {
#             "id": 39,
#             "imagefile": "https://antapi.pythonanywhere.com/media/upload_pics/2100_03CcJBm.png"
#         },
#         "name": "Coca-Cola",
#         "price": "RM4.53",
#         "category": "Beverages",
#         "cartadded": False,
#         "ordered": False,
#         "order_id": ""
#     },
#     {
#         "id": 1,
#         "avatar": {
#             "id": 40,
#             "imagefile": "https://antapi.pythonanywhere.com/media/upload_pics/1028_IwVvaDb.png"
#         },
#         "name": "McChicken",
#         "price": "RM8.49",
#         "category": "Burgers",
#         "cartadded": False,
#         "ordered": False,
#         "order_id": ""
#     }
# ]
#     },
#     "errorCode": 0
# }

api_urls = {
    "success": True,
    "data": [
        {
            "id": 1,
            "list": [
                {
                    "id": 2,
                    "user": {
                        "id": 1,
                        "email": "admin@admin.com",
                        "user_name": "admin",
                        "is_active": True,
                        "avatar": "https://antapi.pythonanywhere.com/media/upload_pics/287279348080d90deec11dfa24065fc0.jpg",
                        "status": "ok",
                        "currentAuthority": "admin",
                        "success": "true"
                    },
                    "product_id": "not set",
                    "product_name": "laptop",
                    "addcart_id": True
                }
            ],
            "cart_id": "not set",
            "customer": "admin"
        }
    ],
    "errorCode": 0
}

@api_view(['GET'])
def apiOverview(request):
	
	return Response(api_urls)

# def apiOverview(request):
#     queryset = Cart.objects.all()
#     serializer = CartSerializer(queryset, many=True)

#     jsonoutput = {
#                 "success": True,
#                 'data' : serializer.data,
#                 "errorCode": 0
#             }

#     return HttpResponse(json.dumps(jsonoutput), content_type='application/json')



class CartList(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['=forum']

    def get_queryset(self):
        # return Certificate.objects.filter(user=self.request.user).order_by('-id')
        return Cart.objects.filter().order_by('-id')


class CartDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer




