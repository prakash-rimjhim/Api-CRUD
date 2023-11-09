from .models import Task

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from django.core.exceptions import ObjectDoesNotExist



@api_view(['GET'])
def apiOverview(request):   
    return Response("API BASE POINT" )


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    try:
        tasks = Task.objects.get(id = pk)
        serializer = TaskSerializer(tasks , many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({"error": "Task not found"}, status=404)
    

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=tasks, data= request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def taskDelete(request,pk):
    tasks = get_object_or_404(Task, id=pk)
    tasks.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)