from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    learn = Course.objects.all()
    return render(request, 'index.html', {'learn': learn})
