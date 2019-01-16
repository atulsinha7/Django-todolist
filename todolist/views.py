from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . models import users, checklist
from . serializers import userserializers, checklistserializers
import json


class board():
    def __init__(self, uname, uid, tname):
        self.uname = uname
        self.uid = uid
        self.tname = tname

@api_view(['GET'])
def getUsers(request):
    allusers = users.objects.all()
    serializer = userserializers(allusers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getList(request, user_id):
    list_items = checklist.objects.filter(uid=user_id)
    serializer = checklistserializers(list_items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = userserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_task(request, user_id, tname):
    # task = checklist.objects.get(uid=user_id)
    # serializer = checklistserializers(task.objects.get(taskname=tname))
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    obj = checklist.objects.get(uid = user_id, taskname=tname)
    obj.state = True
    temp = {"uid": obj.uid,
             "taskname": obj.taskname,
             "state": obj.state}
    serializer = checklistserializers(data=temp)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def del_user(request, user_id):
    # user = users.objects.get(id=user_id)
    try:
        user = users.objects.get(id=user_id)
    except users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['DELETE'])
def del_list(request, user_id):
    pass