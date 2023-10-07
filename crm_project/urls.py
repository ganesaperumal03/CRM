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
]
