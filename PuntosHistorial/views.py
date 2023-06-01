from django.shortcuts import render
from CreacionPJ.models import RazasTabla1
from GuardarPersonaje.models import Personaje, Personaje_HabSec, Personaje_Idiomas, Personaje_Sort
from ImprimirHoja.views import dibujar_hoja

# Create your views here.

def puntos_de_historial(request):
    nombre_pj=request.session.get('nombre_pj')
    usuario=request.session.get('usuario')
    nivel=request.session.get('nivel')
    
    dibujar_hoja(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel)

    raza = Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel).raza
    puntos_de_historial=RazasTabla1.objects.get(raza__exact=raza).puntos_de_historial

    context={"puntos_de_historial":puntos_de_historial}

    return render(request, "PuntosHistorial/PDH.html", context)

def pdh(request, tipo_pdh, dato, nombre_pj, usuario, nivel):
    
    pj= Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel)
    personaje=[
        value for key, value in pj.__dict__.items()
        if key not in ['id', '_state']
    ]
    
    inst_habilidades_secundarias=Personaje_HabSec.objects.filter(Personaje_id=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel).id)
    lista_hab_sec = [[habilidad_secundaria.hab_sec, habilidad_secundaria.grados] for habilidad_secundaria in inst_habilidades_secundarias]
    
    inst_idiomas=Personaje_Idiomas.objects.filter(Personaje_id=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel).id)
    lista_idiomas = [[idioma.idiomas, idioma.grados] for idioma in inst_idiomas]
    
    inst_sortilegios=Personaje_Sort.objects.filter(Personaje_id=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel).id)
    lista_sortilegios = [sortilegio.lista for sortilegio in inst_sortilegios]

    personaje=[
        personaje[0:7],         #[0] caracteristicas
        personaje[7:26],        #[1] datos basicos
        personaje[26:53],       #[2] grados hab. prim
        lista_hab_sec,          #[3] hab sec
        personaje[53:86],       #[4] bonif. esp hab. prim
        [
        personaje[86:91],       #[5][0]
        personaje[91:98],       #[5][1]
        personaje[98:102],      #[5][2]
        personaje[102:106],     #[5][3]
        personaje[106:109],     #[5][4]
        personaje[109:113],     #[5][5]
        [],                     #[5][6]
        personaje[113:119]      #[5][7]
        ],
        lista_idiomas,          #[6]
        lista_sortilegios,      #[7]
        ]
    
    if tipo_pdh == 1:           #Hab. Esp.
        hab_esp_1(dato, personaje)
    elif tipo_pdh == 2:         #Obj. Esp.
        pass
    elif tipo_pdh == 3:         #Dinero
        pass
    elif tipo_pdh == 4:         #Idioma
        pass
    elif tipo_pdh == 5:         #+1 x 3 Caract.
        pass
    elif tipo_pdh == 6:         #+2 x 1 Caract.
        pass
    elif tipo_pdh == 7:         #+2 grados Hab. Prim.
        pass
    elif tipo_pdh == 8:         #+5 grados Hab. Sec.
        pass

def hab_esp_1(dato, personaje):
    personaje[4][dato]=personaje[4][dato]+5
    return (True, '+5 Hab. Prim.', 'Bonificación especial de +5 a una habilidad primaria cualquiera.')

def hab_esp_26(dato, personaje):
    if len(personaje[3])==0:
        return [False]
    else:
        personaje[3][dato][2]=personaje[3][dato][2]+15
        return (True, '+15 Hab. Sec.', 'Bonificación especial de +15 a una habilidad secundaria cualquiera.')

def hab_esp_34(dato, personaje):
    return (True, 'Empatía con animal', 'Empatía con una especie de animal: se comienza con una mascota o leal acompañante de dicha especie. Cualquier maniobra con o sobre un animal de dicha especie recibe una bonificación especial de +25.')

def hab_esp_35(dato, personaje):
    return (True, 'Infravisión', 'Infravisión: capacidad de ver las fuentes de calor en la oscuridad. El alcance es hasta 30m.')

def hab_esp_36(dato, personaje):
    return (True, 'Olfato distinguido', 'Olfato distinguido: el Pj puede discernir la localización exacta de la fuente de cualquier olor, siempre que dicha fuente se halle a menos de 30 metros y falle una TR contra un ataque de nivel 10.')

def hab_esp_37(dato, personaje):
    return (True, 'Oido agudo', 'Oido agudo: El Pj puede discernir la localización exacta de cualquier sonido, siempre que dicha fuente se halla a menos de 30 metros y falle una TR contra un ataque de nivel 10.')

def hab_esp_38(dato, personaje):
    return (True, 'Tacto extremo', 'Tacto extremo: El Pj es capaz de distinguir hasta los relieves más suaves con el simple tacto. +50 a los intentos de descubrir trampas y puertas secretas mediante este método.')

def hab_esp_39(dato, personaje):
    return (True, 'Gran gusto', 'Gran gusto: el Pj es capaz de separar cualquier mezcla de sabores. Es capaz de descubrir cualquier tipo de veneno antes de tragarlo si previamente ha podido estudiar su sabor.')

def hab_esp_40(dato, personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Seducción":
            personaje[3][i][2] = personaje[3][i][2] + 25
    return (True, 'Gran seductor/a', 'Gran seductor/a: cae bien a todas las personas del sexo contrario en la primera impresión. +25 a seducir.')

def hab_esp_41(dato, personaje):
    for i in range(6):
        personaje[4][i+27]=personaje[4][i+27]+10
    return (True, 'Resistencia', 'Resistencia: una bonificación especial de +10 a las TR contra algún tipo de adversidad, normalmente los sortilegios de esencia, los de canalización, los de mentalismo, los venenos o las enfermedades.')

def hab_esp_42(dato, personaje):
    return (True, 'Orientación especial', 'Orientación especial: el Pj siempre sabra donde está el norte, no importa donde se encuentre.')

def hab_esp_43(dato, personaje):
    for i in range(6):
        personaje[4][i+27]=personaje[4][i+27]+10
    return (True, 'Resistencia extraordinaria', 'Resistencia extraordinaria: una bonificación especial de +10 a todas las TR que haga.')

def hab_esp_44(dato, personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Voluntad":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Fuerza interior', 'El Pj dispone de una destacada fuerza interior: +10 a la Voluntad.')

def hab_esp_45(dato, personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Frenesí":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Frensí', 'El Pj se enfurece y pierde el control con facilidad: +10 al frenesí.')

def hab_esp_46(dato, personaje):
    personaje[7].append(dato)

    return (True, 'Lista extra Sort.', 'Eficacia con los sortilegios: se comienza teniendo una lista de sortilegios extra (esta opción de historial sólo se puede escoger una vez). El tipo de la lista sigue estando limitado por la profesión o la raza.')

def hab_esp_47(dato, personaje):
    return (True, 'Resistencia alcólica', 'Resistencia alcólica: el Pj es capaz de resistir cantidades asombrosas de alcohol.')

def hab_esp_48(dato, personaje):
    for i in range(6):
        personaje[4][i]=personaje[4][i]+10
    return (True, '+10 MM', 'Buenas aptitudes para las maniobras de movimiento: bonificación especial de +10 a todas las MM.')

def hab_esp_49(dato, personaje):
    personaje[4][15]=personaje[4][15]+10
    personaje[4][23]=personaje[4][23]+10
    return (True, 'Muy observador', 'Muy observador: +10 a la percepción, rastrear y orientación.')

def hab_esp_50(dato, personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Tácticas" or personaje[3][i][0] == "Oratoria":
            personaje[3][i][2] = personaje[3][i][2] + 10
    personaje[4][24]=personaje[4][24]+10
    return (True, 'Lider nato', 'Lider nato: +10 al Liderazgo, Tácticas y oratoria.')

def hab_esp_51(dato, personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Construir trampas":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Conocimientos de mecánica', 'Conocimientos de mecánica: +10 a construir trampas, descubrir puertas secretas y descubrir trampas en interiores.')


def hab_esp_52(dato, personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Primeros Auxilios" or personaje[3][i][0] == "Supervivencia" or personaje[3][i][0] == "Forrajear":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Superviviente', 'El pj fue abandonado en condiciones extremas (en un desierto, en medio de un bosque...) y sobrevivió. +10 a la supervivencia, forrajear y primeros auxilios.')

def hab_esp_53(dato, personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Investigación" or personaje[3][i][0] == "Ocultismo":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'El pj es un detective nato', 'El pj es un detective nato: +10 a investigación y ocultismo.')

def hab_esp_54(dato, personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Comercio/Negociar" or personaje[3][i][0] == "Administración":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'El pj se crió en un ambiente mercader', 'El pj se crió en un ambiente mercader: +10 al comercio, evaluación, administración y matemáticas.')

def hab_esp_55(dato, personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Navegar" or personaje[3][i][0] == "Conocimiento del cielo" or personaje[3][i][0] == "Cordeleria":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'El pj se crió en ambiente marinero', 'El pj se crió en ambiente marinero: +10 a navegación, conocimiento del cielo y cordelería.')

def hab_esp_56(dato, personaje):
    personaje[4][20]=personaje[4][20]+10
    return (True, 'Educación mágica', 'Educación mágica: el Pj ha recibido una educación o ha podido estudiar la magia durante su infancia. +10 a Leer Runas y Conocimiento de magia.')

def hab_esp_57(dato, personaje):
    for i in range(7):
        personaje[4][i+6]=personaje[4][i+6]+10
    personaje[4][22]=personaje[4][22]+10
    return (True, 'Reflejos rápidos', 'Reflejos rápidos: +5 a la BD y a todas las BO.')

## PENSAR ##

# def hab_esp_58(dato, personaje): 
#     for i in range(len(personaje[3])):
#         if personaje[3][i][0] == "Navegar" or personaje[3][i][0] == "Conocimiento del cielo" or personaje[3][i][0] == "Cordeleria":
#             personaje[3][i][2] = personaje[3][i][2] + 10
#     return (True, 'Carismático', 'Carismático: +10 a las habilidades sociales y artísticas.')

def hab_esp_59(dato, personaje):
    return

def hab_esp_60(dato, personaje):
    return

def hab_esp_61(dato, personaje):
    return

def hab_esp_62(dato, personaje):
    return

def hab_esp_63(dato, personaje):
    return

def hab_esp_64(dato, personaje):
    return

def hab_esp_65(dato, personaje):
    return

def hab_esp_66(dato, personaje):
    return

def hab_esp_67(dato, personaje):
    return

def hab_esp_68(dato, personaje):
    return

def hab_esp_69(dato, personaje):
    return

def hab_esp_70(dato, personaje):
    return

def hab_esp_71(dato, personaje):
    return

def hab_esp_72(dato, personaje):
    return

def hab_esp_73(dato, personaje):
    return

def hab_esp_74(dato, personaje):
    return

def hab_esp_75(dato, personaje):
    return

def hab_esp_76(dato, personaje):
    return

def hab_esp_77(dato, personaje):
    return

def hab_esp_78(dato, personaje):
    return

def hab_esp_79(dato, personaje):
    return

def hab_esp_80(dato, personaje):
    return

def hab_esp_81(dato, personaje):
    return

def hab_esp_82(dato, personaje):
    return

def hab_esp_83(dato, personaje):
    return

def hab_esp_84(dato, personaje):
    return

def hab_esp_85(dato, personaje):
    return

def hab_esp_86(dato, personaje):
    return

def hab_esp_87(dato, personaje):
    return

def hab_esp_88(dato, personaje):
    return

def hab_esp_89(dato, personaje):
    return

def hab_esp_90(dato, personaje):
    return

def hab_esp_91(dato, personaje):
    return

def hab_esp_92(dato, personaje):
    return

def hab_esp_93(dato, personaje):
    return

def hab_esp_94(dato, personaje):
    return

def hab_esp_95(dato, personaje):
    return

def hab_esp_96(dato, personaje):
    return

def hab_esp_97(dato, personaje):
    return

def hab_esp_98(dato, personaje):
    return

def hab_esp_99(dato, personaje):
    return

def hab_esp_100(dato, personaje):
    return


