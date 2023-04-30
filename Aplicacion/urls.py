from django.urls import path
from Aplicacion import views

app_name = 'Aplicacion'

urlpatterns = [
    path('', views.vista, name = 'Inicio'),
    
    #Clases con vistas
    #path('equipos/editar-info/agregar-info/', views.crear_equipo, name = 'Agregar Información'),
    #path('equipos/editar-info/lista-equipos/', views.lista_equipos, name = 'Lista Equipos'),
    #path('equipos/editar-info/eliminar-equipos/<int:id_equipo>/', views.eliminar_equipo, name = 'Eliminar Equipos'),
    #path('equipos/<int:id_equipo>/', views.mostrar_equipo, name = 'Mostrar Equipos'),
    #path('editar-info/modificar-equipos/<int:id_equipo>/', views.modificar_equipo, name = 'Modificar Equipos'),
    
    #Clases con CBV
    path('equipos/lista-equipos/', views.ListaEquipos.as_view(), name = 'Lista Equipos'),
    path('equipos/editar-info/agregar-info/', views.CrearEquipo.as_view(), name = 'Crear Equipo'),
    path('editar-info/modificar-equipos/<int:pk>/', views.EditarEquipo.as_view(), name = 'Modificar Equipos'),
    path('equipos/editar-info/eliminar-equipos/<int:pk>/', views.EliminarEquipo.as_view(), name = 'Eliminar Equipos'),
    path('equipos/<int:pk>/', views.MostrarEquipo.as_view(), name = 'Mostrar Equipos'),
]