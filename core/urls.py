from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('home', views.home, name="homepage"),
    path('crearusuario', views.crearusuario, name="crearusuario"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('iniciativa', views.iniciativa, name="iniciativa"),
    path('inscribir', views.inscribir, name="inscribir"),
    path('login', views.login, name="login"),
    path('modificar/<id>', views.modificar, name="modificar"),
    path('borrar/<id>', views.borrar, name="borrar"),
    path('administracion', views.administracion, name="administracion"),
]
