from rest_framework.routers import DefaultRouter
from servicios.api.views import *


router = DefaultRouter()

router.register(r'areas', AreasViewSet)
router.register(r'cattecnicos', CatTecnicosViewSet)
router.register(r'controlfol', ControlfolViewSet)
router.register(r'dependencias', DependenciasViewSet)
router.register(r'estaciona', EstacionaViewSet)
router.register(r'estasube', EstasubeViewSet)
router.register(r'movfallas', MovfallasViewSet)
router.register(r'movpartes', MovpartesViewSet)
router.register(r'mserv', MservViewSet)
router.register(r'municipios', MunicipiosViewSet)
router.register(r'pdservicios', PdserviciosViewSet)
router.register(r'servicios', ServiciosViewSet)
router.register(r'serviciosrad', ServiciosradViewSet)
router.register(r'tfallas', TfallasViewSet)
router.register(r'tipos', TiposViewSet)
router.register(r'tpartes', TpartesViewSet)
