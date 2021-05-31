from django.shortcuts import render
from . import forms
from . import models


def home(request):
    context = {}
    return render(request, 'app/index.html', context=context)


def crearusuario(request):
    context = {
        "form": forms.CrearUsuarioForm()
    }
    return render(request, 'app/crearusuario.html', context)


def dashboard(request):
    context = {}
    return render(request, 'app/dashboard.html', context=context)


def iniciativa(request):
    context = {}
    return render(request, 'app/iniciativa.html', context=context)


def inscribir(request):
    context = {
        "form": forms.InscribirPunto()
    }


    if request.method == 'POST':
        formulario = forms.InscribirPunto(request.POST, request.FILES or None)
        if formulario.is_valid:
            formulario.save()
            context['mensaje'] = 'Guardados correctamente'

    return render(request, 'app/inscribir.html', context=context)


def login(request):
    context = {}
    return render(request, 'app/login.html', context=context)


def modificar(request):
    context = {
        "form": forms.ModificarPunto()
    }
    return render(request, 'app/modificar.html', context=context)
