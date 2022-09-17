from django.contrib import admin
from appCompeticion.models import *

# Register your models here.

class paisAdmin(admin.ModelAdmin):
    list_display=['pais_id','nombre']

admin.site.register(tipo_competicion)
admin.site.register(competicion)
admin.site.register(pais,paisAdmin)
admin.site.register(deporte)
admin.site.register(grupo)
admin.site.register(detalle_grupo)
admin.site.register(tabla)