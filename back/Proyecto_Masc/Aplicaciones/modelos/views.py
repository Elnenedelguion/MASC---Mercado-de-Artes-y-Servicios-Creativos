# masc/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto, Carrito, CarritoProducto
from .serializers import ProductoSerializer, CarritoSerializer, CarritoProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class CarritoProductoViewSet(viewsets.ModelViewSet):
    queryset = CarritoProducto.objects.all()
    serializer_class = CarritoProductoSerializer


