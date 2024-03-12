from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):

    return render(request, 'usereg/index.html')

def register(request):

    return render(request, 'usereg/register.html')

def login(request):

    return render(request, 'usereg/login.html')

def dashboard(request):

    return render(request, 'usereg/dashboard.html')