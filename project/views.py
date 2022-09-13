from django.http import HttpResponse
import datetime

from django.template import Template, Context

def saludo(request):

    doc_externo=open("plantillas/miplantilla.html")
    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

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