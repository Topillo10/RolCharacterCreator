
from django.db import models

class ModeloPrincipal(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.CharField(max_length=100)

class ModeloCampoAdicional(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    modelo_principal = models.ForeignKey(ModeloPrincipal, on_delete=models.CASCADE)

modelo_principal = ModeloPrincipal.objects.create(campo1='valor1', campo2='valor2')
ModeloCampoAdicional.objects.create(nombre='nombre1', valor='valor1', modelo_principal=modelo_principal)
ModeloCampoAdicional.objects.create(nombre='nombre2', valor='valor2', modelo_principal=modelo_principal)
