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
        },
        {
            "id": "xxx3",
            "title": "Ant Design",
            "logo": "https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png",
            "description": "城镇中有那么多的酒馆，她却偏偏走进了我的酒馆",
            "updatedAt": "2021-08-20T11:32:01.107Z",
            "member": "中二少女团",
            "href": "",
            "memberLink": ""
        },
        {
            "id": "xxx4",
            "title": "Ant Design Pro",
            "logo": "https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png",
            "description": "那时候我只会想自己想要什么，从不想自己拥有什么",
            "updatedAt": "2017-07-23T00:00:00.000Z",
            "member": "程序员日常",
            "href": "",
            "memberLink": ""
        },
        {
            "id": "xxx5",
            "title": "Bootstrap",
            "logo": "https://gw.alipayobjects.com/zos/rmsportal/siCrBXXhmvTQGWPNLBow.png",
            "description": "凛冬将至",
            "updatedAt": "2017-07-23T00:00:00.000Z",
            "member": "高逼格设计天团",
            "href": "",
            "memberLink": ""
        },
        {
            "id": "xxx6",
            "title": "React",
            "logo": "https://gw.alipayobjects.com/zos/rmsportal/kZzEzemZyKLKFsojXItE.png",
            "description": "生命就像一盒巧克力，结果往往出人意料",
            "updatedAt": "2017-07-23T00:00:00.000Z",
            "member": "骗你来学计算机",
            "href": "",
            "memberLink": ""
        }
    ]
}

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def apiOverview1(request):
	
	return Response(api_urls)

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



