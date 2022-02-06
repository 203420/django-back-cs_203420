from rest_framework import routers, serializers, viewsets

from loadImage.models import Imagen

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ('__all__')