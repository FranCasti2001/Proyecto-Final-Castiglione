from django.shortcuts import render
from Aplicacion.models import Equipo
from Aplicacion.forms import *

def vista(request):
    return render(request, 'index.html')

def agregar_info(request):
      if request.method == 'POST':    
            formulario = EquipoFormulario(request.POST)
            
            if formulario.is_valid():
                datos_correctos = formulario.cleaned_data
            
            equipo =  Equipo(Nombre = datos_correctos['Nombre'], Apodo = datos_correctos['Apodo'], Dt = datos_correctos['Dt'], Año_de_Creacion =  datos_correctos['Año_de_Creacion'])
            equipo.save()
        
      formulario = EquipoFormulario()
      return render(request,"agregar_info.html", {'formulario':formulario})

def buscar_info(request):
    return render(request, 'buscar_info.html')