from http.client import responses
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout
# Create your views here.
def getLoginForm(request):
    return render(request, 'login.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect("/books")
        else:
            render(request,"error.html")

def getRegisterForm(request):
    return render(request,"register.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponseRedirect("/books")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")
      
            
        