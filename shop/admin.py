from django.contrib import admin
from .models import  Item, CartItem, ContactUs, Wishlist, Order, Country
from .forms import ContactUsForm
# Register your models here.


admin.site.register(Item)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(ContactUs)
admin.site.register(Order)
admin.site.register(Country)



     