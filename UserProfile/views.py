from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import json 

#Importaciones de modelos
from UserProfile.models import UserProfile

#Importaciones de serializadores
from UserProfile.serializers import UserProfileSerializer

# Create your views here.
class UserProfileView(APIView):

    def response_custom(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res=json.dumps(data)
        response = json.loads(res)

        return response

    def get(self, request, format=None):
        queryset = UserProfile.objects.all()
        serializer = UserProfileSerializer(queryset , many=True, context={'request':request})
        response = self.response_custom("success", serializer.data, status=status.HTTP_200_OK)
        return Response(response)

    def post(self, request, format=None):
        serializer = UserProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response= self.response_custom("success", datas, status=status.HTTP_200_OK)
            return Response(response)    
        response= self.response_custom("error", serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(response)


class UserProfileDetail(APIView):
    def response_custom(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res=json.dumps(data)
        response = json.loads(res)

        return response

    def get_object(self, pk):
        try:
            return UserProfile.objects.get(id_user = pk)
        except UserProfile.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response = UserProfileSerializer(id_response)
            return Response(id_response.data, status=status.HTTP_200_OK)
        return Response("No hay datos", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            user_profile.url_image.delete(save=True)
            serializer.save()
            return Response(self.response_custom("Success", serializer.data, status=status.HTTP_200_OK))
        return Response(self.response_custom("Error", serializer.errors, status = status.HTTP_400_BAD_REQUEST))

    def delete(self, request, pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response.delete()
            user = User.objects.filter(id=pk)
            user.delete()
            return Response("Perfil eliminado", status=status.HTTP_200_OK)
        return Response("No se ha podido eliminar", status=status.HTTP_400_BAD_REQUEST)

class UserProfileData (APIView):
    def custom_response_get(self, msg, user, status):
        data ={
            "message": msg,
            "first_name":user[0]['first_name'],
            "last_name":user[0]['last_name'],
            "username":user[0]['username'],
            "email":user[0]['email'],
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response

    def put(self, request, pk, format=None):
        user = User.objects.filter(id=pk)
        user.update(username = request.data.get('username'))
        user.update(email = request.data.get('email'))
        user.update(first_name = request.data.get('first_name'))
        user.update(last_name = request.data.get('last_name'))
        user2 = User.objects.filter(id=pk).values()
        return Response(self.custom_response_get("Actualizado", user2, status=status.HTTP_200_OK))