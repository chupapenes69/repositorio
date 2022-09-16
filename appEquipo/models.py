from django.db import models

# Create your models here.

class tipo_equipo(models.Model):
    tipo_equipo_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()

class equipo(models.Model):
    equipo_id=models.BigAutoField(primary_key=True)
    logo=models.BinaryField(max_length=None)
    vestimenta=models.BinaryField()
    nombre=models.CharField(max_length=70)
    siglas=models.CharField(max_length=3)
    tipo_equipo_id=models.ForeignKey(tipo_equipo,on_delete=models.CASCADE)
    sede_id=models.ForeignKey("appPartido.sede",on_delete=models.CASCADE)
    deporte_id=models.ForeignKey("appCompeticion.deporte",on_delete=models.CASCADE)
    encuentro_id=models.ForeignKey("appPartido.encuentro",on_delete=models.CASCADE)

class posicion_jugador(models.Model):
    posicion_jugador_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)

class alineacion_equipo(models.Model):
    alineacion_equipo_id=models.BigAutoField(primary_key=True)
    equipo_id=models.ForeignKey(equipo,on_delete=models.CASCADE)
    dorsal=models.IntegerField()
    posicion_jugador_id=models.ForeignKey(posicion_jugador,on_delete=models.CASCADE)
    capitan=models.BooleanField()
    estado=models.BooleanField()
    contrato_id=models.ForeignKey("appContrato.contrato",on_delete=models.CASCADE)

