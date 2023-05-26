from django.shortcuts import render
from .models import Module, Supplier, Client, Product


def home(request):
    return render(request, 'home.html')


def modules(request):
    modules = Module.objects.all()
    return render(request, 'modules.html', {'modules': modules})


def login(request):
    return render(request, 'registration/login.html')


def register(request):
    return render(request, 'registration/register.html')


def get_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers.html', {'suppliers': suppliers})


def get_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


def new_client(request):

    return render(request, 'new-client.html')


def get_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
