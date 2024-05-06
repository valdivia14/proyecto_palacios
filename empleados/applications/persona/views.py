from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Empleado
from django.views.generic.edit import CreateView

# Create your views here.

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/add.html'
    #fields = ['first_name','last_name', 'job']
    fields = ('__all__')
class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 4
    ordering = 'first_name'
    model = Empleado
    context_object_name = 'lista'
    # Para activar esto necesitamos una url.


class SuccessView(TemplateView):
    template_name = "persona/success.html"


# Listar por área
class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        # Recojo variable de la url
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(departamento__shor_name=area)
        return lista


class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'lista'

    def get_queryset(self):
        print('*****************************************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        print('LISTA RESULTADO: ', lista)
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.Habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'
    context_object_name = 'empleado'  # Cambiar el nombre del contexto (lista) a 'empleado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context