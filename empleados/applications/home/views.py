from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
# Create your views here.

from .models import Prueba

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset = ['0','10','20','30']

class ListarPrueba(ListView):
    template_name= "home/listar_prueba.html"
    model = Prueba
    context_object_name = "lista"

class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    fields = ['titulo','subtitulo','cantidad']