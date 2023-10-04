from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request,'myapp/index.html')

def about(request):
    return render(request,'myapp/about.html')

def registration(request):
    return render(request,'myapp/registration.html')