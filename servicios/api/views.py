from rest_framework.viewsets import ModelViewSet
from servicios.models import *
from servicios.api.serializers import *


class AreasViewSet(ModelViewSet):
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer

class CatTecnicosViewSet(ModelViewSet):
    queryset = CatTecnicos.objects.all()
    serializer_class = CatTecnicosSerializer


class ControlfolViewSet(ModelViewSet):
    queryset = Controlfol.objects.all()
    serializer_class = ControlfolSerializer

class DependenciasViewSet(ModelViewSet):
    queryset = Dependencias.objects.all()
    serializer_class = DependenciasSerializer

class EstacionaViewSet(ModelViewSet):
    queryset = Estaciona.objects.all()
    serializer_class = EstacionaSerializer

class EstasubeViewSet(ModelViewSet):
    queryset = Estasube.objects.all()
    serializer_class = EstasubeSerializer

class MovfallasViewSet(ModelViewSet):
    queryset = Movfallas.objects.all()
    serializer_class = MovfallasSerializer

class MovpartesViewSet(ModelViewSet):
    queryset = Movpartes.objects.all()
    serializer_class = MovpartesSerializer

class MservViewSet(ModelViewSet):
    queryset = Mserv.objects.all()
    serializer_class = MservSerializer

class MunicipiosViewSet(ModelViewSet):
    queryset = Municipios.objects.all()
    serializer_class = MunicipiosSerializer

class PdserviciosViewSet(ModelViewSet):
    queryset = Pdservicios.objects.all()
    serializer_class = PdserviciosSerializer


class ServiciosViewSet(ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer

class ServiciosradViewSet(ModelViewSet):
    queryset = Serviciosrad.objects.all()
    serializer_class = ServiciosradSerializer

class TfallasViewSet(ModelViewSet):
    queryset = Tfallas.objects.all()
    serializer_class = TfallasSerializer

class TiposViewSet(ModelViewSet):
    queryset = Tipos.objects.all()
    serializer_class = TiposSerializer

class TpartesViewSet(ModelViewSet):
    queryset = Tpartes.objects.all()
    serializer_class = TpartesSerializer

