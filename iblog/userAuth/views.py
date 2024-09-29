from django.shortcuts import render
from userAuth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            print('loggedin')
            return redirect('home')
        else:
            print('not-found')
            return redirect('login')
    return render(request, 'userAuth/login.html')


def signup_user(request):
    if request.method == 'POST':
        full_name = request.POST['full-name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(
            name=full_name,
            email=email,
            password=password
        )
        login(request, user)
        return redirect('home')
    return render(request, "userAuth/register.html")