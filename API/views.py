from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from API import serializers

# Create your views here.
@api_view(['GET'])
def apilinks(request):
    api_urls = {
        'List' : '/todo-list/',
        'Detail View' : '/todo-detail/<str:pk>/',
        'Create' : '/todo-create/',
        'Update' : '/todo-update/<str:pk>/',
        'Delete' : '/todo-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def TodoList(request):
    tasks = Todo.objects.all()
    serializer = TodoSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def TodoDetail(request, pk):
    tasks = Todo.objects.get(id=pk)
    serializer = TodoSerializer(tasks, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def TodoUpdate(request, pk):
    tasks= Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response (serializer.data)

@api_view(['POST'])
def TodoCreate(request,pk):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def TodoDelete(request, pk):
    tasks = Todo.objects.get(id = pk)
    tasks.delete()
    return Response("This Todo is deleted successfully.")

