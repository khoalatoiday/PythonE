from django.contrib import admin
from .models import Book, OrderedBook, Shoes,Clothes
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','description',"image","category")
    search_fields = ['name']
    list_filter = ('id','name','price','description','image',"category")

class ShoesAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','description',"image","category")
    search_fields = ['name']
    list_filter = ('id','name','price','description','image',"category")

class ClothesAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','description',"image","category")
    search_fields = ['name']
    list_filter = ('id','name','price','description','image',"category")

class OrderedBookAdmin(admin.ModelAdmin):
    list_display = ('id','quantity','book','totalPrice','cart', "shoes","clothes")
    search_fields = ['id']
    list_filter = ('id','quantity','book','totalPrice','cart', "shoes","clothes")

admin.site.register(Book, BookAdmin)
admin.site.register(OrderedBook,OrderedBookAdmin)
admin.site.register(Shoes, ShoesAdmin)
admin.site.register(Clothes, ClothesAdmin)