from django.db import models


class Module(models.Model):
    id_module = models.AutoField(primary_key=True)
    title_module = models.CharField(max_length=250)
    description_module = models.TextField(blank=False)

    def __str__(self):
        return self.title_module


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name_client = models.CharField(max_length=500)
    last_name_client = models.CharField(max_length=500)
    email_client = models.CharField(max_length=800)

    def __str__(self):
        return self.name_client + " " + self.last_name_client


class Supplier(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    name_supplier = models.CharField(max_length=500)
    phone_supplier = models.CharField(max_length=500)
    email_supplier = models.CharField(max_length=500)

    def __str__(self):
        return self.name_supplier


class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name_product = models.CharField(max_length=800)
    sell_price_product = models.FloatField()
    buy_price_product = models.FloatField()

    def __str__(self):
        return self.name_product
