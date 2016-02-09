#-*- coding: utf-8 -*-
from django.forms import ModelForm
from models import UserProfile, Order
from django import forms
from django.contrib.auth.models import User
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','first_name', 'email', 'password')
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Login'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
            'first_name'    : forms.TextInput(attrs = {'placeholder': 'Name'}),
            'password'    : forms.TextInput(attrs = {'placeholder': 'Password'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone',)
        widgets = {
            'phone' : forms.TextInput(attrs = {'placeholder': 'Phone'}),
        }
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'text' : forms.TextInput(attrs = {'placeholder': 'Район,Улица,Дата,Особые пожелания'}),
        }

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20,required=True)
    order_text = forms.CharField(max_length=200)
    widgets = {
        'order_text' : forms.TextInput(attrs = {'placeholder': 'Район,Улица,Дата,Особые пожелания'}),
        'phone' : forms.TextInput(attrs = {'placeholder': 'Телефон'}),
        'email' : forms.TextInput(attrs = {'placeholder': 'Email'}),
    }
