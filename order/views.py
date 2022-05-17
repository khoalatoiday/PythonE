from importlib.resources import contents
from itertools import product
import json
from multiprocessing import context
from venv import create
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
import customer
from customer.models import Customer
from .models import *
from product import models as ProductModel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login/")
def renderCart(request):
  # exception

  cart_qs = Cart.objects.filter(customer=request.user.customer, status=False)
  shipments = Shipment.objects.all()
  payments = Payment.objects.all()

  if cart_qs.exists():
    ordered_books = ProductModel.OrderedBook.objects.filter(cart=cart_qs[0])

    
    context = {
      "ordered_books": ordered_books,
      "cart": cart_qs[0],
      "payments":payments,
      "shipments": shipments
    }
    return render(request, "./Templates/cart.html",
    context=context
    )
  else:
    return render(request, "./Templates/cart.html")


@login_required(login_url="login/")
def renderCheckoutOrder(request):
  customer = request.user.customer
  cart = Cart.objects.get(customer=customer,status=False)
  ordered_books = ProductModel.OrderedBook.objects.filter(cart=cart)
  
  if request.method == "POST":
    shipment_id = request.POST['shipment']
    payment_id = request.POST['payment']
    shipment = Shipment.objects.get(id=shipment_id)
    payment = Payment.objects.get(id=payment_id)
    totalPrice = cart.totalPrice + shipment.extra_price + payment.extra_price
    request.session['shipment']= shipment_id
    request.session['payment'] = payment_id
    request.session['totalPrice']= totalPrice

  context={
    "user": request.user,
    "customer": customer,
    "ordered_books": ordered_books,
    "cart": cart,
    "totalPrice": totalPrice,
    "shipment": shipment,
    "payment": payment
  }
  return render(request,"./Templates/checkout-page.html", context=context)

@login_required(login_url="login/")
def renderCheckOut(request):
  if request.user.is_authenticated:
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer=customer)
    orderItems = ProductModel.OrderedBook.get(cart=cart)
  else: 
    orderItems = []

  context = {"orderItems", orderItems}
  return render(request, "checkout.html",context=context)


@login_required(login_url="login/")
def addToCart(request, id):
  category = request.GET.get("category")
  book = None
  shoes = None
  clothes = None

  if category == "book":
    book = get_object_or_404(ProductModel.Book, id=id)

  if category == "shoes":
    shoes = get_object_or_404(ProductModel.Shoes, id=id)

  if category == "clothes":
    clothes = get_object_or_404(ProductModel.Clothes, id=id)

  if book:
    totalPrice = book.price
  if clothes:
    totalPrice = clothes.price
  if shoes:
    totalPrice = shoes.price

  cart_qs = Cart.objects.filter(customer=request.user.customer, status=False)
  if cart_qs.exists():
    cart = cart_qs[0]
    orderedBook_qs = ProductModel.OrderedBook.objects.filter(cart=cart,book=book,shoes=shoes,clothes=clothes)
    if orderedBook_qs.exists():
      orderedBook = orderedBook_qs[0]
      orderedBook.quantity += 1
      orderedBook.totalPrice += totalPrice
      cart.totalPrice += totalPrice
      cart.save()
      orderedBook.save()
      messages.info(request, "Sản phẩm đã được cập nhật vào giỏ hàng!")
    else:
      orderedBook = ProductModel.OrderedBook.objects.create(cart=cart,book=book,shoes=shoes,clothes=clothes, totalPrice=totalPrice)
      cart.totalPrice += totalPrice
      cart.save()
      orderedBook.save()
      request.session['count'] += 1
      messages.info(request, "Sản phẩm đã được thêm vào giỏ hàng!")
  else:
    customer = Customer.objects.get(id=request.user.customer.id)
    cart = Cart.objects.create(customer=customer) 
    orderedBook = ProductModel.OrderedBook.objects.create(book=book,shoes=shoes,clothes=clothes,cart=cart,totalPrice=totalPrice)
    cart.totalPrice += (book.price or clothes.price or shoes.price)
    cart.save()
    orderedBook.save()
    request.session['count'] = 1
    messages.info(request, "Sản phẩm đã được thêm vào giỏ hàng!")
  return redirect('/cart')

@login_required(login_url="login/")
def remove_item_from_cart(request,id):
  category = request.GET.get("category")

  book = None
  shoes = None
  clothes = None
  if category == "book":
    book = get_object_or_404(ProductModel.Book, id=id)
  if category == "shoes":
    shoes = get_object_or_404(ProductModel.Shoes, id=id)
  if category == "clothes":
    clothes = get_object_or_404(ProductModel.Clothes, id =id)
  cart_qs = Cart.objects.filter(customer=request.user.customer, status=False)
  if cart_qs.exists():
    cart = cart_qs[0]
    orderedBook_qs = ProductModel.OrderedBook.objects.filter(cart=cart,book=book, clothes=clothes, shoes=shoes)
    if orderedBook_qs.exists:
      orderedBook = orderedBook_qs[0]
      cart.totalPrice -= (orderedBook.totalPrice)
      ProductModel.OrderedBook.objects.filter(id=orderedBook.id).delete()
      cart.save()
      messages.info(request, "Sản phẩm đã được xóa khỏi giỏ hàng!")
      request.session["count"] -= 1
  return redirect('/cart')  

@login_required(login_url="login/")
def incre_single_item(request,id):
  category = request.GET.get("category")

  book = None
  shoes = None
  clothes = None
  totalPrice = 0

  if category == "book":
    book = get_object_or_404(ProductModel.Book, id=id)
    totalPrice = book.price
  if category == "shoes":
    shoes = get_object_or_404(ProductModel.Shoes, id=id)
    totalPrice = shoes.price
  if category == "clothes":
    clothes = get_object_or_404(ProductModel.Clothes, id =id)
    totalPrice = clothes.price
  cart_qs = Cart.objects.filter(customer=request.user.customer, status=False)
  if cart_qs.exists():
    cart = cart_qs[0]
    orderedBook_qs = ProductModel.OrderedBook.objects.filter(cart=cart,book=book,clothes=clothes,shoes=shoes)
    if orderedBook_qs.exists:
      orderedBook = orderedBook_qs[0]
      orderedBook.quantity += 1
      orderedBook.totalPrice +=totalPrice 
      cart.totalPrice += totalPrice
      orderedBook.save()
      cart.save()
      messages.info(request, "Sản phẩm đã được cập nhật trong giỏ hàng!")
  return redirect("/cart")

@login_required(login_url="login/")
def decre_single_item(request,id):
  category = request.GET.get("category")

  book = None
  shoes = None
  clothes = None
  totalPrice = 0

  if category == "book":
    book = get_object_or_404(ProductModel.Book, id=id)
    totalPrice = book.price
  if category == "shoes":
    shoes = get_object_or_404(ProductModel.Shoes, id=id)
    totalPrice = shoes.price
  if category == "clothes":
    clothes = get_object_or_404(ProductModel.Clothes, id =id)
    totalPrice = clothes.price
  cart_qs = Cart.objects.filter(customer=request.user.customer, status=False)
  print(book)
  if cart_qs.exists():
    cart = cart_qs[0]
    print(clothes," ",shoes," ", cart)
    orderedBook_qs = ProductModel.OrderedBook.objects.filter(cart=cart,book=book,clothes=clothes,shoes=shoes)
    print(orderedBook_qs)
    if orderedBook_qs.exists:
      orderedBook = orderedBook_qs[0]
      orderedBook.quantity -= 1
      orderedBook.totalPrice -=totalPrice 
      cart.totalPrice -= totalPrice
      orderedBook.save()
      cart.save()
      messages.info(request, "Sản phẩm đã được cập nhật trong giỏ hàng!")
      if orderedBook.quantity == 0:
        ProductModel.OrderedBook.objects.filter(id=orderedBook.id).delete()
        request.session['count'] -= 1
  return redirect("/cart")

@login_required(login_url="login/")
def create_order(request):
  if request.method == 'POST':
    address = request.POST['address']
    cart = Cart.objects.get(customer=request.user.customer,status=False)
    cart.status = True
    shipment = Shipment.objects.get(id=request.session.get("shipment"))
    payment = Payment.objects.get(id=request.session.get("payment"))
    order = Order.objects.create(customer=request.user.customer,cart=cart,shipment=shipment,
    payment=payment,address=address, totalPrice=request.session.get("totalPrice"))
    cart.save()
    order.save()
    del request.session['payment']
    del request.session['shipment']
    del request.session['totalPrice']
    del request.session['count']
  return redirect("/products/all?page=1")

@login_required(login_url="login/")
def renderOrder(request):
  orders = Order.objects.filter(customer=request.user.customer)
  context = {
    "orders": orders
  }

  return render(request,"./Templates/orders.html",context=context)

@login_required(login_url="login/")
def finishOrder(request):
  id = request.GET.get("id")
  order = get_object_or_404(Order,id=id) 
  order.status = True
  order.save()
  return redirect("/order-admin") 

@login_required(login_url="login/")
def renderOrderAdmin(request):
  orders = Order.objects.all()
  context = {
    "orders": orders
  }

  return render(request,"./Templates/orders-admin.html",context=context)



