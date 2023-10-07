from django.shortcuts import render
import os
# Create your views here.
def home(request):
    return render(request,"index.html")

def dashboard(request):
    return render(request,"dashboard.html")

def login(request):
    return render(request,"login.html")

def customer(request):
    return render(request,"customer/customer.html")