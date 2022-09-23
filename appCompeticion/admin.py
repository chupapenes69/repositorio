from django.contrib import admin
from appCompeticion.models import *

# Register your models here.
class tipo_competicionAdmin(admin.ModelAdmin):
    list_display=['tipo_competicion_id','nombre','estado']
    ordering=['tipo_competicion_id']

class competicionAdmin(admin.ModelAdmin):
    list_display=['competicion_id','nombre','pais_id','tipo_competicion_id']
    ordering=['competicion_id']

class paisAdmin(admin.ModelAdmin):
    list_display=['pais_id','nombre']
    ordering=['pais_id']

class deporteAdmin(admin.ModelAdmin):
    list_display=['deporte_id','nombre','estado']
    ordering=['deporte_id']

class grupoAdmin(admin.ModelAdmin):
    list_display=['grupo_id','nombre']
    ordering=['grupo_id']

class detalle_grupoAdmin(admin.ModelAdmin):
    list_display=['detalle_grupo_id','equipo_id','grupo_id','competicion_id']
    ordering=['detalle_grupo_id']

class tablaAdmin(admin.ModelAdmin):
    list_display=['tabla_id','competicion_id','equipo_id','ganado','perdido','empatado','goles_favor','goles_contra','tarjetas_amarillas','tarjetas_rojas','puntos']
    ordering=['tabla_id']

admin.site.register(tipo_competicion,tipo_competicionAdmin)
admin.site.register(competicion,competicionAdmin)
admin.site.register(pais,paisAdmin)
admin.site.register(deporte,deporteAdmin)
admin.site.register(grupo,grupoAdmin)
admin.site.register(detalle_grupo,detalle_grupoAdmin)
admin.site.register(tabla,tablaAdmin)