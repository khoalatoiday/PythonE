from ast import Add
from asyncio.windows_events import NULL
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views import View

from customer.models import Customer, Address, FullName
from customer.forms import  AccountDetailsForm

@login_required(login_url="login/")
def getCustomerInfo(request):
    address = Address.objects.get(customer=request.user.customer)
    customer = request.user.customer
    if address:
        context = {"customer":customer, "address": address}
    else:
        context = {"customer":customer, "address": address}
    return render(request,"./Templates/accountDetail.html", context)

class AccountDetailView(View):
    def get(self, request):


        customer = request.user.customer
        print(customer.avatar)

        initial_obj = {
            "firstName": customer.fullName.firstName if customer.fullName != None else "",
            "userName": request.user.username,
            "lastName": customer.fullName.lastName if customer.fullName != None else "",
            "street": customer.address.street if customer.address != None else "",
            "city": customer.address.city if customer.address != None else "",
            "district":customer.address.district if customer.address != None else "",
            "email": request.user.email,
            "phoneNumber": request.user.customer.phoneNumber,
        }

        form = AccountDetailsForm(initial=initial_obj)
        context = {
            'form': form
        }
        return render(self.request,'./Templates/accountDetail.html',context=context)

    def post(self,request):
        form = AccountDetailsForm(request.POST)
        customer = Customer.objects.get(id=request.user.customer.id)
       
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            userName= form.cleaned_data['userName']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            district = form.cleaned_data['district']
            email = form.cleaned_data['email']
            phoneNumber = form.cleaned_data['phoneNumber']

            if firstName or lastName:
                if customer.fullName == None:
                    fullName = FullName.objects.create(firstName=firstName, lastName=lastName)
                else:
                    fullName= FullName.objects.get(id=customer.fullName.id)
                    if firstName != None:
                        fullName.firstName = firstName
                    if lastName != None:
                        fullName.lastName = lastName
                customer.fullName = fullName
                fullName.save()
            if street or city or district:
               
                if customer.address == None:
                    address = Address.objects.create(street=street, city=city, district=district)
                else:
                    address = Address.objects.get(id=customer.address.id)
                    if street != None:
                        address.street = street
                    if city != None:
                        address.city = city
                    if district != None:
                        address.district = district
                address.save()
                customer.address = address
            if phoneNumber:
                customer.phoneNumber = phoneNumber
            customer.save()
        return redirect("/userinfo")
