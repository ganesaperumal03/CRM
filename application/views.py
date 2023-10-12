from django.shortcuts import render, redirect, get_object_or_404
from .forms import LeadForm,DealForm
from .models import Leads,Deals
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render(request, "user/index.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to CRM page after login
    return render(request, 'user/login.html') 

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user
            auth_login(request, user)
            return redirect('user_login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'user/signup.html', {'form': form})

def user_logout(request):
    return render(request, 'user/logout.html') 

def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def login(request):
    return render(request, "login.html")

def customer(request):

    return render(request, "customer/customer.html")

def customer_register(request):
    return render(request, "customer/customer_register.html")


def leads(request):
    leads = Leads.objects.all()
    return render(request, "leads/leads.html", {'leads': leads})

def leads_register(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads')  # Redirect to the leads list view
    else:
        form = LeadForm()

    return render(request, 'leads/leads_register.html', {'form': form})

def leads_update(request, lead_id):
    lead = get_object_or_404(Leads, pk=lead_id)  # Use 'pk' instead of 'lead_id'

    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads')
    else:
        form = LeadForm(instance=lead)

    return render(request, 'leads/leads_update.html', {'form': form, 'lead': lead})

def leads_delete(request, lead_id):
    lead = get_object_or_404(Leads, pk=lead_id)  # Use 'pk' instead of 'lead_id
    if request.method == 'POST':
        lead.delete()
        return redirect('leads')
    return render(request, 'leads/leads_delete.html', {'lead': lead})

# deals views start
def deals(request):
    deals = Deals.objects.all()  # Fetch all deals from the database
    return render(request, 'deals/deals.html', {'deals': deals})

def deals_register(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deals')  # Redirect to the deals list view
    else:
        form = DealForm()
    return render(request, 'deals/deals_register.html', {'form': form})

def deals_delete(request, deal_id):
    deal = get_object_or_404(Deals, deal_id=deal_id)
    if request.method == 'POST':
        deal.delete()
        return redirect('deals_list')
    return render(request, 'deals/deals_delete.html', {'deal': deal})

def deals_update(request, deal_id):
    deal = get_object_or_404(Deals, deal_id=deal_id)
    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            return redirect('deals')
    else:
        form = DealForm(instance=deal)

    return render(request, 'deals/deals_update.html', {'form': form, 'deal': deal})


# deals views End

def analytics(request):
    return render(request, "analytics/analytics.html")

def deals_analytics(request):
    return render(request, "analytics/deals_analytics.html")

def leads_analytics(request):
    return render(request, "analytics/leads_analytics.html")

