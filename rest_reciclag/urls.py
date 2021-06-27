from django.urls import path
from rest_reciclag import views

urlpatterns = [
    path('get_puntos', views.get_puntos, name="get_puntos"),
    path('get_puntos_public', views.get_puntos_public, name="get_puntos_public"),
    path('create_punto', views.create_punto, name="create_punto"),
    path('api_login', views.api_login, name="api_login"),
]
