# masc/views.py
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Producto, Carrito, CarritoProducto, HistorialCarrito
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ProductoSerializer, CarritoSerializer, CarritoProductoSerializer, HistorialCarritoSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class CarritoProductoViewSet(viewsets.ModelViewSet):
    queryset = CarritoProducto.objects.all()
    serializer_class = CarritoProductoSerializer

class HistorialCarritoViewSet(viewsets.ModelViewSet):
    queryset = HistorialCarrito.objects.all()
    serializer_class = HistorialCarritoSerializer

    class RegisterView(generics.CreateAPIView):
     queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

