from rest_framework import routers
from camiones.viewsets import RutasViewSet

router = routers.DefaultRouter()
router.register(r'rutas', RutasViewSet)

urlpatterns = router.urls