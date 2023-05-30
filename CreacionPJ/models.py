from django.db import models

# Create your models here.

###########################################################################################################
##                                       DATOS DEL MANUAL                                                ##
###########################################################################################################

class RazasTabla1(models.Model):
    raza=models.CharField(max_length=20)
    fuerza=models.IntegerField()
    agilidad=models.IntegerField()
    constitucion=models.IntegerField()
    inteligencia=models.IntegerField()
    intuicion=models.IntegerField()
    presencia=models.IntegerField()
    sin_armadura=models.IntegerField()
    cuero=models.IntegerField()
    cuero_endurecido=models.IntegerField()
    cota_de_malla=models.IntegerField()
    coraza=models.IntegerField()
    de_filo=models.IntegerField()
    contundentes=models.IntegerField()
    a_dos_manos=models.IntegerField()
    arrojadizas=models.IntegerField()
    proyectiles=models.IntegerField()
    armas_de_asta=models.IntegerField()
    escudo=models.IntegerField()
    trepar=models.IntegerField()
    montar=models.IntegerField()
    nadar=models.IntegerField()
    rastrear=models.IntegerField()
    emboscar=models.IntegerField()
    acechar_y_esconderse=models.IntegerField()
    abrir_cerraduras=models.IntegerField()
    desactivar_trampas=models.IntegerField()
    leer_runas=models.IntegerField()
    usar_objetos=models.IntegerField()
    sortilegios_dirigidos=models.IntegerField()
    percepcion=models.IntegerField()
    liderazgo_e_influencia=models.IntegerField()
    desarrollo_fisico=models.IntegerField()
    puntos_de_poder=models.IntegerField()
    prob_sort=models.IntegerField()
    idiomas=models.IntegerField()
    puntos_de_historial=models.IntegerField()

class RazasTabla2(models.Model):
    raza=models.CharField(max_length=20)
    sin_armadura=models.IntegerField()
    cuero=models.IntegerField()
    cuero_endurecido=models.IntegerField()
    cota_de_malla=models.IntegerField()
    coraza=models.IntegerField()
    de_filo=models.IntegerField()
    contundentes=models.IntegerField()
    a_dos_manos=models.IntegerField()
    arrojadizas=models.IntegerField()
    proyectiles=models.IntegerField()
    armas_de_asta=models.IntegerField()
    escudo=models.IntegerField()
    trepar=models.IntegerField()
    montar=models.IntegerField()
    nadar=models.IntegerField()
    rastrear=models.IntegerField()
    emboscar=models.IntegerField()
    acechar_y_esconderse=models.IntegerField()
    abrir_cerraduras=models.IntegerField()
    desactivar_trampas=models.IntegerField()
    leer_runas=models.IntegerField()
    usar_objetos=models.IntegerField()
    sortilegios_dirigidos=models.IntegerField()
    percepción=models.IntegerField()
    liderazgo_e_influencia=models.IntegerField()
    desarrollo_fisico=models.IntegerField()
    puntos_de_poder=models.IntegerField()
    esencia=models.IntegerField()
    canalizacion=models.IntegerField()
    veneno=models.IntegerField()
    enfermedad=models.IntegerField()
    calor=models.IntegerField()
    frio=models.IntegerField()

class RazasTabla3(models.Model):
    raza=models.CharField(max_length=20)
    acrobacias=models.IntegerField()
    actividades_con_animales=models.IntegerField()
    actuar=models.IntegerField()
    administración=models.IntegerField()
    alquimia=models.IntegerField()
    antropología=models.IntegerField()
    arquitectura=models.IntegerField()
    artesanía=models.IntegerField()
    barrido_y_lanzamientos=models.IntegerField()
    cambiante=models.IntegerField()
    cantar_y_baile=models.IntegerField()
    ceremonias_y_rituales=models.IntegerField()
    charlatanería=models.IntegerField()
    comercio_y_negociar=models.IntegerField()
    conocimiento_callejero=models.IntegerField()
    conocimiento_de_cuevas=models.IntegerField()
    conocimiento_de_la_naturaleza=models.IntegerField()
    conocimiento_del_cielo=models.IntegerField()
    construir_trampas=models.IntegerField()
    contorsionismo=models.IntegerField()
    cordeleria=models.IntegerField()
    defensa_adrenal=models.IntegerField()
    diplomacia=models.IntegerField()
    falsificación=models.IntegerField()
    forrajear=models.IntegerField()
    frenesí=models.IntegerField()
    geografía=models.IntegerField()
    golpe_i_al_iv=models.IntegerField()
    hacer_flechas=models.IntegerField()
    heráldica=models.IntegerField()
    herbología_y_cocinar=models.IntegerField()
    herreria=models.IntegerField()
    historia=models.IntegerField()
    investigación=models.IntegerField()
    jugar_y_estrategia=models.IntegerField()
    liderazgo=models.IntegerField()
    magia_con_armadura=models.IntegerField()
    maña_y_robar_bolsillos=models.IntegerField()
    medicina=models.IntegerField()
    meditación=models.IntegerField()
    mendigar=models.IntegerField()
    mitos_y_leyendas=models.IntegerField()
    música=models.IntegerField()
    narración_y_poesía=models.IntegerField()
    navegar=models.IntegerField()
    ocultismo=models.IntegerField()
    oratoria=models.IntegerField()
    primeros_auxilios=models.IntegerField()
    religión=models.IntegerField()
    remar=models.IntegerField()
    seducción=models.IntegerField()
    señales=models.IntegerField()
    supervivencia=models.IntegerField()
    tácticas=models.IntegerField()
    tallar_madera=models.IntegerField()
    tallar_piedra=models.IntegerField()
    trabajar_el_cuero=models.IntegerField()
    trato_con_animales=models.IntegerField()
    velocidad_adrenal=models.IntegerField()
    voluntad=models.IntegerField()

class RazasTabla4(models.Model):
    raza=models.CharField(max_length=20)
    acrobacias=models.IntegerField()
    actividades_con_animales=models.IntegerField()
    actuar=models.IntegerField()
    administración=models.IntegerField()
    alquimia=models.IntegerField()
    antropología=models.IntegerField()
    arquitectura=models.IntegerField()
    artesanía=models.IntegerField()
    barrido_y_lanzamientos=models.IntegerField()
    cambiante=models.IntegerField()
    cantar_y_baile=models.IntegerField()
    ceremonias_y_rituales=models.IntegerField()
    charlatanería=models.IntegerField()
    comercio_y_negociar=models.IntegerField()
    conocimiento_callejero=models.IntegerField()
    conocimiento_de_cuevas=models.IntegerField()
    conocimiento_de_la_naturaleza=models.IntegerField()
    conocimiento_del_cielo=models.IntegerField()
    construir_trampas=models.IntegerField()
    contorsionismo=models.IntegerField()
    cordeleria=models.IntegerField()
    defensa_adrenal=models.IntegerField()
    diplomacia=models.IntegerField()
    falsificación=models.IntegerField()
    forrajear=models.IntegerField()
    frenesí=models.IntegerField()
    geografía=models.IntegerField()
    golpe_i_al_iv=models.IntegerField()
    hacer_flechas=models.IntegerField()
    heráldica=models.IntegerField()
    herbología_y_cocinar=models.IntegerField()
    herreria=models.IntegerField()
    historia=models.IntegerField()
    investigación=models.IntegerField()
    jugar_y_estrategia=models.IntegerField()
    liderazgo=models.IntegerField()
    magia_con_armadura=models.IntegerField()
    maña_y_robar_bolsillos=models.IntegerField()
    medicina=models.IntegerField()
    meditación=models.IntegerField()
    mendigar=models.IntegerField()
    mitos_y_leyendas=models.IntegerField()
    música=models.IntegerField()
    narración_y_poesía=models.IntegerField()
    navegar=models.IntegerField()
    ocultismo=models.IntegerField()
    oratoria=models.IntegerField()
    primeros_auxilios=models.IntegerField()
    religión=models.IntegerField()
    remar=models.IntegerField()
    seducción=models.IntegerField()
    señales=models.IntegerField()
    supervivencia=models.IntegerField()
    tácticas=models.IntegerField()
    tallar_madera=models.IntegerField()
    tallar_piedra=models.IntegerField()
    trabajar_el_cuero=models.IntegerField()
    trato_con_animales=models.IntegerField()
    velocidad_adrenal=models.IntegerField()
    voluntad=models.IntegerField()

class RazasIdiomas(models.Model):
    raza=models.CharField(max_length=20)
    idiomas=models.CharField(max_length=30)
    grados=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.idiomas
    
class Habilidades_Secundarias(models.Model):
    hab_sec=models.CharField(max_length=20)
    caracteristica=models.IntegerField()
    tipo=models.CharField(max_length=20)

    def __str__(self):
        return self.hab_sec

class Sortilegios(models.Model):
    lista=models.CharField(max_length=20)
    dominio=models.CharField(max_length=20)
    profesion=models.CharField(max_length=20)
    
    def __str__(self):
        return self.lista

class Profesiones(models.Model):
    profesion=models.CharField(max_length=20)
    sin_armadura=models.IntegerField()
    cuero=models.IntegerField()
    cuero_endurecido=models.IntegerField()
    cota_de_malla=models.IntegerField()
    coraza=models.IntegerField()
    de_filo=models.IntegerField()
    contundentes=models.IntegerField()
    a_dos_manos=models.IntegerField()
    arrojadizas=models.IntegerField()
    proyectiles=models.IntegerField()
    armas_de_asta=models.IntegerField()
    escudo=models.IntegerField()
    trepar=models.IntegerField()
    montar=models.IntegerField()
    nadar=models.IntegerField()
    rastrear=models.IntegerField()
    emboscar=models.IntegerField()
    acechar_y_esconderse=models.IntegerField()
    abrir_cerraduras=models.IntegerField()
    desactivar_trampas=models.IntegerField()
    leer_runas=models.IntegerField()
    usar_objetos=models.IntegerField()
    sortilegios_dirigidos=models.IntegerField()
    sortilegios_base=models.IntegerField()
    percepcion=models.IntegerField()
    liderazgo_e_influencia=models.IntegerField()
    desarrollo_fisico=models.IntegerField()
    movimiento_y_maniobra=models.IntegerField()
    habilidades_en_armas=models.IntegerField()
    habilidades_generales=models.IntegerField()
    habilidades_de_subterfugio=models.IntegerField()
    habilidades_mágicas=models.IntegerField()
    desarrollo_físico=models.IntegerField()
    habilidades_secundarias=models.IntegerField()
    idiomas=models.IntegerField()
    listas_de_sortilegio=models.IntegerField()
    atleticas=models.IntegerField()
    exteriores=models.IntegerField()
    sociales=models.IntegerField()
    académicas=models.IntegerField()
    manuales=models.IntegerField()
    artes_marciales=models.IntegerField()
    especiales=models.IntegerField()
    artísticas=models.IntegerField()
    religiosas=models.IntegerField()
    callejeras=models.IntegerField()

###########################################################################################################
##                                           FORMUALARIOS                                                ##
###########################################################################################################

class DatosBasicos(models.Model):
    nombre_pj = models.CharField(max_length=255, blank=True)
    genero = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino')))
    estatura = models.FloatField(blank=True)
    peso = models.IntegerField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    pelo = models.CharField(max_length=255, blank=True)
    ojos = models.CharField(max_length=255, blank=True)
    especial_fisico = models.CharField(max_length=255, blank=True)
    personalidad = models.CharField(max_length=255, blank=True)
    motivacion = models.CharField(max_length=255, blank=True)
    alineamiento = models.CharField(max_length=255, choices=(
        ('Legal Bueno', 'Legal Bueno'),
        ('Legal Neutral', 'Legal Neutral'),
        ('Legal Malo', 'Legal Malo'),
        ('Neutral Bueno', 'Neutral Bueno'),
        ('Neutral Neutral', 'Neutral Neutral'),
        ('Neutral Malo', 'Neutral Malo'),
        ('Caótico Bueno', 'Caótico Bueno'),
        ('Caótico Neutral', 'Caótico Neutral'),
        ('Caótico Malo', 'Caótico Malo'),
    ))
    status = models.CharField(max_length=255, blank=True)
    familia=models.CharField(max_length=255, blank=True)
    experiencia=models.IntegerField(blank=True, null=True)

class RazaYProfesion(models.Model):
    RAZA_CHOICES = (
        ('Enano','Enano'),
        ('Umli','Umli'),
        ('Elfos Noldor','Elfos Noldor'),
        ('Elfos Sindar','Elfos Sindar'),
        ('Elfos Silvano','Elfos Silvano'),
        ('Medio Elfos','Medio Elfos'),
        ('Hobbit','Hobbit'),
        ('Beórnidas','Beórnidas'),
        ('Núm. Negros','Núm. Negros'),
        ('Corsarios','Corsarios'),
        ('Dorwinrim','Dorwinrim'),
        ('Dúnedain','Dúnedain'),
        ('Dunledinos','Dunledinos'),
        ('Hombres del Este','Hombres del Este'),
        ('Haradrim del Norte','Haradrim del Norte'),
        ('Haradrim del Sur','Haradrim del Sur'),
        ('Lossoth','Lossoth'),
        ('Rohirrim','Rohirrim'),
        ('Campesinos','Campesinos'),
        ('Burgueses','Burgueses'),
        ('Variags','Variags'),
        ('H. de los Bosques','H. de los Bosques'),
        ('Woses','Woses'),
        ('Orcos','Orcos'),
        ('Uruk-Hai','Uruk-Hai'),
        ('Medio Orcos','Medio Orcos'),
        ('Trolls','Trolls'),
        ('Olog-Hai','Olog-Hai'),
        ('Medio Trolls','Medio Trolls'),
    )
    PROFESION_CHOICES = (
        ('Guerrero', 'Guerrero'),
        ('Montaraz', 'Montaraz'),
        ('Explorador', 'Explorador'),
        ('Mago', 'Mago'),
        ('Animista', 'Animista'),
        ('Bardo', 'Bardo'),
    )
    DOMINIO_CHOICES = (
        ('Esencia', 'Esencia'),
        ('Canalizacion', 'Canalización'),
    )
    raza = models.CharField(max_length=100, choices=RAZA_CHOICES)
    profesion = models.CharField(max_length=100, choices=PROFESION_CHOICES)
    dominio_magico = models.CharField(max_length=100, choices=DOMINIO_CHOICES)

class Caracteristicas(models.Model):

    CARACTERISTICAS_CHOICES = (
        ('---', '---'),
        ('FUE', 'FUE'),
        ('AGI', 'AGI'),
        ('CON', 'CON'),
        ('INT', 'INT'),
        ('I', 'I'),
        ('PRE', 'PRE'),
        ('APA', 'APA')
    )

    caract1= models.CharField(max_length=255, choices=CARACTERISTICAS_CHOICES)
    caract2= models.CharField(max_length=255, choices=CARACTERISTICAS_CHOICES)
    caract3= models.CharField(max_length=255, choices=CARACTERISTICAS_CHOICES)
    caract4= models.CharField(max_length=255, choices=CARACTERISTICAS_CHOICES)
    caract5= models.CharField(max_length=255, choices=CARACTERISTICAS_CHOICES)
    caract6= models.CharField(max_length=255, choices=CARACTERISTICAS_CHOICES)
    caract7= models.CharField(max_length=255, choices=CARACTERISTICAS_CHOICES)
