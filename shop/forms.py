from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ContactUs

from users.models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # Interacts with User model
        model = CustomUser
        # What fields to show and in which order
        fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ["username", "email"]



class ShippingAddressUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ["shippingAddress", 'country', 'city']

        # labels = {
        #     "shippingAddress": "",
        #     "country": "",
        #     "city": "",
        # }

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
    
