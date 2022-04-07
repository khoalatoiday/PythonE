from ast import Add
from http.client import responses
from tokenize import group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from customer.models import Customer as Customer
from customer.models import Address as Address
# Create your views here.
def getLoginForm(request):
    return render(request, 'login.html')

@login_required(login_url="login/")
def getChangePassWordForm(request):
    return render(request, 'changePassword.html',{"account": request.user}) 

def loginAction(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/books")
        else:
            return HttpResponseRedirect("/error")

def getRegisterForm(request):
    return render(request,"register.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        user = authenticate(username=username, password= password)
        if user and user.is_active:
            login(request,user)
            return HttpResponseRedirect("/books")
         
        user = User.objects.create_user(username,email,password)
        g = Group.objects.get(name='user')
        user.groups.add(g)
        Customer.objects.create(user=user).save()
        return HttpResponseRedirect("/books")

def logout_view(request):
    print(request)
    logout(request)
    return HttpResponseRedirect("/login")

def change_password(request):
    if request.method == "POST":
        username = request.POST['username']
        currentPassword = request.POST['currentPassword']
        newPassword = request.POST['newPassword']
        user = authenticate(request,username=username,password=currentPassword)
        if user is not None:
            u = User.objects.get(username=username)
            u.set_password(newPassword)
            u.save()
            return HttpResponseRedirect("/books")
        else:
            return HttpResponseRedirect("/error")
      
@login_required
def my_account(request, template_name="registration/my_account.html"):
    page_title = 'My Account'
    name = request.user.username
    return render_to_response(template_name, locals(),
        context_instance=RequestContext(request))
        