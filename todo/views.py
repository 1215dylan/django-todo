from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
@api_view(['GET','POST','PUT'])
def todo_list(request):
    if request.method =='GET':
        todos=Todo.objects.all()
        print(todos)
        todosSerializers=TodoSerializer(todos,many=True)
        # print('????????')
        return Response(todosSerializers.data)
    elif request.method == 'POST':
        #request.data 字典
        cp_req=request.data.copy()
        cp_req['title']=request.data.pop('content','default')
        cp_req['completed']=False
        todosSerializers=TodoSerializer(data=cp_req)
        
        if todosSerializers.is_valid():
            todosSerializers.save()
            return Response(todosSerializers.data,status=201)
        
        return Response(todosSerializers.errors,status=400)
    
    elif request.method == 'PUT':
        if 'id' not in request.data:
            return Response({'error':'id is required'},status=400)
        
        target_todo=Todo.objects.get(id=request.data['id'])
        # target_todo.completed=request.data.pop('completed',False)
        todoSerializer=TodoSerializer(instance=target_todo,data=request.data,partial=True)
        
        if todoSerializer.is_valid():
            todoSerializer.save()
            return Response(todoSerializer.data,status=200)
        
        return Response(todoSerializer.errors,status=400)