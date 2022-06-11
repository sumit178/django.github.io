from django.urls import path
from . import views

urlpatterns=[
   
    path('about', views.aboutme, name='about'),
    path('spacehero', views.spacehero, name='spacehero'),
    path('', views.writeups, name='writeups'),
    path('feedback', views.feedback, name='feedback'),
    path('jersey', views.jersey, name='jersey'),


]