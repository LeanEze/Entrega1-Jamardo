import re
from django.shortcuts import render
from django.http import HttpResponse
from mi_app.forms import cerdoFormulario, gatoFormulario, perroFormulario
from mi_app.models import Cerdo, Gato, Perro


def mostrar_inicio(request):
    
    return render(request, "mi_app/inicio.html", {})#templete


def datos_cerdos(request):
    
    return render(request, "mi_app/cerdos.html", {})

def datos_perros(request):
    
    return render(request, "mi_app/perros.html", {})

def datos_gatos(request):
    
    return render(request, "mi_app/gatos.html", {})


def perro_formulario(request):
    
    if  request.method == "POST":
        
        miFormulario = perroFormulario(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:
           
            informacion = miFormulario.cleaned_data
           
            perros = Perro (nombre=informacion['nombre'], genero=informacion['genero'], 
            raza=informacion['raza'], edad=informacion['edad'])
           
            perros.save()

            return render(request, "mi_app/perros.html")
    else:
        
        miFormulario = perroFormulario()
   
    return render(request, "mi_app/perros.html",{"miFormulario": miFormulario})


def gato_formulario(request):
    
    if  request.method == "POST":
        
        miFormulario = gatoFormulario(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:
           
            informacion = miFormulario.cleaned_data
           
            gatos = Gato (nombre=informacion['nombre'], genero=informacion['genero'], 
            raza=informacion['raza'], edad=informacion['edad'])
           
            gatos.save()

            return render(request, "mi_app/gatos.html")
    else:
        
        miFormulario = gatoFormulario()
   
    return render(request, "mi_app/gatos.html", {"miFormulario": miFormulario})


def cerdo_formulario(request):
    
    if  request.method == "POST":
        
        miFormulario = cerdoFormulario(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:
           
            informacion = miFormulario.cleaned_data
           
            cerdos = Cerdo (nombre=informacion['nombre'], genero=informacion['genero'], 
            raza=informacion['raza'], edad=informacion['edad'])
           
            cerdos.save()

            return render(request, "mi_app/cerdos.html")
    else:
        
        miFormulario = cerdoFormulario()
   
    return render(request, "mi_app/cerdos.html", {"miFormulario": miFormulario})


def busqueda_formularios(request):

    return render(request, "mi_app/buscarFormularios.html")

    
def buscar(request):

    
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        perros = Perro.objects.filter(nombre__contains=nombre)
        
        
        return render (request, "mi_app/buscarFormularios.html", {"perros":perros})

    else:
        respuesta = "no enviaste datos"
          

    return render (request, "mi_app/buscarFormularios.html", {"respuesta": respuesta})
   
