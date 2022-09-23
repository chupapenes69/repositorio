from django.shortcuts import render
from appArbitro.models import arbitro
from appContrato.models import persona
from appEquipo.models import equipo
# Create your views here.

def contadoresAdmin(request):
    arbitros = arbitro.objects.count()
    entrenadores = persona.objects.filter(tipo_persona_id=2).count()
    jugadores = persona.objects.filter(tipo_persona_id=1).count()
    equipos = equipo.objects.count()
    data = {
        'arbitros' : arbitros,
        'entrenadores' : entrenadores,
        'jugadores' : jugadores,
        'equipos' : equipos
    }
    return render(request, 'admin/index.html', data)

