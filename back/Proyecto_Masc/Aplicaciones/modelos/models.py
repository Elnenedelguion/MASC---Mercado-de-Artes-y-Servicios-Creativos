
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=25)
    email_usuario = models.EmailField(max_length=25, unique=True)
    password_usuario = models.CharField(max_length=10)
    telefono_usuario = models.CharField(max_length=15, unique=True)
    token_usuario = models.CharField(max_length=30, blank=True, null=True)
    bio_usuario = models.TextField(blank=True, null=True)
    fotodeperfil_usuario = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    fecha_creacion_usuario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_usuario

class Pago(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=255)
    fecha_pago = models.DateTimeField(default=timezone.now)
    total_pago = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.usuario.nombre_usuario} - {self.metodo_pago} - {self.total_pago}"

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    fecha_creacion_categoria = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre_categoria

class Subcategoria(models.Model):
    nombre_subcategoria = models.CharField(max_length=100)
    fecha_creacion_subcategoria = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_subcategoria

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=255)
    descripcion_producto = models.TextField()
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion_producto = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto

class CarritoProducto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_carrito_producto = models.PositiveIntegerField()
    fecha_carrito = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.cantidad_carrito_producto} de {self.producto.nombre_producto} para {self.usuario.nombre_usuario}"

class HistorialCarrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_historial_carrito = models.DateTimeField(default=timezone.now)
    total_historial_carrito = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Historial de {self.usuario.nombre_usuario} - {self.fecha_historial_carrito}"

class Facturacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total_facturacion = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_facturacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Facturación de {self.usuario.nombre_usuario} - {self.fecha_facturacion}"

