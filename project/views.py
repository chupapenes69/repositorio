from django.shortcuts import render
from appArbitro.models import arbitro
from appContrato.models import persona
# Create your views here.

def contadoresAdmin(request):
    arbitros= arbitro.objects.count()
    entrenadores= persona.objects.filter(tipo_persona_id=2).count()
    data = {
        'arbitros' : arbitros,
        'entrenadores' : entrenadores
    }
    return render(request, 'admin/index.html', data)

