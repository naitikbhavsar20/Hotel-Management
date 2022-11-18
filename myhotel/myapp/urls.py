from django import views
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('booking', views.booking, name="booking"),
    path('index', views.index,name="index"),
    path('index1', views.index1,name="index1"),
    path('', views.login,name="login"),
    path('auth', views.auth,name="auth"),
    path('add', views.add,name="add"),
    path('addrecord', views.addrecord, name='addrecord'),
]