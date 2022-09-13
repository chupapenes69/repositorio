from django.http import HttpResponse
import datetime

from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):

    p1=Persona("Juan", "Díaz")
    
    #nombre="Marco"
    #apellido="Padilla"

    ahora=datetime.datetime.now()

    doc_externo=open("plantillas/miplantilla.html")
    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"comentario":"Este es un comentario","momento_actual":ahora})

    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Chau")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad,agno):

    periodo=agno-2022
    edadFutura=edad+periodo
    documento="<body><h2>En el año %s tendrás %s años</h2></body></html>" %(agno,edadFutura)

    return HttpResponse(documento)