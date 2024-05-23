# Aplicaciones/modelos/carrito_models.py
from django.db import models
from django.contrib.auth.models import User
from .producto_models import Producto 

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

class HistorialCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.JSONField()  # Almacenar productos como JSON
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
