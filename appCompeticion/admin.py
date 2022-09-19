from django.contrib import admin
from appCompeticion.models import *

# Register your models here.
class tipo_competicionAdmin(admin.ModelAdmin):
    list_display=['tipo_competicion_id','nombre','estado']

class competicionAdmin(admin.ModelAdmin):
    list_display=['competicion_id','nombre','pais_id','tipo_competicion_id']

class paisAdmin(admin.ModelAdmin):
    list_display=['pais_id','nombre']

class deporteAdmin(admin.ModelAdmin):
    list_display=['deporte_id','nombre','estado']

class grupoAdmin(admin.ModelAdmin):
    list_display=['grupo_id','nombre']

class detalle_grupoAdmin(admin.ModelAdmin):
    list_display=['detalle_grupo_id','equipo_id','grupo_id','competicion_id']

class tablaAdmin(admin.ModelAdmin):
    list_display=['tabla_id','competicion_id','equipo_id','ganado','perdido','empatado','goles_favor','goles_contra','tarjetas_amarillas','tarjetas_rojas','puntos']

admin.site.register(tipo_competicion,tipo_competicionAdmin)
admin.site.register(competicion,competicionAdmin)
admin.site.register(pais,paisAdmin)
admin.site.register(deporte,deporteAdmin)
admin.site.register(grupo,grupoAdmin)
admin.site.register(detalle_grupo,detalle_grupoAdmin)
admin.site.register(tabla,tablaAdmin)