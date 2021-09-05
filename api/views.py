from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated


from .serializers import TaskSerializer
from .models import Task


# Create your views here.
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

api_urls1 = {
    "data": {
        "name": "Serati Ma",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png",
        "userid": "00000001",
        "email": "antdesign@alipay.com",
        "signature": "海纳百川，有容乃大",
        "title": "交互专家",
        "group": "蚂蚁金服－某某某事业群－某某平台部－某某技术部－UED",
        "tags": [
            {
                "key": "0",
                "label": "很有想法的"
            },
            {
                "key": "1",
                "label": "专注设计"
            },
            {
                "key": "2",
                "label": "辣~"
            },
            {
                "key": "3",
                "label": "大长腿"
            },
            {
                "key": "4",
                "label": "川妹子"
            },
            {
                "key": "5",
                "label": "海纳百川"
            }
        ],
        "notifyCount": 12,
        "unreadCount": 11,
        "country": "China",
        "geographic": {
            "province": {
                "label": "浙江省",
                "key": "330000"
            },
            "city": {
                "label": "杭州市",
                "key": "330100"
            }
        },
        "address": "西湖区工专路 77 号",
        "phone": "0752-268888888"
    }
}

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def apiOverview1(request):
	
	return Response(api_urls1)

def custom_exception_handler(exc, context):
	
    if isinstance(exc, NotAuthenticated):
        return Response(api_urls, status=401)

    # else
    # default case
    return exception_handler(exc, context)

# BK Testing
@api_view(['GET'])
def apiOverview(request):
	# api_urls = {
	# 	'List':'/task-list/',
	# 	'Detail View':'/task-detail/<str:pk>/',
	# 	'Create':'/task-create/',
	# 	'Update':'/task-update/<str:pk>/',
	# 	'Delete':'/task-delete/<str:pk>/',
	# 	}
	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')



