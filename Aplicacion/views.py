from django.shortcuts import render,redirect
from Aplicacion.models import Equipo
from Aplicacion.forms import EquipoFormulario, BuscarEquipo, FormularioEditarEquipo
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

def vista(request):
    return render(request, 'index.html')

#Clases normales para equipo

def crear_equipo(request):
      if request.method == 'POST':    
            formulario = EquipoFormulario(request.POST)
            
            if formulario.is_valid():
                datos_correctos = formulario.cleaned_data
            
            equipo =  Equipo(nombre = datos_correctos['nombre'], apodo = datos_correctos['apodo'], dt = datos_correctos['dt'], anio_de_creacion =  datos_correctos['anio_de_creacion'])
            equipo.save()
            
            return redirect('Aplicacion:Lista Equipos')
        
      formulario = EquipoFormulario()
      return render(request,'crear_equipo.html', {'formulario':formulario})

def lista_equipos(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar:
        equipos = Equipo.objects.filter(nombre__icontains = nombre_a_buscar)
    else:
        equipos = Equipo.objects.all()
    formulario_busqueda = BuscarEquipo()
    return render(request,'lista_equipos.html', {'equipos':equipos, 'formulario':formulario_busqueda})

def eliminar_equipo(request, id_equipo):
    equipo_a_eliminar = Equipo.objects.get(id = id_equipo)
    equipo_a_eliminar.delete()
    return redirect('Aplicacion:Lista Equipos')

def mostrar_equipo(request, id_equipo):
    equipo_a_mostrar = Equipo.objects.get(id = id_equipo)
    return render(request,'mostrar_equipo.html', {'equipo_a_mostrar':equipo_a_mostrar})

def modificar_equipo(request, id_equipo):
    equipo_a_modificar = Equipo.objects.get(id = id_equipo)
    if request.method =="POST": 
        formulario = FormularioEditarEquipo(request.POST)
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
            equipo_a_modificar.nombre = datos_correctos['nombre']
            equipo_a_modificar.apodo = datos_correctos['apodo'] 
            equipo_a_modificar.dt = datos_correctos['dt']
            equipo_a_modificar.anio_de_creacion = datos_correctos['anio_de_creacion']
            equipo_a_modificar.save()
            return redirect('Aplicacion:Lista Equipos')
        else:
            return render(request, 'modificar_equipo.html', {'formulario':formulario, 'id_equipo':id_equipo})
    
    formulario = FormularioEditarEquipo(initial = {'nombre':equipo_a_modificar.nombre, 'apodo':equipo_a_modificar.apodo, 'dt':equipo_a_modificar.dt, 'anio_de_creacion':equipo_a_modificar.anio_de_creacion})
    return render(request, 'modificar_equipo.html', {'formulario':formulario, 'id_equipo':id_equipo})

#CBV para equipos

class ListaEquipos(ListView):
    model = Equipo
    template_name = 'CBV/lista_equipos.html'
    
class CrearEquipo(CreateView):
    model = Equipo
    template_name = 'CBV/crear_equipo.html'
    success_url = '/equipos/lista-equipos/'
    fields = ['nombre', 'apodo', 'dt', 'anio_de_creacion']
    
class EditarEquipo(UpdateView):
    model = Equipo
    template_name = 'CBV/modificar_equipo.html'
    success_url = '/equipos/lista-equipos/'
    fields = ['nombre', 'apodo', 'dt', 'anio_de_creacion']
    
class EliminarEquipo(DeleteView):
    model = Equipo
    template_name = 'CBV/eliminar_equipo.html'
    success_url = '/equipos/lista-equipos/'
    
class MostrarEquipo(DetailView):
    model = Equipo
    template_name = 'CBV/mostrar_equipo.html'