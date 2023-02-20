from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .forms import  ContactUsForm, RegisterForm, ShippingAddressUpdateForm


from .models import ContactUs, Item, CartItem, Wishlist, Order
from users.models import CustomUser

# Create your views here.

def home(request):
    products = Item.objects.all()
    context = {"products":products}

    return render(request, "shop/home.html", context)

def product_page(request, product_name, id):
    product = Item.objects.get(id=id)
    
    context = {"product":product}

    return render(request, "shop/product.html", context)

@login_required
def add_item_to_cart(request, id):
    user = CustomUser.objects.filter(id=request.user.id).first()
    item = Item.objects.get(id=id)
    cart = CartItem()
    cart.user = user
    cart.item = item
    cart.save()
    messages.success(request, f"{item.name} added to cart!")
    return redirect("shop_home")


@login_required
def cart(request):
    user = CustomUser.objects.get(id=request.user.id)
    items = CartItem.objects.filter(user = user)
    count = items.count()
    total = sum([product.item.price for product in items])

    context = {"products":items, "count":count, "total_price":total, "user":user}

    return render(request, 'shop/cart.html', context)

@login_required
def delete_item_cart(request, id, product_name):
    item = CartItem.objects.get(id=id)
    item.delete()

    messages.success(request, f"{product_name} was removed from cart successfully!")
    return redirect("shop_cart")


@login_required
def checkout(request):
    user = CustomUser.objects.get(id=request.user.id)
    items = CartItem.objects.filter(user = user)
    count = items.count()
    total = sum([product.item.price for product in items])

    context = {"products":items, "count":count, "total_price":total, "user":user}

    return render(request, "shop/checkout.html", context)

def setting_order(request):
    user = CustomUser.objects.get(id=request.user.id)
    items = CartItem.objects.filter(user = user)
    for item in items:
        order = Order.objects.create(user=user, item=item)
        order.product = Item.objects.get(id=item.item.id)
        if order.product.quantity > 0:
            order.save()
            order.product.quantity -= 1
            order.product.save()
            item.delete()
            messages.success(request, f"Your order of {order.product.name} has been confirmed!")
        else:
            messages.warning(request, f"{item} is out of stock")
    return redirect("shop_home")

def orders(request):
    user = CustomUser.objects.get(id=request.user.id)
    orders = Order.objects.filter(user=user)



    context = {"orders":orders}
    return render(request, "shop/orders.html", context)



@login_required
def wishlist(request):

    
    user = CustomUser.objects.get(id=request.user.id)
    items = Wishlist.objects.filter(user = user)


    context = {"products":items}
    return render(request, "shop/wishlist.html", context)

@login_required
def add_to_wishlist(request, product_id):
    user = CustomUser.objects.get(id=request.user.id)
    item = Item.objects.get(id = product_id)
    product = Wishlist.objects.create(user=user, item=item)
    product.save()
    messages.success(request, f"{item} added to wishlist successfully!")

    return redirect("shop_product", product_name=item.name, id=product_id)

@login_required
def delete_item_wishlist(request, product_id):
    product = Item.objects.get(id = product_id)
    item_in_wishlist = Wishlist.objects.filter(item =product).first()

    messages.success(request, f"{item_in_wishlist.item.name} was removed from your wishlist successfully!")
    item_in_wishlist.delete()
    return redirect("shop_wishlist")


# def FAQ(request):
#     return render(request, "shop/FAQ.html")


@login_required
def contact_us(request):
    
    user = CustomUser.objects.get(id=request.user.id)
    if request.method == "POST":
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            contact =  form.save(commit=False)
            contact.email = request.user.email
            contact.user = user
            contact.message = form.cleaned_data['messageForm']
            contact.subject = form.cleaned_data['subjectForm']
            # send_mail(
            #     f"Plinkershop | {form.cleaned_data['subjectForm']}",
            #     f"From {request.user.email} {form.cleaned_data['messageForm']}",
            #     f'{request.user.email}',
            #     ["karaymehzaid@gmail.com"],
            #     fail_silently=False,
            # )
            form.save()

            messages.success(request, f"Message sent successfully using {request.user.email}")
            return redirect("shop_home")
    else:
        form = ContactUsForm()
    
    context = {"form":form}




    return render(request, "shop/contact.html", context)



@login_required
def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    if request.method == "POST":
        form = ShippingAddressUpdateForm(request.POST, instance= user)
        if form.is_valid():
            form.save()
            messages.success(request, "Shipping address updated successfully!")
            return redirect("profile")
    else:
        form = ShippingAddressUpdateForm(instance=user)
    context = {"user":user, "form":form}
    return render(request, "users/profile.html", context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created! You are now able to log in ")
            return redirect("login")
    else:

        form = RegisterForm()

    context = {"form": form}

    return render(request, "users/register.html", context)