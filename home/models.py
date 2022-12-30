from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    product_id = models.IntegerField(null=True)
    product_name = models.CharField(max_length=30, null=True)
    product_desc = models.CharField(max_length=120, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    # image

    def __str__(self):
        return self.product_name


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    t_id = models.CharField(max_length=30, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def cartTotal(self):
        items = self.item_set.all()
        total = sum([item.total for item in items])
        return total

    @property
    def getCartItem(self):
        items = self.item_set.all()
        total = sum([item.quantity for item in items])
        return total

# order_item


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        total = self.product.price * self.quantity
        return total


class Address(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=120, null=True)
    city = models.CharField(max_length=120, null=True)
    state = models.CharField(max_length=120, null=True)
    zipcode = models.CharField(max_length=120, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
