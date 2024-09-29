from django.shortcuts import render
from userAuth.models import User


def login_user(request):
    if request.method == 'POST':
        pass
    return render(request, 'userAuth/login.html')

def signup_user(request):
    if request.method == 'POST':
        pass
    return render(request, "userAuth/register.html")