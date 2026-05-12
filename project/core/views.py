from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def landing(request):
    return render(request, 'core/landing.html')

def login_view(request):
    return render(request, 'core/login.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')


# Create your views here.
