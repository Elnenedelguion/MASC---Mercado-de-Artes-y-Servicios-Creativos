from django.contrib import admin
from .models import Usuario, Pago, Categoria, Subcategoria, Producto, Carrito,CarritoProducto, HistorialCarrito, Facturacion

admin.site.register(Usuario)
admin.site.register(Pago)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(CarritoProducto)
admin.site.register(HistorialCarrito)
admin.site.register(Facturacion)

