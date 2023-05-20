from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro/', views.registrar, name='registro'),
    path('ver-perfil', views.ver_perfil, name='ver_perfil'),   
    path('editar-perfil/', views.editar_perfil, name='editar'),
    path('cambio-contrasenia/', views.CambioContra.as_view(), name='cambio_contrasenia'),

]
