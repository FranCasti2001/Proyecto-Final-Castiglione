from django.shortcuts import render
from Aplicacion.models import Equipo, Paleta
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Aplicacion.forms import BuscarEquipo, BuscarPaleta

def vista(request):
    return render(request, 'index.html')


class ListaEquipos(ListView):
    model = Equipo
    template_name = 'CBV/lista_equipos.html'

    
class CrearEquipo(CreateView):
    model = Equipo
    template_name = 'CBV/crear_equipo.html'
    success_url = reverse_lazy('Aplicacion:lista_equipos')
    fields = ['nombre', 'apodo', 'dt', 'anio_de_creacion', 'escudo']

    
class EditarEquipo(LoginRequiredMixin, UpdateView):
    model = Equipo
    template_name = 'CBV/modificar_equipo.html'
    success_url = reverse_lazy('Aplicacion:lista_equipos')
    fields = ['nombre', 'apodo', 'dt', 'anio_de_creacion', 'escudo']

    
class EliminarEquipo(LoginRequiredMixin, DeleteView):
    model = Equipo
    template_name = 'CBV/eliminar_equipo.html'
    success_url = reverse_lazy('Aplicacion:lista_equipos')

    
class MostrarEquipo(DetailView):
    model = Equipo
    template_name = 'CBV/mostrar_equipo.html'
 
    
def about(request):
    return render(request, 'about.html')


class PaletaListView(ListView):
    model = Paleta
    template_name = "CBV/lista_paleta.html"
 
   
class PaletaDetailView(DetailView):
    model = Paleta
    template_name = "CBV/detalle_paleta.html"
 
    
class PaletaCreateView(LoginRequiredMixin, CreateView):
    model = Paleta
    template_name = "CBV/crear_paleta.html"
    fields = ['nombre', 'apodo', 'dt', 'anio_de_creacion', 'dato_curioso', 'escudo']
    success_url = '/paletas/'
 
   
class PaletaUpdateView(LoginRequiredMixin, UpdateView):
    model = Paleta
    template_name = "CBV/actualiza_paleta.html"
    fields = ['nombre', 'apodo', 'dt', 'anio_de_creacion', 'dato_curioso', 'escudo']
    success_url = '/paletas/'

    
class PaletaDeleteView(LoginRequiredMixin, DeleteView):
    model = Paleta
    template_name = "CBV/borra_paleta.html"
    success_url = '/paletas/'
    
##########
def buscar_equipo(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar:
        equipos = Equipo.objects.filter(nombre__icontains = nombre_a_buscar)
    else:
        equipos = Equipo.objects.all()
    formulario_busqueda = BuscarEquipo()
    return render(request,'buscar_equipo.html', {'equipos':equipos, 'formulario':formulario_busqueda})

def buscar_paleta(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar:
        paletas = Paleta.objects.filter(nombre__icontains = nombre_a_buscar)
    else:
        paletas = Paleta.objects.all()
    formulario_busqueda = BuscarPaleta()
    return render(request,'buscar_paletas.html', {'paletas':paletas, 'formulario':formulario_busqueda})



