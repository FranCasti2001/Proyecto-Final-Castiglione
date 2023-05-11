from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('registro/', views.registrar, name='Registro'),
    path('editar-perfil/', views.editar_perfil, name='Editar'),
    path('cambio-contrasenia/', views.CambioContra.as_view(), name='CambioContrasenia'),

]
