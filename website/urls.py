from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home,name='home'),
    path('menu/',views.menu,name='menu'),
    path('basket/',views.basket,name='basket'),
    path('checkout/',views.checkout,name='checkout'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name='contact'),
    path('reservation/',views.reservation,name='reservation'),
    path('staff/',views.staff,name='staff'),
    path('gallery/',views.gallery,name='gallery'),
]