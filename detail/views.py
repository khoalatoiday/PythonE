from django.shortcuts import render
from product.models import Book as BookModel

# Create your views here.
def get_details(request,id):
    choosenBook = BookModel.objects.get(id = id)
    return render(request,"detail.html",{'choosenBook': choosenBook})