from django.shortcuts import render,redirect
from Aplicacion.models import Equipo
from Aplicacion.forms import EquipoFormulario, BuscarEquipo

def vista(request):
    return render(request, 'index.html')

def agregar_info(request):
      if request.method == 'POST':    
            formulario = EquipoFormulario(request.POST)
            
            if formulario.is_valid():
                datos_correctos = formulario.cleaned_data
            
            equipo =  Equipo(Nombre = datos_correctos['Nombre'], Apodo = datos_correctos['Apodo'], Dt = datos_correctos['Dt'], Año_de_Creacion =  datos_correctos['Año_de_Creacion'])
            equipo.save()
            
            return redirect('Aplicacion:Lista Equipos')
        
      formulario = EquipoFormulario()
      return render(request,'agregar_info.html', {'formulario':formulario})

def lista_equipos(request):
    nombre_a_buscar = request.GET.get('Nombre', None)
    
    if nombre_a_buscar:
        equipos = Equipo.objects.filter(Nombre__icontains = nombre_a_buscar)
    else:
        equipos = Equipo.objects.all()
    formulario_busqueda = BuscarEquipo()
    return render(request,'lista_equipos.html', {'equipos':equipos, 'formulario':formulario_busqueda})