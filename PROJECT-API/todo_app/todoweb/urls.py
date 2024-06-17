from django.urls import path
from .views import List_Todo, Create_Todo

urlpatterns = [
    path('', List_Todo, name="home"),
    path('create/', Create_Todo, name="create")

]