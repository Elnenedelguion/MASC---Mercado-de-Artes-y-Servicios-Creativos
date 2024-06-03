from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import Usuario, Pago, Categoria, Subcategoria, Producto, CarritoProducto, HistorialCarrito, Facturacion
from .serializers import UsuarioSerializer, PagoSerializer, CategoriaSerializer, SubcategoriaSerializer, ProductoSerializer, CarritoProductoSerializer, HistorialCarritoSerializer, FacturacionSerializer, RegisterSerializer
from .forms import RegisterForm 

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class SubcategoriaViewSet(viewsets.ModelViewSet):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CarritoProductoViewSet(viewsets.ModelViewSet):
    queryset = CarritoProducto.objects.all()
    serializer_class = CarritoProductoSerializer

class HistorialCarritoViewSet(viewsets.ModelViewSet):
    queryset = HistorialCarrito.objects.all()
    serializer_class = HistorialCarritoSerializer

class FacturacionViewSet(viewsets.ModelViewSet):
    queryset = Facturacion.objects.all()
    serializer_class = FacturacionSerializer

class RegisterView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save(password_usuario=make_password(request.data['password_usuario']))
        headers = self.get_success_headers(serializer.data)
        return Response(UsuarioSerializer(usuario).data, status=status.HTTP_201_CREATED, headers=headers)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            request.session.set_expiry(0)  # La sesión expira al cerrar el navegador
            return Response(UsuarioSerializer(user).data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
