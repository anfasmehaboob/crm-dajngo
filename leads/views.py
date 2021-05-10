from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm,UserRegisterForm,CreateProduct
from .filter import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def register(request): 
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'user created for ' + user)
                return redirect('loginpage')


        context = {
            'form':form
        }
        return render(request,'accounts/register.html',context)



def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'username or password is incorrect')
        
        return render(request,'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('loginpage')


@login_required(login_url='loginpage')
def home(request):
    customers = Customer.objects.all();
    orders = Order.objects.all();

    total_orders = orders.count()

    total_delived = orders.filter(status='Delivered').count()

    total_pending = orders.filter(status='Pending').count()

    context = {
        'customers':customers,
        'orders':orders,
        'total_orders':total_orders,
        'total_delived':total_delived,
        'total_pending':total_pending


    }
    return render(request,'accounts/dashboard.html',context)

@login_required(login_url='loginpage')
def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})


def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    total_orders = orders.count()
    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs
    context = {
        'customer':customer,
        'orders':orders,
        'total_orders':total_orders,
        'myFilter':myFilter
    }

    return render(request,'accounts/customer.html',context)


def createProduct(request):
    form = CreateProduct()
    if request.method == 'POST':
        form = CreateProduct(request.POST)
        if form.is_valid:
            form.save()
            return redirect('products')
    context = {
        'from':form
    }
    return render(request,'accounts/product_create.html',context)



@login_required(login_url='loginpage')
def createOrder(request): 
    form = OrderForm()
    if request.method == 'POST':
        # print ('post data',request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {
        'form':form
    }
    return render (request,'accounts/create.html',context)



def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        # print ('post data',request.POST)
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {
        'form':form
    }
    return render (request,'accounts/create.html',context)



def Delete(request,pk_del):
    order = Order.objects.get(id=pk_del)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item':order
    }
    return render(request,'accounts/delete.html',context)