from django.db import models
from datetime import *

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Estatus')

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Estado')

    def __str__(self):
        return self.name


class Colonia(models.Model):
    name = models.CharField(max_length=20, verbose_name='Colonia')

    def __str__(self):
        return self.name


class Modelo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Año')

    def __str__(self):
        return self.name


class Submarca(models.Model):
    name = models.CharField(max_length=120, verbose_name='Submarca')

    def __str__(self):
        return self.name


class Marca(models.Model):
    name = models.CharField(max_length=120, verbose_name='Marca')
    submarca = models.ForeignKey(Submarca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    first_name = models.CharField(max_length=30, verbose_name='apellido paterno')
    second_name = models.CharField(max_length=30, verbose_name='apellido materno')
    apodo = models.CharField(max_length=30, verbose_name='apodo', null=True, blank=True)
  #  curp = models.CharField(max_length=18, verbose_name='curp', unique=True)
    rfc = models.CharField(max_length=13, verbose_name='rfc', unique=True)
    mail = models.EmailField(verbose_name='correo', unique=True, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    cp = models.PositiveIntegerField(verbose_name='cp')
    street = models.CharField(max_length=200, verbose_name='calle')
    number = models.PositiveIntegerField(verbose_name='numero', unique=True)
    interior = models.PositiveIntegerField(verbose_name='interior', null=True,blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date_create = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now_add=True)
    capital = models.DecimalField(verbose_name='capital', max_digits=9, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Unidad(models.Model):
    Numero = models.PositiveIntegerField(unique=True,verbose_name='Numero de unidad')
   # placas = models.CharField(max_length=50, verbose_name='Placas')
   # year = models.ForeignKey(Modelo, on_delete=models.CASCADE)
   # marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
   # submarca = models.ForeignKey(Submarca, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Owner,on_delete=models.CASCADE)
    valor = models.FloatField(verbose_name='Valor Factura')
    tasa = models.PositiveIntegerField(verbose_name='Tasa')
    plazo = models.PositiveIntegerField(verbose_name='Plazo')
    tiie = models.FloatField(verbose_name='TIIE')
    date_create = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.Numero)



class Tipo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Tipo')
    def __str__(self):
        return self.name


class Conceptos(models.Model):
    name = models.CharField(max_length=100, verbose_name='Concepto')
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Register(models.Model):
    owner = models.ForeignKey(Owner,verbose_name='propietario',on_delete=models.CASCADE)
    concepto = models.ForeignKey(Conceptos,verbose_name='concepto',on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo,verbose_name='tipo',on_delete=models.CASCADE)
    importe = models.PositiveIntegerField(verbose_name='importe', default=0)
    referencia = models.CharField(max_length=100,verbose_name='referencia',null=True,blank=True)
    comentarios = models.TextField(max_length=100,verbose_name='comentario', null=True , blank=True)
    fecha = models.DateField(auto_now=True, verbose_name='fecha')
    date_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.concepto)

class AccountStatus(models.Model):
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad,on_delete=models.CASCADE)
    concepto = models.ForeignKey(Conceptos,on_delete=models.CASCADE)
    ref = models.CharField(max_length=150,verbose_name='ref')

    def __str__(self):
        return self.owner
