from rest_framework import serializers
from .models import Rutas

class RutasSerializer(serializers.ModelSerializer):
	ruta = serializers.StringRelatedField()
	conductor = serializers.StringRelatedField()

	class Meta:
		model = Rutas
		fields = '__all__'