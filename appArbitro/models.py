from tkinter import CASCADE
from django.db import models

# Create your models here.

class arbitro(models.Model):
    arbitro_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField()
    tipo_arbitro=models.CharField(max_length=1)
    pais_id=models.ForeignKey("appCompeticion.pais",on_delete=models.CASCADE)
    estado=models.BooleanField()

class terma_arbitral(models.Model):
    terma_arbitral_id=models.BigAutoField(primary_key=True)
    estado=models.BooleanField()

class detalle_terma(models.Model):
    detalle_terma_id=models.BigAutoField(primary_key=True)
    terma_arbitral_id=models.ForeignKey(terma_arbitral,on_delete=models.CASCADE)
    arbitro_id=models.ForeignKey(arbitro,on_delete=models.CASCADE)
    estado_jugo=models.BooleanField()
