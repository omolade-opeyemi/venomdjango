from django.shortcuts import render
from rest_framework import generics
from . models import List
from .serializers import ToDoSerializer


# Create your views here.
class TodoList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ToDoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ToDoSerializer






