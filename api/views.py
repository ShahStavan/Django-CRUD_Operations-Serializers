from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from api import serializers

# Create your views here.


# Getting structure of the API
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'detail': '/task-detail/<str:pk>/',
        'create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls) 

# TaskList 
@api_view(['GET'])
def taskList(request):
    task = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(task, many=True)
   
    return Response(serializer.data)

# Task Detail
@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializers = TaskSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    else:
        return Response(serializers.errors)
    return Response(serializers.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializers = TaskSerializer(instance=task,data=request.data)
    
    if serializers.is_valid():
        serializers.save()
    else:
        return Response(serializers.errors)
    return Response(serializers.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item succesfully deleted!')