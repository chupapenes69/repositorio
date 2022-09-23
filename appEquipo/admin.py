from django.contrib import admin
from appEquipo.models import *

# Register your models here.

class equipoAdmin(admin.ModelAdmin):
    list_display=['equipo_id','logo','vestimenta','nombre','siglas','tipo_equipo_id','sede_id','deporte_id']
    ordering=['equipo_id']

class tipoEquipoAdmin(admin.ModelAdmin):
    list_display=['tipo_equipo_id','descripcion','estado']
    ordering=['tipo_equipo_id']

class posicionJugadorAdmin(admin.ModelAdmin):
    list_display=['posicion_jugador_id','descripcion']
    ordering=['posicion_jugador_id']

class AlineacionEquipoAdmin(admin.ModelAdmin):
    list_display=['alineacion_equipo_id','equipo_id','dorsal','posicion_jugador_id','capitan','estado','contrato_id']
    ordering=['alineacion_equipo_id']

admin.site.register(tipo_equipo,tipoEquipoAdmin)
admin.site.register(equipo,equipoAdmin)
admin.site.register(posicion_jugador,posicionJugadorAdmin)
admin.site.register(alineacion_equipo,AlineacionEquipoAdmin)
