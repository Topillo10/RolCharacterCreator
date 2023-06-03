from django.shortcuts import render, redirect
from ImprimirHoja.views import dibujar_hoja
from CreacionPJ.models import RazasTabla1, Habilidades_Secundarias
from GuardarPersonaje.models import Personaje, Personaje_HabSec, Personaje_Idiomas, Personaje_Sort, Personaje_PDH
from CreacionPJ.forms import SortilegiosPersonajeForm, IdiomasPersonajeForm
from PuntosHistorial.forms import HabPrimForm, HabSecForm, ConocimientosForm
import random

# Create your views here.

def puntos_de_historial(request):
    nombre_pj=request.session.get('nombre_pj')
    usuario=request.session.get('usuario')
    nivel=request.session.get('nivel')
    puntos_de_historial=request.session.get('nivel')
    pdh=request.session.get('pdh')

    dibujar_hoja(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel)
    tirada = random.randint(1, 100)
    
    request.session['nombre_pj']=nombre_pj
    request.session['usuario']=usuario
    request.session['nivel']=nivel
    request.session['tirada']=tirada
    request.session['puntos_de_historial']=puntos_de_historial
    request.session['pdh']=pdh

    context={"puntos_de_historial":puntos_de_historial}

    return render(request, "PuntosHistorial/PDH.html", context)

def pdh_1(request):
    pdh=request.session.get('pdh')
    nombre_pj=request.session.get('nombre_pj')
    usuario=request.session.get('usuario')
    nivel=request.session.get('nivel')
    tirada=request.session.get('tirada')
    puntos_de_historial=request.session.get('puntos_de_historial')

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
        personaje[86:91],       #[5][0] objetos
        personaje[91:98],       #[5][1]
        personaje[98:102],      #[5][2]
        personaje[102:106],     #[5][3]
        personaje[106:109],     #[5][4]
        personaje[109:113],     #[5][5]
        [],                     #[5][6]
        personaje[113:119]      #[5][7]
        ],
        lista_idiomas,          #[6] idiomas
        lista_sortilegios,      #[7] habilidades secundarias
        ]
    
    dato=0

    if tirada == 1:
        #Elegir habilidad primaria
        form = HabPrimForm(request.POST)
    elif tirada == 26:
        #Elegir habilidad secundaria 
        form = HabSecForm(request.POST, dominio=personaje[1][17], profesion=personaje[1][15], nombre_pj=personaje[1][0], usuario=personaje[1][1], nivel=personaje[1][16])
    elif tirada == 46:
        #Elegir lista de sortilegios 
        form = SortilegiosPersonajeForm(request.POST, dominio=personaje[1][17], profesion=personaje[1][15], nombre_pj=personaje[1][0], usuario=personaje[1][1], nivel=personaje[1][16])
    elif tirada == 65:
        # Elegir habilidad secundaria (conocimientos)
        form = ConocimientosForm(request.POST, dominio=personaje[1][17], profesion=personaje[1][15], nombre_pj=personaje[1][0], usuario=personaje[1][1], nivel=personaje[1][16])
    elif tirada == 67:
        #Elegir idioma
        form = IdiomasPersonajeForm(request.POST, nombre_pj=personaje[1][0], usuario=personaje[1][1], nivel=personaje[1][16])
    elif tirada == 92:
        #Elegir caracteristica
        personaje[0][dato]=personaje[0][dato]+1
    elif tirada == 100:
        #Elegir tirada
        funcion_hab_esp = dict_func_hab_esp[tirada]
        funcion_hab_esp=funcion_hab_esp(personaje)

    dict_func_hab_esp= {
        1: hab_esp_1,
        26: hab_esp_26,
        34: hab_esp_34,
        35: hab_esp_35,
        36: hab_esp_36,
        37: hab_esp_37,
        38: hab_esp_38,
        39: hab_esp_39,
        40: hab_esp_40,
        41: hab_esp_41,
        42: hab_esp_42,
        43: hab_esp_43,
        44: hab_esp_44,
        45: hab_esp_45,
        46: hab_esp_46,
        47: hab_esp_47,
        48: hab_esp_48,
        49: hab_esp_49,
        50: hab_esp_50,
        51: hab_esp_51,
        52: hab_esp_52,
        53: hab_esp_53,
        54: hab_esp_54,
        55: hab_esp_55,
        56: hab_esp_56,
        57: hab_esp_57,
        58: hab_esp_58,
        59: hab_esp_59,
        60: hab_esp_60,
        61: hab_esp_61,
        62: hab_esp_62,
        63: hab_esp_63,
        64: hab_esp_64,
        65: hab_esp_65,
        66: hab_esp_66,
        67: hab_esp_67,
        68: hab_esp_68,
        69: hab_esp_69,
        70: hab_esp_70,
        71: hab_esp_71,
        72: hab_esp_72,
        73: hab_esp_73,
        74: hab_esp_74,
        75: hab_esp_75,
        76: hab_esp_76,
        77: hab_esp_77,
        78: hab_esp_78,
        79: hab_esp_79,
        80: hab_esp_80,
        81: hab_esp_81,
        82: hab_esp_82,
        83: hab_esp_83,
        84: hab_esp_84,
        85: hab_esp_85,
        86: hab_esp_86,
        87: hab_esp_87,
        88: hab_esp_88,
        89: hab_esp_89,
        90: hab_esp_90,
        91: hab_esp_91,
        92: hab_esp_92,
        93: hab_esp_93,
        94: hab_esp_94,
        95: hab_esp_95,
        96: hab_esp_96,
        97: hab_esp_97,
        98: hab_esp_98,
        99: hab_esp_99,
        100: hab_esp_100,
    }

    tirada_original=tirada

    if tirada < 26:
        tirada = 1
    elif tirada < 34:
        tirada = 26

    funcion_hab_esp = dict_func_hab_esp[tirada]

    funcion_hab_esp=funcion_hab_esp(personaje)

    request.session['personaje']=personaje
    request.session['tirada']=tirada
    request.session['puntos_de_historial']=puntos_de_historial
    request.session['dict_func_hab_esp']=dict_func_hab_esp
    request.session['pdh']=pdh
    request.session['funcion_hab_esp']=funcion_hab_esp

    context={
        "tirada":tirada,
        "tirada_original":tirada_original,
        "hab_esp_resumido":funcion_hab_esp[1],
        "hab_esp_completo":funcion_hab_esp[2],
        "form":form,
    }

    return render(request, "PuntosHistorial/PDH_Hab_Esp.html", context)

def pdh_1_accept(request):

    pdh=request.session.get('pdh')
    personaje=request.session.get('personaje')
    tirada=request.session.get('nivel')
    puntos_de_historial=request.session.get('puntos_de_historial') #puntos restantes
    dict_func_hab_esp=request.session.get('dict_func_hab_esp')
    funcion_hab_esp=request.session.get('funcion_hab_esp')

    puntos_de_historial=puntos_de_historial-1

    dato=0

    if tirada == 1:
        #Elegir habilidad primaria
        personaje[4][dato]=personaje[4][dato]+5
    elif tirada == 26:
        #Elegir habilidad secundaria 
        personaje[3][dato][2]=personaje[3][dato][2]+15
    elif tirada == 46:
        #Elegir lista de sortilegios
        personaje[7].append(dato)
    elif tirada == 65:
        for i in dato:
            personaje[6].append([i,5,0])
    elif tirada == 67:
        #Elegir idioma
        personaje[6].append([dato, 5])
    elif tirada == 92:
        #Elegir caracteristica
        personaje[0][dato]=personaje[0][dato]+1
    elif tirada == 100:
        #Elegir tirada
        funcion_hab_esp = dict_func_hab_esp[tirada]
        funcion_hab_esp=funcion_hab_esp(personaje)

    pdh.append(funcion_hab_esp[1])

    request.session['pdh']=pdh                                  #puntos de historial elegidos
    request.session['tirada']=tirada
    request.session['puntos_de_historial']=puntos_de_historial  #puntos restantes
    request.session['personaje']=personaje

    return redirect("Historial")

###########################################################################################################
##                                      CAPACIDADES ESPECIALES                                           ##
###########################################################################################################

def hab_esp_1(personaje):
    return (True, '+5 Hab. Prim.', 'Bonificación especial de +5 a una habilidad primaria cualquiera.')

def hab_esp_26(personaje):
    if len(personaje[3])==0:
        return [False]
    else:
        return (True, '+15 Hab. Sec.', 'Bonificación especial de +15 a una habilidad secundaria cualquiera.')

def hab_esp_34(personaje):
    return (True, 'Empatía con animal', 'Empatía con una especie de animal: se comienza con una mascota o leal acompañante de dicha especie. Cualquier maniobra con o sobre un animal de dicha especie recibe una bonificación especial de +25.')

def hab_esp_35(personaje):
    return (True, 'Infravisión', 'Infravisión: capacidad de ver las fuentes de calor en la oscuridad. El alcance es hasta 30m.')

def hab_esp_36(personaje):
    return (True, 'Olfato distinguido', 'Olfato distinguido: el Pj puede discernir la localización exacta de la fuente de cualquier olor, siempre que dicha fuente se halle a menos de 30 metros y falle una TR contra un ataque de nivel 10.')

def hab_esp_37(personaje):
    return (True, 'Oido agudo', 'Oido agudo: El Pj puede discernir la localización exacta de cualquier sonido, siempre que dicha fuente se halla a menos de 30 metros y falle una TR contra un ataque de nivel 10.')

def hab_esp_38(personaje):
    return (True, 'Tacto extremo', 'Tacto extremo: El Pj es capaz de distinguir hasta los relieves más suaves con el simple tacto. +50 a los intentos de descubrir trampas y puertas secretas mediante este método.')

def hab_esp_39(personaje):
    return (True, 'Gran gusto', 'Gran gusto: el Pj es capaz de separar cualquier mezcla de sabores. Es capaz de descubrir cualquier tipo de veneno antes de tragarlo si previamente ha podido estudiar su sabor.')

def hab_esp_40(personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Seducción":
            personaje[3][i][2] = personaje[3][i][2] + 25
    return (True, 'Gran seductor/a', 'Gran seductor/a: cae bien a todas las personas del sexo contrario en la primera impresión. +25 a seducir.')

def hab_esp_41(personaje):
    for i in range(6):
        personaje[4][i+27]=personaje[4][i+27]+10
    return (True, 'Resistencia', 'Resistencia: una bonificación especial de +10 a las TR contra algún tipo de adversidad, normalmente los sortilegios de esencia, los de canalización, los de mentalismo, los venenos o las enfermedades.')

def hab_esp_42(personaje):
    return (True, 'Orientación especial', 'Orientación especial: el Pj siempre sabra donde está el norte, no importa donde se encuentre.')

def hab_esp_43(personaje):
    for i in range(6):
        personaje[4][i+27]=personaje[4][i+27]+10
    return (True, 'Resistencia extraordinaria', 'Resistencia extraordinaria: una bonificación especial de +10 a todas las TR que haga.')

def hab_esp_44(personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Voluntad":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Fuerza interior', 'El Pj dispone de una destacada fuerza interior: +10 a la Voluntad.')

def hab_esp_45(personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Frenesí":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Frensí', 'El Pj se enfurece y pierde el control con facilidad: +10 al frenesí.')

def hab_esp_46(personaje):
    return (True, 'Lista extra Sort.', 'Eficacia con los sortilegios: se comienza teniendo una lista de sortilegios extra (esta opción de historial sólo se puede escoger una vez). El tipo de la lista sigue estando limitado por la profesión o la raza.')

def hab_esp_47(personaje):
    return (True, 'Resistencia alcólica', 'Resistencia alcólica: el Pj es capaz de resistir cantidades asombrosas de alcohol.')

def hab_esp_48(personaje):
    for i in range(6):
        personaje[4][i]=personaje[4][i]+10
    return (True, '+10 MM', 'Buenas aptitudes para las maniobras de movimiento: bonificación especial de +10 a todas las MM.')

def hab_esp_49(personaje):
    personaje[4][15]=personaje[4][15]+10
    personaje[4][23]=personaje[4][23]+10
    return (True, 'Muy observador', 'Muy observador: +10 a la percepción, rastrear y orientación.')

def hab_esp_50(personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Tácticas" or personaje[3][i][0] == "Oratoria":
            personaje[3][i][2] = personaje[3][i][2] + 10
    personaje[4][24]=personaje[4][24]+10
    return (True, 'Lider nato', 'Lider nato: +10 al Liderazgo, Tácticas y oratoria.')

def hab_esp_51(personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Construir trampas":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Conocimientos de mecánica', 'Conocimientos de mecánica: +10 a construir trampas, descubrir puertas secretas y descubrir trampas en interiores.')

def hab_esp_52(personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Primeros Auxilios" or personaje[3][i][0] == "Supervivencia" or personaje[3][i][0] == "Forrajear":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Superviviente', 'El pj fue abandonado en condiciones extremas (en un desierto, en medio de un bosque...) y sobrevivió. +10 a la supervivencia, forrajear y primeros auxilios.')

def hab_esp_53(personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Investigación" or personaje[3][i][0] == "Ocultismo":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'El pj es un detective nato', 'El pj es un detective nato: +10 a investigación y ocultismo.')

def hab_esp_54(personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Comercio/Negociar" or personaje[3][i][0] == "Administración":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'El pj se crió en un ambiente mercader', 'El pj se crió en un ambiente mercader: +10 al comercio, evaluación, administración y matemáticas.')

def hab_esp_55(personaje):
    for i in range(len(personaje[3])):
        if personaje[3][i][0] == "Navegar" or personaje[3][i][0] == "Conocimiento del cielo" or personaje[3][i][0] == "Cordeleria":
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'El pj se crió en ambiente marinero', 'El pj se crió en ambiente marinero: +10 a navegación, conocimiento del cielo y cordelería.')

def hab_esp_56(personaje):
    personaje[4][20]=personaje[4][20]+10
    return (True, 'Educación mágica', 'Educación mágica: el Pj ha recibido una educación o ha podido estudiar la magia durante su infancia. +10 a Leer Runas y Conocimiento de magia.')

def hab_esp_57(personaje):
    for i in range(7):
        personaje[4][i+6]=personaje[4][i+6]+10
    personaje[4][22]=personaje[4][22]+10
    return (True, 'Reflejos rápidos', 'Reflejos rápidos: +5 a la BD y a todas las BO.')

def hab_esp_58(personaje): 
    queryset = Habilidades_Secundarias.objects.filter(tipo__in=["Sociales", "Artísticas"]).values_list('hab_sec', flat=True)
    for i in range(len(personaje[3])):
        if personaje[3][i][0] in queryset:
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Carismático', 'Carismático: +10 a las habilidades sociales y artísticas.')

def hab_esp_59(personaje):
    queryset = Habilidades_Secundarias.objects.filter(tipo__in=["Académicas"]).values_list('hab_sec', flat=True)
    for i in range(len(personaje[3])):
        if personaje[3][i][0] in queryset:
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Maestro ejemplar', 'Maestro ejemplar: +10 a las habilidades académicas.')

def hab_esp_60(personaje):
    queryset = Habilidades_Secundarias.objects.filter(tipo__in=["Callejeras"]).values_list('hab_sec', flat=True)
    for i in range(len(personaje[3])):
        if personaje[3][i][0] in queryset:
            personaje[3][i][2] = personaje[3][i][2] + 10    
    return (True, 'Se crió en las calles', 'El Pj se ha criado en las calles o ha tenido un gran contacto con ellas: +10 a las habilidades callejeras.')

def hab_esp_61(personaje):
    queryset = Habilidades_Secundarias.objects.filter(tipo__in=["Manuales"]).values_list('hab_sec', flat=True)
    for i in range(len(personaje[3])):
        if personaje[3][i][0] in queryset:
            personaje[3][i][2] = personaje[3][i][2] + 10    
    return (True, 'Precisión manual', 'Precisión manual: +10 a las habilidades manuales.')

def hab_esp_62(personaje):
    queryset = Habilidades_Secundarias.objects.filter(tipo__in=["Exteriores"]).values_list('hab_sec', flat=True)
    for i in range(len(personaje[3])):
        if personaje[3][i][0] in queryset:
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Crianza en contacto con la naturaleza', 'Crianza en contacto con la naturaleza: +10 a las habilidades exteriores.')

def hab_esp_63(personaje):
    queryset = Habilidades_Secundarias.objects.filter(tipo__in=["Atleticas"]).values_list('hab_sec', flat=True)
    for i in range(len(personaje[3])):
        if personaje[3][i][0] in queryset:
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Cuerpo atlético', 'Cuerpo atlético: +10 a las habilidades atléticas.')

def hab_esp_64(personaje):
    queryset = Habilidades_Secundarias.objects.filter(tipo__in=["Religiosas"]).values_list('hab_sec', flat=True)
    for i in range(len(personaje[3])):
        if personaje[3][i][0] in queryset:
            personaje[3][i][2] = personaje[3][i][2] + 10
    return (True, 'Se crió en una sociedad religiosa', 'El Pj se ha criado con la sociedad religiosa de su cultura: +10 a las habilidades religiosas.')

def hab_esp_65(personaje):
    return (True, 'Viajero', 'El Pj ha viajado mucho a lo largo de su vida. Dispone de 3 habilidades de Conocimientos de la Tierra Media a escoger entre él y el Dj con 5 cuadros.')

def hab_esp_66(personaje):
    return (True, 'Predicción onírica', 'Predicción onírica: cada cierto tiempo, el Pj padece sueños en los cuales puede vislumbrar posibles futuros (a interpretar por el Dj)')

def hab_esp_67(personaje):
    return (True, 'Crianza con cultura extranjera', 'Crianza con cultura extranjera: el Pj, por alguna razón, ha pasado parte de su infancia con una cultura extraña a la suya, pudiendo aprender su idioma hasta grado 5. (Idiomas a los que normalmente el Dj no deja acceso nada más hacerse el personaje).')

def hab_esp_68(personaje):
    return (True, 'Afinidad con las plantas', 'Afinidad con las plantas: el Pj posee una afinidad especial por las plantas y es capaz de "notar" lo que les ocurre.')

def hab_esp_69(personaje):
    return (True, 'Afinidad con los animales', 'Afinidad con los animales: el Pj es capaz de comprender a los animales y de comunicarse con ellos mediante gestos simples (tratar como un idioma a grado 3 a la hora de entenderlos y como uno de grado 2 a la hora de comunicarles ideas).')

def hab_esp_70(personaje):
    return (True, 'Memoria fotográfica', r'Memoria fotográfica: 40% + bonus de inteligencia de recordar algo visto u oido.')

def hab_esp_71(personaje):
    return (True, 'Sexto sentido', r'Sexto sentido: 40% + bonus de intuición de intuir peligros acechantes.')

def hab_esp_72(personaje):
    return (True, 'Curación rápida', r'Curación rápida: el Pj sólo necesita el 40% + bonus de constitución de tiempo para curarse (máximo 80%).')

def hab_esp_73(personaje):
    return (True, 'Concentración mental', 'Concentración mental: el Pj es capaz de estudiar sin importar el medio en el que esté (taberna, a la intemperie, etc..).')

def hab_esp_74(personaje):
    return (True, 'Valiente', 'Valiente: el Pj tiene derecho a dos tiradas de resistencia de voluntad.')

def hab_esp_75(personaje):
    return (True, 'Resistencia a las enfermedades', 'Resistencia a las enfermedades: el Pj tiene derecho a dos tiradas de resistencia contra enfermedades. Si es un elfo puede volver a tirar.')

def hab_esp_76(personaje):
    if personaje[1][2].startswith("Elfo"):
        return [False]
    else:
        return (True, 'Resistencia a los venenos', 'Resistencia a los venenos: el Pj tiene derecho a dos tiradas de resistencia contra venenos.')

def hab_esp_77(personaje):
    return (True, 'Rapidez de estudio', 'Rapidez de estudio: el Pj aprende listas con la mitad del tiempo normal.')

def hab_esp_78(personaje):
    return (True, 'Facilidad con los idiomas', 'Facilidad con los idiomas: el Pj sólo necesita gastarse la mitad de puntos para aprender un idioma hasta el grado que quiera. Esto NO quiere decir que los puntos que tenga en idiomas se doblen.')

def hab_esp_79(personaje):
    if personaje[1][2].startswith("Elfo"):
        return [False]
    else:
        return (True, 'Meditación natural', 'Meditación natural: el Pj es capaz de entrar en trance meditativo sin necesidad de tirar. Si es un elfo puede volver a tirar.')

def hab_esp_80(personaje):
    return (True, 'Consciencia alerta', 'Consciencia alerta: el Pj no puede quedar aturdido, aunque si puede quedar obligado a parar.')

def hab_esp_81(personaje):
    return (True, 'Concentración distinguida', 'Concentración distinguida: todas aquellas acciones que necesitan prepararse durante un tiempo se reducen en 1 asalto (sortilegios, movimientos adrenales, etc...).')

def hab_esp_82(personaje):
    return (True, 'Resistencia a la sobrecarga de peso', r'Resistencia a la sobrecarga de peso: el Pj es capaz de llevar un 25% de peso más de lo permitido.')

def hab_esp_83(personaje):
    return (True, 'Resistencia al cansancio', 'Resistencia al cansancio: el Pj aguante excelentemente el cansancio. Cada grado de agotamiento se reduce en uno (extenuado -30 pasa a cansado -20).')

def hab_esp_84(personaje):
    return (True, 'Endurecimiento de la piel', 'Endurecimiento de la piel: la piel del Pj, por algún motivo a determinar entre Pj y DJ, se ha endurecido más de lo normal. Tratar como C/8.')

def hab_esp_85(personaje):
    return (True, 'Ambidiestro', 'El Pj es ambidiestro. Si ya lo era por tirada normal, volver a tirar.')

def hab_esp_86(personaje):
    return (True, 'Buena capacidad mental', 'Buena capacidad mental: el Pj recibe un punto de poder más por nivel (si normalmente tiene 2 por nivel ahora tendrá 3).')

def hab_esp_87(personaje):
    return (True, 'Afinidad con el mundo de las sombras', 'Afinidad con el mundo de las sombras: el Pj es capaz de distinguir a los espíritus en sus verdaderas formas en el mundo de las sombras, así como una mayor percepción de esta.')

def hab_esp_88(personaje):
    return (True, 'Resistencia a los espectros', 'Resistencia a los espectros: al Pj no le afectan los ataques al alma (incluido el Soplo Negro) que ocasionan los muertos vivientes.')

def hab_esp_89(personaje):
    return (True, 'Resistencia al dolor', 'Resistencia al dolor: +3 a cada tirada de 1D10 para puntos de vida debidas al desarrollo físico como habilidad.')

def hab_esp_90(personaje):
    if personaje[1][2].startswith("Elfo"):
        return [False]
    else:
        return (True, 'Larga esperanza de vida', r'Larga esperanza de vida: el Pj aumentará en un 20% su esperanza de vida. Si es un elfo volver a tirar.')

def hab_esp_91(personaje):
    return (True, 'Buena constitución', r'Buena constitución: el Pj aumentará en un 20% sus puntos de vida máximos.')

def hab_esp_92(personaje):
    return (True, 'Característica especial', 'Característica especial: el Pj puede sumar uno a una de sus características. Incluso puede subir un 102 a 103.')

def hab_esp_93(personaje):
    personaje[1][17]="Esencia y Canalizacion"
    return (True, 'Afinidad con la magia', 'Afinidad con la magia: el Pj es capaz de manejar dos reinos de magia. Si resulta que ya es un híbrido, podrá manejar el restante.')

def hab_esp_94(personaje):
    if personaje[0][6] < 80:
        personaje[0][6] = 80
    else:
        return False
    return (True, 'Gran hermosura', 'Gran hermosura: si la apariencia del Pj es menor a 80, ahora será 80 más la bonificación de presencia (máximo 102). Si ya era mayor a 80 volver a tirar.')

def hab_esp_95(personaje):
    return (True, 'Transcender armadura', 'Transcender armadura: el Pj es capaz de llevar cualquier tipo de armadura sin que ello interfiera con los sortilegios que puede lanzar.')

def hab_esp_96(personaje):
    return (True, 'Afinidad con los objetos mágicos', 'Afinidad con los objetos mágicos: una vez por aventura (no acumulativo) el Pj aprenderá a usar un objeto mágico sin necesidad de tirar.')

def hab_esp_97(personaje):
    return (True, 'Nacido con buena estrella', 'Nacido con buena estrella: una vez por aventura el PJ puede sumar +100 a una tirada normal de habilidad, o bien evitar ser excluido en una tirada aleatoria entre los Pjs (por ejemplo, para ver a quien le cae la roca que cae desde el acantilado).')

def hab_esp_98(personaje):
    return (True, 'Licantropia', 'El Pj sufre de licantropía.')

def hab_esp_99(personaje):
    return (True, 'Fama y reconocimiento', 'El Pj ha realizado alguna acción importante que le ha proporcionado fama y reconocimiento. Empezará a jugar con un nivel más. Esta opción sólo puede ser escogida una vez.')

def hab_esp_100(personaje):
    return (True, 'Elige una habilidad especial', 'El Pj puede escoger alguna de las capacidades anteriores.')
