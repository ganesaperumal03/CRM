from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home, name="home"),  # Changed name to "home"
    path('dashboard', views.dashboard, name="dashboard"),
    path('login', views.login, name="login"),
    path('customer', views.customer, name="customer"),
    path('submit_customer', views.submit_customer, name="submit_customer"),
    path('customer_register', views.customer_register, name="customer_register"),
    path('leads', views.leads, name="leads"),
    path('leads_register', views.leads_register, name="leads_register"),
    path('submit_leads', views.submit_leads, name="submit_leads"),
    path('leads_analytics', views.leads_analytics, name="leads_analytics"),
    path('deals', views.deals, name="deals"),
    path('deals_analytics', views.deals_analytics, name="deals_analytics"),
]
