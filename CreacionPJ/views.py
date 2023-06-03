from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from CreacionPJ.models import RazasTabla1, RazasTabla2, RazasTabla3, RazasTabla4, Profesiones, DatosBasicos, RazaYProfesion, RazasIdiomas, Sortilegios
from GuardarPersonaje.models import Personaje, Personaje_Sort, Personaje_HabSec, Personaje_Idiomas
import random
from CreacionPJ.forms import DatosBasicosForm, RazaYProfesionForm, CaracteristicasForm, SortilegiosPersonajeForm, IdiomasPersonajeForm
from GuardarPersonaje.views import guardar_personaje, guardar_sortilegios, guardar_idiomas
from ImprimirHoja.views import dibujar_hoja

# Create your views here.

###########################################################################################################

###########################################################################################################

def home(request):
    
    return render(request, "CreacionPJ/home.html")

def levelup(request):

    return render(request, "CreacionPJ/levelup.html")

def news(request):

    return render(request, "CreacionPJ/noticias.html")

def search(request):
    
    return render(request, "CreacionPJ/search.html")

###########################################################################################################

###########################################################################################################

def tirada_caracteristicas():
    listado_tiradas=[]
    for i in range(7):
        tirada = random.randint(30, 100)
        listado_tiradas.append(tirada)
    return listado_tiradas

def pjcreation01(request):
    form = DatosBasicosForm()

    return render(request, "CreacionPJ/pjcreation01.html", {'form':form})

def pjcreation02(request):

    tirada1=tirada_caracteristicas()
    tirada2=tirada_caracteristicas()

    request.session['tirada1']=tirada1
    request.session['tirada2']=tirada2

    if request.method == 'POST':
        form_db01 = DatosBasicosForm(request.POST)
        if form_db01.is_valid():
            form_db01.save()
            context={"tirada1": tirada1, "tirada2": tirada2}
            return render(request, "CreacionPJ/pjcreation02.html", context)
    else:
        return redirect('PJCreation01')

    context={"tirada1": tirada1, "tirada2": tirada2}

    return render(request, "CreacionPJ/pjcreation02.html", context)

def elegirt1(request):

    tirada_elegida=request.session.get('tirada1')

    request.session['tirada_elegida']=tirada_elegida

    form_car = CaracteristicasForm()

    context={"tirada_elegida": tirada_elegida,
             "form": form_car}

    return render(request, "CreacionPJ/pjcreation03.html", context)

def elegirt2(request):

    tirada_elegida=request.session.get('tirada2')

    request.session['tirada_elegida']=tirada_elegida

    form_car = CaracteristicasForm()

    context={"tirada_elegida": tirada_elegida,
             "form": form_car}

    return render(request, "CreacionPJ/pjcreation03.html", context)

def elegirt3(request):

    tirada3=tirada_caracteristicas()

    tirada_elegida=tirada3

    request.session['tirada_elegida']=tirada_elegida
    
    form_car = CaracteristicasForm()

    context={"tirada_elegida":tirada_elegida,
             "form": form_car}


    return render(request, "CreacionPJ/pjcreation03.html", context)

def pjcreation04(request):

    tirada_elegida=request.session.get('tirada_elegida')

    if request.method == 'POST':
        form_car = CaracteristicasForm(request.POST)
        var1=request.POST['caract1']
        var2=request.POST['caract2']
        var3=request.POST['caract3']
        var4=request.POST['caract4']
        var5=request.POST['caract5']
        var6=request.POST['caract6']
        var7=request.POST['caract7'] 

        caracteristicas={var1:tirada_elegida[0],
                         var2:tirada_elegida[1],
                         var3:tirada_elegida[2],
                         var4:tirada_elegida[3],
                         var5:tirada_elegida[4],
                         var6:tirada_elegida[5],
                         var7:tirada_elegida[6],}
        form = RazaYProfesionForm()
    else:
        form = RazaYProfesionForm()

    request.session['caracteristicas']=caracteristicas

    context={'form':form,
             'caracteristicas':caracteristicas}

    return render(request, "CreacionPJ/pjcreation04.html", context)

def pjcreation05(request):

            # Caracteristicas

    caracteristicas=request.session.get('caracteristicas')

            # Razas y Profesiones 

    if request.method == 'POST':
        form = RazaYProfesionForm(request.POST)
        if form.is_valid():
            form.save()
            raza=request.POST['raza']
            prof=request.POST['profesion']
            dom=request.POST['dominio_magico']

            datos_basicos02={
                     "Raza":raza.title(),
                     "Profesión":prof.title(),
                     "Dominio Magico":dom.title(),}

            # Datos Basicos

            datos_basicos_bd= DatosBasicos.objects.latest('id')
            
            datos_basicos01={}

            for field in datos_basicos_bd._meta.fields:
                if field.name not in ['_state', 'id']:
                    datos_basicos01[field.name] = getattr(datos_basicos_bd, field.name)
            datos_basicos_values=list(datos_basicos01.values())

            form=DatosBasicosForm()
            datos_basicos_key=[field.label_tag().split('>')[1].split('<')[0].strip(':') for field in form]

            datos_basicos01=dict(zip(datos_basicos_key, datos_basicos_values))
            datos_basicos01.update({"Nivel":0})

#########################################################################################
        
            razast1= RazasTabla1.objects.get(raza__exact=request.POST['raza'])
            razas_t1={
                key: value for key, value in razast1.__dict__.items()
                if key not in ['id', '_state']
            }

            razast2= RazasTabla2.objects.get(raza__exact=request.POST['raza'])
            razas_t2={
                key: value for key, value in razast2.__dict__.items()
                if key not in ['id', '_state']
            }

            razast3= RazasTabla3.objects.get(raza__exact=request.POST['raza'])
            razas_t3={
                key: value for key, value in razast3.__dict__.items()
                if key not in ['id', '_state']
            }
            
            razast4= RazasTabla4.objects.get(raza__exact=request.POST['raza'])
            razas_t4={
                key: value for key, value in razast4.__dict__.items()
                if key not in ['id', '_state']
            }            
            
            proft1= Profesiones.objects.get(profesion=request.POST['profesion'])
            prof_t1={
                key: value for key, value in proft1.__dict__.items()
                if key not in ['id', '_state']
            }
                        
            def desarrollo_fisico_y_pp(t1,t2,t3):
                if t1==10:
                    valor=personaje[2][25] #valor de desarrollo fisico
                else:
                    valor=personaje[2][26] #valor de pp
                tiradas_des_fis_o_pp=[]
                for i in range(valor): 
                    if i < 10:
                        tirada = random.randint(1, t1)
                        tiradas_des_fis_o_pp.append(tirada)
                    elif i < 15:
                        tirada = random.randint(1, t2)
                        tiradas_des_fis_o_pp.append(tirada)
                    else:
                        tirada = random.randint(1, t3)
                        tiradas_des_fis_o_pp.append(tirada)                           
                return tiradas_des_fis_o_pp
            
#########################################################################################
            cons_caracteristicas=[
                caracteristicas['FUE'],
                caracteristicas['AGI'],
                caracteristicas['CON'],
                caracteristicas['INT'],
                caracteristicas['I'],
                caracteristicas['PRE'],
                caracteristicas['APA'],
            ]

            cons_datos_basicos=[
                datos_basicos01["Nombre PJ"],       
                "Usuario logueado",                       #-->Jugador
                datos_basicos02["Raza"],
                datos_basicos01["Estatura (mts)"],
                datos_basicos01["Peso (kg.)"],
                datos_basicos01["Género"],
                datos_basicos01["Edad"],
                datos_basicos01["Pelo"],
                datos_basicos01["Ojos"],
                datos_basicos01["Especial Físico"],
                datos_basicos01["Personalidad"],
                datos_basicos01["Motivacion"],
                datos_basicos01["Alineamiento"],
                datos_basicos01["Status"],
                datos_basicos01["Familia"],
                datos_basicos02["Profesión"],
                datos_basicos01["Nivel"],
                datos_basicos02["Dominio Magico"],
                datos_basicos01["Experiencia"]
            ]

            cons_grados_hab_prim=[
                razas_t1['sin_armadura'],
                razas_t1['cuero'],
                razas_t1['cuero_endurecido'],
                razas_t1['cota_de_malla'],
                razas_t1['coraza'],
                razas_t1['de_filo'],
                razas_t1['contundentes'],
                razas_t1['a_dos_manos'],
                razas_t1['arrojadizas'],
                razas_t1['proyectiles'],
                razas_t1['armas_de_asta'],
                razas_t1['escudo'],
                razas_t1['trepar'],
                razas_t1['montar'],
                razas_t1['nadar'],
                razas_t1['rastrear'],
                razas_t1['emboscar'],
                razas_t1['acechar_y_esconderse'],
                razas_t1['abrir_cerraduras'],
                razas_t1['desactivar_trampas'],
                razas_t1['leer_runas'],
                razas_t1['usar_objetos'],
                razas_t1['sortilegios_dirigidos'],
                razas_t1['percepcion'],
                razas_t1['liderazgo_e_influencia'],
                razas_t1['desarrollo_fisico'],
                razas_t1['puntos_de_poder'],
            ]

            cons_grados_hab_sec=[
                
            ]

            cons_especial_1=[
                0,  #MM
                0,
                0,
                0,
                0,
                0,  #ARMAS
                0,
                0,
                0,
                0,
                0,
                0,
                0,  #GENERALES
                0,
                0,
                0,
                0,  #SUBTERFUGIO
                0,
                0,
                0,
                0,  #MAGICAS
                0,
                0,
                0,  #PERCEPCION
                0,  #LIDERAZGO E INFLUENCIA
                0,  #DESARROLLO FISICO
                0,  #PUNTOS DE PODER
                0,  #TIRADAS DE RESISTENCIA
                0,
                0,
                0,
                0,
                0,
            ]

            cons_objetos=[
                [0,0,0,0,0],            #MM
                [0,0,0,0,0,0,0],        #ARMAS
                [0,0,0,0],              #GENERALES
                [0,0,0,0],              #SUBTERFUGIO
                [0,0,0],                #MAGICAS
                [0,0,5,0],              #OTRAS
                [0,0,0,0,0,0,0,0,0],    #SECUNDARIAS
                [0,0,0,0,0,0]           #TIRADAS_RESISTENCIA
            ]

            cons_idiomas=[

            ]

            cons_sortilegios=[

            ]

            personaje=[
                cons_caracteristicas,
                cons_datos_basicos,
                cons_grados_hab_prim,
                cons_grados_hab_sec,
                cons_especial_1,
                cons_objetos,
                cons_idiomas,
                cons_sortilegios
            ]
            
            prof=("Guerrero","Explorador","Montaraz","Mago","Animista","Bardo")
            for i in range(6):
                if personaje[1][15]==prof[i] and personaje[0][i]<90:
                    personaje[0][i]=90

            personaje[2][25]=desarrollo_fisico_y_pp(10,6,4) #desarrollo fisico
            personaje[2][26]=desarrollo_fisico_y_pp(6,4,2)  #puntos de poder

            mano_habil= random.randint(1, 100)
            sortilegio_raza = random.randint(1, 100)

            if mano_habil > 10:
                mano_habil_text="Tu personaje es diestro"
            elif mano_habil > 3:
                mano_habil_text="Tu personaje es zurdo"
            else:
                mano_habil_text="Tu personaje es ambidiestro"
            
            # request.session['prob_sort']=razas_t1['prob_sort']

            guardar_personaje(personaje)

            context={
                "prob_sort":razas_t1['prob_sort'],
                "mano_habil":mano_habil,
                "mano_habil_text":mano_habil_text,
                "sortilegio_raza":sortilegio_raza,
                "caracteristicas":caracteristicas,
                "datos_basicos01":datos_basicos01,
                "datos_basicos02":datos_basicos02,
                "razas_t1":razas_t1,
                "razas_t2":razas_t2,
                "razas_t3":razas_t3,
                "razas_t4":razas_t4,
                "prof_t1":prof_t1,
                "personaje":personaje           
                }

            return render(request, "CreacionPJ/pjcreation05.html", context)
        else:
             return render(request, "CreacionPJ/pjcreation05.html")
    else:
        form = RazaYProfesionForm()
    
        return render(request, "CreacionPJ/pjcreation05.html")

def pjcreation06(request):

    if request.method == 'POST':
        raza=request.POST['raza']
        nombre_pj=request.POST['nombre_pj']
        usuario=request.POST['usuario']
        nivel=request.POST['nivel']
        profesion=request.POST['profesion']
        dominio=request.POST['dominio']
        prob_sort=request.POST['prob_sort']
        sortilegios=request.POST['sortilegios']
        grados_idioma=request.POST['grados_idioma']

        idiomas=RazasIdiomas.objects.filter(raza__exact=request.POST['raza'])
        idiomas = [[idioma, grado] for idioma, grado in idiomas.values_list('idiomas', 'grados')]
        idiomas_original=dict(idiomas)

        guardar_idiomas(idiomas, nombre_pj, usuario, nivel)

        request.session['nombre_pj']=nombre_pj
        request.session['usuario']=usuario
        request.session['nivel']=nivel
        request.session['profesion']=profesion
        request.session['dominio']=dominio
        request.session['prob_sort']=prob_sort
        request.session['sortilegios']=sortilegios
        request.session['idiomas']=idiomas
        request.session['idiomas_original']=idiomas_original
        request.session['grados_idioma']=grados_idioma
        request.session['raza']=raza

    
    elif request.method == 'GET':
        nombre_pj=request.session.get('nombre_pj')
        usuario=request.session.get('usuario')
        nivel=request.session.get('nivel')
        profesion=request.session.get('profesion')
        dominio=request.session.get('dominio')
        prob_sort=request.session.get('prob_sort')
        sortilegios=request.session.get('sortilegios')
        idiomas=request.session.get('idiomas')
        idiomas_original=request.session.get('idiomas_original')
        grados_idioma=request.session.get('grados_idioma')
        raza=request.session.get('raza')


    form1 = SortilegiosPersonajeForm(request.POST, dominio=dominio, profesion=profesion, nombre_pj=nombre_pj, usuario=usuario, nivel=nivel)
    form2 = IdiomasPersonajeForm(request.POST, nombre_pj=nombre_pj, usuario=usuario, nivel=nivel)
    
    context={
        "form1":form1,
        "form2":form2,
        "idiomas":idiomas,
        "prob_sort":prob_sort,
        "sortilegios":sortilegios,
        "idiomas_original":idiomas_original,
        "nombre_pj":nombre_pj,
        "usuario":usuario,
        "nivel":nivel,
        "profesion":profesion,
        "dominio":dominio,
        "raza":raza,
        "grados_idioma":grados_idioma,
        }

    return render(request, "CreacionPJ/pjcreation06.html", context)

def salida(request):
    if request.method == 'POST':
        nombre_pj=request.POST['nombre_pj']
        usuario=request.POST['usuario']
        nivel=request.POST['nivel']
        profesion=request.POST['profesion']
        dominio=request.POST['dominio']
        form1 = SortilegiosPersonajeForm(request.POST, dominio=dominio, profesion=profesion, nombre_pj=nombre_pj,usuario=usuario,nivel=nivel)
        if form1.is_valid(): 
            lista=[request.POST['lista']]
            guardar_sortilegios(lista, nombre_pj, usuario, nivel)
        idiomas=request.POST['idiomas']
        idiomas=eval(idiomas)
        guardar_idiomas(idiomas, nombre_pj, usuario, nivel)
        
        raza = Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel).raza
        puntos_de_historial=RazasTabla1.objects.get(raza__exact=raza).puntos_de_historial
        pdh=[]

        request.session['pdh']=pdh
        request.session['puntos_de_historial']=puntos_de_historial
        request.session['nombre_pj']=nombre_pj
        request.session['usuario']=usuario
        request.session['nivel']=nivel

    return redirect("Historial")

def agregar_grado(request,idioma):
    idiomas=request.session.get('idiomas')
    grados_idioma=int(request.session.get('grados_idioma'))
    iteracion=-1
    for i in idiomas:
        iteracion=iteracion+1
        if i[0] == idioma:
            idiomas[iteracion][1]=idiomas[iteracion][1]+1
    grados_idioma=grados_idioma-1
    request.session['idiomas']=idiomas
    request.session['grados_idioma']=grados_idioma
    return redirect("PJCreation06")

def restar_grado(request,idioma):
    nombre_pj=request.session.get('nombre_pj')
    usuario=request.session.get('usuario')
    nivel=request.session.get('nivel')
    idiomas=request.session.get('idiomas')
    grados_idioma=int(request.session.get('grados_idioma'))
    iteracion=-1
    for i in idiomas:
        iteracion=iteracion+1
        if i[0] == idioma:
            if i[1] == 1:
                del idiomas[iteracion]
                guardar_idiomas(idiomas, nombre_pj, usuario, nivel)
            else:    
                idiomas[iteracion][1]=idiomas[iteracion][1]-1
    grados_idioma=grados_idioma+1
    request.session['idiomas']=idiomas
    request.session['grados_idioma']=grados_idioma
    return redirect("PJCreation06")

def agregar_idioma(request):
    nombre_pj=request.session.get('nombre_pj')
    usuario=request.session.get('usuario')
    nivel=request.session.get('nivel')
    idiomas=request.session.get('idiomas')
    grados_idioma=int(request.session.get('grados_idioma'))
    if request.method == 'POST':
        form = IdiomasPersonajeForm(request.POST, nombre_pj=nombre_pj, usuario=usuario, nivel=nivel)
        if form.is_valid():
            idioma=request.POST['idiomas']
            idiomas=idiomas+[[idioma,1]]
            grados_idioma=grados_idioma-1
            guardar_idiomas(idiomas, nombre_pj, usuario, nivel)

        request.session['idiomas']=idiomas
        request.session['grados_idioma']=grados_idioma
    return redirect("PJCreation06")

