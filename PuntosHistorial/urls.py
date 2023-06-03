from django.urls import path
from PuntosHistorial import views


urlpatterns = [
    path('historial', views.puntos_de_historial, name="Historial"),
    path('historial/hab_esp', views.pdh_1, name="PDH1"),
]
