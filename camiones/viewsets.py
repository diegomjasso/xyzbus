from rest_framework import viewsets
from .serializers import RutasSerializer
from .models import Rutas


class RutasViewSet(viewsets.ModelViewSet):
    queryset = Rutas.objects.all()
    serializer_class = RutasSerializer