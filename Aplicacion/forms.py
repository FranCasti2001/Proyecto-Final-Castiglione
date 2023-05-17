from django import forms
 
class EquipoFormulario(forms.Form):
     
    nombre = forms.CharField (max_length = 30)
    apodo = forms.CharField (max_length = 30)
    dt = forms.CharField (max_length = 30)
    anio_de_creacion = forms.IntegerField ()
    escudo = forms.ImageField(required = False)

    
class FormularioEditarEquipo(forms.Form):
     
    nombre = forms.CharField (max_length = 30)
    apodo = forms.CharField (max_length = 30)
    dt = forms.CharField (max_length = 30)
    anio_de_creacion = forms.IntegerField ()
    escudo = forms.ImageField(required = False)
    

class BuscarEquipo(forms.Form):
     
    nombre = forms.CharField (max_length = 30, required = False)
    
class BuscarPaleta(forms.Form):
     
    nombre = forms.CharField (max_length = 30, required = False)
