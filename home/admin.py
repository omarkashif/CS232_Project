from django.contrib import admin
from home.models import Order, Customer, Item, Address, Product
# Register your models here.

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Address)
