from django.contrib import admin
from appArbitro.models import *

# Register your models here.

class ArbitroAdmin(admin.ModelAdmin):
    list_display=['arbitro_id','nombre','apellido','tipo_arbitro']

admin.site.register(arbitro,ArbitroAdmin)
admin.site.register(terma_arbitral)
admin.site.register(detalle_terma)