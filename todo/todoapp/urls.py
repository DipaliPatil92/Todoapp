from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.index),
    path('home',views.home),
    path('contact',views.contact),
    path('product',views.product),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('evenodd/<n>',views.evenodd),
    path('tloop',views.loop),
    path('about',views.about),
    path('create',views.create_task),
    path('all',views.cdashboard),
    path('ltoh',views.lowtohigh),
    path('htol',views.hightolow),
    path('dform',views.showform),
    path('modelform',views.showmodelform),
    path('cview',views.MyView.as_view()),
    path('register',views.register),
]

