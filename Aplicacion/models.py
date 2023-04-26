from django.db import models

class Equipo(models.Model):
    
    Nombre = models.CharField (max_length = 30)
    Apodo = models.CharField (max_length = 30)
    Dt = models.CharField (max_length = 30)
    Año_de_Creacion = models.IntegerField ()
    
    def __str__(self):
        return f'{self.Nombre}'
