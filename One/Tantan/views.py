from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('123')


def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')