from rest_framework import routers
from camiones.viewsets import RutasViewSet, CorridasViewSet, Catalogo_rutasViewSet

router = routers.DefaultRouter()
router.register(r'rutas', RutasViewSet)
router.register(r'corridas', CorridasViewSet)
router.register(r'catalgo_rutas', Catalogo_rutasViewSet)

urlpatterns = router.urls