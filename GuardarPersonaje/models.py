from django.db import models

###########################################################################################################
##                                      CREACION DE PERSONAJES                                           ##
###########################################################################################################

class Personaje(models.Model):
    fuerza=models.IntegerField()                                                ## 7 CAMPOS
    agilidad=models.IntegerField()
    constitucion=models.IntegerField()
    inteligencia=models.IntegerField()
    intuicion=models.IntegerField()
    presencia=models.IntegerField()
    apariencia=models.IntegerField()
    
    nombre_pj = models.CharField(max_length=30, blank=True, null=True)         ## 19 CAMPOS
    usuario = models.CharField(max_length=255, blank=True, null=True)
    raza = models.CharField(max_length=30, blank=True, null=True)
    estatura = models.FloatField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    pelo = models.CharField(max_length=50, blank=True, null=True)
    ojos = models.CharField(max_length=50, blank=True, null=True)
    especial_fisico = models.CharField(max_length=100, blank=True, null=True)
    personalidad = models.CharField(max_length=50, blank=True, null=True)
    motivacion = models.CharField(max_length=100, blank=True, null=True)
    alineamiento = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    familia=models.CharField(max_length=50, blank=True, null=True)
    profesion = models.CharField(max_length=30, blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    dominio_magico = models.CharField(max_length=30, blank=True, null=True)
    experiencia = models.IntegerField(blank=True, null=True)

    gr_sin_armadura = models.IntegerField(blank=True, null=True)                   ## 27 CAMPOS
    gr_cuero = models.IntegerField(blank=True, null=True)
    gr_cuero_endurecido = models.IntegerField(blank=True, null=True)
    gr_cota_de_malla = models.IntegerField(blank=True, null=True)
    gr_coraza = models.IntegerField(blank=True, null=True)
    gr_de_filo = models.IntegerField(blank=True, null=True)
    gr_contundentes = models.IntegerField(blank=True, null=True)
    gr_a_dos_manos = models.IntegerField(blank=True, null=True)
    gr_arrojadizas = models.IntegerField(blank=True, null=True)
    gr_proyectiles = models.IntegerField(blank=True, null=True)
    gr_armas_de_asta = models.IntegerField(blank=True, null=True)
    gr_escudo = models.IntegerField(blank=True, null=True)
    gr_trepar = models.IntegerField(blank=True, null=True)
    gr_montar = models.IntegerField(blank=True, null=True)
    gr_nadar = models.IntegerField(blank=True, null=True)
    gr_rastrear = models.IntegerField(blank=True, null=True)
    gr_emboscar = models.IntegerField(blank=True, null=True)
    gr_acechar_y_esconderse = models.IntegerField(blank=True, null=True)
    gr_abrir_cerraduras = models.IntegerField(blank=True, null=True)
    gr_desactivar_trampas = models.IntegerField(blank=True, null=True)
    gr_leer_runas = models.IntegerField(blank=True, null=True)
    gr_usar_objetos = models.IntegerField(blank=True, null=True)
    gr_sortilegios_dirigidos = models.IntegerField(blank=True, null=True)
    gr_percepcion = models.IntegerField(blank=True, null=True)
    gr_liderazgo_e_influencia = models.IntegerField(blank=True, null=True)
    gr_desarrollo_fisico = models.CharField(max_length=255, blank=True, null=True)
    gr_puntos_de_poder = models.CharField(max_length=255, blank=True, null=True)

    esp_sin_armadura = models.IntegerField(blank=True, null=True)                   ## 33 CAMPOS
    esp_cuero = models.IntegerField(blank=True, null=True)
    esp_cuero_endurecido = models.IntegerField(blank=True, null=True)
    esp_cota_de_malla = models.IntegerField(blank=True, null=True)
    esp_coraza = models.IntegerField(blank=True, null=True)
    esp_de_filo = models.IntegerField(blank=True, null=True)
    esp_contundentes = models.IntegerField(blank=True, null=True)
    esp_a_dos_manos = models.IntegerField(blank=True, null=True)
    esp_arrojadizas = models.IntegerField(blank=True, null=True)
    esp_proyectiles = models.IntegerField(blank=True, null=True)
    esp_armas_de_asta = models.IntegerField(blank=True, null=True)
    esp_escudo = models.IntegerField(blank=True, null=True)
    esp_trepar = models.IntegerField(blank=True, null=True)
    esp_montar = models.IntegerField(blank=True, null=True)
    esp_nadar = models.IntegerField(blank=True, null=True)
    esp_rastrear = models.IntegerField(blank=True, null=True)
    esp_emboscar = models.IntegerField(blank=True, null=True)
    esp_acechar_y_esconderse = models.IntegerField(blank=True, null=True)
    esp_abrir_cerraduras = models.IntegerField(blank=True, null=True)
    esp_desactivar_trampas = models.IntegerField(blank=True, null=True)
    esp_leer_runas = models.IntegerField(blank=True, null=True)
    esp_usar_objetos = models.IntegerField(blank=True, null=True)
    esp_sortilegios_dirigidos = models.IntegerField(blank=True, null=True)
    esp_percepcion = models.IntegerField(blank=True, null=True)
    esp_liderazgo_e_influencia = models.IntegerField(blank=True, null=True)
    esp_desarrollo_fisico = models.IntegerField(blank=True, null=True)
    esp_puntos_de_poder = models.IntegerField(blank=True, null=True)
    esp_esencia = models.IntegerField(blank=True, null=True)
    esp_canalizacion = models.IntegerField(blank=True, null=True)
    esp_veneno = models.IntegerField(blank=True, null=True)
    esp_enfermedad = models.IntegerField(blank=True, null=True)
    esp_frio = models.IntegerField(blank=True, null=True)
    esp_calor = models.IntegerField(blank=True, null=True)
    
    obj_sin_armadura = models.IntegerField(blank=True, null=True)                   ## 33 CAMPOS
    obj_cuero = models.IntegerField(blank=True, null=True)
    obj_cuero_endurecido = models.IntegerField(blank=True, null=True)
    obj_cota_de_malla = models.IntegerField(blank=True, null=True)
    obj_coraza = models.IntegerField(blank=True, null=True)
    obj_de_filo = models.IntegerField(blank=True, null=True)
    obj_contundentes = models.IntegerField(blank=True, null=True)
    obj_a_dos_manos = models.IntegerField(blank=True, null=True)
    obj_arrojadizas = models.IntegerField(blank=True, null=True)
    obj_proyectiles = models.IntegerField(blank=True, null=True)
    obj_armas_de_asta = models.IntegerField(blank=True, null=True)
    obj_escudo = models.IntegerField(blank=True, null=True)
    obj_trepar = models.IntegerField(blank=True, null=True)
    obj_montar = models.IntegerField(blank=True, null=True)
    obj_nadar = models.IntegerField(blank=True, null=True)
    obj_rastrear = models.IntegerField(blank=True, null=True)
    obj_emboscar = models.IntegerField(blank=True, null=True)
    obj_acechar_y_esconderse = models.IntegerField(blank=True, null=True)
    obj_abrir_cerraduras = models.IntegerField(blank=True, null=True)
    obj_desactivar_trampas = models.IntegerField(blank=True, null=True)
    obj_leer_runas = models.IntegerField(blank=True, null=True)
    obj_usar_objetos = models.IntegerField(blank=True, null=True)
    obj_sortilegios_dirigidos = models.IntegerField(blank=True, null=True)
    obj_percepcion = models.IntegerField(blank=True, null=True)
    obj_liderazgo_e_influencia = models.IntegerField(blank=True, null=True)
    obj_desarrollo_fisico = models.IntegerField(blank=True, null=True)
    obj_puntos_de_poder = models.IntegerField(blank=True, null=True)
    obj_esencia = models.IntegerField(blank=True, null=True)
    obj_canalizacion = models.IntegerField(blank=True, null=True)
    obj_veneno = models.IntegerField(blank=True, null=True)
    obj_enfermedad = models.IntegerField(blank=True, null=True)
    obj_frio = models.IntegerField(blank=True, null=True)
    obj_calor = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario} - {self.nombre_pj} - {self.raza} - {self.profesion} - Nivel:{self.nivel}" 
    
class Personaje_Sort(models.Model):
    Personaje = models.ForeignKey("Personaje", on_delete=models.CASCADE)
    lista=models.CharField(max_length=30)

    def __str__(self):
        return self.lista

class Personaje_HabSec(models.Model):
    Personaje = models.ForeignKey("Personaje", on_delete=models.CASCADE)
    hab_sec=models.CharField(max_length=20)
    grados=models.IntegerField()
    especial=models.IntegerField()

    def __str__(self):
        return self.hab_sec

class Personaje_Idiomas(models.Model):
    Personaje = models.ForeignKey("Personaje", on_delete=models.CASCADE)
    idiomas=models.CharField(max_length=30)
    grados=models.IntegerField()

    def __str__(self):
        return self.idiomas