from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','description',"image")
    search_fields = ['name']
    list_filter = ('id','name','price','description')

admin.site.register(Book, BookAdmin)