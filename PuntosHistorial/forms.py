from django import forms
from CreacionPJ.models import Sortilegios
from CreacionPJ.models import Habilidades_Secundarias
from GuardarPersonaje.models import Personaje_Sort
from GuardarPersonaje.models import Personaje_Idiomas
from GuardarPersonaje.models import Personaje_HabSec
from GuardarPersonaje.models import Personaje

class HabPrimForm(forms.Form):
    
    CHOICES_SEPARATOR= (
        (None, '----'),
        (0,'Sin Armadura'),
        (1,'Cuero'),
        (2,'Cuero Endurecido'),
        (3,'Cota de Malla'),
        (4,'Coraza'),
        (5,'De Filo'),
        (6,'Contundentes'),
        (7,'A Dos Manos'),
        (8,'Arrojadizas'),
        (9,'Proyectiles'),
        (10,'Armas de Asta'),
        (11,'Escudo'),
        (12,'Trepar'),
        (13,'Montar'),
        (14,'Nadar'),
        (15,'Rastrear'),
        (16,'Emboscar'),
        (17,'Acechar y Esconderse'),
        (18,'Abrir Cerraduras'),
        (19,'Desactivar Trampas'),
        (20,'Leer Runas'),
        (21,'Usar Objetos'),
        (22,'Sortilegios Dirigidos'),
        (23,'Percepcion'),
        (24,'Liderazgo e Influencia'),
        (25,'Desarrollo Fisico'),
        (26,'Puntos de Poder')
        )

    hab_prim = forms.ChoiceField(
        label='Habilidad Primaria',
        choices=[CHOICES_SEPARATOR],
        widget=forms.Select(attrs={'class': 'form-control'})
        )

class HabSecForm(forms.Form):
    CHOICES_SEPARATOR= (None, '----')

    hab_sec = forms.ChoiceField(
        label='Habilidades Secundarias', 
        choices=[CHOICES_SEPARATOR], 
        widget=forms.Select(attrs={'class': 'form-control'})
        )

    def __init__(self, *args, **kwargs):
        nombre_pj = kwargs.pop('nombre_pj', None)
        usuario = kwargs.pop('usuario', None)
        nivel = kwargs.pop('nivel', None)
        super().__init__(*args, **kwargs)
        
        queryset = Personaje_HabSec.objects.filter(Personaje_id=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel))
        
        opciones= [(str(hab_sec), str(hab_sec)) for hab_sec in queryset]
        
        self.fields['hab_sec'].choices += opciones

class ConocimientosForm(forms.Form):

    CHOICES_SEPARATOR= (None, '----')

    conocimiento = forms.ChoiceField(
        label='Habilidad de Conocimiento', 
        choices=[CHOICES_SEPARATOR], 
        widget=forms.Select(attrs={'class': 'form-control'})
        )

    def __init__(self, *args, **kwargs):
        nombre_pj = kwargs.pop('nombre_pj', None)
        usuario = kwargs.pop('usuario', None)
        nivel = kwargs.pop('nivel', None)
        super().__init__(*args, **kwargs)
        
        queryset = Habilidades_Secundarias.objects.filter(hab_sec__startswith='Conocimiento')
        queryset_to_exclude = Personaje_HabSec.objects.filter(Personaje_id=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel))

        result_queryset = queryset.exclude(hab_sec__in=queryset_to_exclude.values_list('hab_sec', flat=True))
        opciones= [(str(hab_sec), str(hab_sec)) for hab_sec in result_queryset]
        
        self.fields['hab_sec'].choices += opciones

class CaracteristicasForm(forms.Form):

    fue = forms.IntegerField(label='FUE')
    agi = forms.IntegerField(label='AGI')
    con = forms.IntegerField(label='CON')
    int = forms.IntegerField(label='INT')
    i = forms.IntegerField(label='I')
    pre = forms.IntegerField(label='PRE')
    apa = forms.IntegerField(label='AGI')

    def __init__(self, *args, **kwargs):
        nombre_pj = kwargs.pop('nombre_pj', None)
        usuario = kwargs.pop('usuario', None)
        nivel = kwargs.pop('nivel', None)
        super().__init__(*args, **kwargs)
        personaje=Personaje.objects.get(nombre_pj=nombre_pj,usuario=usuario,nivel=nivel)
        self.fields['fue'].value=personaje.fuerza
        # self.fields['fue'].max=personaje.fuerza
        self.fields['agi'].value=personaje.agilidad
        self.fields['con'].value=personaje.constitucion
        self.fields['int'].value=personaje.inteligencia
        self.fields['i'].value=personaje.intuicion
        self.fields['pre'].value=personaje.presencia
        self.fields['apa'].value=personaje.apariencia




class HabPrimForm(forms.Form):
    pass

class HabPrimForm(forms.Form):
    pass

class HabPrimForm(forms.Form):
    pass

