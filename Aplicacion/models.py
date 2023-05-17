from django.db import models
from ckeditor.fields import RichTextField

class Equipo(models.Model):
    
    nombre = models.CharField (max_length = 30)
    apodo = models.CharField (max_length = 30)
    dt = models.CharField (max_length = 30)
    anio_de_creacion = models.IntegerField ()
    escudo = models.ImageField(upload_to = 'avatares', null = True, blank = True)

    def __str__(self):
        return f'Nombre del equipo: {self.nombre} - Apodo del equipo: {self.apodo} - Dt del equipo: {self.dt} - Año de creación: {self.anio_de_creacion} - Escudo: '

class Paleta(models.Model):
    nombre = models.CharField (max_length = 30)
    apodo = models.CharField (max_length = 30)
    dt = models.CharField (max_length = 30)
    anio_de_creacion = models.IntegerField ()
    dato_curioso = RichTextField()
    escudo = models.ImageField (upload_to = 'avatares', null = True, blank = True)
    
    def __str__(self):
        return f'{self.nombre}'
    