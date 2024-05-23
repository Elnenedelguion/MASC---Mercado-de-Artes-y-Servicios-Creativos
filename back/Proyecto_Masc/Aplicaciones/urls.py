# masc/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # incluir otros patrones de URLs mas adelante
]
