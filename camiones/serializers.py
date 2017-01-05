from rest_framework import serializers
from .models import Rutas, Corridas, Catalogo_rutas, Coordenadas_rutas

class RutasByCatalogoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Catalogo_rutas
		fields = '__all__'

class RutasSerializer(serializers.ModelSerializer):
	ruta = RutasByCatalogoSerializer()
	conductor = serializers.StringRelatedField()

	class Meta:
		model = Rutas
		fields = '__all__'

class CorridasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Corridas
		fields = '__all__'

class Coordenadas_rutaSerializer(serializers.ModelSerializer):
	ruta = serializers.StringRelatedField()
	
	class Meta:
		model = Coordenadas_rutas
		fields = '__all__'

class CoordenadasByRutasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Coordenadas_rutas
		fields = '__all__'

class Catalogo_rutasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Catalogo_rutas
		fields = '__all__'