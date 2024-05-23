# masc/views.py
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Producto, Carrito, CarritoProducto, HistorialCarrito
from .serializers import ProductoSerializer, CarritoSerializer, CarritoProductoSerializer, HistorialCarritoSerializer


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


