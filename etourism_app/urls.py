from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='login.html'),
    path('add', views.login_signup, name='add'),
    path('checkuser', views.checklogin, name='checkuser'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('index1', views.index1, name='index1.html'),
    path('index', views.index, name='index.html'),
    path('about', views.about, name='about.html'),
    path('inquiry', views.inquiry_data, name='inquiry.html'),
    path('book', views.book, name='book.html'),
    path('book1/<int:id>', views.book1, name='book.html'),
    path('contact', views.contact, name='contact.html'),
    path('detail1', views.detail1, name='detail1.html'),
    path('detail1/<int:id>', views.detail1, name='detail1.html'),
    path('Package', views.Package, name='Package.html'),
    path('gallery', views.gallery, name='gallery.html'),
    path('logout', views.logout, name='logout'),
    path('dobookings', views.dobookings, name='dobookings'),
]
