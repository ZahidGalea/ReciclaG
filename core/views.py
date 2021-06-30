from django.contrib.auth import authenticate, login as lg
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response

from . import forms
from . import models


def home(request):
    context = {}
    return render(request, 'app/index.html', context=context)


def crearusuario(request):
    context = {
        "form": forms.UserCreationFormM()
    }

    if request.method == 'POST':
        formulario = forms.UserCreationFormM(request.POST)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = 'Usuario guardado correctamente'
            # Autenticación instantánea
            new_user = authenticate(username=formulario.cleaned_data['username'],
                                    password=formulario.cleaned_data['password1'],
                                    )
            lg(request, new_user)
            return redirect(to="dashboard")
        else:
            context['mensaje'] = 'Usuario no guardado correctamente'
    return render(request, 'app/crearusuario.html', context)


@login_required
def dashboard(request):
    user = request.user
    puntos = models.PuntoReciclag.objects.filter(id_usuario=user)
    context = {
        "puntos": puntos
    }
    return render(request, 'app/dashboard.html', context=context)


@login_required
def administracion(request):
    user = request.user
    if user.username != 'admin':
        return redirect(to="dashboard")
    # crear o recuperar un token
    token, created = Token.objects.get_or_create(user=user)

    puntos = models.PuntoReciclag.objects.all()
    context = {
        "puntos": puntos,
        "user_token": token
    }
    return render(request, 'app/administracion.html', context=context)


def iniciativa(request):
    puntos = models.PuntoReciclag.objects.all()

    context = {
        "puntos": puntos
    }

    return render(request, 'app/iniciativa.html', context=context)


@login_required
def inscribir(request):
    context = {
        "form": forms.InscribirPunto()
    }

    if request.method == 'POST':
        formulario = forms.InscribirPunto(request.POST, request.FILES or None)
        fs = formulario.save(commit=False)
        fs.id_usuario = request.user
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = 'Punto guardados correctamente'
        else:
            context['mensaje'] = 'El punto no ha podido ser guardado correctamente'
        if request.user.username == 'admin':
            return redirect(to='administracion')

        return redirect(to="dashboard")

    return render(request, 'app/inscribir.html', context=context)


def login(request):
    context = {
        "form": forms.LoginForm()
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            lg(request, user)
            if request.user.username == 'admin':
                return redirect(to='administracion')
            return redirect(to='dashboard')

    return render(request, 'app/login.html', context=context)


@login_required
def modificar(request, id):
    punto = models.PuntoReciclag.objects.get(id=id)
    context = {
        "form": forms.ModificarPunto(instance=punto)
    }

    if request.method == 'POST':
        formulario = forms.ModificarPunto(request.POST, request.FILES or None,
                                          instance=punto)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = 'Punto guardados correctamente'
        else:
            context['mensaje'] = 'El punto no ha podido ser guardado correctamente'

        if request.user.username == 'admin':
            return redirect(to='administracion')
        return redirect(to="dashboard")
    return render(request, 'app/modificar.html', context=context)


@login_required
def borrar(request, id):
    punto = models.PuntoReciclag.objects.get(id=id)
    punto.delete()
    if request.user.username == 'admin':
        return redirect(to='administracion')
    return redirect(to="dashboard")
