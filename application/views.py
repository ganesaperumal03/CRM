from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

def home(request):
    return render(request, "index.html")

def dashboard(request):
    customers = Customer.objects.all()
    return render(request, "dashboard.html", {'customers': customers})

def login(request):
    return render(request, "login.html")

def customer(request):
    return render(request, "customer/customer.html")

def submit_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the data to the Customer table
            return redirect('customer')  # Redirect to the 'customer' page after successful submission
    else:
        form = CustomerForm()

    return render(request, 'index.html')
