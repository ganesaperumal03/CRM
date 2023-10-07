
from django.contrib import admin
from django.urls import path
from application import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="Home"),
    path('dashboard', views.dashboard,name="dashboard"),
    path('login', views.login,name="login"),
    path('customer', views.customer,name="customer"),


]
