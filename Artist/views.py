from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def landingpage(request):
    context = {}
    return render(request, 'temp/base.html', context)

def homepage(request):
    context = {}
    return render()

def loginpage(request):
    if request.method == "POST":
        username = authenticate(
            email = request.POST['email'],
            password = request.POST['password']
        )
        if username is not None:
            login(request, username)
            return redirect('profile')
    context = {}
    return render(request, 'temp/login.html', context)

def profilepage(request):
    context = {}
    return render(request, 'temp/profile.html', context)