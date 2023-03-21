from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import TelegramSNSerializer, TelegramCommentSerializer, TelegramUserSerializer
from .models import TelegramSN, TelegramComment, TelegramUser

# Create your views here.
class TelegramSNList(generics.ListAPIView):
    queryset = TelegramSN.objects.all()
    serializer_class = TelegramSNSerializer

    def get_queryset(self):
        return TelegramSN.objects.filter().order_by('-id')
    
    
class TelegramUserList(generics.ListAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer

    def get_queryset(self):
        return TelegramUser.objects.filter().order_by('-id')
    

class TelegramUserDetail(generics.RetrieveAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    lookup_field = 'telegram_id'


class TelegramSNDetail(generics.RetrieveAPIView):
    queryset = TelegramSN.objects.all()
    serializer_class = TelegramSNSerializer
    lookup_field = 'sn'


class PostToUser(APIView):

    def post(self, request, *args, **kwargs):

        telegram_user_id = request.data.get('user_id')
        telegram_first_name = request.data.get('first_name')

        if TelegramUser.objects.filter(telegram_id=telegram_user_id).exists():
            query01 = TelegramUser.objects.get(telegram_id=telegram_user_id)
            query01.request_count += 1
            query01.save()
        else:    
            new_user = TelegramUser.objects.create(
                telegram_id=telegram_user_id,
                first_name=telegram_first_name,
            )

        query02 = TelegramUser.objects.get(telegram_id=telegram_user_id)
        serializer = TelegramUserSerializer(query02)
        return JsonResponse(serializer.data, safe=False)
    
    
class PostToUserList(APIView):

    def post(self, request, *args, **kwargs):

        telegram_user_id = request.data.get('user_id')
        telegram_first_name = request.data.get('first_name')

        if TelegramUser.objects.filter(telegram_id=telegram_user_id).exists():
            query01 = TelegramUser.objects.get(telegram_id=telegram_user_id)
            query01.request_count += 1
            query01.save()
        else:    
            new_user = TelegramUser.objects.create(
                telegram_id=telegram_user_id,
                first_name=telegram_first_name,
            )

        # query03 = TelegramSN.objects.get(id=1)
        query03 = TelegramSN.objects.all()
        serializer = TelegramSNSerializer(query03, many=True)
        return JsonResponse(serializer.data, safe=False)
    

class PostToSNDetail(APIView):

    def post(self, request, *args, **kwargs):

        telegram_user_id = request.data.get('user_id')
        telegram_first_name = request.data.get('first_name')
        telegram_sn = request.data.get('sn')

        if TelegramUser.objects.filter(telegram_id=telegram_user_id).exists():
            query01 = TelegramUser.objects.get(telegram_id=telegram_user_id)
            query01.request_count += 1
            query01.save()
        else:    
            new_user = TelegramUser.objects.create(
                telegram_id=telegram_user_id,
                first_name=telegram_first_name,
            )

        query03 = TelegramSN.objects.get(sn=telegram_sn)
        serializer = TelegramSNSerializer(query03)
        return JsonResponse(serializer.data, safe=False)
