from django.contrib import admin
from .models import CustomerUser, Item, CartItem, ContactUs, Wishlist, Order

from .forms import ContactUsForm
# Register your models here.


admin.site.register(CustomerUser)
admin.site.register(Item)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(ContactUs)
admin.site.register(Order)



     