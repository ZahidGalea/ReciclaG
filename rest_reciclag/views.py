import logging

from rest_framework import status

from core.models import PuntoReciclag
from .serializers import CompletePuntoSerializer, PublicPuntoSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET'])
def get_puntos_public(request):
    if request.method == 'GET':
        punto = PuntoReciclag.objects.all()
        serializer = PublicPuntoSerializer(punto, many=True)
        logging.debug(serializer.data)
        return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_puntos(request):
    if request.method == 'GET':
        punto = PuntoReciclag.objects.all()
        serializer = CompletePuntoSerializer(punto, many=True)
        logging.debug(serializer.data)
        return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_punto(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = CompletePuntoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_login(request):
    data = JSONParser().parse(request)
    # print(data)

    username = data['username']
    password = data['password']

    # validar usuario
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario no existe")

    # validar pass
    pass_valida = check_password(password, user.password)

    if not pass_valida:
        return Response("Password incorrecta")

    # crear o recuperar un token
    token, created = Token.objects.get_or_create(user=user)

    # retorno del token asociado al usuario
    return Response(token.key)
