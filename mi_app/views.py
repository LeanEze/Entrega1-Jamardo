from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import cerdo
from mi_app.models import perro
from mi_app.models import gato


def mostrar_inicio(request):
    
    return render(request, "mi_app/inicio.html", {})#templete


def datos_cerdos(request):
    
    return render(request, "mi_app/cerdos.html", {})

def datos_perros(request):
    
    return render(request, "mi_app/perros.html", {})

def datos_gatos(request):
    
    return render(request, "mi_app/gatos.html", {})