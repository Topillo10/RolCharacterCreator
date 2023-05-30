from django import forms
from CreacionPJ.models import DatosBasicos
from CreacionPJ.models import RazaYProfesion
from CreacionPJ.models import Caracteristicas
from CreacionPJ.models import Sortilegios
from CreacionPJ.models import RazasIdiomas
from GuardarPersonaje.models import Personaje_Sort
from GuardarPersonaje.models import Personaje_Idiomas
from GuardarPersonaje.models import Personaje

class DatosBasicosForm(forms.ModelForm):

    ALINEAMIENTO_CHOICES = (
        ('Legal Bueno', 'Legal Bueno'),
        ('Legal Neutral', 'Legal Neutral'),
        ('Legal Malo', 'Legal Malo'),
        ('Neutral Bueno', 'Neutral Bueno'),
        ('Neutral Neutral', 'Neutral Neutral'),
        ('Neutral Malo', 'Neutral Malo'),
        ('Caótico Bueno', 'Caótico Bueno'),
        ('Caótico Neutral', 'Caótico Neutral'),
        ('Caótico Malo', 'Caótico Malo'),
    )

    nombre_pj = forms.CharField(label='Nombre PJ', required=False, widget=forms.TextInput(attrs={'placeholder': 'Ej: Eitri'}))
    genero = forms.ChoiceField(label='Género', choices=(('M', 'Masculino'), ('F', 'Femenino')), widget=forms.Select(attrs={'id': 'Genero'}))
    estatura = forms.FloatField(label='Estatura (mts)', required=False, widget=forms.NumberInput(attrs={'placeholder': 'Ej: 1.30', 'step': '0.01', 'value': '1.50'}))
    peso = forms.IntegerField(label='Peso (kg.)', required=False, widget=forms.NumberInput(attrs={'placeholder': 'Ej: 85'}))
    edad = forms.IntegerField(label='Edad', required=False, widget=forms.NumberInput(attrs={'placeholder': 'Ej: 22', 'value': '18'}))
    pelo = forms.CharField(label='Pelo', required=False, widget=forms.TextInput(attrs={'placeholder': 'Ej: Rojo'}))
    ojos = forms.CharField(label='Ojos', required=False, widget=forms.TextInput(attrs={'placeholder': 'Ej: Celestes'}))
    especial_fisico = forms.CharField(label='Especial Físico', required=False, widget=forms.TextInput(attrs={'placeholder': 'Ej: Cicatriz en X'}))
    personalidad = forms.CharField(label='Personalidad', required=False, widget=forms.TextInput(attrs={'placeholder': 'XXXXXXXX'}))
    motivacion = forms.CharField(label='Motivacion', required=False, widget=forms.TextInput(attrs={'placeholder': 'Ej: Buscar al asesino de mi padre'}))
    alineamiento = forms.ChoiceField(label='Alineamiento', choices=ALINEAMIENTO_CHOICES, widget=forms.Select(attrs={'id': 'Alineamiento'}))
    status = forms.CharField(label='Status', required=False, widget=forms.TextInput(attrs={'placeholder': 'Ej: Fugitivo del reino'}))
    familia = forms.CharField(label='Familia', required=False, widget=forms.TextInput(attrs={'placeholder': 'Datos de la familia'}))
    experiencia = forms.IntegerField(label='Experiencia', required=False, initial=0, widget=forms.NumberInput(attrs={'readonly': True}))

    class Meta:
        model = DatosBasicos
        fields = [
            'nombre_pj',
            'genero',
            'estatura',
            'peso',
            'edad',
            'pelo',
            'ojos',
            'especial_fisico',
            'personalidad',
            'motivacion',
            'alineamiento',
            'status',
            'familia',
            'experiencia',
        ]

class RazaYProfesionForm(forms.ModelForm):

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

    raza = forms.ChoiceField(label='Raza', choices=RAZA_CHOICES)
    profesion = forms.ChoiceField(label='Profesión', choices=PROFESION_CHOICES)
    dominio_magico = forms.ChoiceField(label='Dominio Mágico', choices=DOMINIO_CHOICES)

    class Meta:
        model = RazaYProfesion
        fields = ('raza', 'profesion', 'dominio_magico')

class CaracteristicasForm(forms.ModelForm):

    CARACTERISTICAS_CHOICES = ()

    caract1 = forms.ChoiceField(choices=CARACTERISTICAS_CHOICES, widget=forms.Select(attrs={'id': 'caract1'}))
    caract2 = forms.ChoiceField(choices=CARACTERISTICAS_CHOICES, widget=forms.Select(attrs={'id': 'caract2'}))
    caract3 = forms.ChoiceField(choices=CARACTERISTICAS_CHOICES, widget=forms.Select(attrs={'id': 'caract3'}))
    caract4 = forms.ChoiceField(choices=CARACTERISTICAS_CHOICES, widget=forms.Select(attrs={'id': 'caract4'}))
    caract5 = forms.ChoiceField(choices=CARACTERISTICAS_CHOICES, widget=forms.Select(attrs={'id': 'caract5'}))
    caract6 = forms.ChoiceField(choices=CARACTERISTICAS_CHOICES, widget=forms.Select(attrs={'id': 'caract6'}))
    caract7 = forms.ChoiceField(choices=CARACTERISTICAS_CHOICES, widget=forms.Select(attrs={'id': 'caract7'}))

    class Meta:
        model = Caracteristicas
        fields = ('caract1', 'caract2', 'caract3', 'caract4', 'caract5', 'caract6', 'caract7')

class SortilegiosPersonajeForm(forms.Form):

    CHOICES_SEPARATOR= (None, '----')

    lista = forms.ChoiceField(
        label='Listas de Sortilegios', 
        choices=[CHOICES_SEPARATOR], 
        widget=forms.Select(attrs={'class': 'form-control'})
        )

    def __init__(self, *args, **kwargs):
        dominio = kwargs.pop('dominio', None)
        profesion = kwargs.pop('profesion', None)
        nombre_pj = kwargs.pop('nombre_pj', None)
        usuario = kwargs.pop('usuario', None)
        nivel = kwargs.pop('nivel', None)
        super().__init__(*args, **kwargs)
        
        queryset = Sortilegios.objects.filter(dominio=dominio, profesion=profesion)
        queryset_to_exclude = Personaje_Sort.objects.filter(Personaje_id=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel))
        
        result_queryset = queryset.exclude(lista__in=queryset_to_exclude.values_list('lista', flat=True))
        opciones= [(str(lista), str(lista)) for lista in result_queryset]
        
        self.fields['lista'].choices += opciones

class IdiomasPersonajeForm(forms.Form):

    CHOICES_SEPARATOR= (None, '----')

    idiomas = forms.ChoiceField(
        label='Agregar idioma',
        choices=[CHOICES_SEPARATOR],
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    def __init__(self, *args, **kwargs):
        nombre_pj = kwargs.pop('nombre_pj', None)
        usuario = kwargs.pop('usuario', None)
        nivel = kwargs.pop('nivel', None)
        super().__init__(*args, **kwargs)
        
        queryset = RazasIdiomas.objects.values('idiomas').distinct()
        queryset_to_exclude = Personaje_Idiomas.objects.filter(Personaje_id=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel))
        
        options=[(idioma['idiomas'], idioma['idiomas']) for idioma in queryset if idioma['idiomas'] not in [elem.idiomas for elem in queryset_to_exclude]]
        self.fields['idiomas'].choices += options
    
