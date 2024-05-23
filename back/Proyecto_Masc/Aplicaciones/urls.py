# masc/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CarritoViewSet, CarritoProductoViewSet

# Inicializar el router
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'carritos', CarritoViewSet)
router.register(r'carrito-productos', CarritoProductoViewSet)

# Definir los patrones de URL
urlpatterns = [
    path('', include(router.urls)),
    # Incluir otros patrones de URLs más adelante si es necesario
]
