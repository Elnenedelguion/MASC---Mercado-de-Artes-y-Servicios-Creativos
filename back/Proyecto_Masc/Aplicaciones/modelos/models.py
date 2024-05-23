# masc/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Producto
from .models import Carrito



class Usuario (models.Model):
    id_usuario = models.PositiveIntegerField()  
    nombre = models.CharField(max_length=30)
    email = models.EmailField (max_length=30)
    contraseña = models.CharField (max_length=30)
    token = models.CharField (max_length=30, validators=[RegexValidator(regex='^[a-zA-Z0-9]*$', message='Solo letras y números están permitidos.')])
    bio = models.TextField(blank=True)
    fotodeperfil = models.ImageField(upload_to='profile_pics/', blank=True)
    fecha_creacion_usuario = models.DateTimeField(default=timezone.now)

  
class Mensaje (models.Model):
    id_mensaje= models.PositiveIntegerField()  
    remitente = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    asunto = models.CharField(max_length=500)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    fecha_creacion_mensaje = models.DateTimeField(default=timezone.now)



class Pago(models.Model):
    id_producto = models.PositiveIntegerField()  
    fecha = models.DateTimeField(default=timezone.now)
  
class Categoria (models.Model):
    id_categoria = models.PositiveIntegerField()  
    nombre_categoria = models.CharField(max_length=100)
    fecha_creacion_categoria = models.DateTimeField(default=timezone.now)

class Subcategoria (models.Model):
    id_subcategoria = models.PositiveIntegerField()  
    nombre_subcategoria = models.CharField(max_length=100)
    fecha_creacion_subcategoria = models.DateTimeField(default=timezone.now)

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, related_name='productos', on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion_producto = models.DateTimeField(default=timezone.now)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    class Carrito(models.Model):
     id_carrito = models.PositiveIntegerField()
     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
     productos = models.ManyToManyField(Producto, through='CarritoProducto')
     total = models.DecimalField(max_digits=10, decimal_places=2)

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
