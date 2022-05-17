from django.contrib import admin
from .models import Cart,Shipment,Payment,Order
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('id','status','totalPrice','customer')
    search_fields = ['name']
    list_filter = ('id','status','totalPrice','customer')

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('id','type','extra_price')
    search_fields = ['name']
    list_filter =  ('id','type','extra_price')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','type','extra_price')
    search_fields = ['name']
    list_filter = ('id','type','extra_price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','orderDate','totalPrice','status','discount','cart','shipment','payment','customer')
    search_fields = ['name']
    list_filter = ('id','orderDate','totalPrice','status','discount','cart','shipment','payment','customer')

admin.site.register(Cart, CartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Shipment,ShipmentAdmin)
admin.site.register(Payment,PaymentAdmin)


