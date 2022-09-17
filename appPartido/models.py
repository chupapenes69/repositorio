from django.db import models

# Create your models here.

class estado(models.Model):
    estado_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)

class ciudad(models.Model):
    ciudad_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    norma=models.CharField(max_length=5)

class sede(models.Model):
    sede_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    capacidad=models.IntegerField()
    ciudad_id=models.ForeignKey(ciudad, on_delete=models.CASCADE,db_column='ciudad_id')
    estado_id=models.ForeignKey(estado, on_delete=models.CASCADE,db_column='estado_id')
    pais_id=models.ForeignKey("appCompeticion.pais",on_delete=models.CASCADE,db_column='pais_id')

class encuentro(models.Model):
    encuentro_id=models.BigAutoField(primary_key=True)
    equipo_local_id=models.ForeignKey("appEquipo.equipo", on_delete=models.CASCADE, related_name='equipo_local_id', db_column='equipo_local_id')
    equipo_visitante_id=models.ForeignKey("appEquipo.equipo", on_delete=models.CASCADE, related_name='equipo_visitante_id', db_column='equipo_visitante_id')
    resultado_general=models.CharField(max_length=1)
    resultado_equipo_a=models.IntegerField()
    resultado_equipo_b=models.IntegerField()
    sede_id=models.ForeignKey(sede,on_delete=models.CASCADE,db_column='sede_id')
    terma_arbitral_id=models.ForeignKey("appArbitro.terma_arbitral", on_delete=models.CASCADE,db_column='terma_arbitral_id')
    fecha=models.DateField()
    humedad=models.IntegerField()
    clima=models.IntegerField()
    estado_jugado=models.BooleanField()

class evento(models.Model):
    evento_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()

class evento_persona(models.Model):
    encuentro_evento_id=models.BigAutoField(primary_key=True)
    encuentro_id=models.ForeignKey(encuentro,on_delete=models.CASCADE,db_column='encuentro_id')
    evento_id=models.ForeignKey(evento,on_delete=models.CASCADE,db_column='evento_id')
    persona_id=models.ForeignKey("appContrato.persona",on_delete=models.CASCADE,db_column='persona_id')
    tiempo=models.IntegerField()

