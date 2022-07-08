from operator import ge
from xml import dom
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import PersonajeDatosBasicosModel


# Create your views here.

def pjcreation01(request):

    return render(request, "pjcreation/pjcreation01.html")

def pjcreation01create(request):
    nombrepj=request.POST('NombrePJ')
    jugador=User.get_username()
    genero=request.POST('Genero')
    estatura=request.POST('Estatura')
    peso=request.POST('peso')
    raza=request.POST('Raza')
    edad=request.POST('Edad')
    pelo=request.POST('Pelo')
    ojos=request.POST('Ojos')
    especialfisico=request.POST('Especial Fisico')
    personalidad=request.POST('Personalidad')
    motivacion=request.POST('Motivacion')
    alineamiento=request.POST('Alineamiento')
    status=request.POST('Status')
    profesion=request.POST('Profesion')
    nivel=0
    dominiomagico=request.POST('Dominio Mágico')

    personaje=PersonajeDatosBasicosModel.objects.create(nombrepj=nombrepj, jugador=jugador, genero=genero, estatura=estatura,
    peso=peso, raza=raza, edad=edad, pelo=pelo, ojos=ojos, especialfisico=especialfisico, personalidad=personalidad, motivacion=motivacion,
    alineamiento=alineamiento, status=status, profesion=profesion, nivel=nivel, dominiomagico=dominiomagico)

    return redirect('PJCreation02') 

def pjcreation02(request):

    return render(request, "pjcreation/pjcreation02.html")
