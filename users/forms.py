from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['style'] = 'height:40px;'
        self.fields['password'].widget.attrs['style'] = 'height:40px;'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        

class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=155, 
        widget=forms.TextInput(
            attrs={
                "style":"height:40px;",
                "class":"form-control"
            }
            ))
    class Meta:
        model = CustomUser
        fields = ['full_name',  "email", "phone_number"]
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs['style'] = 'height:40px;'
        self.fields['phone_number'].widget.attrs['style'] = 'height:40px;'
        self.fields['email'].widget.attrs['style'] = 'height:40px;'
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

class RegisterForm(UserCreationForm):
    class Meta:
        # Interacts with User model
        model = CustomUser
        # What fields to show and in which order
        fields = ["first_name", "last_name", "email",
                  "password1", "password2", 
                  "birth_date", "phone_number"]
        '''labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "phone_number": "Phone Number",
            "password1": "Password",
            "password2": "Confirm Password",
            "birth_date": "Birth Date",
        }'''
        widgets = {
            'birth_date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['first_name'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['last_name'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['email'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['password1'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['password2'].widget.attrs['style'] = 'width:100%; height:40px;'
        self.fields['birth_date'].widget.attrs['style'] = 'height:40px;'
        self.fields['phone_number'].widget.attrs['style'] = 'width:100%; height:40px;'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['last_name'].widget.attrs['class'] = 'form-control'
        # self.fields['email'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        # self.fields['birth_date'].widget.attrs['class'] = 'form-control'
        # self.fields['phone_number'].widget.attrs['class'] = 'form-control'

"""
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
"""
