from rest_framework_nested import routers
from django.conf.urls import url, include
from camiones.viewsets import RutasViewSet, CorridasViewSet, Catalogo_rutasViewSet, Coordenadas_rutasViewSet, Coordenadas_corridasViewSet

router = routers.DefaultRouter()
router.register(r'rutas', RutasViewSet)
router.register(r'corridas', CorridasViewSet)
router.register(r'catalogo_rutas', Catalogo_rutasViewSet)
router.register(r'coordenadas_rutas', Coordenadas_rutasViewSet)
router.register(r'coordenadas_corridas', Coordenadas_corridasViewSet)

coordenadas_router = routers.NestedSimpleRouter(router, r'catalogo_rutas', lookup='catalogo_ruta')
coordenadas_router.register(r'coordenadas', Coordenadas_rutasViewSet, base_name='rutas-coordenadas')

coordenadas_corrida_router = routers.NestedSimpleRouter(router, r'corridas', lookup='corrida')
coordenadas_corrida_router.register(r'coordenadas', Coordenadas_corridasViewSet, base_name='corridas-coordenadas')

urlpatterns = [
	url(r'', include(router.urls)),
	url(r'', include(coordenadas_router.urls)),
	url(r'', include(coordenadas_corrida_router.urls))
]