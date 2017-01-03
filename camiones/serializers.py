from rest_framework import serializers
from .models import Rutas, Corridas, Catalogo_rutas

class RutasSerializer(serializers.ModelSerializer):
	ruta = serializers.StringRelatedField()
	conductor = serializers.StringRelatedField()

	class Meta:
		model = Rutas
		fields = '__all__'

class CorridasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Corridas
		fields = '__all__'

class Catalogo_rutasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Catalogo_rutas
		fields = '__all__'