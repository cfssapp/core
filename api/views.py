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
		"data": 
			{
				"isLogin": "false"
			},
		"errorCode": "401",
    	"errorMessage": "Please login!",
    	"success": "true"
	}

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def apiOverview(request):
	
	return Response(api_urls)

def custom_exception_handler(exc, context):
	
    if isinstance(exc, NotAuthenticated):
        return Response(api_urls, status=401)

    # else
    # default case
    return exception_handler(exc, context)

# BK Testing
@api_view(['GET'])
def apiOverviewbk(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}
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



