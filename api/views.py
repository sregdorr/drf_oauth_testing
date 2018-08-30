from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.generics import CreateAPIView

from . import serializers
from . import models


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = serializers.UserSerializer


class VehicleApiView(generics.ListCreateAPIView):
    serializer_class = serializers.VehicleSerializer
    queryset = models.Vehicle.objects.all()



