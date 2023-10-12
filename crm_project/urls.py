from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from application import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home, name="home"),
    path('user_login', views.user_login, name="user_login"),
    path('user_signup', views.user_signup, name="user_signup"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('', views.home, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('login', views.login, name="login"),
    path('customer', views.customer, name="customer"),
    path('customer_register', views.customer_register, name="customer_register"),
    path('leads', views.leads, name="leads"),
    path('leads_register', views.leads_register, name="leads_register"),
    path('deals/update/<int:lead_id>/', views.leads_update, name='leads_update'),
    path('deals/delete/<int:lead_id>/', views.leads_delete, name='leads_delete'),
    path('leads_analytics', views.leads_analytics, name="leads_analytics"),
    path('deals', views.deals, name="deals"),
    path('deals_register', views.deals_register, name="deals_register"),
    path('deals_delete/<int:deal_id>/', views.deals_delete, name="deals_delete"),
    path('deals_update/<int:deal_id>/', views.deals_update, name="deals_update"),
    path('deals_analytics', views.deals_analytics, name="deals_analytics"),
    path('analytics', views.analytics, name="analytics"),
]
