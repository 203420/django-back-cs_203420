from django.shortcuts import render

# IMPORTACIONES
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class UserAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
