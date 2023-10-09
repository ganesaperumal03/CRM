from django.shortcuts import render, redirect
from .forms import CustomerForm,LeadForm
from .models import Customer,Lead
def home(request):
    return render(request, "index.html")

def dashboard(request):
    customers = Customer.objects.all()
    return render(request, "dashboard/dashboard.html", {'customers': customers})

def login(request):
    return render(request, "login.html")

def customer(request):
    customers = Customer.objects.all()
    return render(request, "customer/customer.html", {'customers': customers})

def customer_register(request):
    return render(request, "customer/customer_register.html")

def submit_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('customer')  
    else:
        form = CustomerForm()
    return render(request, 'customer/customer_register.html')

def leads(request):
    leads = Lead.objects.all()
    return render(request, "leads/leads.html", {'leads': leads})
    
def leads_register(request):
    form = LeadForm()
    return render(request, "leads/leads_register.html",{'form': form})

def leads_analytics(request):
    form = CustomerForm()
    return render(request, "leads/leads_analytics.html",{'form': form})

def submit_leads(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('leads')  
    else:
        pass

def deals(request):
    return render(request, "deals/deals.html")

def deals_analytics(request):
    form = CustomerForm()
    return render(request, "deals/deals_analytics.html",{'form': form})