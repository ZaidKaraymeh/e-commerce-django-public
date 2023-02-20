from django.db import models
from django.contrib.auth.models import User
# Create your models here.



# class CustomerUser(User):
#     shippingAddress = models.TextField(null=True, max_length=500)


    
    

class Item(models.Model):
    name = models.CharField(null=True, max_length=150)
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    description = models.TextField(null=True, max_length=10000)
    icon = models.ImageField(null=True, upload_to="images", height_field=None, width_field=None, max_length=None)
    quantity = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.name 

class CartItem(models.Model):
    user = models.ForeignKey('users.CustomUser',null = True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True)
    def __str__(self):
        return str(self.item)

class Wishlist(models.Model):
    user = models.ForeignKey('users.CustomUser',null = True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item)

class ContactUs(models.Model):
    user = models.ForeignKey('users.CustomUser',null = True, on_delete=models.CASCADE)
    email = models.EmailField(null=True, max_length=300)
    subject = models.CharField(null=True, max_length=50)
    message = models.TextField(null=True, max_length=9000)
    def __str__(self):
        return str(self.email)


class Order(models.Model):
    user = models.ForeignKey('users.CustomUser',null = True, on_delete=models.CASCADE)
    item = models.ForeignKey(CartItem, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    product = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.product )

class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name