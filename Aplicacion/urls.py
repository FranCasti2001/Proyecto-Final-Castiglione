from django.urls import path
from Aplicacion import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Aplicacion'

urlpatterns = [
    path('', views.vista, name = 'inicio'),
    path('equipos/lista-equipos/', views.ListaEquipos.as_view(), name = 'lista_equipos'),
    path('equipos/editar-info/agregar-info/', views.CrearEquipo.as_view(), name = 'crear_equipo'),
    path('editar-info/modificar-equipos/<int:pk>/', views.EditarEquipo.as_view(), name = 'modificar_equipos'),
    path('equipos/editar-info/eliminar-equipos/<int:pk>/', views.EliminarEquipo.as_view(), name = 'eliminar_equipos'),
    path('equipos/<int:pk>/', views.MostrarEquipo.as_view(), name = 'mostrar_equipos'),
    path('about-me/', views.about, name = 'about'),
    path('paletas/', views.PaletaListView.as_view(), name = 'lista_paletas'),
    path('paletas/<int:pk>/', views.PaletaDetailView.as_view(), name = 'detalle_paletas'),
    path('paletas/crear/', views.PaletaCreateView.as_view(), name = 'crear_paletas'),
    path('paletas/<int:pk>/Modificar/', views.PaletaUpdateView.as_view(), name = 'modificar_paletas'),
    path('paletas/<int:pk>/aliminar/', views.PaletaDeleteView.as_view(), name = 'borrar_paletas'),
    path('equipos/buscar', views.buscar_equipo, name = 'buscador_equipos'),
    path('paletas/buscar', views.buscar_paleta, name = 'buscador_paletas'),



]