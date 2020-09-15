from django.shortcuts import render

# Create your views here.
def home(request):
    return  render(request,'website/index.html')

def menu(request):
    return render(request,'website/menu.html')

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