from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

# Definir los patrones de URL
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('Aplicaciones.modelos.urls')),
  
]
