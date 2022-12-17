from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name="gift"),
    path("about", views.about, name="about"),
    path("contact ", views.contact, name="contact"),
    path("watch", views.watch, name="watch"),
    path("wallet", views.wallet, name="wallet"),
    path("perfume", views.perfume, name="perfume"),
    path("BuyNow", views.buy, name="BuyNow"),
    path("c", views.c, name="c")

]
