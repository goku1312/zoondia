from django.urls import path
from app import views
urlpatterns = [
   
    path('',views.register),
    path("register",views.register),
    path("login",views.login),
    path("home",views.home),
]