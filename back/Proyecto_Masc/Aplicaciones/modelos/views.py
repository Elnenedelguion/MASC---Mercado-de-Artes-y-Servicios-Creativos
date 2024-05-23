# masc/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from .models import Carrito
from .models import CarritoProducto
from .serializers  import CarritoSerializer
from .serializers  import CarritoProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class CarritoProductoViewSet(viewsets.ModelViewSet):
    queryset = CarritoProducto.objects.all()
    serializer_class = CarritoProductoSerializer


