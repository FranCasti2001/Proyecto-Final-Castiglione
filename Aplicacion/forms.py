from django import forms
 
class EquipoFormulario(forms.Form):
     
    nombre = forms.CharField (max_length = 30)
    apodo = forms.CharField (max_length = 30)
    dt = forms.CharField (max_length = 30)
    anio_de_creacion = forms.IntegerField ()
    
class FormularioEditarEquipo(forms.Form):
     
    nombre = forms.CharField (max_length = 30)
    apodo = forms.CharField (max_length = 30)
    dt = forms.CharField (max_length = 30)
    anio_de_creacion = forms.IntegerField ()

class BuscarEquipo(forms.Form):
     
    nombre = forms.CharField (max_length = 30, required = False)