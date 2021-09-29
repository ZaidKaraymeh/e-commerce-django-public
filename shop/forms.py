from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerUser, ContactUs

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # Interacts with User model
        model = CustomerUser
        # What fields to show and in which order
        fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomerUser
        fields = ["username", "email"]



class ShippingAddressUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomerUser
        fields = ["shippingAddress"]

        labels = {
            "shippingAddress": ""
        }

class ContactUsForm(forms.ModelForm):
    subjectForm = forms.CharField(
        max_length=300,
        widget=forms.Textarea(attrs={'style':'max-height: 32px;'}),
        required=True,
        label="")

    messageForm = forms.CharField(
        max_length=9000,
        widget=forms.Textarea(attrs={'class':'contactUsStyling' }),
        required=True,
        label="")
    class Meta:
        model = ContactUs
        fields = ["subjectForm", "messageForm"]

        labels = {
            "subjectForm": "",
            "messageForm": "",
        }
    
