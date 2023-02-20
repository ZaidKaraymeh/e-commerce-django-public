from payments.models import Topup
from .forms import RegisterForm, LoginForm, ProfileForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import json
# Create your views here.
from django.conf import settings
from users.models import CustomUser
from core.models import Balance, Transaction

def register(request):
    user_type = request.GET.get('user_type')
    print(user_type)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            if user_type == "ADM":
                user.user_type = "ADM"
            else:
                messages.success(
                    request, f"Your account has been created! You are now able to log in ")
            user.save()
            if user_type == "ADM":
                messages.success(request, f"Employee registered successfully!")
                return redirect("list_employees")
            else:
                return redirect("login")
        else:
            if user_type == "ADM":
                return redirect("list_employees")
            else:
                return redirect("register")

    else:
        form = RegisterForm()

    context = {"form": form}

    return render(request, "users/register.html", context)

# for AJAX login validation
# def login_ajax(request):
#     form = LoginForm(request.POST or None)
#     if form.is_valid():
#         # You could actually save through AJAX and return a success code here
#         form.save()
#         return HttpResponse(json.dumps({"success": True}))
#     return HttpResponse(json.dumps({'success': False}))


def profile(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    balance, created = Balance.objects.get_or_create(user=user)
    transactions = Transaction.objects.filter(user=user).order_by('-created_at')[:4]
    topups = Topup.objects.filter(user=user).order_by('-created_at')[:4]
    context = {
        "user":user,
        "balance":balance,
        "transactions":transactions,
        "topups":topups,
    }

    return render(request, "users/profile.html", context)

def edit_profile(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    balance, created = Balance.objects.get_or_create(user=user)
    transactions = Transaction.objects.filter(user=user).order_by('-created_at')[:4]
    if request.method == "POST":
        profile_form = ProfileForm(
            request.POST, 
            instance=user, 
            initial={"full_name": f"{user.first_name} {user.last_name}"}
            )
        if profile_form.is_valid():
            obj = profile_form.save(commit=False)
            res = [i for j in profile_form.cleaned_data['full_name'].split() for i in (j, ' ')][:-1]
            while(" " in res):
                res.remove(" ")
            obj.first_name = res[0]
            res = res[1:]
            obj.last_name = " ".join([str(item) for item in res])
            obj.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('profile', user_id)
    else:
        profile_form = ProfileForm(
            instance=user, 
            initial={"full_name": f"{user.first_name} {user.last_name}"}
            )

    context = {
        "user":user,
        "balance":balance,
        "transactions":transactions,
        "profile_form": profile_form
    }


    return render(request, "users/edit_profile.html", context)


# delete admin
def delete_employee(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.delete()
    messages.success(request, "Employee Deleted Successfully")
    return redirect("list_employees")