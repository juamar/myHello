from django.http import HttpResponse
import datetime

#definir una funcion que crea una pagina web

def current_datetime(request):
    now=datetime.datetime.now()

    #datetime es el modulo y datatime es la clase.

    html="<html><body><h1>hola!</h1><p>la hora es : %s</p></body></html>" %now
    return HttpResponse(html)
