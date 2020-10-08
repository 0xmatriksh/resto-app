from django.shortcuts import render
from .models import Product,Order,OrderItem,ShippingAddress
import json,datetime
from django.http import JsonResponse

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

def login(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
    else:
        order = {'total_items':0,'total_price':0}
    context = {
        'order': order,
    }
    return render(request, 'website/login.html',context)

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