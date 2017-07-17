# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

import psutil

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.parsers import *

from todoapp.models import *
from todoapp.serializers import *
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("HEllo world")
        if form.is_valid():
            new_user = form.save()
            print("h1111")
            return HttpResponseRedirect("/todo/login/")
    else:
        form = UserCreationForm()
    return render(request,"registration/register.html",{'form':form,})


def homeview(request):
    return render(request,"todoapp/cards.html")


def list_create(request):
    return render(request,"todoapp/list_create.html")
class TodoList(APIView):
    """
    List all todolists, or create a new todolist.
    """
    def get(self, request, format=None):
        lists = Todolists.objects.filter(user_id=request.user.id)
        serializer = TodolistsSerializer(lists, many=True)
        return Response(serializer.data,content_type='application/json')

    def post(self, request, format=None):

        print(request.data)
        obj={}
        obj["id"]=request.data["id"]
        obj["name"]=request.data["name"]
        obj["creation_date"]=request.data["creation_date"]
        obj["user"]=request.user.id
        # obj=request.data
        # print(obj)
        # obj["user"]=request.user.id
        serializer = TodolistsSerializer(data=obj)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data["id"], status=201)
        return HttpResponse(serializer.errors)


class TodoListItems_all(APIView):
    """
    Retrieve, update or delete a list item.def get(self, request, pk, format=None):
    """
    def get_object(self,pk):
        try:
            return Todoitems.objects.filter(todolist_id=pk)
        except Todoitems.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk, format=None):
        list_items=self.get_object(pk)
        serializer = TodoitemsSerializer(list_items,many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        # list_items=self.get_object(pk)
        obj={}
        obj["id"]=request.data["id"];
        obj["description"]=request.data["description"];
        obj["completed"] = request.data["completed"]
        obj["due_by"] = request.data["due_by"];
        obj["todolist"] =pk;
       # request.data["todolist"]=pk
        # return Response('hiiiii')
        serializer = TodoitemsSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data["id"])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk,format=None):
        item =Todolists.objects.get(id=pk)
        print(item)
        # data["id"]=itemid
        obj = {}
        obj["id"] = request.data["id"]
        obj["name"] = request.data["name"]
        obj["creation_date"] = request.data["creation_date"]
        obj["user"] = request.user.id
        print(request.data)
        serializer = TodolistsSerializer(item, data=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = Todolists.objects.get(id=pk)
        item.delete()
        return Response(status=204)

class TodoListItems_single(APIView):
    """
        Retrieve, update or delete a list item.def get(self, request, pk, format=None):
        """

    def get_object(self,itemid):
        try:
            return Todoitems.objects.get(id=itemid)
        except Todoitems.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk,itemid, format=None):
        # item = self.get_object(itemid)
        item=Todoitems.objects.filter(id=itemid)
        serializer = TodoitemsSerializer(item, many=True)
        return Response(serializer.data)

    def put(self, request,pk, itemid, format=None):
        item = self.get_object(itemid)

        # data["id"]=itemid
        serializer = TodoitemsSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk, itemid, format=None):
        item = self.get_object(itemid)
        item.delete()
        return Response(status=204)

#
# from todoapp.models import *
# from todoapp.serializers import *
# from rest_framework import generics
#
#
# class TodoList(generics.ListCreateAPIView):
#     queryset = Todolists.objects.all()
#     serializer_class = TodolistsSerializer
#
#
# class TodoListDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todolists.objects.all()
#     serializer_class = TodolistsSerializer

#
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer















# def sample(request):
#     s=psutil.cpu_stats()
#     t=psutil.cpu_times()
#     return render(request, 'todoapp/sample.html', {'stats': s,'time':t})
# def listview(request):
#     c=Todolists.objects.all()
#     return render(request, 'todoapp/todolists.html', {'lists': c})
#
# def viewitemsbyid(request,listid):
#     d = Todolists.objects.filter(id=listid)
#     c=Todoitems.objects.filter(todolist_id=listid)
#
#     # d=Student.objects.filter(college_id=collegeid)
#     # e=MockTest1.objects.values("student__name","student__email","total").filter(student__college_id=collegeid).order_by("total")
#     return render(request,'todoapp/todoitems.html',{'items':c,'list':d})
#
# def viewall(request):
#     c=Todolists.objects.all()
#     d={}
#     for list in c:
#         d[list.name]=Todoitems.objects.filter(todolist_id=list.id)
#     # d=Student.objects.filter(college_id=collegeid)
#     # e=MockTest1.objects.values("student__name","student__email","total").filter(student__college_id=collegeid).order_by("total")
#     return render(request,'todoapp/all_lists_items.html',{'itemslist':d})

# [<QuerySet [<Todoitems: sleep well>]>, <QuerySet [<Todoitems: eat well>]>, <QuerySet [<Todoitems: enjoy well>]>, <QuerySet [<Todoitems: be passionate>]>, <QuerySet [<Todoitems: sleep well>]>, <QuerySet [<Todoitems: sleep well>]>, <QuerySet [<Todoitems: eat well>]>, <QuerySet [<Todoitems: enjoy well>]>, <QuerySet [<Todoitems: be passionate>]>, <QuerySet [<Todoitems: sleep well>]>]
