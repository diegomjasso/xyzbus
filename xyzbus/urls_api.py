from rest_framework import routers
from camiones.viewsets import RutasViewSet, CorridasViewSet

router = routers.DefaultRouter()
router.register(r'rutas', RutasViewSet)
router.register(r'corridas', CorridasViewSet)

urlpatterns = router.urls