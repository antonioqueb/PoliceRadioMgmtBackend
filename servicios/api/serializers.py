
from rest_framework.serializers import ModelSerializer
from servicios.models import *


class AreasSerializer(ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'


class CatTecnicosSerializer(ModelSerializer):
    class Meta:
        model = CatTecnicos
        fields = '__all__'


class ControlfolSerializer(ModelSerializer):
    class Meta:
        model = Controlfol
        fields = '__all__'

class DependenciasSerializer(ModelSerializer):
    class Meta:
        model = Dependencias
        fields = '__all__'

class EstacionaSerializer(ModelSerializer):
    class Meta:
        model = Estaciona
        fields = '__all__'

class EstasubeSerializer(ModelSerializer):
    class Meta:
        model = Estasube
        fields = '__all__'

class MovfallasSerializer(ModelSerializer):
    class Meta:
        model = Movfallas
        fields = '__all__'

class MovpartesSerializer(ModelSerializer):
    class Meta:
        model = Movpartes
        fields = '__all__'

class MservSerializer(ModelSerializer):
    class Meta:
        model = Mserv
        fields = '__all__'

class MunicipiosSerializer(ModelSerializer):
    class Meta:
        model = Municipios
        fields = '__all__'

class PdserviciosSerializer(ModelSerializer):
    class Meta:
        model = Pdservicios
        fields = '__all__'


class ServiciosSerializer(ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'

class ServiciosradSerializer(ModelSerializer):
    class Meta:
        model = Serviciosrad
        fields = '__all__'

class TfallasSerializer(ModelSerializer):
    class Meta:
        model = Tfallas
        fields = '__all__'

class TiposSerializer(ModelSerializer):
    class Meta:
        model = Tipos
        fields = '__all__'

class TpartesSerializer(ModelSerializer):
    class Meta:
        model = Tpartes
        fields = '__all__'

