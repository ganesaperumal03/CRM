from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm 

# Customer View

# List all customers
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customer_list.html', {'customers': customers})

# View details of a specific customer
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'crm/customer_detail.html', {'customer': customer})

# Add a new customer
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'crm/add_customer.html', {'form': form})

# Edit customer information
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'crm/edit_customer.html', {'form': form, 'customer': customer})

# Delete a customer
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'crm/delete_customer.html', {'customer': customer})


# Company View

# List all companies
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'crm/company_list.html', {'companies': companies})

# View details of a specific company
def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'crm/company_detail.html', {'company': company})

# Add a new company
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'crm/add_company.html', {'form': form})

# Edit company information
def edit_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'crm/edit_company.html', {'form': form, 'company': company})

# Delete a company
def delete_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, 'crm/delete_company.html', {'company': company})


# Contacts View

# List all contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'crm/contact_list.html', {'contacts': contacts})

# View details of a specific contact
def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'crm/contact_detail.html', {'contact': contact})

# Add a new contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'crm/add_contact.html', {'form': form})

# Edit contact information
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'crm/edit_contact.html', {'form': form, 'contact': contact})

# Delete a contact
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'crm/delete_contact.html', {'contact': contact})


# Service request View

# List all service requests
def service_request_list(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'crm/service_request_list.html', {'service_requests': service_requests})

# View details of a specific service request
def service_request_detail(request, service_request_id):
    service_request = get_object_or_404(ServiceRequest, pk=service_request_id)
    return render(request, 'crm/service_request_detail.html', {'service_request': service_request})

# Create a new service request
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'crm/create_service_request.html', {'form': form})

# Edit service request details
def edit_service_request(request, service_request_id):
    service_request = get_object_or_404(ServiceRequest, pk=service_request_id)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm(instance=service_request)
    return render(request, 'crm/edit_service_request.html', {'form': form, 'service_request': service_request})

# Change the status of a service request
def change_service_request_status(request, service_request_id, new_status):
    service_request = get_object_or_404(ServiceRequest, pk=service_request_id)
    service_request.status = new_status
    service_request.save()
    return redirect('service_request_list')

# Delete a service request
def delete_service_request(request, service_request_id):
    service_request = get_object_or_404(ServiceRequest, pk=service_request_id)
    if request.method == 'POST':
        service_request.delete()
        return redirect('service_request_list')
    return render(request, 'crm/delete_service_request.html', {'service_request': service_request})
