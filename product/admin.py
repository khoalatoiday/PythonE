from django.contrib import admin
from .models import Book, OrderedBook
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','description',"image")
    search_fields = ['name']
    list_filter = ('id','name','price','description','image')

class OrderedBookAdmin(admin.ModelAdmin):
    list_display = ('id','quantity','book','totalPrice','cart')
    search_fields = ['id']
    list_filter = ('id','quantity','book','totalPrice','cart')

admin.site.register(Book, BookAdmin)
admin.site.register(OrderedBook,OrderedBookAdmin)