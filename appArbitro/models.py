from tabnanny import verbose
from django.db import models

# Create your models here.

class arbitro(models.Model):
    arbitro_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField()
    tipo_arbitro=models.CharField(max_length=1)
    pais_id=models.ForeignKey("appCompeticion.pais",on_delete=models.CASCADE,db_column='pais_id')
    estado=models.BooleanField()

    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        verbose_name_plural='arbitro'
        

class terma_arbitral(models.Model):
    terma_arbitral_id=models.BigAutoField(primary_key=True)
    estado=models.BooleanField()
    
    def __str__(self):
        return str(self.terma_arbitral_id)

    class Meta:
        verbose_name_plural='terma_arbitral'

class detalle_terma(models.Model):
    detalle_terma_id=models.BigAutoField(primary_key=True)
    terma_arbitral_id=models.ForeignKey(terma_arbitral,on_delete=models.CASCADE,db_column='tema_arbitral_id')
    arbitro_id=models.ForeignKey(arbitro,on_delete=models.CASCADE,db_column='arbitro_id')
    estado_jugo=models.BooleanField()

    def __str__(self):
        return str(self.terma_arbitral_id)

    class Meta:
        verbose_name_plural='detalle_terma'

