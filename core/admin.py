from django.contrib import admin
from .models import Module, Supplier, Client, Product

# Register your models here.
admin.site.register(Module)
admin.site.register(Supplier)
admin.site.register(Client)
admin.site.register(Product)