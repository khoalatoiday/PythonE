from django.contrib import admin

# Register your models here.
from .models import Customer,Address,FullName

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','gender','user','fullName', "phoneNumber", "address","avatar")
    search_fields = ['user']
    list_filter = ('id','gender','user','fullName', "phoneNumber","address","avatar")

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','city','street','district')
    search_fields = ['name']
    list_filter = ('id','city','street','district')


class FullNameAdmin(admin.ModelAdmin):
    list_display = ('id','firstName','middleName','lastName')
    search_fields = ['firstName']
    list_filter = ('id','firstName','middleName','lastName')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(FullName, FullNameAdmin)