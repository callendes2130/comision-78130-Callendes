from django.db import models 
import uuid  
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    universidad= models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    comision = models.IntegerField(unique=True)
    code = models.CharField(
        max_length=32,
        unique=True,
        default=uuid.uuid4().hex
    )