from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Aplicaciones.modelos.views import index, dashboard, login_view, register_view, logout_view

router = DefaultRouter()

# Definir los patrones de URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Aplicaciones.modelos.urls')),
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
