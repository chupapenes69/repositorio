from django.http import HttpResponse

def saludo(request):

    return HttpResponse("Hola mundo cruel .l.")

def despedida(request):
    return HttpResponse("Chau")
