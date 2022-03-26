# from tkinter import Widget
# from turtle import width
# from django.db import models
from django import forms
from django.contrib.auth.models import User
from auth_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password') 
        #for unique value combinations/togather

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')