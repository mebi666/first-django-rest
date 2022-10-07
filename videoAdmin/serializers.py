from rest_framework import serializers
from .models import Usuario, Peliculas

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class PeliculasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peliculas
        fields = ('__all__')
