# masc/serializers.py
from rest_framework import serializers
from .models import Producto, Carrito, CarritoProducto, HistorialCarrito


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class CarritoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoProducto
        fields = '__all__'

class HistorialCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialCarrito
        fields = '__all__'



