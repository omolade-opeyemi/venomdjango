from django.shortcuts import render
from todos.models import List

# Create your views here.
def List_Todo(request):
    list = List.objects.all()
    context = {'list':list}
    return render(request, 'index.html', context)

def Create_Todo(request):
    task = request.POST['task']
    author = request.User
    print(task, author)
    return render(request, 'index.html')

