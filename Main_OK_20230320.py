##################################################################################################################
##                                                     TO DO                                                    ##                                                 
##################################################################################################################

"""
Desde el boton Hab. Esp. de PDH.html me debe llevar a PDH_Hab_Esp.html el cual tendrá un boton "Aceptar" y otro de
"Rechazar", el aceptar ejecutará la funcion correspondiente y grabará en BD, mientras que el de rechazar redirigirá
directamente a la BD.

Casos que usan los datos: 1, 26, 65, 67, 92 -----> esto se manejará con if en el template.

"""


"""
Hab Sec: [Hab_Sec, grados, especial]
"""


"""
- Aramar la variable personaje (input de Dibujar Hoja)
- Crear funcion para Puntos de Historial
    1.Capacidades Especiales
    2.Objetos Especiales
    3.Dinero
    4.Incrementar Caracteristicas
    5.Idiomas
    6.Aumentar Hab. Prim. (2) o Sec. (5)        
"""

"""
python manage.py flush
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata Profesiones.json
python manage.py loaddata RazaTabla1.json
python manage.py loaddata RazaTabla2.json
python manage.py loaddata RazaTabla3.json
python manage.py loaddata RazaTabla4.json
python manage.py loaddata Sortilegios.json
python manage.py loaddata Sortilegios2.json
python manage.py loaddata HabSec.json
python manage.py loaddata Idiomas.json
"""


##################################################################################################################

from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
import os
import random
import pandas as pd

# Abrir la imagen predefinida
image = Image.open(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\Ficha de Calidad (Hoja 1).png")

# Crear un objeto ImageDraw para dibujar sobre la imagen
draw = ImageDraw.Draw(image)

pd.options.mode.chained_assignment = None  # default='warn'

df_razas = pd.read_excel(r'C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\Razas.xlsx')
df_prof = pd.read_excel(r'C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\Profesiones.xlsx')

def crear_personaje():
    def bonif(bonif):
        if bonif < 75:
            bonif=0         
        elif bonif < 90:
            bonif=5
        elif bonif < 95:
            bonif=10
        elif bonif < 98:
            bonif=15
        elif bonif < 100:
            bonif=20
        elif bonif < 101:
            bonif=25
        elif bonif < 102:
            bonif=30
        else:
            bonif=35
        return bonif
    def tiradas_caracteristicas():
        def tirada_caracteristicas():
            listado_tiradas=[]
            for i in range(7):
                tirada = random.randint(29, 100)
                listado_tiradas.append(tirada)
            print(listado_tiradas)
            return listado_tiradas

        tirada1=tirada_caracteristicas()
        tirada2=tirada_caracteristicas()
        num=input('Indiquie si elige la Tirada [1] o [2]. En caso de requerir una tercera tirada indique [3]:')

        if num=="1":
            tirada_final=tirada1
        elif num=="2":
            tirada_final=tirada2
        elif num=="3":
            tirada_final=tirada_caracteristicas()
        print('Sus caracteristicas son:', tirada_final)
        return tirada_final
    def seleccionar_caracteristicas():
        caract_asign=[0,0,0,0,0,0,0]
        caracteristicas=tiradas_caracteristicas()
        caract=["FUE","AGI","CON","INT","I","PRE","APA"]
        caract2=["FUE","AGI","CON","INT","I","PRE","APA"]
        while len(caract)>0:
            car1=input('Indique la Caracteristica a asignar: %a' %caract)
            if car1 in caract:
                car=input('Indique el valor a asignar: %a' %caracteristicas)
                car=int(car)
                if car in caracteristicas:
                    caract_asign[caract2.index(car1)]=car
                    caract.remove(car1)
                    caracteristicas.remove(car)
            else:
                pass
        return caract_asign
    def datos_basicos():
        razas=['Enano','Umli','Elfos Noldor','Elfos Sindar','Elfos Silvano','Medio Elfos','Hobbit',
               'Beórnidas','Núm. Negros','Corsarios','Dorwinrim','Dúnedain','Dunledinos',
               'Hombres del Este','Haradrim del Norte','Haradrim del Sur','Lossoth','Rohirrim',
               'Campesinos','Burgueses','Variags','H. de los Bosques','Woses','Orcos','Uruk-Hai',
               'Medio Orcos','Trolls','Olog-Hai','Medio Trolls']
        profesiones=['Guerrero','Explorador','Montaraz','Mago','Animista','Bardo']
        nombre=input("Indique el nombre del jugador: ")                           #Para Producción
        nombrepj=input("Indique el nombre del personaje: ")                       #Para Producción
        raza=input("Indique el número de la raza que desee para su personaje:\n"
                    "[1].Enano	   [9].Núm. Negros	    [17].Lossoth	    [25].Uruk-Hai\n"
                    "[2].Umli	   [10].Corsarios	    [18].Rohirrim	    [26].Medio Orcos\n"
                    "[3].Elfos Noldor   [11].Dorwinrim	    [19].Campesinos	    [27].Trolls\n"
                    "[4].Elfos Sindar   [12].Dúnedain	    [20].Burgueses	    [28].Olog-Hai\n"
                    "[5].Elfos Silvano  [13].Dunledinos	    [21].Variags	    [29].Medio Trolls\n"
                    "[6].Medio Elfos	   [14].Hombres del Este    [22].H. de los Bosques\n"	
                    "[7].Hobbit	   [15].Haradrim del Norte  [23].Woses\n"	
                    "[8].Beórnidas      [16].Haradrim del Sur    [24].Orcos\n")	


        estatura=input("Indique la estatura del personaje: ")                     #Para Producción
        peso=input("Indique el peso del personaje: ")                             #Para Producción
        genero=input("Indique el genero del personaje [M] o [F]: ")               #Para Producción
        edad=input("Indique la edad del personaje: ")                             #Para Producción
        pelo=input("Indique el color de pelo del personaje: ")                    #Para Producción
        ojos=input("Indique el color de ojos del personaje: ")                    #Para Producción
        esp_fisico=input("Indique el rasgo distintivo de su personaje: ")         #Para Producción
        personalidad=input("Indique la personalidad de su personaje: ")           #Para Producción
        motivacion=input("Indique la motivación del personaje: ")                 #Para Producción
        alineamiento=input("Indique el alineamiento del personaje: ")             #Para Producción
        status=input("Indique el status del personaje: ")                         #Para Producción
        familia=input("Indique la familia del personaje: ")                       #Para Producción
        profesion=input("Indique el número de la profesion que desee para su personaje:\n"
                        "[1].Guerrero\n[2].Explorador\n[3].Montaraz\n[4].Mago\n[5].Animista\n[6].Bardo\n")
        # nombre="Topo"                                             #Para prueba
        # nombrepj="Eitri"                                          #Para prueba
        # estatura="1.30 m"                                         #Para prueba
        # peso="80 kg."                                             #Para prueba
        # genero="Masc."                                            #Para prueba
        # edad=19                                                   #Para prueba
        # pelo="Rojo"                                               #Para prueba
        # ojos="Celestes"                                           #Para prueba
        # esp_fisico="Cicatriz en X"                                #Para prueba
        # personalidad="Codicioso"                                  #Para prueba
        # motivacion="Buscar al asesino de mi padre"                #Para prueba
        # alineamiento="Caotico Bueno"                              #Para prueba
        # status="Libre"                                            #Para prueba
        # familia="Hermano"                                         #Para prueba
        nivel=0                                                   #Para prueba
        experiencia=0                                             #Para prueba
        datos_basicos=[nombre,nombrepj,razas[int(raza)-1],estatura,peso,genero,edad,pelo,ojos,esp_fisico,personalidad,
                       motivacion,alineamiento,status,familia,profesiones[int(profesion)-1],nivel,experiencia]
        return datos_basicos,int(raza),int(profesion)
    def desarrollo_fisico_y_pp(t1,t2,t3):
        des_fis=list(df_razas.loc[int(datosbasicos[1])-1,'Grados - Desarrollo fisico':'Grados - Desarrollo fisico'].astype(int).values)
        tiradas_des_fis_o_pp=[]
        for i in range(int(des_fis[0])): 
        # for i in range(20):        
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
    def calcular_total_caracteristicas(tiradas_total):
        tiradas_total=[]
        for i in range(6):
            caracteristicas_raza=list(df_razas.loc[int(datosbasicos[1])-1,'FUE':'APA'].astype(int).values)
            tiradas_total.append(bonif(caract_asign[i])+caracteristicas_raza[i])
        return tiradas_total    
    def pdh(pdh):
        def ph_1():
            return "Habilidades Especiales"
        def ph_2():
            return "Objetos Especiales"
        def ph_3():
            return "Dinero"
        def ph_4():
            return "Incrementar Caracteristicas"
        def ph_5():
            return "Idiomas"
        def ph_6():
            return "Aumentar Hab. Prim. (2) o Sec. (5)"
        ph=pdh    
        if ph=="1":
            ph_1()
        elif ph=="2":
            ph_2()
        elif ph=="3":
            ph_3()
        elif ph=="4":
            ph_4()
        elif ph=="5":
            ph_5()
        elif ph=="6":
            ph_6()
    def puntos_de_hist():
        historiales=[]
        puntos_de_historial=list(df_razas.loc[int(datosbasicos[1])-1,'Puntos de Historial':'Puntos de Historial'].astype(int).values)
        puntos_de_historial=puntos_de_historial[0]

        for i in range(puntos_de_historial):
            puntos_de_historial=puntos_de_historial-i
            ph=input("Usted tiene %i puntos de historial para distribuir.\n" 
                    "Seleccione una opción:\n"
                    "[1].Habilidades Especiales       [4].Incrementar Caracteristicas\n"
                    "[2].Objetos Especiales           [5].Idiomas\n"
                    "[3].Dinero                       [6].Aumentar Hab. Prim. (2) o Sec. (5)" %puntos_de_historial)
            historiales.append(pdh(ph))

        caracteristicas=tiradas_caracteristicas()
        caract=["FUE","AGI","CON","INT","I","PRE","APA"]
        caract2=["FUE","AGI","CON","INT","I","PRE","APA"]
        while len(caract)>0:
            car1=input('Indique la Caracteristica a asignar: %a' %caract)
            if car1 in caract:
                car=input('Indique el valor a asignar: %a' %caracteristicas)
                car=int(car)
                if car in caracteristicas:
                    caract_asign[caract2.index(car1)]=car
                    caract.remove(car1)
                    caracteristicas.remove(car)
            else:
                pass
        return caract_asign        

    # caract_asign=[52, 99, 69, 93, 61, 53, 45]           #Para prueba
    caract_asign=seleccionar_caracteristicas()        #Para Producción
    datosbasicos=datos_basicos()
    tiradas_des_fis=desarrollo_fisico_y_pp(10,6,4)
    caract_total=calcular_total_caracteristicas(caract_asign)
    tiradas_pp=desarrollo_fisico_y_pp(6,4,2)
    grados_de_habilidad=list(df_razas.loc[int(datosbasicos[1])-1,'Grados - Sin armadura':'Grados - Liderazgo e Influencia'].astype(int).values)
    # puntos_de_hist()

    return caract_asign,datosbasicos,grados_de_habilidad,tiradas_des_fis,caract_total,tiradas_pp
    
personaje=crear_personaje() # [caract_asign , [datosbasicos , raza , profesion] , grados_de_habilidad, tiradas_des_fis, tiradas_pp, caract_total]

def dibujar_hoja():
    def bonif(bonif):
        if bonif < 75:
            bonif=0         
        elif bonif < 90:
            bonif=5
        elif bonif < 95:
            bonif=10
        elif bonif < 98:
            bonif=15
        elif bonif < 100:
            bonif=20
        elif bonif < 101:
            bonif=25
        elif bonif < 102:
            bonif=30
        else:
            bonif=35
        return bonif
    def dibujar_gdh(grados_de_hab,ejex,ejey,paso_correc,coef_correc,habilidad):
        resultado_hab=[]
        font = ImageFont.truetype(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\arial.ttf", 36) # Fuente y tamaño
        font2 = ImageFont.truetype(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\arial.ttf", 14) # Fuente y tamaño
        for j in range(len(grados_de_hab)):
            resultado=-25
            for cont in range(grados_de_hab[j]):
                max=grados_de_hab[j]-1
                if cont < 10:
                    draw.text((ejex+cont*14+cont//2, ejey+22*j+(j//paso_correc)*coef_correc), "•", fill=(0, 0, 0), font=font)
                    resultado= (cont + 1) * 5
                elif cont < 15:
                    draw.text((ejex+10+cont*14+cont//2, ejey+22*j+(j//paso_correc)*coef_correc), "•", fill=(0, 0, 0), font=font)
                    resultado= (cont -9) * 2 + 50
                elif cont < 20:
                    if cont == max:
                        grado_residual=cont-14
                        draw.text((ejex+262-0.5*coef_correc, ejey+11+23*j), str(grado_residual), fill=(0, 0, 0), font=font2, align ="right")                
                    resultado= (cont -9) * 2 + 50
                elif cont == max:
                    grado_residual=cont-19
                    draw.text((ejex+262-0.5*coef_correc, ejey+11+23*j), str(grado_residual), fill=(0, 0, 0), font=font2, align ="right")
                    resultado= (cont -19) + 70
                else:
                    pass
            draw.text((ejex+321-2*coef_correc, ejey+26+23*j), str(resultado), fill=(0, 0, 0), font=font2, anchor ="ms")
            posicion_caract=((1,1,1,0,0),(0,0,0,1,1,0,1),(1,4,1,3),(10,5,3,4),(3,4,1),(4,5)) #Esto indica el indice de la caracteristica que suma cada habilidad
            pxn=list(df_prof.loc[int(personaje[1][2])-1,'Sin armadura':'Liderazgo e Influencia'].astype(int).values)
            pxn=pxn[0:5],pxn[5:12],pxn[12:16],pxn[16:20],pxn[20:23],pxn[23:25]
            esp_hab_prim_raza=list(df_razas.loc[int(personaje[1][1])-1,'Esp - Sin armadura':'Esp - Liderazgo e Influencia'].astype(int).values)
            esp_hab_prim_raza=esp_hab_prim_raza[0:5],esp_hab_prim_raza[5:12],esp_hab_prim_raza[12:16],esp_hab_prim_raza[16:20],esp_hab_prim_raza[20:23],esp_hab_prim_raza[23:25]
            draw.text((ejex+497-2*coef_correc, ejey+26+23*j), str(esp_hab_prim_raza[habilidad][j]), fill=(0, 0, 0), font=font2, anchor ="ms")
            esp_hab_prim=[[0,-15,-30,-45,-60],[0,0,0,0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0],[0,0]]
            objeto=[[0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0],[0,0]]
            draw.text((ejex+597-2*coef_correc, ejey+26+23*j), str(objeto[habilidad][j]), fill=(0, 0, 0), font=font2, anchor ="ms")

            if habilidad==0:
                pass
            elif (habilidad==3 and j==0):
                draw.text((ejex+547-2*coef_correc, ejey+26+23*j), str(esp_hab_prim[habilidad][j]), fill=(0, 0, 0), font=font2, anchor ="ms")
            else:
                draw.text((ejex+452-2*coef_correc, ejey+26+23*j), str(((pxn[habilidad][j]*personaje[1][0][16]))), fill=(0, 0, 0), font=font2, anchor ="ms")
                draw.text((ejex+547-2*coef_correc, ejey+26+23*j), str(esp_hab_prim[habilidad][j]), fill=(0, 0, 0), font=font2, anchor ="ms")
            try:
                draw.text((ejex+402-2*coef_correc, ejey+26+23*j), str(personaje[4][posicion_caract[habilidad][j]]), fill=(0, 0, 0), font=font2, anchor ="ms")
            except IndexError:
                pass
            try:
                total=resultado+personaje[4][posicion_caract[habilidad][j]]+pxn[habilidad][j]+esp_hab_prim_raza[habilidad][j]+esp_hab_prim[habilidad][j]+objeto[habilidad][j]
                draw.text((ejex+648-2*coef_correc, ejey+26+23*j), str(total), fill=(0, 0, 0), font=font2, anchor ="ms")            
            except IndexError:
                total=resultado+pxn[habilidad][j]+esp_hab_prim_raza[habilidad][j]+esp_hab_prim[habilidad][j]+objeto[habilidad][j]
                draw.text((ejex+648-2*coef_correc, ejey+26+23*j), str(total), fill=(0, 0, 0), font=font2, anchor ="ms")            

            resultado_hab.append(resultado)
        return resultado_hab #,pxn,esp_hab_prim_raza,esp_hab_prim,objeto
    def dibujar_caracteristicas(caracteristicas,ejex,ejey,paso_correc,coef_correc):
        font2 = ImageFont.truetype(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\arial.ttf", 14) # Fuente y tamaño
        total_caracteristicas=[]
        for i in range(7):
            if i==6:
                total_caracteristica=bonif(caracteristicas[5])+caracteristicas_raza[5]+caracteristicas[i]
                draw.text((ejex+7, ejey+15+22*i+(i//paso_correc)*coef_correc), str(caracteristicas[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
                draw.text((ejex+190, ejey+15+22*i+(i//paso_correc)*coef_correc), str(total_caracteristica), fill=(0, 0, 0), font=font2, anchor ="ms")
            else:
                caracteristicas_raza=list(df_razas.loc[int(personaje[1][1])-1,'FUE':'APA'].astype(int).values)
                total_caracteristica=bonif(caracteristicas[i])+caracteristicas_raza[i]
                draw.text((ejex+7, ejey+15+22*i+(i//paso_correc)*coef_correc), str(caracteristicas[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
                draw.text((ejex+72, ejey+15+22*i+(i//paso_correc)*coef_correc), str(bonif(caracteristicas[i])), fill=(0, 0, 0), font=font2, anchor ="ms")
                draw.text((ejex+130, ejey+15+22*i+(i//paso_correc)*coef_correc), str(caracteristicas_raza[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
                draw.text((ejex+190, ejey+15+22*i+(i//paso_correc)*coef_correc), str(total_caracteristica), fill=(0, 0, 0), font=font2, anchor ="ms")  
    def dibujar_individual(dato,ejex,ejey):
        font2 = ImageFont.truetype(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\arial.ttf", 14) # Fuente y tamaño
        draw.text((ejex , ejey), str(dato), fill=(0, 0, 0), font=font2)
    def dibujar_tr(ejex,ejey):
        font2 = ImageFont.truetype(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\arial.ttf", 14) # Fuente y tamaño
        esp_tr_raza=list(df_razas.loc[int(personaje[1][1])-1,'Esp - ESE':'Esp - TR Frio'].astype(int).values)
        posicion_caract=(3,4,2,2,2,2)
        esp_tr=(0,0,0,0,0,0)
        objeto=(0,0,0,0,0,0)
        for i in range(6):
            draw.text((ejex, ejey+22*i), str(personaje[4][posicion_caract[i]]), fill=(0, 0, 0), font=font2, anchor ="ms")
            draw.text((ejex+90, ejey+22*i), str(esp_tr_raza[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
            draw.text((ejex+135, ejey+22*i), str(esp_tr[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
            draw.text((ejex+185, ejey+22*i), str(objeto[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
            total_tr=personaje[4][posicion_caract[i]]+esp_tr_raza[i]+esp_tr[i]+objeto[i]
            draw.text((ejex+245, ejey+22*i), str(total_tr), fill=(0, 0, 0), font=font2, anchor ="ms")
    def dibujar_des_fis_y_pp(tiradas_des_fis,ejex,ejey,correc,objeto="no"):
        for i in range(len(tiradas_des_fis)):
            font2 = ImageFont.truetype(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\arial.ttf", 14) # Fuente y tamaño
            if i < 10:
                draw.text((ejex+i*19+i//2, ejey), str(tiradas_des_fis[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
            elif i <15:
                draw.text((ejex+i*19+i//2+59, ejey), str(tiradas_des_fis[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
            else:
                max=len(tiradas_des_fis)-1
                if i == max:
                    puntos_des_fis=sum(tiradas_des_fis[14:])
                    draw.text((ejex+425, ejey), str(puntos_des_fis), fill=(0, 0, 0), font=font2, anchor ="ms")

        draw.text((ejex+478, ejey+correc), str(sum(tiradas_des_fis)), fill=(0, 0, 0), font=font2, anchor ="ms") #resultado
        draw.text((ejex+558, ejey+correc), str(personaje[0][2]), fill=(0, 0, 0), font=font2, anchor ="ms") #caracteristica
        esp_hab_prim_raza=list(df_razas.loc[int(personaje[1][1])-1,'Esp - Desarrollo fisico':'Esp - Desarrollo fisico'].astype(int).values) 
        draw.text((ejex+653, ejey+correc), str(esp_hab_prim_raza[0]), fill=(0, 0, 0), font=font2, anchor ="ms") #especial raza
        draw.text((ejex+698, ejey+correc), str(0), fill=(0, 0, 0), font=font2, anchor ="ms") #especial
        pxn=list(df_prof.loc[int(personaje[1][2])-1,'Desarrollo fisico':'Desarrollo fisico'].astype(int).values)
        if objeto=="no":
            objeto=0
            draw.text((ejex+745, ejey+correc), str(objeto), fill=(0, 0, 0), font=font2, anchor ="ms")
        else:
            draw.text((ejex+608, ejey+correc), str(((pxn[0]*personaje[1][0][16]))), fill=(0, 0, 0), font=font2, anchor ="ms") #profxnivel
        total_des_fis=sum(tiradas_des_fis)+personaje[4][2]+pxn[0]+esp_hab_prim_raza[0]+objeto+5
        draw.text((ejex+808, ejey+correc), str(total_des_fis), fill=(0, 0, 0), font=font2, anchor ="ms") #total
    def dibujar_idiomas(ejex,ejey):
        font2 = ImageFont.truetype(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\arial.ttf", 14)
        cadena = "(Khuzdul,1),(Labba,2),(Oestrón,2),(Umítico,5)"
        cadena = cadena.replace("(", "").replace(")", "")
        cadena=cadena.split(",")
        cadena = zip(cadena[0::2], cadena[1::2])
        cadena = [list(t) for t in cadena]
        idioma_natal=cadena[0]
        otros_idiomas=cadena[1:]
        draw.text((ejex, ejey-24), str(idioma_natal[0]), fill=(0, 0, 0), font=font2, anchor ="ms")
        draw.text((ejex+150, ejey-24), str(idioma_natal[1]), fill=(0, 0, 0), font=font2, anchor ="ms")
        for i in range(len(otros_idiomas)):
            draw.text((ejex-35, ejey+i*24), str(otros_idiomas[i][0]), fill=(0, 0, 0), font=font2, anchor ="ms")
            draw.text((ejex+150, ejey+i*24), str(otros_idiomas[i][1]), fill=(0, 0, 0), font=font2, anchor ="ms")
        
        
        
    def llamar_funciones():
        caracteristicas=dibujar_caracteristicas(personaje[0],973,50,6,7)
        mym=dibujar_gdh(personaje[2][0:5],501,524,1,0,0) 
        armas=dibujar_gdh(personaje[2][5:12],501,658,1,0,1)
        generales=dibujar_gdh(personaje[2][12:16],501,834,1,0,2)
        subterfugio=dibujar_gdh(personaje[2][16:20],501,948,1,0,3)
        magicas=dibujar_gdh(personaje[2][20:23],501,1060,1,0,4)
        otras=dibujar_gdh(personaje[2][23:25],501,1180,1,0,5)
        des_fis=dibujar_des_fis_y_pp(personaje[3],347,1295,3,0)
        pp=dibujar_des_fis_y_pp(personaje[5],347,1352,-2,"no")
        nombre=dibujar_individual(personaje[1][0][0],130,24)
        nombrepj=dibujar_individual(personaje[1][0][1],360,24)
        raza=dibujar_individual(personaje[1][0][2],95,50)
        estatura=dibujar_individual(personaje[1][0][3],305,50)
        peso=dibujar_individual(personaje[1][0][4],400,50)
        genero=dibujar_individual(personaje[1][0][5],100,75)
        edad=dibujar_individual(personaje[1][0][6],195,75)
        pelo=dibujar_individual(personaje[1][0][7],290,75)
        ojos=dibujar_individual(personaje[1][0][8],400,75)
        esp_fisico=dibujar_individual(personaje[1][0][9],135,100)
        personalidad=dibujar_individual(personaje[1][0][10],125,126)
        motivacion=dibujar_individual(personaje[1][0][11],125,152)
        alineamiento=dibujar_individual(personaje[1][0][12],135,177)
        status=dibujar_individual(personaje[1][0][13],85,202)
        familia=dibujar_individual(personaje[1][0][14],325,202)
        profesion=dibujar_individual(personaje[1][0][15],130,227)
        nivel=dibujar_individual(personaje[1][0][16],325,227)
        experiencia=dibujar_individual(personaje[1][0][17],378,227)
        tr=dibujar_tr(910,1622)
        # secundarias=dibujar_gdh(grados_de_hab_sec,510,1374,3,4,6)
        dibujar_idiomas(130,344)
        datosbasicos=[nombre,nombrepj,raza,estatura,peso,genero,edad,pelo,ojos,esp_fisico, personalidad,
                      motivacion,alineamiento,status,familia,profesion,nivel,experiencia]
        return datosbasicos,caracteristicas, mym, armas, generales, subterfugio, magicas, otras, des_fis,pp
    
    llamar_funciones()

def imprimir_pdf():
    image.save(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\resultado.png")
    width, height = image.size
    pdf = canvas.Canvas(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\resultado.pdf", pagesize=(width, height))
    pdf.drawImage(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\resultado.png", 0, 0, width=width, height=height)
    pdf.showPage()
    pdf.save()
    os.remove(r"C:\Users\gesse\OneDrive\Escritorio\Django\DJANGO CODO A CODO\resultado.png")

dibujar_hoja()
imprimir_pdf()