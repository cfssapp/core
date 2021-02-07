from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions
from rest_framework.views import APIView



# Create your views here.
def fake_data_01(request):
	api_urls = {
    "salesData": [
        {
            "x": "Jan",
            "y": 1
        },
        {
            "x": "Feb",
            "y": 2
        },
        {
            "x": "Mar",
            "y": 3
        },
        {
            "x": "Apr",
            "y": 4
        },
        {
            "x": "May",
            "y": 5
        },
        {
            "x": "Jun",
            "y": 6
        },
        {
            "x": "Jul",
            "y": 7
        },
        {
            "x": "Aug",
            "y": 8
        },
        {
            "x": "Sep",
            "y": 9
        },
        {
            "x": "Oct",
            "y": 10
        },
        {
            "x": "Nov",
            "y": 11
        },
        {
            "x": "Dec",
            "y": 12
        }
    ],
}

	return JsonResponse(api_urls, safe=False)