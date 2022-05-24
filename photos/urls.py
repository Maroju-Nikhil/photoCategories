from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add,name="add"),
    path('detail/<str:pk>',views.detail,name="detail"),
    path('',views.home,name="home"),
]