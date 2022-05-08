from argparse import Namespace
from django.urls import path
from .views import *

app_name="product"

urlpatterns = [
    path("admin/books/", get_products_for_admin),
    path('', get_products_for_users),
    path("details/<int:id>/", get_details, name='details'),
    path("bookForm",getAddBookForm),
    path("add",addBook),
    path("bookForm/<int:id>/",getEditBookForm),
    path("edit/<int:id>/",editBook),
]
