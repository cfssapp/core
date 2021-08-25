from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated

api_urls = {
    "data": [
        {
            "id": "xxx1",
            "title": "Alipay",
            "logo": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
            "description": "那是一种内在的东西，他们到达不了，也无法触及的",
            "updatedAt": "2021-08-20T11:32:01.107Z",
            "member": "科学搬砖组",
            "href": "",
            "memberLink": ""
        },
        {
            "id": "xxx2",
            "title": "Angular",
            "logo": "https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png",
            "description": "希望是一个好东西，也许是最好的，好东西是不会消亡的",
            "updatedAt": "2017-07-24T00:00:00.000Z",
            "member": "全组都是吴彦祖",
            "href": "",
            "memberLink": ""
        }
    ]
}

# BK Testing
@api_view(['GET'])
def apiOverview(request):
	
	return Response(api_urls)