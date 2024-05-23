# masc/serializers.py
from rest_framework import serializers
from .models import Producto
from .models import Carrito
from .models import CarritoProducto



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CarritoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoProducto
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    productos = CarritoProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Carrito
        fields = '__all__'
