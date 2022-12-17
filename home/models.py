from django.db import models

# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=120)
    date = models.DateField()
