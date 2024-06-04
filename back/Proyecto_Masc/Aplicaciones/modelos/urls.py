from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, LogoutView, UsuarioViewSet, PagoViewSet, CategoriaViewSet, SubcategoriaViewSet, ProductoViewSet, CarritoProductoViewSet, HistorialCarritoViewSet, FacturacionViewSet, index, dashboard, login_view, register_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Aplicaciones.modelos.views import index, dashboard, login_view, register_view, logout_view



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
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/login/', LoginView.as_view(), name='auth_login'),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
 
 
]

