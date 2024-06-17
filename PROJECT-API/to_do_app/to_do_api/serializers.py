from django.contrib.auth.models import User
from rest_framework import serializers
from . models import List



class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'