from django.shortcuts import render
from GuardarPersonaje.models import Personaje, Personaje_Sort, Personaje_HabSec, Personaje_Idiomas

def guardar_personaje_completo(personaje):
    guardar_personaje(personaje)
    guardar_hab_sec(personaje[3], personaje[1][0], personaje[1][1], personaje[1][16])
    guardar_idiomas(personaje[6], personaje[1][0], personaje[1][1], personaje[1][16])
    guardar_sortilegios(personaje[7], personaje[1][0], personaje[1][1], personaje[1][16])

def guardar_personaje(personaje):

    Personaje.objects.update_or_create(
        nombre_pj=personaje[1][0],
        usuario=personaje[1][1],
        nivel=personaje[1][16],
        defaults={
            "fuerza":personaje[0][0],
            "agilidad":personaje[0][1],
            "constitucion":personaje[0][2],
            "inteligencia":personaje[0][3],
            "intuicion":personaje[0][4],
            "presencia":personaje[0][5],
            "apariencia":personaje[0][6],
            "raza":personaje[1][2],
            "estatura":personaje[1][3],
            "peso":personaje[1][4],
            "genero":personaje[1][5],
            "edad":personaje[1][6],
            "pelo":personaje[1][7],
            "ojos":personaje[1][8],
            "especial_fisico":personaje[1][9],
            "personalidad":personaje[1][10],
            "motivacion":personaje[1][11],
            "alineamiento":personaje[1][12],
            "status":personaje[1][13],
            "familia": personaje[1][14],
            "profesion":personaje[1][15],
            "dominio_magico":personaje[1][17],
            "experiencia":personaje[1][18],
            "gr_sin_armadura":personaje[2][0],
            "gr_cuero":personaje[2][1],
            "gr_cuero_endurecido":personaje[2][2],
            "gr_cota_de_malla":personaje[2][3],
            "gr_coraza":personaje[2][4],
            "gr_de_filo":personaje[2][5],
            "gr_contundentes":personaje[2][6],
            "gr_a_dos_manos":personaje[2][7],
            "gr_arrojadizas":personaje[2][8],
            "gr_proyectiles":personaje[2][9],
            "gr_armas_de_asta":personaje[2][10],
            "gr_escudo":personaje[2][11],
            "gr_trepar":personaje[2][12],
            "gr_montar":personaje[2][13],
            "gr_nadar":personaje[2][14],
            "gr_rastrear":personaje[2][15],
            "gr_emboscar":personaje[2][16],
            "gr_acechar_y_esconderse":personaje[2][17],
            "gr_abrir_cerraduras":personaje[2][18],
            "gr_desactivar_trampas":personaje[2][19],
            "gr_leer_runas":personaje[2][20],
            "gr_usar_objetos":personaje[2][21],
            "gr_sortilegios_dirigidos":personaje[2][22],
            "gr_percepcion":personaje[2][23],
            "gr_liderazgo_e_influencia":personaje[2][24],
            "gr_desarrollo_fisico":personaje[2][25],
            "gr_puntos_de_poder":personaje[2][26],
            "esp_sin_armadura":personaje[4][0],
            "esp_cuero":personaje[4][1],
            "esp_cuero_endurecido":personaje[4][2],
            "esp_cota_de_malla":personaje[4][3],
            "esp_coraza":personaje[4][4],
            "esp_de_filo":personaje[4][5],
            "esp_contundentes":personaje[4][6],
            "esp_a_dos_manos":personaje[4][7],
            "esp_arrojadizas":personaje[4][8],
            "esp_proyectiles":personaje[4][9],
            "esp_armas_de_asta":personaje[4][10],
            "esp_escudo":personaje[4][11],
            "esp_trepar":personaje[4][12],
            "esp_montar":personaje[4][13],
            "esp_nadar":personaje[4][14],
            "esp_rastrear":personaje[4][15],
            "esp_emboscar":personaje[4][16],
            "esp_acechar_y_esconderse":personaje[4][17],
            "esp_abrir_cerraduras":personaje[4][18],
            "esp_desactivar_trampas":personaje[4][19],
            "esp_leer_runas":personaje[4][20],
            "esp_usar_objetos":personaje[4][21],
            "esp_sortilegios_dirigidos":personaje[4][22],
            "esp_percepcion":personaje[4][23],
            "esp_liderazgo_e_influencia":personaje[4][24],
            "esp_desarrollo_fisico":personaje[4][25],
            "esp_puntos_de_poder":personaje[4][26],
            "esp_esencia":personaje[4][27],
            "esp_canalizacion":personaje[4][28],
            "esp_veneno":personaje[4][29],
            "esp_enfermedad":personaje[4][30],
            "esp_frio":personaje[4][31],
            "esp_calor":personaje[4][32],
            "obj_sin_armadura":personaje[5][0][0],
            "obj_cuero":personaje[5][0][1],
            "obj_cuero_endurecido":personaje[5][0][2],
            "obj_cota_de_malla":personaje[5][0][3],
            "obj_coraza":personaje[5][0][4],
            "obj_de_filo":personaje[5][1][0],
            "obj_contundentes":personaje[5][1][1],
            "obj_a_dos_manos":personaje[5][1][2],
            "obj_arrojadizas":personaje[5][1][3],
            "obj_proyectiles":personaje[5][1][4],
            "obj_armas_de_asta":personaje[5][1][5],
            "obj_escudo":personaje[5][1][6],
            "obj_trepar":personaje[5][2][0],
            "obj_montar":personaje[5][2][1],
            "obj_nadar":personaje[5][2][2],
            "obj_rastrear":personaje[5][2][3],
            "obj_emboscar":personaje[5][3][0],
            "obj_acechar_y_esconderse":personaje[5][3][1],
            "obj_abrir_cerraduras":personaje[5][3][2],
            "obj_desactivar_trampas":personaje[5][3][3],
            "obj_leer_runas":personaje[5][4][0],
            "obj_usar_objetos":personaje[5][4][1],
            "obj_sortilegios_dirigidos":personaje[5][4][2],
            "obj_percepcion":personaje[5][5][0],
            "obj_liderazgo_e_influencia":personaje[5][5][1],
            "obj_desarrollo_fisico":personaje[5][5][2],
            "obj_puntos_de_poder":personaje[5][5][3],
            "obj_esencia":personaje[5][7][0],
            "obj_canalizacion":personaje[5][7][1],
            "obj_veneno":personaje[5][7][2],
            "obj_enfermedad":personaje[5][7][3],
            "obj_frio":personaje[5][7][4],
            "obj_calor":personaje[5][7][5],
            }
        )

def guardar_hab_sec(hab_sec, nombre_pj, usuario, nivel):
    if len(hab_sec)==0:
        pass
    else:
        Personaje_HabSec.objects.filter(Personaje_id=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel).id).delete()
        for i in range(len(hab_sec)):
            Personaje_HabSec.objects.create(
                Personaje=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel),
                hab_sec=hab_sec[i][0],
                grados=hab_sec[i][1],
            )

def guardar_idiomas(idiomas, nombre_pj, usuario, nivel):
    if len(idiomas)==0:
        pass
    else:
        Personaje_Idiomas.objects.filter(Personaje_id=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel).id).delete()
        for i in range(len(idiomas)):
            Personaje_Idiomas.objects.create(
                Personaje=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel),
                idiomas=idiomas[i][0],
                grados=idiomas[i][1],               
            )

def guardar_sortilegios(sortilegios, nombre_pj, usuario, nivel):
    if len(sortilegios)==0:
        pass
    else:
        Personaje_Sort.objects.filter(Personaje_id=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel).id).delete()
        for i in range(len(sortilegios)):
            Personaje_Sort.objects.create(
                Personaje=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel),
                lista=sortilegios[i]
            )

   
    
