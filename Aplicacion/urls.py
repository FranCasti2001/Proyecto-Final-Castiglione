from django.urls import path
from Aplicacion import views

app_name = 'Aplicacion'

urlpatterns = [
    path('', views.vista, name = 'Inicio'),
    path('agregar-info/', views.agregar_info, name = 'Agregar Información'),
    path('equipos/', views.lista_equipos, name = 'Lista Equipos')
]