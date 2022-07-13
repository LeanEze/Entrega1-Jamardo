from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import Cerdo
from mi_app.models import Perro
from mi_app.models import Gato

def datos_cerdos(request):
    context = {}
    context["cerdos"] = Cerdo.objects.all()#modelo
    return render(request, "mi_app/cerdos.html", context)#templete

def datos_perros(request):
    context = {}
    context["perros"] = Perro.objects.all()#modelo
    return render(request, "mi_app/perros.html", context)#templete

def datos_gatos(request):
    context = {}
    context["gatos"] = Gato.objects.all()#modelo
    return render(request, "mi_app/gatos.html", context)#templete