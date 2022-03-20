from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os.path
import json

#Importación de modelos y serializers
from loadImage.serializers import ImagenSerializer
from loadImage.models import Imagen

# Create your views here.
class ImagenViews(APIView):
    def response_custom(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        responseOk = json.loads(res)
        return responseOk

    def post(self, request):
        if 'url_img' not in request.data:
            raise exceptions.ParseError("No has seleccionado el archivo a subir")

        archivo = request.data['url_img']
        nombre, formato = os.path.splitext(archivo.name)
        request.data['name_img'] = nombre
        request.data['format_img'] = formato
        serializer = ImagenSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(self.response_custom("Success",serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.response_custom("Error",serializer.errors, status=status.HTTP_400_BAD_REQUEST))

    def get(self, request, format=None):
        queryset = Imagen.objects.all()
        serializer = ImagenSerializer(queryset , many=True, context={'request':request})
        responseOk= self.response_custom("Success", serializer.data, status=status.HTTP_200_OK)
        return Response(responseOk)

class ImagenViewsDetail(APIView):
    def response_custom(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        responseOk = json.loads(res)
        return responseOk

    def get_object(self, pk):
        try:
            return Imagen.objects.get(pk = pk)
        except Imagen.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response = ImagenSerializer(id_response)
            responseOk= self.response_custom("Success", id_response.data, status=status.HTTP_200_OK)
            return Response(responseOk)
        responseOk= self.response_custom("Error", "No hay datos", status=status.HTTP_200_OK)
        return Response(responseOk)

    def put(self, request, pk, format = None):
        id_response = self.get_object(pk)
        archivo = request.data['url_img']
        nombre, formato = os.path.splitext(archivo.name)
        request.data['name_img'] = nombre
        request.data['format_img'] = formato
        serializer = ImagenSerializer(id_response, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responseOk = self.response_custom("Success", datas, status = status.HTTP_201_CREATED)
            return Response(responseOk)
        responseOk = self.response_custom("Error", serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response(responseOk)

    def delete(self, request, pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response.url_img.delete(save=True)
            id_response.delete()
            return Response(self.response_custom("Success", "Eliminado", status=status.HTTP_200_OK))
        return Response(self.response_custom("Error", "No se ha podido eliminar", status=status.HTTP_400_BAD_REQUEST))