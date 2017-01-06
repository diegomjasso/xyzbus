from rest_framework import viewsets
from .serializers import RutasSerializer, CorridasSerializer,	Catalogo_rutasSerializer, Coordenadas_rutaSerializer
from .models import Rutas, Corridas, Catalogo_rutas, Coordenadas_rutas

class RutasViewSet(viewsets.ReadOnlyModelViewSet):
	queryset	=	Rutas.objects.all()
	serializer_class	=	RutasSerializer

class CorridasViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Corridas.objects.all()
	serializer_class = CorridasSerializer

class Catalogo_rutasViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Catalogo_rutas.objects.all()
	serializer_class = Catalogo_rutasSerializer
	filter_fields = ('ruta',)

class Coordenas_rutasViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Coordenadas_rutas.objects.all()
	serializer_class = Coordenadas_rutaSerializer


	def get_queryset(self):
		if  'catalogo_ruta_pk' in self.kwargs:
			return self.queryset.filter(ruta = self.kwargs['catalogo_ruta_pk']).order_by('order')
		else:
			return self.queryset