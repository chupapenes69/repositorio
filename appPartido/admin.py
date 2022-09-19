from django.contrib import admin
from appPartido.models import *
# Register your models here.

class ciudadAdmin(admin.ModelAdmin):
    list_display=['ciudad_id','nombre','norma']

class estadoAdmin(admin.ModelAdmin):
    list_display=['estado_id','nombre'] 

class sedeAdmin(admin.ModelAdmin):
    list_display=['sede_id','nombre','capacidad','ciudad_id','estado_id','pais_id']

class encuentroAdmin(admin.ModelAdmin):
    list_display=['encuentro_id','equipo_local_id','equipo_visitante_id','resultado_general','resultado_equipo_a','resultado_equipo_b','sede_id','terma_arbitral_id','fecha','humedad','clima','estado_jugado']

class eventoAdmin(admin.ModelAdmin):
    list_display=['evento_id','descripcion','estado']

class evento_personaAdmin(admin.ModelAdmin):
    list_display=['encuentro_evento_id','encuentro_id','evento_id','persona_id','tiempo'] 

admin.site.register(estado,estadoAdmin)
admin.site.register(ciudad,ciudadAdmin)
admin.site.register(sede,sedeAdmin)
admin.site.register(encuentro,encuentroAdmin)
admin.site.register(evento,eventoAdmin)
admin.site.register(evento_persona,evento_personaAdmin)