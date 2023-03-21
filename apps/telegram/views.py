from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics

from .serializers import TelegramSNSerializer, TelegramCommentSerializer
from .models import TelegramSN, TelegramComment, TelegramUser

# Create your views here.
api_urls = {
    "data": [
        {
            "id": "trend-1",
            "updatedAt": "2021-08-20T11:49:35.376Z",
        },
        {
            "id": "trend-2",
            "updatedAt": "2021-08-20T11:49:35.376Z",
            
        },
    ]
}


@api_view(['GET'])
def apiOverview(request):
	
	return Response(api_urls)


class TelegramSNList(generics.ListAPIView):

    queryset = TelegramSN.objects.all()
    serializer_class = TelegramSNSerializer


    def get_queryset(self):

        return TelegramSN.objects.filter().order_by('-id')