
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, UsuarioViewSet, PagoViewSet, CategoriaViewSet, SubcategoriaViewSet, ProductoViewSet,CarritoProductoViewSet, HistorialCarritoViewSet, FacturacionViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Inicializar el router
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pagos', PagoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'subcategorias', SubcategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'carrito_productos', CarritoProductoViewSet)
router.register(r'historial_carritos', HistorialCarritoViewSet)
router.register(r'facturaciones', FacturacionViewSet)

# Definir los patrones de URL
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    # Incluir otros patrones de URLs más adelante si es necesario
]