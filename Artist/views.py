from django.shortcuts import render

# Create your views here.

def landingpage(request):
    context = {}
    return render(request, 'temp/base.html', context)

def homepage(request):
    context = {}
    return render()