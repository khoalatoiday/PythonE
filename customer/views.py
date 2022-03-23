from multiprocessing import context
from django.shortcuts import render
from .models import *
# Create your views here.

def cart(request):
    # # if request.user.is_authenticated:
    # #     customer = request.user.customer
    # #     order, created = Order.objects.get_or_create(customer=customer)
    # #     items = order.orderitem_set.all()
    # # else:
    # #     items = []

    # context={'items':items}
    return render(request,"cart.html")