from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("basee",views.basee,name='home'),
    path("about1",views.about1,name='home'),
    path("front",views.front,name='home'),
]                                               
