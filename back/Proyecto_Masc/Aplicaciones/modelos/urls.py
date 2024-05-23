
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView
from .views import ProductoViewSet, CarritoViewSet, CarritoProductoViewSet, HistorialCarritoViewSet



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Inicializar el router
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'carritos', CarritoViewSet)
router.register(r'carrito-productos', CarritoProductoViewSet)
router.register(r'historial-carritos', HistorialCarritoViewSet)

# Definir los patrones de URL
urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    # Incluir otros patrones de URLs más adelante si es necesario
]

