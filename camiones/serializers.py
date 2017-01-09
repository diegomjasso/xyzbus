from rest_framework import serializers
from .models import Rutas, Rutas_favoritas, Catalogo_rutas, Corridas, Coordenadas_rutas, Coordenadas_corridas

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
	ruta = RutasSerializer()

	class Meta:
		model = Corridas
		fields = '__all__'

class Coordenadas_rutaSerializer(serializers.ModelSerializer):
	ruta = RutasByCatalogoSerializer()
	
	class Meta:
		model = Coordenadas_rutas
		fields = '__all__'

class Catalogo_rutasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Catalogo_rutas
		fields = '__all__'

class Coordenadas_corridaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Coordenadas_corridas
		fields = '__all__'