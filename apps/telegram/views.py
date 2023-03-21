from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
api_urls = {
    "data": [
        {
            "id": "trend-1",
            "updatedAt": "2021-08-20T11:49:35.376Z",
            "user": {
                "name": "曲丽丽",
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png"
            },
            "group": {
                "name": "高逼格设计天团",
                "link": "http://github.com/"
            },
            "project": {
                "name": "六月迭代",
                "link": "http://github.com/"
            },
            "template": "在 @{group} 新建项目 @{project}"
        },
        {
            "id": "trend-2",
            "updatedAt": "2021-08-20T11:49:35.376Z",
            "user": {
                "name": "付小小",
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/cnrhVkzwxjPwAaCfPbdc.png"
            },
            "group": {
                "name": "高逼格设计天团",
                "link": "http://github.com/"
            },
            "project": {
                "name": "六月迭代",
                "link": "http://github.com/"
            },
            "template": "在 @{group} 新建项目 @{project}"
        },
    ]
}


@api_view(['GET'])
def apiOverview(request):
	
	return Response(api_urls)