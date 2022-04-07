from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from customer.models import Customer, Address

@login_required(login_url="login/")
def getCustomerInfo(request):
    address = Address.objects.get(customer=request.user.customer)
    customer = request.user.customer
    context = {"customer":customer, "address": address}
    return render(request,"accountDetail.html", context)

def changeCustomerInfo(request):
    if request.method == "POST":
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        gender = request.POST['gender']
        street = request.POST['street']
        district = request.POST['district']
        city = request.POST['city']

        if email:
            user = User.objects.get(username=request.user.username)
            user.email = email
            user.save()
        if phoneNumber:
            customer = Customer.objects.get(id=request.user.customer.id)
            customer.phoneNumber = phoneNumber
            customer.save()
        if gender:
            customer = Customer.objects.get(id=request.user.customer.id)
            customer.gender = gender
            customer.save()
        if street and district and city:
            address = Address.objects.get(customer=request.user.customer)

            if address:
                address.street = street
                address.district = district
                address.city = city
                address.save()
            else:
                address = Address.objects.create(city, street,district,request.user.customer)
        return redirect("/books")
    else:
        return render(request,"error.html")