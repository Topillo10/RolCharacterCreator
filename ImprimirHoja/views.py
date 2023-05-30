from CreacionPJ.models import Profesiones, RazasTabla1, RazasTabla2, RazasTabla3, RazasTabla4
from GuardarPersonaje.models import Personaje, Personaje_HabSec, Personaje_Idiomas, Personaje_Sort
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
import os


def dibujar_hoja(nombre_pj, usuario, nivel):
    
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
        personaje[0:7],         #[0]
        personaje[7:26],        #[1]
        personaje[26:53],       #[2]
        lista_hab_sec,          #[3]
        personaje[53:86],       #[4]
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
    
    image = Image.open("./ImprimirHoja/Static/ImprimirHoja/img/Character_Sheet.png")

    draw = ImageDraw.Draw(image)

    proft1= Profesiones.objects.get(profesion=personaje[1][15])
    prof_t1=[
        value for key, value in proft1.__dict__.items()
        if key not in ['id', '_state']
    ]

    razast1= RazasTabla1.objects.get(raza__exact=personaje[1][2])
    razas_t1=[
        value for key, value in razast1.__dict__.items()
        if key not in ['id', '_state']
    ]

    razast2= RazasTabla2.objects.get(raza__exact=personaje[1][2])
    razas_t2=[
        value for key, value in razast2.__dict__.items()
        if key not in ['id', '_state']
    ]

    razast3= RazasTabla3.objects.get(raza__exact=personaje[1][2])
    razas_t3=[
        value for key, value in razast3.__dict__.items()
        if key not in ['id', '_state']
    ]
    
    razast4= RazasTabla4.objects.get(raza__exact=personaje[1][2])
    razas_t4=[
        value for key, value in razast4.__dict__.items()
        if key not in ['id', '_state']
    ]

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
        font = ImageFont.truetype("../ImprimirHoja/Static/ImprimirHoja/Fonts/arial.ttf", 36) # Fuente y tamaño
        font2 = ImageFont.truetype("../ImprimirHoja/Static/ImprimirHoja/Fonts/arial.ttf", 14) # Fuente y tamaño
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
            pxn=prof_t1[1:6],prof_t1[6:13],prof_t1[13:17],prof_t1[17:21],prof_t1[21:24],prof_t1[24:26]
            caracteristicas_raza=razas_t1[1:7]
            esp_hab_prim_2=razas_t2[1:6],razas_t2[6:13],razas_t2[13:17],razas_t2[17:21],razas_t2[21:24],razas_t2[24:26]
            esp_hab_prim_1=(personaje[4][0:5],personaje[4][5:12],personaje[4][12:16],personaje[4][16:20],personaje[4][20:23],personaje[4][23:25])        
            draw.text((ejex+497-2*coef_correc, ejey+26+23*j), str(esp_hab_prim_1[habilidad][j]), fill=(0, 0, 0), font=font2, anchor ="ms")
            objeto=personaje[5]
            draw.text((ejex+597-2*coef_correc, ejey+26+23*j), str(objeto[habilidad][j]), fill=(0, 0, 0), font=font2, anchor ="ms")

            if habilidad==0:
                pass
            elif (habilidad==3 and j==0):
                draw.text((ejex+547-2*coef_correc, ejey+26+23*j), str(esp_hab_prim_2[habilidad][j]), fill=(0, 0, 0), font=font2, anchor ="ms")
            else:
                draw.text((ejex+452-2*coef_correc, ejey+26+23*j), str(((pxn[habilidad][j]*personaje[1][16]))), fill=(0, 0, 0), font=font2, anchor ="ms")
                draw.text((ejex+547-2*coef_correc, ejey+26+23*j), str(esp_hab_prim_2[habilidad][j]), fill=(0, 0, 0), font=font2, anchor ="ms")
            try:
                draw.text((ejex+402-2*coef_correc, ejey+26+23*j), str(bonif(personaje[0][posicion_caract[habilidad][j]])+caracteristicas_raza[posicion_caract[habilidad][j]]), fill=(0, 0, 0), font=font2, anchor ="ms")
            except IndexError:
                pass
            try:
                total=resultado+bonif(personaje[0][posicion_caract[habilidad][j]])+caracteristicas_raza[posicion_caract[habilidad][j]]+pxn[habilidad][j]*personaje[1][16]+esp_hab_prim_2[habilidad][j]+esp_hab_prim_1[habilidad][j]+objeto[habilidad][j]
                draw.text((ejex+648-2*coef_correc, ejey+26+23*j), str(total), fill=(0, 0, 0), font=font2, anchor ="ms")            
            except IndexError:
                total=resultado+pxn[habilidad][j]*personaje[1][16]+esp_hab_prim_2[habilidad][j]+esp_hab_prim_1[habilidad][j]+objeto[habilidad][j]
                draw.text((ejex+648-2*coef_correc, ejey+26+23*j), str(total), fill=(0, 0, 0), font=font2, anchor ="ms")            

            resultado_hab.append(resultado)
        return resultado_hab #,pxn,esp_hab_prim_2,esp_hab_prim_1,objeto
    
    def dibujar_caracteristicas(caracteristicas,ejex,ejey,paso_correc,coef_correc):
        font2 = ImageFont.truetype("../ImprimirHoja/Static/ImprimirHoja/Fonts/arial.ttf", 14) # Fuente y tamaño
        total_caracteristicas=[]
        for i in range(7):
            if i==6:
                total_caracteristica=bonif(caracteristicas[5])+caracteristicas_raza[5]+caracteristicas[i]
                if total_caracteristica>102:
                    total_caracteristica=102
                draw.text((ejex+7, ejey+15+22*i+(i//paso_correc)*coef_correc), str(caracteristicas[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
                draw.text((ejex+190, ejey+15+22*i+(i//paso_correc)*coef_correc), str(total_caracteristica), fill=(0, 0, 0), font=font2, anchor ="ms")
            else:
                caracteristicas_raza=razas_t1[1:7]
                total_caracteristica=bonif(caracteristicas[i])+caracteristicas_raza[i]
                draw.text((ejex+7, ejey+15+22*i+(i//paso_correc)*coef_correc), str(caracteristicas[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
                draw.text((ejex+72, ejey+15+22*i+(i//paso_correc)*coef_correc), str(bonif(caracteristicas[i])), fill=(0, 0, 0), font=font2, anchor ="ms")
                draw.text((ejex+130, ejey+15+22*i+(i//paso_correc)*coef_correc), str(caracteristicas_raza[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
                draw.text((ejex+190, ejey+15+22*i+(i//paso_correc)*coef_correc), str(total_caracteristica), fill=(0, 0, 0), font=font2, anchor ="ms")  
    
    def dibujar_individual(dato,ejex,ejey,unidad=""):
        font2 = ImageFont.truetype("../ImprimirHoja/Static/ImprimirHoja/Fonts/arial.ttf", 14) # Fuente y tamaño
        draw.text((ejex , ejey), str(dato)+unidad, fill=(0, 0, 0), font=font2)
    
    def dibujar_tr(ejex,ejey):
        font2 = ImageFont.truetype("../ImprimirHoja/Static/ImprimirHoja/Fonts/arial.ttf", 14) # Fuente y tamaño
        esp_tr_raza=razas_t2[28:34]
        posicion_caract=(3,4,2,2,2,2)
        caracteristicas_raza=razas_t1[1:7]
        esp_tr=personaje[4][27:33]
        objeto=personaje[5][7]
        for i in range(6):
            draw.text((ejex, ejey+22*i), str(bonif(personaje[0][posicion_caract[i]])+caracteristicas_raza[posicion_caract[i]]), fill=(0, 0, 0), font=font2, anchor ="ms")
            draw.text((ejex+90, ejey+22*i), str(esp_tr[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
            draw.text((ejex+135, ejey+22*i), str(esp_tr_raza[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
            draw.text((ejex+185, ejey+22*i), str(objeto[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
            total_tr=bonif(personaje[0][posicion_caract[i]])+caracteristicas_raza[posicion_caract[i]]+esp_tr_raza[i]+esp_tr[i]+objeto[i]
            draw.text((ejex+245, ejey+22*i), str(total_tr), fill=(0, 0, 0), font=font2, anchor ="ms")
    
    def dibujar_des_fis_y_pp(tiradas_des_fis,ejex,ejey,correc,hab):
        font2 = ImageFont.truetype("../ImprimirHoja/Static/ImprimirHoja/Fonts/arial.ttf", 14) # Fuente y tamaño
        caracteristicas_raza=razas_t1[1:7]
        esp_hab_prim_2=razas_t2[26]

        if hab == "pp":
            pxn=0
            objeto=personaje[5][5][3]
            tiradas_pp=personaje[2][26]
            tiradas=eval(tiradas_pp)
            esp_hab_prim_1=personaje[4][26]
            draw.text((ejex+745, ejey+correc), str(objeto), fill=(0, 0, 0), font=font2, anchor ="ms")
            if personaje[1][17]=="Esencia":
                draw.text((ejex+558, ejey+correc), str(bonif(personaje[0][3])+caracteristicas_raza[3]), fill=(0, 0, 0), font=font2, anchor ="ms") #caracteristica
                total=sum(tiradas)+bonif(personaje[0][2])+caracteristicas_raza[3]+pxn+esp_hab_prim_2+esp_hab_prim_1+objeto
            else:
                draw.text((ejex+558, ejey+correc), str(bonif(personaje[0][4])+caracteristicas_raza[4]), fill=(0, 0, 0), font=font2, anchor ="ms") #caracteristica
                total=sum(tiradas)+bonif(personaje[0][2])+caracteristicas_raza[4]+pxn+esp_hab_prim_2+esp_hab_prim_1+objeto
        else:
            pxn=prof_t1[28]*personaje[1][16]
            objeto=personaje[5][5][2]
            tiradas_des_fis=personaje[2][25]
            tiradas=eval(tiradas_des_fis)
            esp_hab_prim_1=personaje[4][25]
            draw.text((ejex+558, ejey+correc), str(bonif(personaje[0][2])+caracteristicas_raza[2]), fill=(0, 0, 0), font=font2, anchor ="ms") #caracteristica
            draw.text((ejex+608, ejey+correc), str(pxn*personaje[1][16]), fill=(0, 0, 0), font=font2, anchor ="ms") #profxnivel
            total=sum(tiradas)+bonif(personaje[0][2])+caracteristicas_raza[4]+pxn+esp_hab_prim_2+esp_hab_prim_1+objeto
        for i in range(len(tiradas)):
            if i < 10:
                draw.text((ejex+i*19+i//2, ejey), str(tiradas[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
            elif i <15:
                draw.text((ejex+i*19+i//2+59, ejey), str(tiradas[i]), fill=(0, 0, 0), font=font2, anchor ="ms")
            else:
                max=len(tiradas)-1
                if i == max:
                    puntos_extra=sum(tiradas[15:])
                    draw.text((ejex+425, ejey), str(puntos_extra), fill=(0, 0, 0), font=font2, anchor ="ms")
        draw.text((ejex+478, ejey+correc), str(sum(tiradas)), fill=(0, 0, 0), font=font2, anchor ="ms") #resultado
        draw.text((ejex+653, ejey+correc), str(esp_hab_prim_1), fill=(0, 0, 0), font=font2, anchor ="ms") #especial raza
        draw.text((ejex+698, ejey+correc), str(esp_hab_prim_2), fill=(0, 0, 0), font=font2, anchor ="ms") #especial           
        draw.text((ejex+808, ejey+correc), str(total), fill=(0, 0, 0), font=font2, anchor ="ms") #total
    
    def dibujar_idiomas(ejex,ejey):
        font2 = ImageFont.truetype("../ImprimirHoja/Static/ImprimirHoja/Fonts/arial.ttf", 14)
        idioma_natal=personaje[6][0]
        otros_idiomas=personaje[6][1:]
        draw.text((ejex, ejey-24), str(idioma_natal[0]), fill=(0, 0, 0), font=font2, anchor ="ms")
        draw.text((ejex+150, ejey-24), str(idioma_natal[1]), fill=(0, 0, 0), font=font2, anchor ="ms")
        for i in range(len(otros_idiomas)):
            draw.text((ejex-35, ejey+i*24), str(otros_idiomas[i][0]), fill=(0, 0, 0), font=font2, anchor ="ms")
            draw.text((ejex+150, ejey+i*24), str(otros_idiomas[i][1]), fill=(0, 0, 0), font=font2, anchor ="ms")

    def dibujar_sortilegios(ejex,ejey):
        font2 = ImageFont.truetype("../ImprimirHoja/Static/ImprimirHoja/Fonts/arial.ttf", 14)
        sortilegios=personaje[7]
        for i in range(len(sortilegios)):
            draw.text((ejex, ejey+i*48), str(sortilegios[i]), fill=(0, 0, 0), font=font2, anchor ="ms")

    def llamar_funciones():

        caracteristicas=dibujar_caracteristicas(personaje[0],973,50,6,7)
        mym=dibujar_gdh(personaje[2][0:5],501,524,1,0,0) 
        armas=dibujar_gdh(personaje[2][5:12],501,658,1,0,1)
        generales=dibujar_gdh(personaje[2][12:16],501,834,1,0,2)
        subterfugio=dibujar_gdh(personaje[2][16:20],501,948,1,0,3)
        magicas=dibujar_gdh(personaje[2][20:23],501,1060,1,0,4)
        otras=dibujar_gdh(personaje[2][23:25],501,1180,1,0,5)
        des_fis=dibujar_des_fis_y_pp(personaje[2][25],347,1295,3,"des_fis")
        pp=dibujar_des_fis_y_pp(personaje[2][26],347,1352,-2,"pp")
        nombrepj=dibujar_individual(personaje[1][1],360,24)
        nombre=dibujar_individual(personaje[1][0],130,24)
        raza=dibujar_individual(personaje[1][2],95,50)
        estatura=dibujar_individual(personaje[1][3],305,50," m")
        peso=dibujar_individual(personaje[1][4],400,50," kg")
        genero=dibujar_individual(personaje[1][5],100,75)
        edad=dibujar_individual(personaje[1][6],195,75)
        pelo=dibujar_individual(personaje[1][7],290,75)
        ojos=dibujar_individual(personaje[1][8],400,75)
        esp_fisico=dibujar_individual(personaje[1][9],135,100)
        personalidad=dibujar_individual(personaje[1][10],125,126)
        motivacion=dibujar_individual(personaje[1][11],125,152)
        alineamiento=dibujar_individual(personaje[1][12],135,177)
        status=dibujar_individual(personaje[1][13],85,202)
        familia=dibujar_individual(personaje[1][14],325,202)
        profesion=dibujar_individual(personaje[1][15],130,227)
        nivel=dibujar_individual(personaje[1][16],325,227)
        experiencia=dibujar_individual(personaje[1][18],378,227)
        tr=dibujar_tr(910,1622)
        idiomas=dibujar_idiomas(130,344)
        sortilegios=dibujar_sortilegios(120, 650)

        # secundarias=dibujar_gdh(grados_de_hab_sec,510,1374,3,4,6)
        # return datosbasicos,caracteristicas, mym, armas, generales, subterfugio, magicas, otras, des_fis,pp
    
    llamar_funciones()

    image.save("./ImprimirHoja/Output/%s - Lvl. %i.png" %(personaje[1][0], personaje[1][16])) 
    width, height = image.size
    pdf = canvas.Canvas("./ImprimirHoja/Output/%s - Lvl. %i.pdf" %(personaje[1][0], personaje[1][16]), pagesize=(width, height))
    pdf.drawImage("./ImprimirHoja/Output/%s - Lvl. %i.png" %(personaje[1][0], personaje[1][16]), 0, 0, width=width, height=height)
    pdf.showPage()
    pdf.save()
    os.remove("./ImprimirHoja/Output/%s - Lvl. %i.png" %(personaje[1][0], personaje[1][16]))

