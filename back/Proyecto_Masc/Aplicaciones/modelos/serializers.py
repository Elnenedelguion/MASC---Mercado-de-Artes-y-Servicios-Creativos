from rest_framework import serializers
from .models import Usuario, Pago, Categoria, Subcategoria, Producto, CarritoProducto, HistorialCarrito, Facturacion

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CarritoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoProducto
        fields = '__all__'

class HistorialCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialCarrito
        fields = '__all__'

class FacturacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facturacion
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'email_usuario', 'password_usuario', 'telefono_usuario', 'bio_usuario', 'fotodeperfil_usuario']

    def create(self, validated_data):
        usuario = Usuario(
            nombre_usuario=validated_data['nombre_usuario'],
            email_usuario=validated_data['email_usuario'],
            telefono_usuario=validated_data['telefono_usuario'],
            bio_usuario=validated_data.get('bio_usuario', ''),
            fotodeperfil_usuario=validated_data.get('fotodeperfil_usuario', None)
        )
        usuario.password_usuario = validated_data['password_usuario']  # Aquí podrías usar make_password para hashear la contraseña
        usuario.save()
        return usuario
