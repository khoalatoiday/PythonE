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
from argparse import Namespace
from math import prod
from pipes import Template
from django.contrib import admin
from django.urls import path,include
from product import views as product
from authen import views as authen
from django.conf.urls.static import static
from django.conf import settings
from customer import views as customer

from product import urls as productUrls

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', include('product.urls')),
   path('',include('customer.urls')),
   path('',include('authen.urls')),
   path('',include('order.urls'))
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)


admin.site.site_header="Khoa_Koha"

