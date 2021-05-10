from django.forms import ModelForm
from .models import Order,Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateProduct(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']