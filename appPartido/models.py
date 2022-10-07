from email.policy import default
from django.db import models

# Create your models here.

class formacion(models.Model):
    formacion_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=10)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural='formacion'

class estado(models.Model):
    estado_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural='estado'

class ciudad(models.Model):
    ciudad_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    norma=models.CharField(max_length=5)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural='ciudad'

class sede(models.Model):
    sede_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    alias=models.CharField(max_length=50)
    capacidad=models.IntegerField()
    fecha_inauguracion=models.DateField()
    ciudad_id=models.ForeignKey(ciudad, on_delete=models.CASCADE,db_column='ciudad_id')
    estado_id=models.ForeignKey(estado, on_delete=models.CASCADE,db_column='estado_id')
    pais_id=models.ForeignKey("appCompeticion.pais",on_delete=models.CASCADE,db_column='pais_id')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='sede'

class encuentro(models.Model):
    encuentro_id=models.BigAutoField(primary_key=True)
    sede_id=models.ForeignKey(sede,on_delete=models.CASCADE,db_column='sede_id')
    terna_arbitral_id=models.ForeignKey("appArbitro.terna_arbitral", on_delete=models.CASCADE,db_column='terna_arbitral_id')
    fecha=models.DateField()
    humedad=models.IntegerField()
    clima=models.IntegerField()
    estado_jugado=models.BooleanField()

    def __str__(self):
        return str(self.encuentro_id)
    
    class Meta:
        verbose_name_plural='encuentro'

class detalle_encuentro(models.Model):
    CHOICE_TIPO_EQUIPO= [
        ('L','LOCAL'),
        ('V','VISITA'),
    ]

    detalle_encuentro_id=models.BigAutoField(primary_key=True)
    encuentro_id=models.ForeignKey('encuentro',on_delete=models.CASCADE,db_column='encuentro_id')
    equipo_id=models.ForeignKey('appEquipo.equipo', on_delete=models.CASCADE,db_column='equipo_id')
    formacion_id=models.ForeignKey('formacion',on_delete=models.CASCADE,db_column='formacion_id')
    # CHOICE_TIPO_EQUIPO | L = LOCAL | V = VISITA
    tipo_equipo=models.CharField(max_length=1,choices=CHOICE_TIPO_EQUIPO)
    resultado=models.CharField(max_length=3)

    def __str__(self):
        return str(self.detalle_encuentro_id)

    class Meta:
        verbose_name_plural='detalle_encuentro'
    
class evento(models.Model):
    evento_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural='evento'

class evento_persona(models.Model):
    CHOICE_TIPO_SUCESO= [
        ('E','ENTRADA'),
        ('S','SALIDA'),
    ]

    encuentro_evento_id=models.BigAutoField(primary_key=True)
    encuentro_id=models.ForeignKey(encuentro,on_delete=models.CASCADE,db_column='encuentro_id')
    evento_id=models.ForeignKey(evento,on_delete=models.CASCADE,db_column='evento_id')
    persona_id=models.ForeignKey("appContrato.persona",on_delete=models.CASCADE,db_column='persona_id')
    suceso=models.CharField(max_length=5,default='ABC')
    # CHOICE_TIPO_SUCESO | E = ENTRADA , S = SALIDA
    tipo_suceso=models.CharField(max_length=1,choices=CHOICE_TIPO_SUCESO,blank=True,null=True)   
    tiempo=models.IntegerField()
    observacion=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return str(self.encuentro_evento_id)

    class Meta:
        verbose_name_plural='evento_persona'

