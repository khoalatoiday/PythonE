"""eecommerece URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from math import prod
from pipes import Template
from django.contrib import admin
from django.urls import path
from home import views as home
from product import views as product
from detail import views as detail
from authen import views as authen

from django.conf.urls.static import static
from django.conf import settings


from customer import views as customer

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",home.get_home),
    path("admin/books/", product.get_products),
    path("books", product.get_products_for_users),
    path("detail/<int:id>/", detail.get_details),
    path("bookForm",product.getAddBookForm),
    path("add",product.addBook),
    path("bookForm/<int:id>/",product.getEditBookForm),
    path("edit/<int:id>/",product.editBook),
    path("login", authen.getLoginForm),
    path("register", authen.getRegisterForm),
    path("activeRegister",authen.register),
    path("activeLogin",authen.loginAction),
    path("logout",authen.logout_view),
    path("delete/<int:id>/",product.deleteBook),
    path("changePassword",authen.getChangePassWordForm),
    path("changePasswordAction", authen.change_password),
    path("userinfo",customer.getCustomerInfo),
    path("changeUserInfo", customer.changeCustomerInfo),
   
   path("error", home.get_error)
   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header="Khoa_Koha"

