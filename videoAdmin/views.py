from django.shortcuts import render
from django.urls import reverse_lazy 
from videoAdmin.models import Usuario, Peliculas
from rest_framework import viewsets
from .serializers import UsuarioSerializer, PeliculasSerializer

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('-numberId')
    serializer_class = UsuarioSerializer

class PeliculasViewSet(viewsets.ModelViewSet):
    queryset = Peliculas.objects.all()
    serializer_class = PeliculasSerializer
