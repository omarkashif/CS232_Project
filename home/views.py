from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Order
# Create your views here.


def index(request):
    return render(request, "home.html")
    # return HttpResponse("Home PaGe!!!")


def about(request):
    return render(request, "about.html")


def watch(request):
    return render(request, "watch.html")


def wallet(request):
    return render(request, "wallet.html")


def perfume(request):
    return render(request, "perfume.html")


def buy(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        ord = Order(name=name, address=address,
                    phone=phone, date=datetime.today())
        ord.save()
    return render(request, "BuyNow.html")


def c(request):
    return render(request, "c.html")


def contact(request):
    return render(request, "contact.html")
