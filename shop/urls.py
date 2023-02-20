from .views import home, product_page, add_item_to_cart, cart, delete_item_cart, checkout, wishlist, add_to_wishlist, delete_item_wishlist, contact_us, setting_order, orders
from django.urls import path

urlpatterns = [
    path("", home, name="shop_home"),
    path("cart/", cart, name="shop_cart"),
    path("contactus/", contact_us, name="shop_contact_us"),

    path("<str:product_name>/<int:id>", product_page, name="shop_product"),

    path("<int:id>", add_item_to_cart, name="shop_add_item_cart"),

    path("cart/<int:id>/<str:product_name>/delete", delete_item_cart, name="shop_delete_item_cart"),

    path("checkout/", checkout, name="shop_cart_checkout"),
    path("wishlist/", wishlist, name="shop_wishlist"),
    path("wishlist/add/item/<int:product_id>/", add_to_wishlist, name="shop_add_to_wishlist"),
    path("wishlist/delete/<int:product_id>/", delete_item_wishlist, name="shop_delete_item_wishlist"),
    path("checking-out/order/now", setting_order, name="shop_setting_order"),
    path("orders/", orders, name="shop_orders")
]