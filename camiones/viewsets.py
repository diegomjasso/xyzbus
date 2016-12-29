from rest_framework import viewsets
from .serializers import RutasSerializer, CorridasSerializer
from .models import Rutas, Corridas


class RutasViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Rutas.objects.all()
  serializer_class = RutasSerializer

class CorridasViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Corridas.objects.all()
	serializer_class = CorridasSerializer