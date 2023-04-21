from django.db import models

class Equipo(models.Model):
    
    Nombre = models.CharField (max_length = 30)
    Apodo = models.CharField (max_length = 30)
    Dt = models.CharField (max_length = 30)
    Año_de_Creacion = models.CharField (max_length = 4)
