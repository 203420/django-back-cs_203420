from pyexpat import model
from django.forms import fields
from rest_framework import routers, serializers, viewsets

#Importación de modelos
from primerComponente.models import PrimerTabla

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields = ('nombre', 'edad')