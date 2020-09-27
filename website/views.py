from django.shortcuts import render
from .models import Product,Order,OrderItem

# Create your views here.
def home(request):
    foods = Product.objects.all()
    drinks = Product.objects.filter(category='Drinks')
    indians = Product.objects.filter(category='Indian')
    chineses = Product.objects.filter(category='Chinese')
    context = {
        'foods':foods,
        'drinks':drinks,
        'chineses':chineses,
        'indians':indians,
    }
    return  render(request,'website/index.html',context)

def menu(request):
    drinks = Product.objects.filter(category='Drinks')
    indians = Product.objects.filter(category='Indian')
    chineses = Product.objects.filter(category='Chinese')
    context = {
        'drinks':drinks,
        'chineses':chineses,
        'indians':indians,
    }
    return render(request,'website/menu.html',context)

def basket(request):
    customer = request.user.customer
    order = Order.objects.get(customer=customer)
    foods = OrderItem.objects.all()
    context = {
        'order':order,
        'foods':foods,
    }
    return render(request, 'website/basket.html',context)

def checkout(request):
    customer = request.user.customer
    order = Order.objects.get(customer=customer)
    foods = OrderItem.objects.all()
    context = {
        'order': order,
        'foods': foods,
    }
    return render(request, 'website/checkout.html',context)

def login(request):
    return render(request, 'website/login.html')

def contact(request):
    return render(request, 'website/contact.html')

def about(request):
    return render(request, 'website/about.html')

def gallery(request):
    return render(request, 'website/gallery.html')

def reservation(request):
    return render(request, 'website/reservation.html')

def staff(request):
    return render(request, 'website/staff.html')