from django import forms
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=("portfolio","picture")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=("username","email","password")
        
