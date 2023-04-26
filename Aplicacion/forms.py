from django import forms
 
class EquipoFormulario(forms.Form):
     
    Nombre = forms.CharField (max_length = 30)
    Apodo = forms.CharField (max_length = 30)
    Dt = forms.CharField (max_length = 30)
    Año_de_Creacion = forms.IntegerField ()

class BuscarEquipo(forms.Form):
     
    Nombre = forms.CharField (max_length = 30, required = False)