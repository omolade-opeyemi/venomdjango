from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['pass']
        user = auth.authenticate(username=user, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid user')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        user = request.POST['user']
        email = request.POST['email']
        pass1 = request.POST['pass2']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username = user).exists():
                messages.info(request, 'name taken')
                return redirect('register')
            elif (User.objects.filter(email = email)).exists():
                print('emial taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=user, password=pass1, email=email,first_name = first, last_name = last)
                user.save();
                print('user saved')
                return redirect('/')
        else:
            print('pass error')
            return redirect('register')

    else:
        return render(request, 'register.html')
