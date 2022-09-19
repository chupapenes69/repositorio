from django.contrib import admin
from appArbitro.models import *

# Register your models here.

class arbitroAdmin(admin.ModelAdmin):
    list_display=['arbitro_id','nombre','apellido','tipo_arbitro','estado']

class temaArbitralAdmin(admin.ModelAdmin):
    list_display=['terma_arbitral_id','estado']

class detalleTermaArbitralAdmin(admin.ModelAdmin):
    list_display=['detalle_terma_id','terma_arbitral_id','arbitro_id','estado_jugo']

admin.site.register(arbitro,arbitroAdmin)
admin.site.register(terma_arbitral,temaArbitralAdmin)
admin.site.register(detalle_terma,detalleTermaArbitralAdmin)