from django.urls import path
from Aplicacion import views

app_name = 'Aplicacion'

urlpatterns = [
    path('', views.vista, name = 'Inicio'),
    path('agregar-info/', views.agregar_info, name = 'Agregar Información'),
    path('buscar-info/', views.buscar_info, name = 'Buscar Informacion'),
]