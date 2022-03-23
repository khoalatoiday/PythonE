from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .models import Book as Book_Model
# Create your views here.
def get_products(request):
    books_list = Book_Model.objects.filter().order_by("id")
    return render(request, 'home.html',{"books_list": books_list});

def get_products_for_users(request):
    books_list = Book_Model.objects.filter().order_by("id")
    return render(request, 'products.html',{"books_list": books_list});

def getEditBookForm(request,id):
    choosenBook = Book_Model.objects.get(id = id)
    return render(request, 'bookEditForm.html',{"choosenBook": choosenBook})
    

def getAddBookForm(request):
    return render(request, 'bookEditForm.html')


def addBook(request):
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']

        book = Book_Model.objects.create(name=name, price=price, description=description, image=image)

        book.save()
        return redirect("/books")
    else:
        return render(request,"error.html")

def editBook(request,id):
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']
        
        book = Book_Model.objects.get(id = id)
        if image:
            book.image = image
        if name:
            book.name = name
        if price:
            book.price = price
        if description:
            book.description = description

        book.save()
        
        return redirect("/books")
    else:
        return render(request,"error.html")

def deleteBook(request,id): 
    book = Book_Model.objects.get(id = id)
    book.delete()
    return redirect("/books")