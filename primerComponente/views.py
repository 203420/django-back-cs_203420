from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json 

#Importaciones de modelos
from primerComponente.models import PrimerTabla

#Importaciones de serializadores
from primerComponente.serializers import PrimerTablaSerializer

# Create your views here.
class PrimerTablaList(APIView):

    def response_custom(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res=json.dumps(data)
        responseOk = json.loads(res)

        return responseOk


    def get(self, request, format=None):
        queryset = PrimerTabla.objects.all()
        serializer = PrimerTablaSerializer(queryset , many=True, context={'request':request})
        response= self.response_custom("success", serializer.data, status=status.HTTP_200_OK)
        return Response(response)

    def post(self, request, format=None):
        serializer = PrimerTablaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response= self.response_custom("success", datas, status=status.HTTP_200_OK)
            return Response(response)
            
        response= self.response_custom("error", serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(response)

class PrimerTablaDetail(APIView):
    def get_object(self, pk):
        try:
            return PrimerTabla.objects.get(pk = pk)
        except PrimerTabla.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response = PrimerTablaSerializer(id_response)
            return Response(id_response.data, status=status.HTTP_200_OK)
        return Response("No hay datos", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id_response = self.get_object(pk)
        serializer = PrimerTablaSerializer(id_response, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response.delete()
            return Response(status=status.HTTP_200_OK)
        return Response("No se ha podido eliminar", status=status.HTTP_400_BAD_REQUEST)

