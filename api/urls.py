from django.urls import path
from . import views

urlpatterns = [
   path('',views.index, name='index') ,
   path('home/',views.home, name='home') ,
   path('form/',views.form, name='form') ,   
   path('home/about/',views.about, name='about') ,
   path('generatedpassword/',views.password, name='password') ,
]  