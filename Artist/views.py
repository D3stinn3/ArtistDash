from django.shortcuts import render

# Create your views here.

def landingpage(request):
    context = {}
    return render(request, 'temp/base.html', context)

def homepage(request):
    context = {}
    return render()

def loginpage(request):
    context = {}
    return render(request, 'temp/login.html', context)

def profilepage(request):
    context = {}
    return render(request, 'temp/profile.html', context)