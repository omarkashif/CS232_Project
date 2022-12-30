from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Order, Customer, Item, Product
from django.http import JsonResponse
import json
# Create your views here.


def index(request):
    return render(request, "home.html")
    # return HttpResponse("Home PaGe!!!")


def about(request):
    return render(request, "about.html")


def watch(request):
    # if request.method == "POST":
    #     p_id = 1
    #     qt = 1
    #     ord = Order(product_id=p_id, quantity=qt)
    #     ord.save()
    return render(request, "watch.html")


def wallet(request):
    return render(request, "wallet.html")


def perfume(request):
    return render(request, "perfume.html")


def c(request):
    return render(request, "c.html")


def contact(request):
    return render(request, "contact.html")


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.item_set.all()
    else:
        items = []
        order = {'cartTotal': 0, 'getCartItem': 0}
    context = {'items': items, 'order': order}
    return render(request, "cart.html", context)


def buy(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.item_set.all()
    else:
        items = []
        order = {'cartTotal': 0, 'getCartItem': 0}
    context = {'items': items, 'order': order}
    return render(request, "BuyNow.html", context)


def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']
    print(productId, ' ', action)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    Item, created = Item.objects.get_or_create()
    return JsonResponse('Item was added', safe=False)
