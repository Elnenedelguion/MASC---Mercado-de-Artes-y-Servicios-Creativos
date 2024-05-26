
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone


class Usuario (models.Model):
    id_usuario = models.PositiveIntegerField()  
    nombre = models.CharField(max_length=30)
    email = models.EmailField (max_length=30)
    contraseña = models.CharField (max_length=30)
    token = models.CharField (max_length=30, validators=[RegexValidator(regex='^[a-zA-Z0-9]*$', message='Solo letras y números están permitidos.')])
    bio = models.TextField(blank=True)
    fotodeperfil = models.ImageField(upload_to='profile_pics/', blank=True)
    fecha_creacion_usuario = models.DateTimeField(default=timezone.now)

  


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


    
   



