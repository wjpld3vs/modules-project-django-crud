"""
URL configuration for modules project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('modules/', views.modules, name='modules'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('modules/products/', views.get_products, name='all_products'),
    path('modules/clients/', views.get_clients, name='all_clients'),
    path('modules/suppliers/', views.get_suppliers, name='all_suppliers'),
    path('modules/clients/new', views.new_client, name='new_client')
]
