from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CreacionPJ.urls')),
    path('', include('GuardarPersonaje.urls')),
    path('', include('ImprimirHoja.urls')),
    path('', include('PuntosHistorial.urls')),
]