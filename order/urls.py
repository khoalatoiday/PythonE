from django.urls import include, path
from .views import *

app_name = "order"

urlpatterns = [
    path("addToCart/<int:id>",addToCart),
    path("cart", renderCart, name="cart"),
    path("check-out",renderCheckoutOrder),
    path("removeFromCart/<int:id>",remove_item_from_cart),
    path("increSingleItem/<int:id>",incre_single_item),
    path("decreSingleItem/<int:id>",decre_single_item),
    path("create-order", create_order),
   
]
