from django.db import models

# Create your models here.

class tipo_competicion(models.Model):
    tipo_competicion_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    estado=models.BooleanField()

class competicion(models.Model):
    competicion_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    pais_id=models.IntegerField()
    tipo_competicion_id=models.ForeignKey(tipo_competicion,on_delete=models.CASCADE)

class pais(models.Model):
    pais_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)

class deporte(models.Model):
    deporte_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    estado=models.BooleanField()

class grupo(models.Model):
    grupo_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)

class detalle_grupo(models.Model):
    detalle_grupo_id=models.BigAutoField(primary_key=True)
    equipo_id=models.ForeignKey("appEquipo.equipo",on_delete=models.CASCADE)
    grupo_id=models.ForeignKey(grupo,on_delete=models.CASCADE)
    competicion_id=models.ForeignKey(competicion,on_delete=models.CASCADE)

class tabla(models.Model):
    tabla_id=models.BigAutoField(primary_key=True)
    competicion_id=models.ForeignKey(competicion,on_delete=models.CASCADE)
    equipo_id=models.ForeignKey("appEquipo.equipo",on_delete=models.CASCADE)
    ganado=models.IntegerField()
    perdido=models.IntegerField()
    empatado=models.IntegerField()
    goles_favor=models.IntegerField()
    goles_contra=models.IntegerField()
    tarjetas_amarillas=models.IntegerField()
    tarjetas_rojas=models.IntegerField()
    puntos=models.IntegerField()


