from django import forms
 
class EquipoFormulario(forms.Form):
     
    Nombre = forms.CharField(max_length= 20)
    Apodo = forms.CharField(max_length= 20)
    Dt = forms.CharField(max_length= 20)
    Año_de_Creacion = forms.IntegerField()