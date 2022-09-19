from django.db import models

# Create your models here.

class tipo_persona(models.Model):
    tipo_persona_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural='tipo_persona'


class persona(models.Model):
    persona_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    alias=models.CharField(max_length=20)
    sexo=models.CharField(max_length=1)
    fecha_nacimiento=models.DateField()
    pais_id=models.ForeignKey("appCompeticion.pais",on_delete=models.CASCADE, db_column='pais_id')
    estatura=models.FloatField()
    peso=models.FloatField()
    estado=models.BooleanField()
    tipo_persona_id=models.ForeignKey(tipo_persona,on_delete=models.CASCADE, db_column='tipo_persona_id')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='persona'

class contrato(models.Model):
    contrato_id=models.BigAutoField(primary_key=True)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    valor=models.FloatField()
    tipo_contrato=models.CharField(max_length=1)
    estado=models.BooleanField()
    persona_id=models.ForeignKey(persona,on_delete=models.CASCADE, db_column='persona_id')

    def __str__(self):
        return str(self.tipo_contrato)

    class Meta:
        verbose_name_plural='contrato'