from django.contrib import admin
from .models import RazasTabla1, RazasTabla2, RazasTabla3, RazasTabla4, Profesiones
from .models import RazasIdiomas, Habilidades_Secundarias, Sortilegios


@admin.register(RazasTabla1)
class AdminRazasTabla1(admin.ModelAdmin):
    list_display = ['raza']

@admin.register(RazasTabla2)
class AdminRazasTabla2(admin.ModelAdmin):
    list_display = ['raza']

@admin.register(RazasTabla3)
class AdminRazasTabla3(admin.ModelAdmin):
    list_display = ['raza']

@admin.register(RazasTabla4)
class AdminRazasTabla4(admin.ModelAdmin):
    list_display = ['raza']

@admin.register(Profesiones)
class AdminProfesiones(admin.ModelAdmin):
    list_display = ['profesion']

@admin.register(RazasIdiomas)
class AdminRazasIdiomas(admin.ModelAdmin):
    list_display = ['raza', 'grados', 'idiomas']

@admin.register(Habilidades_Secundarias)
class AdminHabilidades_Secundarias(admin.ModelAdmin):
    list_display = ['hab_sec', 'caracteristica', 'tipo']

@admin.register(Sortilegios)
class AdminSortilegios(admin.ModelAdmin):
    list_display = ['lista', 'profesion', 'dominio']

    