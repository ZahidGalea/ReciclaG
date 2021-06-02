from django.shortcuts import render, redirect
from . import forms
from . import models


def home(request):
    context = {}
    return render(request, 'app/index.html', context=context)


def crearusuario(request):
    context = {
        "form": forms.CrearUsuarioForm()
    }

    if request.method == 'POST':
        formulario = forms.CrearUsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            context['mensaje'] = 'Usuario guardado correctamente'
            return redirect(to="dashboard")
    return render(request, 'app/crearusuario.html', context)


def dashboard(request):
    puntos = models.PuntoReciclag.objects.all()
    context = {
        "puntos": puntos
    }
    return render(request, 'app/dashboard.html', context=context)


def iniciativa(request):
    puntos = models.PuntoReciclag.objects.all()

    context = {
        "puntos": puntos
    }

    return render(request, 'app/iniciativa.html', context=context)


def inscribir(request):
    context = {
        "form": forms.InscribirPunto()
    }

    if request.method == 'POST':
        formulario = forms.InscribirPunto(request.POST, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = 'Punto guardados correctamente'
        else:
            context['mensaje'] = 'El punto no ha podido ser guardado correctamente'

        return redirect(to="dashboard")

    return render(request, 'app/inscribir.html', context=context)


def login(request):
    context = {
        "form": forms.LoginForm()
    }

    return redirect(to="dashboard")

    return render(request, 'app/login.html', context=context)


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

        return redirect(to="dashboard")
    return render(request, 'app/modificar.html', context=context)


def borrar(request, id):
    punto = models.PuntoReciclag.objects.get(id=id)
    punto.delete()
    return redirect(to="dashboard")
