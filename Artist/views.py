from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreate
# Create your views here.

def landingpage(request):
    context = {}
    return render(request, 'temp/base.html', context)

def homepage(request):
    context = {}
    return render()

def signoutpage(request):
    logout(request)
    return redirect('landing')

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

def signuppage(request):
    if request.method == 'POST':
        user_form= UserCreate(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
        
    else:
        user_form =UserCreate()
    
    context = {'form': user_form}
    return render(request, 'temp/signin.html', context)

def activetasks(request):
    context = {}
    return render(request, 'temp/active.html', context)

def pendingtasks(request):
    context = {}
    return render(request, 'temp/pending.html', context)