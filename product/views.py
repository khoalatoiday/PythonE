from asyncio.windows_events import NULL
import itertools
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Book as Book_Model;
from .models import Shoes as Shoes_Model
from .models import Clothes as Clothes_Model
from .models import OrderedBook
from order import models as OrderModel
from django.core.paginator import Paginator
from django.db.models.functions import Concat
import array

# Create your views here.

def get_products_for_admin(request):
    books_list = Book_Model.objects.filter().order_by("id")
    return render(request, './Templates/admin_products.html',{"books_list": books_list})

def get_products_for_users(request, category=None, name =None):
    books_list = []
    clothes_list = []
    shoes_list = []
    allList = []

    if category == "all":
        books_list = list(Book_Model.objects.filter().order_by("id"))
        clothes_list = list(Clothes_Model.objects.filter().order_by("id"))
        shoes_list = list(Shoes_Model.objects.filter().order_by("id"))
        allList = list(itertools.chain(books_list, clothes_list, shoes_list))
        request.session['category'] = False

    if category == 'books':
        allList = list(Book_Model.objects.filter().order_by("id"))
    
    if category == 'shoes':
        allList = list(Clothes_Model.objects.filter().order_by("id"))

    if category == 'clothes':
        allList = list(Shoes_Model.objects.filter().order_by("id"))

    name = request.GET.get("name")

    if name and category == 'all':
        books_list = list(Book_Model.objects.filter(name=name).order_by("id"))
        clothes_list = list(Clothes_Model.objects.filter(name=name).order_by("id"))
        shoes_list = list(Shoes_Model.objects.filter(name=name).order_by("id"))
        allList = list(itertools.chain(books_list, clothes_list, shoes_list))
        request.session['category'] = category
    
    if name and category == 'books':
        allList = list(Book_Model.objects.filter(name=name).order_by("id"))

    if name and category == 'shoes':
        allList = list(Shoes_Model.objects.filter(name=name).order_by("id"))


    if name and category == 'clothes':
        allList = list(Clothes_Model.objects.filter(name=name).order_by("id"))

    p = Paginator(allList,1)

    page_number = request.GET.get('page')
    page_number = int(page_number)
    
    pages = array.array('i',[])
    for i in range(1, round(p.count / 1)+1):
        pages.append(i)
   
    context = {
        "page": p.get_page(page_number),
        "pages": pages,
        "page_number":page_number
    }
    return render(request, './Templates/home-page.html',context=context)

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
        if request.FILES['image']:
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

def get_details(request,id):
    choosenBook = Book_Model.objects.get(id = id)
    return render(request,"./Templates/product-page.html",{'choosenBook': choosenBook})

def search_products_by_category(request):
    if request.method == "POST":
        category = request.POST['category']
        request.session['category'] = category
        url = "/products/" + category + "?page=1"
        return redirect(url)
   

def search_products_by_key(request):
    if request.method == 'POST':
        name = request.POST['name']
        url = "/products/" + request.session['category'] + "?page=1&" + "name=" + name
        return redirect(url)
