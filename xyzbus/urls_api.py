from rest_framework_nested import routers
from django.conf.urls import url, include
from camiones.viewsets import RutasViewSet, CorridasViewSet, Catalogo_rutasViewSet, Coordenas_rutasViewSet

router = routers.DefaultRouter()
router.register(r'rutas', RutasViewSet)
router.register(r'corridas', CorridasViewSet)
router.register(r'catalogo_rutas', Catalogo_rutasViewSet)
router.register(r'coordenadas_rutas', Coordenas_rutasViewSet)

coordenadas_router = routers.NestedSimpleRouter(router, r'catalogo_rutas', lookup='catalogo_ruta')
coordenadas_router.register(r'coordenadas', Coordenas_rutasViewSet, base_name='rutas-coordenadas')

urlpatterns = [
url(r'', include(router.urls)),
url(r'', include(coordenadas_router.urls))
]