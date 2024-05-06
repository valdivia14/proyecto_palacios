"""
URL configuration for empleados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view(),name='prueba'),
    path('lista-prueba/', views.ListarPrueba.as_view(),name='pruebalista'),
    path('lista/', views.PruebaListView.as_view(),name='listarprueba'),
    path('add/', views.PruebaCreateView.as_view(),name='createviewprueba'),
    ]
