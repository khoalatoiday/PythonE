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
from django.contrib.auth.decorators import login_required
# Create your views here.

def init(request):
    return redirect("/products/all?page=1")

@login_required(login_url="login/")
def get_products_for_admin(request):
    books_list = list(Book_Model.objects.filter().order_by("id"))
    clothes_list = list(Clothes_Model.objects.filter().order_by("id"))
    shoes_list = list(Shoes_Model.objects.filter().order_by("id"))
    allList = list(itertools.chain(books_list, clothes_list, shoes_list))
    return render(request, './Templates/admin_products.html',{"all_lists": allList})


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

@login_required(login_url="login/")
def getEditBookForm(request,id):
    category = request.GET.get("category")
    if category == 'book':
        product = Book_Model.objects.get(id = id)
    if category == 'clothes':
        product = Clothes_Model.objects.get(id=id)
    if category == "shoes":
        product = Shoes_Model.objects.get(id=id)
    

    return render(request, 'bookEditForm.html',{"product": product})
    
@login_required(login_url="login/")
def getAddBookForm(request):
    return render(request, 'bookEditForm.html')

@login_required(login_url="login/")
def addProduct(request):

    category = request.GET.get("category")
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        category = request.POST['category']
        image = request.FILES['image'] 

        if category == "book":
            book = Book_Model.objects.create(name=name, price=price, description=description, image=image)
            book.save()

        if category == 'shoes':
            shoes = Shoes_Model.objects.create(name=name, price=price, description=description, image=image)
            shoes.save()
        
        if category == 'clothes':
            clothes = Clothes_Model.objects.create(name=name, price=price, description=description, image=image)
            clothes.save()


        return redirect("/products/all?page=1")
    else:
        return render(request,"error.html")

@login_required(login_url="login/")
def editProduct(request,id):

    category = request.GET.get("category")

    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES.get('image', False)
        if category == "book":
            book = Book_Model.objects.get(id = id)
            book.name = name
            book.price = price
            book.description = description
            book.image = image and image or book.image
            book.save()
        if category == "shoes":
            shoes = Shoes_Model.objects.get(id=id)
            shoes.name = name
            shoes.price = price
            shoes.description = description
            shoes.image = image and image
            shoes.save()
        if category == "clothes":
            clothes = Clothes_Model.objects.get(id=id)
            clothes.name = name
            clothes.price = price
            clothes.description = description
            clothes.image = image and image
            clothes.save()

        
        return redirect("/products/all?page=1")
    else:
        return render(request,"error.html")

@login_required(login_url="login/")
def deleteProduct(request,id):
    category = request.GET.get("category")
    if category == "book":
        book = Book_Model.objects.get(id = id)
        book.delete()
    if category == "shoes":
        shoes = Shoes_Model.objects.get(id = id)
        shoes.delete()
    if category == "clothes":
        clothes = Clothes_Model.objects.get(id=id)
        clothes.delete()
         
    return redirect("/products/all?page=1")

@login_required(login_url="login/")
def get_details(request,id):
    category = request.GET.get("category")
    if category == "book":
        product = Book_Model.objects.get(id = id)
       
    if category == "shoes":
        product = Shoes_Model.objects.get(id = id)
       
    if category == "clothes":
        product = Clothes_Model.objects.get(id=id)
       
    return render(request,"./Templates/product-page.html",{'product': product})

@login_required(login_url="login/")
def search_products_by_category(request):
    if request.method == "POST":
        category = request.POST['category']
        request.session['category'] = category
        url = "/products/" + category + "?page=1"
        return redirect(url)
   
@login_required(login_url="login/")
def search_products_by_key(request):
    if request.method == 'POST':
        name = request.POST['name']
        url = "/products/" + request.session['category'] + "?page=1&" + "name=" + name
        return redirect(url)
