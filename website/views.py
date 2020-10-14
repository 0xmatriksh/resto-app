from django.shortcuts import render,redirect
from .models import Product,Order,OrderItem,ShippingAddress,Customer
import json,datetime
from django.http import JsonResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login ,logout
from .form import CreateUserForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
    else:
        order = {'total_items':0, 'total_price':0}
    items = Product.objects.all()
    drinks = Product.objects.filter(category='Drinks')
    indians = Product.objects.filter(category='Indian')
    chineses = Product.objects.filter(category='Chinese')
    context = {
        'items':items,
        'order': order,
        'drinks': drinks,
        'chineses': chineses,
        'indians': indians,
    }
    return  render(request,'website/index.html',context)

def menu(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
    else:
        order = {'total_items':0, 'total_price':0}
    drinks = Product.objects.filter(category='Drinks')
    indians = Product.objects.filter(category='Indian')
    chineses = Product.objects.filter(category='Chinese')
    context = {
        'order':order,
        'drinks':drinks,
        'chineses':chineses,
        'indians':indians,
    }
    return render(request,'website/menu.html',context)

def basket(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
        foods = order.orderitem_set.all()
    else:
        order = {'total_items':0,'total_price':0}
        foods = []
    context = {
        'order':order,
        'foods':foods,
    }
    return render(request, 'website/basket.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
        foods = order.orderitem_set.all()
    else:
        order = {'total_items': 0, 'total_price': 0}
        foods = []
    context = {
        'order': order,
        'foods': foods,
    }
    return render(request, 'website/checkout.html',context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            customer = Customer.objects.create(
                            user=user,
                            name=username
                            )
            Order.objects.create(
                            customer=customer,
                            complete=False

            )

            messages.success(request,'Account was created for ' + username)
            return redirect('login')
    context={
        'form':form
    }
    return render(request,'website/register.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('menu')
        else:
            messages.info(request, "Username or password is incorrect")
    context = {
    }
    return render(request, 'website/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='/website/login/')
def updateOrder(request):
    data = json.loads(request.body)
    productId,action = data['productId'],data['action']
    print(productId,action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)
    foods,created = OrderItem.objects.get_or_create(order=order,product=product)

    if action=='add':
        foods.quantity += 1
    elif action=='remove':
        foods.quantity -= 1
    foods.save()

    if foods.quantity <= 0:
        foods.delete()

    return JsonResponse("You are done.",safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    total = float(data['userform']['total'])
    customer = request.user.customer
    order,created = Order.objects.get_or_create(customer=customer,complete=False)
    order.transaction_id = transaction_id

    if order.total_price == total:
        order.complete = True

    shipping  = ShippingAddress.objects.create(
        customer=customer,
        order = order,
        address= data['shippingform']['address'],
        city=data['shippingform']['city'],
        state=data['shippingform']['state'],
        zipcode=data['shippingform']['zipcode'],
    )
    

    return JsonResponse("it was ordered",safe=False)

def contact(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
    else:
        order = {'total_items': 0, 'total_price': 0}
    context = {
        'order': order,
    }
    return render(request, 'website/contact.html',context)

def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
    else:
        order = {'total_items': 0, 'total_price': 0}
    context = {
        'order': order,
    }
    return render(request, 'website/about.html',context)

def gallery(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
    else:
        order = {'total_items': 0, 'total_price': 0}
    context = {
        'order': order,
    }
    return render(request, 'website/gallery.html',context)

def reservation(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
    else:
        order = {'total_items': 0, 'total_price': 0}
    context = {
        'order': order,
    }
    return render(request, 'website/reservation.html',context)

def staff(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
    else:
        order = {'total_items': 0, 'total_price': 0}
    context = {
        'order': order,
    }
    return render(request, 'website/staff.html',context)