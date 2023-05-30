from django.urls import path
from CreacionPJ import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('levelup', views.levelup, name="LevelUp"),
    path('search', views.search, name="Search"),
    path('news', views.news, name="News"),
    path('pjcreation01', views.pjcreation01, name="PJCreation01"),
    path('pjcreation02', views.pjcreation02, name="PJCreation02"),
    path('asignar_caract_t1', views.elegirt1, name="ElegirT1"),
    path('asignar_caract_t2', views.elegirt2, name="ElegirT2"),
    path('asignar_caract_t3', views.elegirt3, name="ElegirT3"),
    path('pjcreation04', views.pjcreation04, name="PJCreation04"),
    path('pjcreation05', views.pjcreation05, name="PJCreation05"),
    path('pjcreation06', views.pjcreation06, name="PJCreation06"),
    path("agregar/<str:idioma>", views.agregar_grado, name="Agregar"),
    path("restar/<str:idioma>", views.restar_grado, name="Restar"),
    path("agregaridioma", views.agregar_idioma, name="AgregarIdioma"),
    path('salida', views.salida, name="Salida"),
]
