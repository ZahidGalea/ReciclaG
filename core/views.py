from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'app/index.html', context=context)


def cambioclave(request):
    context = {}
    return render(request, 'app/cambioclave.html', context=context)


def crearusuario(request):
    context = {}
    return render(request, 'app/crearusuario.html', context=context)


def dashboard(request):
    context = {}
    return render(request, 'app/dashboard.html', context=context)


def iniciativa(request):
    context = {}
    return render(request, 'app/iniciativa.html', context=context)


def inscribir(request):
    context = {}
    return render(request, 'app/inscribir.html', context=context)


def login(request):
    context = {}
    return render(request, 'app/login.html', context=context)


def modificar(request):
    context = {}
    return render(request, 'app/modificar.html', context=context)


def recupclave(request):
    context = {}
    return render(request, 'app/recupclave.html', context=context)


def verificafono(request):
    context = {}
    return render(request, 'app/verificafono.html', context=context)
