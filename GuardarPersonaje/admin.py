from django.contrib import admin
from .models import Personaje, Personaje_Sort, Personaje_HabSec, Personaje_Idiomas

# Register your models here.

@admin.register(Personaje)
class AdminPersonaje(admin.ModelAdmin):
    list_display = ['usuario' , 'nombre_pj', 'raza', 'profesion', 'nivel']

@admin.register(Personaje_Sort)
class AdminPersonaje_Sort(admin.ModelAdmin):
    list_display = ['Personaje' , 'lista']

@admin.register(Personaje_HabSec)
class AdminPersonaje_HabSec(admin.ModelAdmin):
    list_display = ['Personaje' , 'hab_sec', 'grados']

@admin.register(Personaje_Idiomas)
class AdminPersonaje_Idiomas(admin.ModelAdmin):
    list_display = ['Personaje' , 'idiomas', 'grados']