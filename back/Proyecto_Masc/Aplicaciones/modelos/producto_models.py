# Aplicaciones/modelos/producto_models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
from .models import Categoria
from .models import Subcategoria

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion_producto = models.DateTimeField(default=timezone.now)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre