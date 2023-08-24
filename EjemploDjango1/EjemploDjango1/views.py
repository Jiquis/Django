from django.http import HttpResponse

#Cada funcion que se cree dentro del archivo "views" se le denomica vista

def Saludo(request): #Esta es la primera vista
    
    return HttpResponse("Hola, esta es mi primera pagina con Django.")

def Despedida(request):
    return HttpResponse("Hasta pronto, el jueves 25 siguen las clases de Django.")