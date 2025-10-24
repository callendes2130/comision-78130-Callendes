from django.db import models

class T_Proceso(models.Model):
    identificador=models.IntegerField(unique=True)
    descripcion=models.CharField(max_length=50)
    cargo=models.CharField(max_length=100)
    fechainicio=models.DateField()
    fechafin=models.DateField()
    totalpuestos=models.IntegerField()

    def __str__(self):
        return f"Proceso ID:{self.identificador}"

class T_Candidato(models.Model):
    idPostulante=models.CharField(max_length=30)
    nombreC=models.CharField(max_length=30)
    apellidoC=models.CharField(max_length=30)
    emailC=models.EmailField()
    profesion=models.CharField(max_length=100)
    
    def __str__(self):
        return f"Candidato ID:{self.idPostulante}"

class T_Entrevista(models.Model):
    idEntrevista=models.IntegerField(unique=True)
    idProcesoE=models.IntegerField()
    idPostulanteE=models.CharField(max_length=30)
    fechaE=models.DateField()
    nota=models.IntegerField()

    def __str__(self):
        return f"Entrevista ID:{self.idEntrevista}"

# Create your models here.
