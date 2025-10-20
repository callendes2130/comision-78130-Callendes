from django.db import models

class T_Local(models.Model):
    identificador=models.IntegerField(unique=True)
    descripcion=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    comuna=models.CharField(max_length=40)
    totalmesas=models.IntegerField()
    totalempleados=models.IntegerField()

    def __str__(self):
        return f"Local:{self.identificador}"

class T_Cliente(models.Model):
    nombreC=models.CharField(max_length=30)
    apellidoC=models.CharField(max_length=30)
    emailC=models.EmailField()
    
    def __str__(self):
        return f"cliente:{self.nombreC}"

class T_mesero(models.Model):
    nombreM=models.CharField(max_length=30)
    apellidoM=models.CharField(max_length=30)
    emailM=models.EmailField()
    edad=models.IntegerField()

class T_comanda(models.Model):
    numeroC=models.IntegerField()
    mesaC=models.IntegerField()
    localC=models.IntegerField()
    estadoC=models.CharField(max_length=15)
    totalcomanda=models.IntegerField()

# Create your models here.
