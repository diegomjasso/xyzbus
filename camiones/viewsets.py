from rest_framework import viewsets
from .serializers import RutasSerializer, CorridasSerializer,	Catalogo_rutasSerializer, Coordenadas_rutaSerializer, Coordenadas_corridaSerializer
from .models import Rutas, Corridas, Catalogo_rutas, Coordenadas_rutas, Coordenadas_corridas

class RutasViewSet(viewsets.ReadOnlyModelViewSet):
	queryset	=	Rutas.objects.all()
	serializer_class	=	RutasSerializer

class CorridasViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Corridas.objects.all()
	serializer_class = CorridasSerializer
	filter_fields = ('status', 'ruta', 'sentido', 'fecha_inicio', 'fecha_final',)

class Catalogo_rutasViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Catalogo_rutas.objects.all()
	serializer_class = Catalogo_rutasSerializer
	filter_fields = ('ruta',)

class Coordenadas_corridasViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Coordenadas_corridas.objects.all()
	serializer_class = Coordenadas_corridaSerializer

	def get_queryset(self):
		if  'corrida_pk' in self.kwargs:
			return self.queryset.filter(corrida = self.kwargs['corrida_pk']).order_by('id')
		else:
			return self.queryset

class Coordenadas_rutasViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Coordenadas_rutas.objects.all()
	serializer_class = Coordenadas_rutaSerializer

	def get_queryset(self):
		if  'catalogo_ruta_pk' in self.kwargs:
			return self.queryset.filter(ruta = self.kwargs['catalogo_ruta_pk']).order_by('order')
		else:
			return self.queryset