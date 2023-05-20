from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from usuarios.forms import CreacionDeUsuario, EdicionDeUsuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import ExtraData


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                ExtraData.objects.get_or_create(user = request.user)

                return render(request, "index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "index.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

def registrar(request):
    if request.method == 'POST':
        form = CreacionDeUsuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "index.html", {"mensaje": "Usuario Creado :)"})
    else:
        form = CreacionDeUsuario()
        return render(request, "registro.html", {"form": form})

    form = CreacionDeUsuario()
    return render(request, "registro.html", {"form": form})

def ver_perfil(request):
    return render (request, "ver_perfil.html")

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EdicionDeUsuario(request.POST, request.FILES, instance = request.user)
        
        if form.is_valid():
            if form.cleaned_data.get('avatar'):
             request.user.extradata.avatar = form.cleaned_data.get('avatar')
            request.user.extradata.save()
            form.save()
            return redirect('Aplicacion:inicio')
        else:
         return render(request,"editar_perfil.html", {"form":form})
        
    form = EdicionDeUsuario(initial = {'avatar':request.user.extradata.avatar}, instance = request.user)     
    return render(request,"editar_perfil.html", {"form":form})


class CambioContra(PasswordChangeView):
    template_name = "cambiar_contra.html"
    success_url = reverse_lazy ("usuarios:editar")
    